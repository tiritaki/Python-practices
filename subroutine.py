from random import sample
def rnd():
  res = sample(range(1, 10), 6)
  for i in res:
    if i==5:
        print("One of the numbers = 5")
    else: 
        print ("Sorry numbers are not 5, try again")

rnd()