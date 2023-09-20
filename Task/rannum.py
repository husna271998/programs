#randint
#import random
#a=random.randint(1,10)
#print(a)
#random number
import random
def random_generator(a, b):
    while True:
        yield random.randint(a, b)
a = int(input("enter the starting range  "))
b = int(input("enter the ending   "))

random_num = random_generator(a, b)

for _ in range(5): 
    print(next(random_num))
