def cyberPunks(data, n):
    letters = { 'A' : 1 ,  'B' : 2 , 'C' : 3 , 'D' : 4 , 'E' : 5  ,'F' : 6 ,  'G' : 7 , 'H' :8 , 'I' : 9 ,'J' : 10 , 'k' : 11 ,
                                         'L' : 12, 'M' : 13 ,  'N' : 14, 'O' : 15 , 'P' : 16 , 'Q' : 17 ,
                                                        'R' : 18 , 'S' : 19 , 'T' : 20 , 'U' : 21 , 'V' :22 , 'W' : 23 , 'X' :24 , 'Y': 25, 'Z' :26}
    output = ''
    for i in data:
        res = letters[i]
        tes = res + n
        for a, b in letters.items():
            if tes > 26:
                tes -= 26
            if b == tes:
                output += a
    return output

print(cyberPunks("PYTHON",5))


from collections import Counter,defaultdict
string = input("Enter your val:")
def word_counts(string):
    words = string.split()
    result = defaultdict(lambda : defaultdict(int))
    for i, word in enumerate(words):
        if i:
            result[words[i-1]].append(token)
    return {result: Counter() for word , words in rsult.iteritems()}
    
word_counts(string)
'''word = "adedoyin"
a = word.split()
for i in range(len((a))):
    print(i)'''