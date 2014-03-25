def mini(inList):
    answer = None
    for item in inList:
        if answer == None:
            answer = item
        if item < answer:
            answer = item
    return (answer)