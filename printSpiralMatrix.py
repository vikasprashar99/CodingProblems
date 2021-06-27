def printSpiralMatrix():    
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    minr=0
    minc=0
    maxr=len(matrix)-1
    maxc=len(matrix[0])-1
    count=(maxr+1)*(maxc+1)
    tcount=0
    ar=[]
    
    while(tcount<count):
                    # top wall
        for i in range(minc,maxc+1 or tcount<count):
            if(tcount<count):
                ar.append(matrix[minr][i])
                tcount+=1
        minr+=1
                  # right wall
        for i in range(minr,maxr+1 or tcount<count):
            if(tcount<count):
                ar.append(matrix[i][maxc])
                tcount+=1
        maxc-=1
    
                # bottom wall
        for i in range(maxc,minc-1,-1 or tcount<count):
            if(tcount<count):
                ar.append(matrix[maxr][i])
                tcount+=1
        maxr-=1
    
                # left wall
        for i in range(maxr,minr-1,-1 or tcount<count):
            if(tcount<count):
                ar.append(matrix[i][minc])
                tcount+=1
        minc+=1
    return ar
printSpiralMatrix()
    
