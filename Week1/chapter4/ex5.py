"""4-5. Summing a Million: Make a list of the numbers from one to one million, and 
then use min() and max() to make sure your list actually starts at one and ends 
at one million. Also, use the sum() function to see how quickly Python can add 
a million numbers."""

one_milli = list(range(1,1000001))
print(f"minimum of list \n {min(one_milli)}")
print(f"maxmum of list \n {max(one_milli)}")
print(f"sum of list \n {sum(one_milli)}")