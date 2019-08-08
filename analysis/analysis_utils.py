import math
import re

tenhou_tile_to_array_index_lookup = [
     1,  2,  3,  4,  5,  6,  7,  8,  9,
    11, 12, 13, 14, 15, 16, 17, 18, 19,
    21, 22, 23, 24, 25, 26, 27, 28, 29,
    31, 32, 33, 34, 35, 36, 37
]

def convertTile(tile):
    return tenhou_tile_to_array_index_lookup[math.floor(int(tile) / 4)]

def convertHand(hand):
    convertedHand = []
    for i in range(38):
        convertedHand[i] = hand.count(i)
    return convertedHand

meld_pattern = re.compile("m=\"(\\d+?)\"")

def getTilesFromCall(call):
    match = meld_pattern.match(call)
    meldInt = int(match.group(1))
    meldBinary = format(meldInt, "016b")

    if meldBinary[meldBinary.length - 3] == '1':
        # Chii
        tile = meldBinary[0:6]
        tile = int(tile, 2)
        order = tile % 3
        tile = math.floor(tile / 3)
        tile = 9 * math.floor(tile / 7) + (tile % 7)
        tile = convertTile(tile * 4)

        if order == 0:
            return [tile, tile + 1, tile + 2]
        
        if order == 1:
            return [tile + 1, tile, tile + 2]

        return [tile + 2, tile, tile + 1]
    
    elif meldBinary[meldBinary.length - 4] == '1':
        # Pon
        tile = meldBinary[0:7]
        tile = int(tile, 2)
        tile = math.floor(tile / 3)
        tile = convertTile(tile * 4)

        return [tile, tile, tile]
    
    elif meldBinary[meldBinary.length - 5] == '1':
        # Added kan
        tile = meldBinary[0:7]
        tile = int(tile, 2)
        tile = math.floor(tile / 3)
        tile = convertTile(tile * 4)

        return [tile]
    
    elif meldBinary[meldBinary.length - 6] == '1':
        # Nuki
        return [34]
    
    else:
        # Kan
        tile = meldBinary.substr(0, 8)
        tile = int(tile, 2)
        tile = math.floor(tile / 4)
        tile = convertTile(tile * 4)
        return [tile, tile, tile, tile]
    