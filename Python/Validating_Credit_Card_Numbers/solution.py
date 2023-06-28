# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

# Credit card pattern 
pattern = r"^[456][\d]{15}$|^[456][\d]{3}-[\d]{4}-[\d]{4}-[\d]{4}$"

# For each credit card number, validate against pattern and check for repeating digits 
for x in range(int(input())):
    credit_card = input().strip()
    
    if re.match(pattern, credit_card) and not re.search(r"(\d)(-?\1){3}", credit_card):
        print("Valid")
    else:
        print("Invalid")
        
