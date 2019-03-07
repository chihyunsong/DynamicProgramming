def checkPath(m):
    result = []
    #Initialize

    for i in range(len(m)+1):
        result.append([])
        for j in range(len(m[0])+1):
            result[i].append(True)
    for i in range(1, len(m)+1):
        for j in range(1, len(m[0])+1):
            if not m[i-1][j-1] or (not result[i-1][j] and not result[i][j-1]):
                result[i][j] = False

    return result[i][j]

def _getPath(m, i, j, path, failedPath):

    if i < 0 or j<0 or not m[i][j]:
        return False
    if (i,j) in failedPath:
        return False
    isRobot = i==0 and j==0
    location = (i,j)
    if isRobot or _getPath(m,i-1,j,path,failedPath) or _getPath(m,i,j-1,path,failedPath):
        path.append(location)
        return True
    failedPath.append(location)
    return False




def getPath(m):
    path = []
    failedPath =[]
    if _getPath(m, len(m)-1, len(m[0])-1, path, failedPath):
        return path
    else:
        return None

m = [[True,True,True,False],
         [False,True,False,True],
         [True,False,True,True]]

checkPath(m)
getPath(m)









