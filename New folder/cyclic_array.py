def calPascal(i, j):
    
    if j == 0 or j == i:
        
        return 1
        
    else:
        
        return calPascal(i - 1, j - 1) + calPascal(i - 1, j)


def printPascal(n):
    
    triangle = []
    
    for i in range(n):
        
        add = []
        
        for j in range(i+1):
            
            add.append(calPascal(i, j))
            
        triangle.append(add)
        
    return triangle
