import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C
from adafruit_pn532.adafruit_pn532 import MIFARE_CMD_AUTH_B
import config

# I2C connection setup
i2c = busio.I2C(board.SCL, board.SDA)

# reset_pin = DigitalInOut(board.D6)
# On Raspberry Pi, you must also connect a pin to P32 "H_Request" for hardware
# wakeup! this means we don't need to do the I2C clock-stretch thing
# req_pin = DigitalInOut(board.D12)
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

    key = b"\xff\xff\xff\xff\xff\xff"
    pn532.mifare_classic_authenticate_block(uid, 4, MIFARE_CMD_AUTH_B, key)

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
        if not config.is_rescan_possible():
            scanned_tags.append(tag)
    else:
        scan_and_play_once(play)

def read_once():
    print("Waiting for chip...")
    tag = scan()
    print(tag)

# write data of the form TEAM-PLAYER-NUMBER to tag
def write_once(team, player, num):
        print("Waiting for chip...")
        while True:
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)

            # Try again if no card is available.
            if uid is not None:
                break

        key = b"\xff\xff\xff\xff\xff\xff"
        authenticated = pn532.mifare_classic_authenticate_block(uid, 4, MIFARE_CMD_AUTH_B, key)
        if not authenticated:
            print("Authentication failed!")

        data = bytearray(16)
        data[0] = ord(team)
        data[1] = ord(player)
        data[2] = num

        # Write 16 byte block.
        pn532.mifare_classic_write_block(4, data)

        print("Wrote data to chip!")

        return uid

# close the i2c connections
def close_nfc():
    i2c.unlock()
    i2c.deinit()
