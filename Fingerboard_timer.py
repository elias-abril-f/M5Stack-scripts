from m5stack import *
from m5ui import *
from uiflow import *
import time


setScreenColor(0x222222)


mode = None
count_reps = None
timer_value = None
count_sets = None
e = None
sound_state = None
count_exercises = None
s = None
mode_value = None
r = None
d = None
sr = None
rr = None



e_slash = M5TextBox(68, 208, "/", lcd.FONT_Default, 0xFFFFFF, rotate=0)
e_total = M5TextBox(83, 208, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
s_slash = M5TextBox(158, 208, "/", lcd.FONT_Default, 0xFFFFFF, rotate=0)
e_counter = M5TextBox(45, 208, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
s_count = M5TextBox(137, 208, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
s_total = M5TextBox(173, 208, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
r_slash = M5TextBox(245, 208, "/", lcd.FONT_Default, 0xFFFFFF, rotate=0)
r_count = M5TextBox(227, 208, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
r_total = M5TextBox(261, 208, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
exercises = M5TextBox(0, 50, "Exercises:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
exercises_value = M5TextBox(100, 50, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
sets = M5TextBox(0, 100, "Sets:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
sets_value = M5TextBox(100, 100, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
reps = M5TextBox(0, 150, "Reps:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
reps_value = M5TextBox(100, 150, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
times = M5TextBox(261, 100, "Times", lcd.FONT_Default, 0xFFFFFF, rotate=0)
duration = M5TextBox(220, 50, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
reps_rest = M5TextBox(220, 150, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
Mode_label = M5TextBox(0, 0, "Mode: ", lcd.FONT_Default, 0xFFFFFF, rotate=0)
Battery = M5TextBox(279, 0, "%", lcd.FONT_Default, 0xFFFFFF, rotate=0)
timer = M5TextBox(137, 84, "0", lcd.FONT_DejaVu72, 0xFFFFFF, rotate=0)
Mode_value = M5TextBox(44, 0, "Manual", lcd.FONT_Default, 0xFFFFFF, rotate=0)
highlight = M5Line(M5Line.PLINE, 93, 65, 113, 65, 0xFFFFFF)
sets_rest = M5TextBox(220, 100, "0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
sound = M5TextBox(125, 0, "Sound On", lcd.FONT_Default, 0xFFFFFF, rotate=0)

from numbers import Number


# Describe this function...
def beep():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  if sound_state == 'On':
    if timer_value == 4:
      setScreenColor(0xff9900)
    if timer_value <= 4:
      Progress_layer_up()
      speaker.tone(1000, 100)
    if timer_value == 1:
      speaker.tone(1000, 300)

# Describe this function...
def setup():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  count_reps = 0
  count_sets = 0
  count_exercises = 0
  exercises.hide()
  exercises_value.hide()
  sets.hide()
  sets_value.hide()
  reps.hide()
  reps_value.hide()
  times.hide()
  duration.hide()
  reps_rest.hide()
  sets_rest.hide()
  Mode_label.hide()
  Mode_value.hide()
  countdown()

# Describe this function...
def countdown():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  setScreenColor(0xffff00)
  timer_value = 5
  timer.setText(str(timer_value))
  e_total.setText(str(e))
  s_total.setText(str(s))
  r_total.setText(str(r))
  Progress_layer_up()
  timerSch.run('countdown', 1000, 0x00)

# Describe this function...
def update_value():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  timer_value = (timer_value if isinstance(timer_value, Number) else 0) + -1
  if timer_value < 10:
    timer.setPosition(x=137)
  else:
    timer.setPosition(x=116)
  if timer_value == 3 and mode == 'countdown':
    setScreenColor(0xff9900)
    Progress_layer_up()
  timer.setText(str(timer_value))
  r_count.setText(str(count_reps))
  s_count.setText(str(count_sets))
  e_counter.setText(str(count_exercises))

# Describe this function...
def Progress_layer_up():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  timer.show()
  e_total.show()
  e_slash.show()
  e_counter.show()
  s_count.show()
  s_total.show()
  s_slash.show()
  r_slash.show()
  r_count.show()
  r_total.show()


def buttonA_wasDoublePress():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  if mode != 'timer':
    if mode == 0:
      e = (e if isinstance(e, Number) else 0) + -1
      exercises_value.setText(str(e))
    if mode == 1:
      s = (s if isinstance(s, Number) else 0) + -5
      sets_value.setText(str(s))
    if mode == 2:
      r = (r if isinstance(r, Number) else 0) + -5
      reps_value.setText(str(r))
    if mode == 3:
      d = (d if isinstance(d, Number) else 0) + -5
      duration.setText(str(d))
    if mode == 4:
      sr = (sr if isinstance(sr, Number) else 0) + -5
      sets_rest.setText(str(sr))
    if mode == 5:
      rr = (rr if isinstance(rr, Number) else 0) + -5
      reps_rest.setText(str(rr))
    if mode == 6:
      if mode_value == 'Manual':
        mode_value = "Emil's"
        Mode_value.setText("Emil's")
      else:
        mode_value = 'Manual'
        Mode_value.setText('Manual')
      if mode == 7:
        if sound_state == 'On':
          sound_state = 'Off'
          sound.setText('Sound Off')
        else:
          sound_state = 'On'
          sound.setText('Sound On')
  pass
btnA.wasDoublePress(buttonA_wasDoublePress)

def buttonA_wasPressed():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  if mode != 'timer':
    if mode == 0:
      e = (e if isinstance(e, Number) else 0) + -1
      exercises_value.setText(str(e))
    if mode == 1:
      s = (s if isinstance(s, Number) else 0) + -1
      sets_value.setText(str(s))
    if mode == 2:
      r = (r if isinstance(r, Number) else 0) + -1
      reps_value.setText(str(r))
    if mode == 3:
      d = (d if isinstance(d, Number) else 0) + -1
      duration.setText(str(d))
    if mode == 4:
      sr = (sr if isinstance(sr, Number) else 0) + -1
      sets_rest.setText(str(sr))
    if mode == 5:
      rr = (rr if isinstance(rr, Number) else 0) + -1
      reps_rest.setText(str(rr))
    if mode == 6:
      if mode_value == 'Manual':
        mode_value = "Emil's"
        Mode_value.setText("Emil's")
      else:
        mode_value = 'Manual'
        Mode_value.setText('Manual')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  if mode != 'timer' and mode != 'paused_timer' and mode != 'paused_countdown' and mode != 'countdown':
    mode = (mode if isinstance(mode, Number) else 0) + 1
    if mode > 7:
      mode = 0
    if mode == 0:
      highlight.setSize(93, 65, 113, 65)
    if mode == 1:
      highlight.setSize(93, 115, 118, 115)
    if mode == 2:
      highlight.setSize(93, 165, 113, 165)
    if mode == 3:
      highlight.setSize(214, 65, 234, 65)
    if mode == 4:
      highlight.setSize(214, 115, 239, 115)
    if mode == 5:
      highlight.setSize(214, 165, 234, 165)
    if mode == 6:
      highlight.setSize(43, 18, 96, 18)
    if mode == 7:
      highlight.setSize(126, 18, 196, 18)
  else:
    Battery.setText(str((str((power.getBatteryLevel())) + str('%'))))
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  if mode != 'timer':
    if mode == 0:
      e = (e if isinstance(e, Number) else 0) + 1
      exercises_value.setText(str(e))
    if mode == 1:
      s = (s if isinstance(s, Number) else 0) + 1
      sets_value.setText(str(s))
    if mode == 2:
      r = (r if isinstance(r, Number) else 0) + 1
      reps_value.setText(str(r))
    if mode == 3:
      d = (d if isinstance(d, Number) else 0) + 1
      duration.setText(str(d))
    if mode == 4:
      sr = (sr if isinstance(sr, Number) else 0) + 1
      sets_rest.setText(str(sr))
    if mode == 5:
      rr = (rr if isinstance(rr, Number) else 0) + 1
      reps_rest.setText(str(rr))
    if mode == 6:
      if mode_value == 'Manual':
        mode_value = "Emil's"
        Mode_value.setText("Emil's")
      else:
        mode_value = 'Manual'
        Mode_value.setText('Manual')
    if mode == 7:
      if sound_state == 'On':
        sound_state = 'Off'
        sound.setText('Sound Off')
      else:
        sound_state = 'On'
        sound.setText('Sound On')
  pass
btnC.wasPressed(buttonC_wasPressed)

def buttonC_wasDoublePress():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  if mode != 'timer':
    if mode == 0:
      e = (e if isinstance(e, Number) else 0) + 1
      exercises_value.setText(str(e))
    if mode == 1:
      s = (s if isinstance(s, Number) else 0) + 5
      sets_value.setText(str(s))
    if mode == 2:
      r = (r if isinstance(r, Number) else 0) + 5
      reps_value.setText(str(r))
    if mode == 3:
      d = (d if isinstance(d, Number) else 0) + 5
      duration.setText(str(d))
    if mode == 4:
      sr = (sr if isinstance(sr, Number) else 0) + 5
      sets_rest.setText(str(sr))
    if mode == 5:
      rr = (rr if isinstance(rr, Number) else 0) + 5
      reps_rest.setText(str(rr))
  pass
btnC.wasDoublePress(buttonC_wasDoublePress)

def buttonB_wasDoublePress():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  if mode == 'timer':
    mode = 'paused_timer'
    timerSch.stop('exercise_timer')
    timerSch.stop('countdown')
  elif mode == 'countdown':
    mode = 'paused_countdown'
    timerSch.stop('countdown')
    timerSch.stop('exercise_timer')
  elif mode == 'paused_timer':
    mode = 'timer'
    timerSch.run('exercise_timer', 1000, 0x00)
  elif mode == 'paused_countdown':
    mode = 'countdown'
    timerSch.run('countdown', 1000, 0x00)
  else:
    mode = 0
    highlight.setSize(93, 65, 113, 65)
    e = 0
    exercises_value.setText(str(e))
    s = 0
    sets_value.setText(str(s))
    r = 0
    reps_value.setText(str(r))
    d = 0
    duration.setText(str(d))
    sr = 0
    sets_rest.setText(str(sr))
    rr = 0
    reps_rest.setText(str(rr))
  pass
btnB.wasDoublePress(buttonB_wasDoublePress)

def buttonB_pressFor():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  mode = 'timer'
  if mode_value != "Emil's":
    setup()
  else:
    e = 6
    s = 1
    r = 6
    d = 10
    rr = 20
    sr = 20
    setup()
  pass
btnB.pressFor(0.8, buttonB_pressFor)

@timerSch.event('exercise_timer')
def texercise_timer():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  mode = 'timer'
  if timer_value > 0:
    if timer_value == 1 and sound_state == 'On':
      speaker.tone(1000, 300)
    update_value()
  else:
    timerSch.stop('exercise_timer')
    mode = 'countdown'
    count_reps = (count_reps if isinstance(count_reps, Number) else 0) + 1
    r_count.setText(str(count_reps))
    if count_reps < r:
      setScreenColor(0xff0000)
      Progress_layer_up()
      timer_value = rr
      if timer_value < 10:
        timer.setPosition(x=137)
      else:
        timer.setPosition(x=116)
      timer.setText(str(rr))
      timerSch.run('countdown', 1000, 0x00)
    else:
      count_sets = (count_sets if isinstance(count_sets, Number) else 0) + 1
      count_reps = 0
      s_count.setText(str(count_sets))
      if count_sets < s:
        setScreenColor(0xff0000)
        Progress_layer_up()
        timer_value = sr
        if timer_value < 10:
          timer.setPosition(x=137)
        else:
          timer.setPosition(x=116)
        timer.setText(str(sr))
        timerSch.run('countdown', 1000, 0x00)
      else:
        count_exercises = (count_exercises if isinstance(count_exercises, Number) else 0) + 1
        if mode_value == "Emil's" and count_exercises == 2:
          r = 2
          r_total.setText(str(r))
        e_counter.setText(str(count_exercises))
        if count_exercises < e:
          count_reps = 0
          count_sets = 0
          setScreenColor(0x66ffff)
          timer.setPosition(x=65)
          timer.setText('Next')
          wait(1)
          setScreenColor(0xff0000)
          timer_value = sr
          timer.setText(str(sr))
          if timer_value < 10:
            timer.setPosition(x=137)
          else:
            timer.setPosition(x=116)
          Progress_layer_up()
          timerSch.run('countdown', 1000, 0x00)
        else:
          setScreenColor(0x3333ff)
          timer.setPosition(x=65)
          timer.setText('Done')
          if sound_state == 'On':
            speaker.sing(554, 1/2)
            speaker.sing(740, 1/2)
            speaker.sing(554, 1/2)
            speaker.sing(740, 1/2)
  pass

@timerSch.event('countdown')
def tcountdown():
  global mode, count_reps, timer_value, count_sets, e, sound_state, count_exercises, s, mode_value, r, d, sr, rr
  mode = 'countdown'
  if timer_value > 0:
    beep()
    update_value()
  else:
    timerSch.stop('countdown')
    mode = 'timer'
    setScreenColor(0x33ff33)
    Progress_layer_up()
    timer_value = d
    if timer_value < 10:
      timer.setPosition(x=137)
    else:
      timer.setPosition(x=116)
    timer.setText(str(timer_value))
    timerSch.run('exercise_timer', 1000, 0x00)
  pass


speaker.setVolume(1)
Battery.show()
Battery.setText(str((str((power.getBatteryLevel())) + str('%'))))
timer.hide()
e_slash.hide()
e_counter.hide()
e_total.hide()
s_slash.hide()
s_count.hide()
s_total.hide()
r_total.hide()
r_count.hide()
r_slash.hide()
e = 1
exercises_value.setText(str(e))
s = 15
sets_value.setText(str(s))
r = 6
reps_value.setText(str(r))
d = 7
duration.setText(str(d))
rr = 3
reps_rest.setText(str(rr))
sr = 60
sets_rest.setText(str(sr))
mode = 0
mode_value = 'Manual'
sound_state = 'On'
