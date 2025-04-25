import random
cols=int(input("enter the no.of coloumns:"))
rows=int(input("enter the no.of rows"))
grid = []
for i in range(rows):
    row = []
    for j in range(cols):
        num = random.randint(0, 99)
        row.append(num)
    grid.append(row)
print("\nGenerated Grid:")
for row in grid:
    print(" ".join(str(num).rjust(2) for num in row))
    
outer_sum=0
inner_sum=0
for i in range(rows):
    for j in range(cols):
        if i==0 or i==rows-1 or j==0 or j==cols-1:
            outer_sum+=grid[i][j]
        else:
            inner_sum+=grid[i][j]

print("inner sum{}".format(inner_sum))
print("outer sum {}".format(outer_sum))
