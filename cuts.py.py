import math 

def getMinSplit(width, height, nTiles):

    result = 1
    
    factors = []
    for i in range(1, int(math.sqrt(nTiles))+1):
        if (nTiles % i) == 0:
            factors.append(i)
            

    for x in factors:
        if ((x < width) and (nTiles/x < height)) or ((x < height) and (nTiles/x < width)) :
            result = 2
          
    
    size = width * height
    
    if (nTiles > size):
        result = -1
    
    elif (nTiles == size):
        result = 0
      
    return result




_width = int(raw_input("Enter the width of the bar: "));

_height = int(raw_input("Enter the height of the bar: "));

_nTiles = int(raw_input("Enter the number of tiles to be included in the piece to be cut out of the bar: "));



res = getMinSplit(_width, _height, _nTiles)
print "Number of cuts needed: " + str(res)

raw_input()
