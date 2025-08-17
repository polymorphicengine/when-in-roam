import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# I2C connection setup
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

# Configure PN532 to read NFC tags
pn532.SAM_configuration()

tag_number = 0

ids = []

terminate = False

def writeOnce(team, player, num):

    while True:
        # Check if a card is available to read
        uid = pn532.read_passive_target(timeout=0.5)

        # Try again if no card is available.
        if uid is not None:
            break

    data = bytearray(16)
    data[0] = ord(team)
    data[1] = ord(player)
    data[2] = num

    # Write 16 byte block.
    pn532.mifare_classic_write_block(4, data)

    return uid


    
def write(team, player, prev):

    global tag_number

    tagid = writeOnce(team, player, tag_number)

    if tagid != prev:
        tag_number = tag_number + 1
        print(f"Wrote {tag_number} to tag!")
    return tagid

def writePlayer():
    prev = None
    team = input("Enter Team (Y or B):")
    player = input("Enter Player (A,B,C or D):")

    if team == 'Y' or team == 'B':
      if player == 'A' or player == 'B' or player == 'C' or player == 'D':
        while True:
            prev = write(team, player, prev)
            
            
def write_tag(team, player, num):
    print("WAITING FOR TAG")
    writeOnce(team, player, num)
    print("DONE")
    
