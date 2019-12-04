# looping over a range
print('Printing some numbers')
for ii in xrange(0,4):
    print ii/2, ii//2

# make a dictuionary from two lists
keys = ['a','b','c']
vals = range(3,9,2)
MyDict = dict(zip(keys,vals))

# add a key if doesn't exist 
KeyToAdd = u'apple' # this is unicode (default str type in python 3)
ValToAdd = 8.5
if not MyDict.has_key(KeyToAdd):
    # add the apple key
    MyDict[KeyToAdd] = ValToAdd
    print '\nKey ({0:s}) added to dictionary'.format(KeyToAdd)

# iterate over dictionary and do some prints
for (k, v) in MyDict.iteritems():
    if isinstance(k,str):
        print k, v

# remember in python 3 attributes like keys() and some functions like zip()
# do not return lists
print type(MyDict.keys())