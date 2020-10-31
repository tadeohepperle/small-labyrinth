from PIL import Image


def imageFilePathToPixels(filepath):
    img = Image.open(filepath)
    arr = []
    x = img.size[0]
    y = img.size[1]
    for xi in range(x):
        arr.append([])
        for yi in range(y):
            pix = img.getpixel((xi, yi))
            (r, g, b, a) = pix
            pix_as_num = 1 if r+g+b > 700 else 0
            arr[xi].append(pix_as_num)
    return arr


pix_arr = imageFilePathToPixels("labyrinth.png")
print(pix_arr)
