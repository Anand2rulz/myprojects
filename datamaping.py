import random
team=int(input("enter no.of teams"))
print("enter team names:")
teams=[]
for i in range(team):
    teams.append(input())
m=int(input("Enter no of meetings"))
matches=[]
for i in range(team-1):
    for j in range(i+1,team):
        for k in range(m):
            matches.append((teams[i],teams[j]))


random.shuffle(matches)
no=1
for i in matches:
    print("match {} : {} vs {}".format(no,i[0],i[1]))
    print()
    no+=1

