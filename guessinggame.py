import time
import random
name1 =input("enter the player1")
name2=input("enter the player2")
print("Comp has fixed 5 number of integers in its mind")
print("you both have three turns each to guess it")
print("Ready for game?")
nums=[]
while(len(nums)!=5):
    a=random.randint(1,10)
    while(a in nums):
       
        a=random.randint(1,10)
    nums.append(a)
print(nums)
player1=[]
player2=[]
s1=0
s2=0
for i in range(3):
    print("Hai {} Guess your choice no {}.format(name,i+1")
    x=int(input())
    while(x in player1 or x in player2):
        print("already chose,so guess someother num")
        x=int(input())
    player1.append(x)    
    if x in nums:
        print("-->correct")
        s1+=1
    else:
        print("--> worng")
        
for i in range(3):
    print("Hai {} Guess your choice no {}.format(name,i+1")
    x1=int(input())
    while(x1 in player1 or x1 in player2):
        print("already chose,so guess someother num")
        x1=int(input())
    player2.append(x)    
    if x1 in nums:
        print("-->correct")
        s2+=1
    else:
        print("--> worng")

print("\n--- Game Summary ---")
print(f"{name1}'s guesses: {player1} | Score: {s1}")
print(f"{name2}'s guesses: {player2} | Score: {s2}")
print(f"Comp's numbers were: {nums}")
if s1 > s2:
    print(f"\n{name1} wins! ")
elif s2 > s1:
    print(f"\n{name2} wins! ")
else:
    print("\nIt's a tie! ")
