
def knapsack(n, w, v):
    m=[]
    for i in range(len(w)):
        a = []
        for j in range(0,n+1):
            a.append(0)
        m.append(a)


    #initialize
    for j in range(1, n + 1):
        if j >= w[0]:
            m[0][j] = v[0]
    print(m)
    print(m[0])
    for i in range(1, len(w)):
        for j in range(1, n+1):
            if j >= w[i]:
                m[i][j] = max(m[i-1][j], m[i-1][j-w[i]]+v[i])
            else:
                m[i][j] = m[i-1][j]
    print m[i][j]

w =[23,31,29,44,53,38,63,85, 89, 82]
v=[92,57, 49, 68, 60, 43, 67, 84, 87, 72]
knapsack(165,w , v) #Expect 309

