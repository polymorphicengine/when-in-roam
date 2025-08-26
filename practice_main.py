import library.nfc as nfc
import library.practice as practice

if __name__ == '__main__':
    try:
      practice.start_practice()
    except Exception as e:
      print(e)
      nfc.close_nfc()
