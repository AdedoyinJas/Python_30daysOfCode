s = "Hello. I'm Edwin A.J, and you?"
words = s.split(' ')
print(words)
string = []
for word in words:
    string.insert(0, word)

print("Reverse statement:")
print(' '.join(string))