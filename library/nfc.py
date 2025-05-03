import board
import busio
from adafruit_pn532.i2c import PN532_I2C
import config

# I2C connection setup
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

# Configure PN532 to read NFC tags
pn532.SAM_configuration()

# stores tags that have been scanned, so they cannot be scanned again
scanned_tags = []

def scan():
    
    while True:
        # Check if a card is available to read
        uid = pn532.read_passive_target(timeout=0.5)
        # Break if card is available.
        if uid is not None:
            break

    data = pn532.mifare_classic_read_block(4)

    if data is not None:
        return (chr(data[0]),chr(data[1]),int(data[2]))
    else: 
        scan()

# stops scan when specific id is scanned
def scan_for(id):
    while True:
        uid = pn532.read_passive_target(timeout=0.5)
        # print(uid)
        # print(id)
        if uid == id:
            break

# scans for a tag and if it hasn't been scanned, hand it to the callback
def scan_and_play_once(play):
    tag = scan()

    if tag is not None and tag not in scanned_tags:
        play(tag[0], tag[1], tag[2])
        if not config.rescan_possible:
            scanned_tags.append(tag)
    else:
        scan_and_play_once(play)