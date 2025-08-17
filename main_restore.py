import main
import library.restore as restore
import library.led as led

def performance_from_stage():
     if restore.stage == 0:
         main.beginning()
         restore.increaseStage()
     if restore.stage <= 1:
         main.stretching()
         restore.increaseStage()
     if restore.stage <= 2:
         main.first_game()
         restore.increaseStage()
     if restore.stage <= 3:
         main.second_game()
         restore.increaseStage()
     if restore.stage <= 4:
         main.third_game()
         restore.increaseStage()
     if restore.stage <= 5:
         main.last_game()
         restore.increaseStage()
     if restore.stage == 6:
         main.outro()
     
if __name__ == '__main__':
    try:
      restore.restoreScore()
      performance_from_stage()
    finally:
      led.turn_off_red_light() 
      led.turn_off_green_light()
      restore.writeScore()
