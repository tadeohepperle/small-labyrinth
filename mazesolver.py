from PIL import Image
# pip install Pillow
# 1 = weiß "□", 0 = schwarz "■"


def shortenPath(p):
    done = False
    j = 0
    while(not done):
        # print(j)
        # print(p)
        pos = p[j]
        j += 1
        indexesOfPos = [i for i, x in enumerate(p) if x == pos]
        if(len(indexesOfPos) == 1):
            if(j == len(p)-1):
                done = True
                return p
            else:
                continue
        elif(len(indexesOfPos) > 1):
            firstOccurance = indexesOfPos[0]
            lastOccurance = indexesOfPos[-1]
            p = p[0:firstOccurance] + p[lastOccurance: len(p)]
            j -= (lastOccurance - firstOccurance)
            j = 0
    return p


class bcolors:
    HEADER = '\033[95m'
    CRED = '\033[91m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def green(s):
    return bcolors.OKGREEN + s + bcolors.ENDC


def red(s):
    return bcolors.FAIL + s + bcolors.ENDC


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PixelMap:
    map = [[]]
    img = None
    entryCoordinate = (1, 1)
    imageName = ""
    solutionPath = []

    def __init__(self, imagePath, entryCoordinate):
        self.img = Image.open(imagePath)
        self.convertImageToMap()
        self.entryCoordinate = entryCoordinate
        self.imageName = self.img.filename

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

    def __str__(self):
        longstr = ""
        for i in range(len(self.map)):
            s = red("O")
            for pix in self.map[i]:
                s += "■" if pix == 1 else "□"
            longstr += s + "\n"
        return longstr

    def solve(self):
        path = [self.entryCoordinate]
        posRN = self.entryCoordinate
        forbidden = [self.entryCoordinate]
        solved = False
        i = 0
        maxSteps = 10000
        while (not solved and i < maxSteps):
            i += 1
            lastPos = path[len(path)-1]
            validSteps = set(self.getValidSteps(posRN))
            validSteps -= set([posRN, lastPos] + forbidden)
            validSteps = list(validSteps)
            if(len(validSteps) > 0):

                path.append(posRN)
                posRN = validSteps[0]
            else:
                forbidden.append(posRN)
                if(posRN in path):
                    path.remove(lastPos)
                posRN = lastPos
            # check if border is reached:
            if(self.isBorderAtPos(posRN)):
                solved = True
                del path[0]
                path.append(posRN)
                path = shortenPath(path)
                print("completed at position: ", posRN)
                self.printSelfWithPath(path)
            else:
                self.printSelfWithPathAndPoint(path, posRN)
                pass
        self.solutionPath = path

    def solveAndPrintToImage(self):
        self.solve()
        xSize = len(self.map[0])
        ySize = len(self.map)
        output = Image.new(mode="RGB", size=(xSize, ySize))
        pixels = output.load()
        # print basic map:
        for x in range(xSize):
            for y in range(ySize):
                pixels[x, y] = (0, 0, 0) if self.map[y][x] == 0 else (
                    255, 255, 255)
        # print path:
        for pos in self.solutionPath:
            (x, y) = pos
            pixels[x, y] = (255, 50, 50)  # red
        output.save("./solved/solved_" + self.imageName)

    def printSelfWithPoint(self, pos):
        longstr = ""
        for i in range(len(self.map)):
            s = ""
            for j in range(len(self.map[i])):
                valueAtPos = self.map[i][j]
                if(pos == (j, i)):
                    s += red("O")
                else:
                    s += "□" if valueAtPos == 1 else "■"
            longstr += s + "\n"
        print(longstr)

    def printSelfWithPath(self, path):
        longstr = ""
        for i in range(len(self.map)):
            s = ""
            for j in range(len(self.map[i])):
                valueAtPos = self.map[i][j]
                if((j, i) in path):
                    s += red("X")
                else:
                    s += "□" if valueAtPos == 1 else "■"
            longstr += s + "\n"
        print(longstr)

    def printSelfWithPathAndPoint(self, path, pos):
        longstr = ""
        for i in range(len(self.map)):
            s = ""
            for j in range(len(self.map[i])):
                valueAtPos = self.map[i][j]
                if(pos == (j, i)):
                    s += green("O")
                elif((j, i) in path):
                    s += red("X")
                else:
                    s += "□" if valueAtPos == 1 else "■"
            longstr += s + "\n"
        print(longstr)

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
        return goodPosistions

    def isBorderAtPos(self, pos):
        (x, y) = pos
        mapSizeX = len(self.map[0])
        mapSizeY = len(self.map)
        return (x == 0 or y == 0 or x == mapSizeX-1 or y == mapSizeY-1)

    def getValueAtPos(self, pos):
        (x, y) = pos
        mapSizeX = len(self.map[0])
        mapSizeY = len(self.map)
        if(not(0 <= x < mapSizeX)):
            return -1
        if(not(0 <= y < mapSizeY)):
            return -1
        return self.map[y][x]


class MazeSolver:
    @staticmethod
    def solveMazeImage(filename, entryPosition):
        pixelMap = PixelMap(filename, entryPosition)
        pixelMap.solveAndPrintToImage()


MazeSolver.solveMazeImage("labyrinth3.png", (1, 0))
