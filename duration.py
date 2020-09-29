import random
import string

def duration():
  num1 = random.randint(1, 16)
  print(num1)

  for x in range(1, num1):
    print(random.choice([1, x]))


duration()




