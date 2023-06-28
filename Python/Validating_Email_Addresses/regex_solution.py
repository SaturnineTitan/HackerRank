import re 
# One-liner for solving the problem. Regex import required. 
def fun(s):
    return  re.fullmatch(r'([0-9a-zA-Z\_\-]+)\@([a-zA-Z0-9]+)\.([a-zA-Z]{1,3})', s)
