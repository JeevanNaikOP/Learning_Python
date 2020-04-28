'''We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''

def make_chocolate(small, big, goal):
  if(goal>small+5*big): return -1
  if(goal==small+5*big): return small
  if(goal%5>small): return -1
  if(goal<10): return goal%5
  else:return goal-(big*5)
