from fast_langdetect import detect

# Simple detection
def detectLanguage(text):
  text = text.replace("\n", " ")
  return detect(text)['lang']
