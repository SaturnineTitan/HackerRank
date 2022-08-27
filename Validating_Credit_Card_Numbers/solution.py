# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

N = int(input())
pattern = r"^[456][\d]{15}|^[456][\d]{3}-[\d]{4}-[\d]{4}-[\d]{4}$"
no_repeats = r"" # under construction 
filters = [pattern, no_repeats]

for x in range(N):
    credit_card = input()
    if all(re.match(f, credit_card) for f in filters):
        print("Valid")
    else:
        print("Invalid")
    
