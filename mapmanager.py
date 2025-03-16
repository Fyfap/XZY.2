class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)]
        self.startNew()
        self.addBlock((0,10,0))

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def getColor(self, z):
        return self.colors[z % len(self.colors)]

    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)

        self.block.setTag('at', str(position))

        self.block.reparentTo(self.land)


    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filname):
        self.clear()
        with open(filname) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x,y

    def findBlock(self, pos):
        return self.land.findAllMatches('=at', + str(pos))

    def isEmpty(self, pos):
        block = self.findBlock(pos)
        if block:
            return  False
        else:
            return  True
            
        def findHighestEmpty(self, pos):
            x, y, z = pos
            z = 1
            while not self.isEmpty((x, y, z)):
                z += 1
            return (x, y, z)

        def delBlock(self, position):
            pos = x, y, z - 1
            blocks = self.findBlocks(position)
            for block in blocks:
                block.removeNode()

        def buildBlock(self, pos):
            x, y, z = pos
            new = self.findHighestEmpty(pos)
            if new[2] <= z + 1:
                self.addBlock(new)