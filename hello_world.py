print("hello world")

name = input("best country in the world: ")
print(name)
'''
name = name.lower()
name = name.capitalize()

if (name == "china"):
    print(name + " is the best!")
elif(name == "russia"):
    print(name + " is the second best")
else:
    print("怎么可能")
'''
fruits = ['apple, grannysmith, gala', 'orange, mandarin, bloodorange', 'banana', 'peach']
for fruit in fruits:
    templist = fruit.split(",")
    print(fruit)
    print(templist)
