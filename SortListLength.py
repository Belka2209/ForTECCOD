# Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.

#Вариант 1 - Если получать список строк от пользователя и количество строк заранее не известно

numLines = int(input('Укажите какое количество строк вы хотите отсортировать?'))
listStrok = [input() for i in range(numLines)]
poIncreasing = sorted(listStrok, key=len, reverse=True) 
poDescending = sorted(listStrok, key=len, reverse=False) 
 
print('Список отсортирован по возрастанию: ', poIncreasing)
print('Список отсортирован по убыванию: ', poIncreasing)



#Вариант 2 - Если получать непосредственно список строк 

def sortMyList(my_list):
    if type(my_list) != list:
        return 'Error - необходимо передать список строк'
    poIncreasing = sorted(my_list, key=len, reverse=True) 
    poDescending = sorted(my_list, key=len, reverse=False)
    return  print(f'''Список отсортирован по возрастанию:  {poIncreasing}
Список отсортирован по убыванию: ' {poDescending}''')


my_list = listStrok
sortMyList(my_list)