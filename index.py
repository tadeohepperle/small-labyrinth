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
        x = self.img.size[1]
        y = self.img.size[0]
        for xi in range(x):
            arr.append([])
            for yi in range(y):
                pix = self.img.getpixel((xi, yi))
                (r, g, b, a) = pix
                pix_as_num = 1 if r+g+b > 700 else 0
                arr[xi].append(pix_as_num)
        self.map = arr


pixelMap = PixelMap("labyrinth.png", (1, 1))
print(pixelMap.map)
