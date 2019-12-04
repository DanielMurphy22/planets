# looping over a range
print('Printing some numbers')
for ii in range(0,4):
    print(ii/2, ii//2)

# make a dictuionary from two lists
keys = ['a','b','c']
vals = list(range(3,9,2))
MyDict = dict(list(zip(keys,vals)))

# add a key if doesn't exist 
KeyToAdd = 'apple' # this is unicode (default str type in python 3)
ValToAdd = 8.5
if KeyToAdd not in MyDict:
    # add the apple key
    MyDict[KeyToAdd] = ValToAdd
    print('\nKey ({0:s}) added to dictionary'.format(KeyToAdd))

# iterate over dictionary and do some prints
for (k, v) in MyDict.items():
    if isinstance(k,str):
        print(k, v)

# remember in python 3 attributes like keys() and some functions like zip()
# do not return lists
print(type(list(MyDict.keys())))