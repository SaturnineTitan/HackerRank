# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split(' '))
string = '.|.'

for i in range(1, n):
    if i%2 != 0:
        print((string*i).center(m, '-'))
    
print("WELCOME".center(m, '-'))

for i in reversed(range(1, n)):
    if i%2 != 0:
        print((string*i).center(m, '-'))

