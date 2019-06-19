import test
def collatz(n):
    print(n)
    if n==1: return 0

    if n%2==1:
        return 1 + collatz(3*n+1)
    else:
        return 1 + collatz(int(n/2))


