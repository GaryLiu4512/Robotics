grid = []

def printGrid():
    for row in grid:
        print(row)

def checkBalance():
    left = 0
    right = 0
row = input('Enter weights: ')
while row: 
    values =[int(x) for x in row.split()]
    grid.append(values)
    row = input('Enter weights: ')
printGrid()

#split the ship into two parts to make two lists

#left = mass of left side b*1 +a*2
#right = mass of right side d*1+ e*2
#if left!=right:
#print( the hsip is unbalanced)
#Else print( the ship is balacned
splitPoint = len(row//2)
for row in grid: 
    for values in row:
        print(values[:splitPoint])
        for values in splitPoint:
           row[0]  = splitPoint[0]*2
        left = row[0]+row[1]
nums = [1,4,3,7,]
result = 1
for num in nums:
    result = result*num
print(result)
        
        

row[0]*2
row[4]*2
