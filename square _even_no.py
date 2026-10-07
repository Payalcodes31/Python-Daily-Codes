from functools import reduce
numbers=[1,2,3,4,5]
even_no=filter(lambda x: x%2==0,numbers)
sq_no=map(lambda x: x*x,even_no)
total=reduce(lambda x,y:x+y,sq_no)
print(total)