a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def evenlist(a):
    b=[i for i in a if i%2==0]
    print(b)
    
evenlist(a)
