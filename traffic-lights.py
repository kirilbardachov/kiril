from ev3dev2.led import Leds
import time
lights=Leds()
while True:
  lights.set_color("RIGHT","RED")
  lights.set_color("LEFT","RED")
  time.sleep(1)
  lights.set_color("RIGHT","AMBER")
  lights.set_color("LEFT","AMBER")
  time.sleep(1)
  lights.set_color("RIGHT","GREEN")
  lights.set_color("LEFT","GREEN")
  time.sleep(1)
