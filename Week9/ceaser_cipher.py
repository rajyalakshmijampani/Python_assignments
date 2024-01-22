import string

shift = 3

l = list(string.ascii_lowercase)
d = {}
for i in range(len(l)):
  d[l[i]] = l[(i + shift) % 26]

f = open('Week9/secret_message.txt', 'r')
g = open('Week9/encoded_message.txt', 'w')
letter = f.read(1)
print(letter)
while letter != '':
  g.write(d[letter])
  letter = f.read(1)
f.close()
g.close()
