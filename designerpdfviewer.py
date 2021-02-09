import string
dictr = {}
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
s = 'abc'

for i, key in enumerate(string.ascii_lowercase):
    dictr[key] = h[i]
maxheight = 0
for i in s:
    value = dictr[i]
    maxheight = max(maxheight, value)

print(maxheight)
