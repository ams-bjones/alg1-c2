def mini(inList):
    answer = None
    for item in inList:
        if answer == None:
            answer = item
        if item < answer:
            answer = item
    return (answer)

def maxi(inList):
    answer = None
    for item in inList:
        if answer == None:
            answer = item
        if item > answer:
            answer = item
    return (answer)

def inList(size):
    inlist = []
    for i in range (size):
        inlist.append( int(input('please enter number {0} >'.format(i+1))))
    return (inlist)
    
myList = inList(5)
print (myList)
print (maxi(myList))
print(mini(myList))