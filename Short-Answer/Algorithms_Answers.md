#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)the while loop is dependent on the increase of n. linear O(n)

b) we will be looping over n and while j is less than n we do the arithemetic problems which will repeatedly increase j    O(log n)
```
b)  sum = 0
    for i in range(n): Since it's a loop it gets linear O(n)
      j = 1
      while j < n: 
        j *= 2
        sum += 1
```


c) The running time would be O(n)

```
c)  def bunnyEars(bunnies): 
      if bunnies == 0: The base case constant / it will always return 0 once the recursive case hits 0
        return 0

      return 2 + bunnyEars(bunnies-1) This is recursion that is subtracting from n until it reaches 0 and then return the value + 2 O(n)
```

## Exercise II

f = min floor for eggs to break
n = stories in the building 
e = number of eggs you have
curr = current floor
broken  = 0
dropped = 0

There is a chance the the number of stories we loop through will be less than half so time complexity might be O(n)

def story(n): 
  for i in range(n): i would be the current floor your on
    while broken <= 1: you will only allow for one broken egg to know how high you can go without breaking them (constant)
      if i == n or i >= f: if the current floor is = to the number of stories or the floor where the eggs break and higher
        broken += 1
        e - broken
      else: Since you are testing how high you can go without breaking a egg you will still be losing eggs in the process
        dropped += 1
        e - dropped
    print("eggs": e, "floor": i - 1)  return whatever eggs are left and previous floor that is safe


