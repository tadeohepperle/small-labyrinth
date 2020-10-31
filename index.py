from PIL import Image
# pip install Pillow


class PixelMap:
    map = [[]]
    img = None
    entryCoordinate = (1, 1)

    def __init__(self, imagePath, entryCoordinate):
        self.img = Image.open(imagePath)
        self.convertImageToMap()
        self.entryCoordinate = entryCoordinate

    def convertImageToMap(self):
        arr = []
        x = self.img.size[0]
        y = self.img.size[1]
        for yi in range(y):
            arr.append([])
            for xi in range(x):
                pix = self.img.getpixel((xi, yi))
                (r, g, b, a) = pix
                pix_as_num = 0 if r+g+b < 700 else 1
                arr[yi].append(pix_as_num)
        self.map = arr

    def solveMap(self):
        pass

    def __str__(self):
        longstr = ""
        for i in range(len(self.map)):
            s = ""
            for pix in self.map[i]:
                s += "■" if pix == 1 else "□"
            longstr += s + "\n"
        return longstr

    def solve(self):
        self.entryCoordinate

        print(self.getValidSteps(self.entryCoordinate))

    def getValidSteps(self, pos):
        (x, y) = pos
        leftPos = (x-1, y)
        rightPos = (x+1, y)
        upPos = (x, y-1)
        downPos = (x, y+1)
        goodPosistions = []
        if(self.getValueAtPos(leftPos) == 1):
            goodPosistions.append(leftPos)
        if(self.getValueAtPos(rightPos) == 1):
            goodPosistions.append(rightPos)
        if(self.getValueAtPos(upPos) == 1):
            goodPosistions.append(upPos)
        if(self.getValueAtPos(downPos) == 1):
            goodPosistions.append(downPos)

    def getValueAtPos(self, pos):
        (x, y) = pos
        mapSizeX = len(self.map[0])
        mapSizeY = len(self.map)
        if(not(0 <= x < mapSizeX)):
            return -1
        if(not(0 <= y < mapSizeY)):
            return -1
        return self.map[y][x]


pixelMap = PixelMap("labyrinth3.png", (1, 0))
print(pixelMap)
print(pixelMap.getValueAtPos(pixelMap.entryCoordinate))
# pixelMap.solve()
