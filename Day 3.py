pes = []
def Palindrome(val):
    for i in range(11,val):
        if str(i)[::-1] == str(i):         
            pes.append(i)
    print(pes)  
    return len(pes)

print(Palindrome(500))


























'''def checkpali(start,stop,step=1):
    for x in range(start,stop,step):
        if str(x)==str(x)[::-1]:
            return x

print(checkpali(1,120,step=1))'''

'''def checkpali(s):
    s == str(s)
    return s == s[::-1]

def genpali(minx,maxx):
    pes=[]
    for i in range(minx,maxx + 1):
        if checkpali(i):
            pes.append(i)
    return pes

genpali(1,120)'''