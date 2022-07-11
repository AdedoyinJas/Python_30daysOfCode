def magicsquare(mat):
    n = len(mat)
    #sum1 and sum2 are the sum of the two diagonals
    sum1 = 0
    sum2 = 0
    for i in range(n):
        #(i,i) is the diagonal from topleft to bottomright
        #(i , n - i - 1) is the diagonal from topright to bottomleft
        sum1 += mat[i][i]
        sum2 +=mat[i][n-i-1]
        #if the two diagonal sums are unequal then it is not a magic square
        if not(sum1==sum2):
            return False
        for i in range(n):
            #sumr is rowsum and sumc is colsum
            sumr = 0
            sumc = 0
            for j in range(n):
                sumr+=mat[i][j]
                sumc+=mat[j][i]
            if not(sumr==sumc==sumd1):
                return False
            #if all the conditions are satisfied then it is a magic square
        return True

mat = [[2,7,6] , [9,5,1], [4,3,8]]

if (magicsquare(mat)):
    print('Magic Square')
else:
    print('Not a magic square')