import library.nfc as nfc
import library.practice as practice

if __name__ == '__main__':
    try:
      practice.start_practice()
    except:
      nfc.close_nfc()
