from m5stack import *
from m5ui import *
from uiflow import *
import i2c_bus
import machine


setScreenColor(0x222222)
label0 = M5TextBox(0, 0, "label0", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)

I2C_SDA_PIN = 21
I2C_SCL_PIN = 22
i2c=machine.I2C(0,sda=machine.Pin(I2C_SDA_PIN), scl=machine.Pin(I2C_SCL_PIN), freq=400000)

print('Scanning I2C bus.')
label0.setText('Scanning')
devices = i2c.scan() # this returns a list of devices
ignore = ["0x10", "0x68", "0x75"]
device_count = len(devices)
temp = ""

if device_count == 0:
    print('No i2c device found.')
    label0.setText('No i2c device found')
else:
    for device in devices:
      if str(hex(device)) in ignore:
        device_count -= 1
      if device_count == 0:
        print('No i2c device found.')
        label0.setText('No i2c device found')
      else:
        print(device_count, 'devices found.')
        label0.setText(str(device_count))
for device in devices:
    temp += str(hex(device)) + "\n"
    if str(hex(device)) not in ignore:
      print(hex(device))
      label0.setText("Hex address: " + "\n" + temp)





