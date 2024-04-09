def primeNumbers(num1, num2):
    if type(num1) != int or type(num2) != int:
        return 'Error - данные введены не верно, обе переменных должны быть числами'
   
    listNum = sorted([num1, num2])
    result = []

    for i in range(listNum[0], (listNum[1]+1)):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag and i != 1: 
            result.append(i)
    return result        


print(primeNumbers(1,5))


