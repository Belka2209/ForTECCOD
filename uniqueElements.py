def uniqueElements(myList):
    if type(myList) != list:
       return 'Error - введен не список'
    
    listElemNum = all([str(x).isdigit() for x in myList])
    if listElemNum != True:
        return 'Error - Список состоит не только из чисел'
    
    return list(set(myList))




    

