x = [('hi', 'noun'), ('bad', 'adj'), ('run', 'verb'), ('bad', 'adj'), ('good', 'adj')]
y = []
for i, j in x:
    if j == 'adj':
        y.append(i)
print(y)
g = y.count("good")
b = y.count("bad")

if g == b:
    print('neutral')
elif g > b:
    print('positiver')
else:
    print('negative')
