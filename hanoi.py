class Tower:
    def __init__(self, num):
        self.towers = [[],[],[]]
        for i in range(num ,0, -1):
            self.towers[0].append(i)

TOWER_NAME= ['A','B','C']

def move(tower, start, destination, by, depth):
    if depth >= 1:
        move(tower, start, by, destination, depth-1)
        tower.towers[destination].append(tower.towers[start].pop())
        print("move from ", TOWER_NAME[start], "to ", TOWER_NAME[destination])
        move(tower, by, destination, start, depth-1)


tower = Tower(3)
move(tower, 0,2,1,3)
