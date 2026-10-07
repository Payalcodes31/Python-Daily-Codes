def count_even(*num):
       even=0
       for n in num:
  	       if n%2==0:
	 	        even+=1
       print("Total even numbers:",even)
count_even(1,2,3,4,5)