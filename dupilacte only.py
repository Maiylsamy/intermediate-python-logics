some = [12, 34, 65, 8, 65, 34, 12, 34]
dupicate = set([x for x in some if some.count(x) > 1])
print(dupicate)
