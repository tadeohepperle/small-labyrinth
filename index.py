from PIL import Image
# pip install Pillow


class PixelMap:
    x = 0
    y = 0
    map = [[]]
    img = None
    entryCoordinate = (1, 1)

    def __init__(self, imagePath, entryCoordinate):
        self.img = Image.open(imagePath)
        self.convertImageToMap()

    def convertImageToMap(self):
        arr = []
        x = self.img.size[0]
        y = self.img.size[1]
        for yi in range(y):
            arr.append([])
            for xi in range(x):
                pix = self.img.getpixel((xi, yi))
                (r, g, b, a) = pix
                pix_as_num = 1 if r+g+b < 700 else 0
                arr[yi].append(pix_as_num)
        self.map = arr

    def solveMap(self):
        pass

    def __str__(self):
        longstr = ""
        for i in range(len(self.map)):
            s = ""
            for pix in self.map[i]:
                s += str(pix)
            longstr += s + "\n"
        return longstr

    def __repr__(self):
        longstr = ""
        for i in range(len(self.map)):
            s = ""
            for pix in self.map[i]:
                s += str(pix)
            longstr += s + "\n"
        return longstr


pixelMap = PixelMap("labyrinth.png", (1, 1))
print(pixelMap.map)

print(pixelMap)
