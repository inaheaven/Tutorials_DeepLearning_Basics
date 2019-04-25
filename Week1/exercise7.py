mydict = {'a': 20, 'b': 30, 'c':10}

# value bigger
byValues = sorted(mydict.values(), reverse =True)
print(byValues)

byKeys = sorted(mydict.keys(), reverse=True)
print(byKeys)

# show keys while sorted by valiues
keySortByValues = sorted(mydict, key=mydict.get, reverse=True)
print(keySortByValues)

