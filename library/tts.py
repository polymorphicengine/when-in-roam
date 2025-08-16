from threading import Thread
import subprocess
import library.langdetect as langdetect
import config

piper = config.piper_dir + "piper/piper"

models_english = [config.piper_dir + "/models/en/en_US-john-medium.onnx"
                 ,config.piper_dir + "/models/en/en_GB-alan-medium.onnx"
                 ,config.piper_dir + "/models/en/en_GB-alba-medium.onnx"
                 ,config.piper_dir + "/models/en/en_US-amy-medium.onnx"]
models_hungarian = [config.piper_dir + "/models/hu/hu_HU-anna-medium.onnx"
                   ,config.piper_dir + "/models/hu/hu_HU-berta-medium.onnx"
                   ,config.piper_dir + "/models/hu/hu_HU-imre-medium.onnx"]
models_german = [config.piper_dir + "/models/de/de_DE-ramona-low.onnx"
                ,config.piper_dir + "/models/de/de_DE-thorsten-medium.onnx"]

def tts(text, team, num):

  lang = langdetect.detectLanguage(text)

  match lang:
      case 'hu':
          models = models_hungarian
      case 'de':
          models = models_german
      case _:
          models = models_english

  model = models[num % len(models)]

  output = config.sounds_dir + f"game/1-2_SECRET/{team}_SECRET_{num+1}.wav"

  process = subprocess.Popen([piper,"--model", model, "--output_file", output], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)
  process.communicate(input = text)

def startTTS(text, team, num):
  Thread(target=tts, args=(text, team, num)).start()

def ttsTest():
    startTTS("Hello World, I am a great secret! I like chocolate", 'B', 0)
    startTTS("Hallo, ich werde dir mein Geheimnis nie preisgeben! Da kannst du dich darauf verlassen", 'Y', 1)
    startTTS("Hunyadi János volt hadvezér és kormányzó pedig a gyulafehérvári katolikus katedrálisban van eltemetve.",'B' , 2)
