import library.score as score

# keeps track of what stage the game is in
stage = 0

def increaseStage():
    global stage
    stage = stage + 1

def writeScore():
  with open('score_backup.txt', 'w') as f:
     f.write(f"{score.blue_score}\n{score.yellow_score}\n{stage}")
     f.flush()

def restoreScore():
  global stage
  with open('score_backup.txt') as f:
     for i, line in enumerate(f):
         if i == 0:
             score.set_score_blue(int(line))
         if i == 1:
             score.set_score_yellow(int(line))
         if i == 2:
             stage = int(line)

