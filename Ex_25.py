'''
Задача №25. 
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''
#user_list = input("Введите строку: ")
#user_list = user_list.split()
user_list = "a a a b c a a b b d c d d".split()
print(user_list)
new_dist = {}
for i in user_list:
    if i in new_dist:
        print(f'{i}_{new_dist[i]}', end= " ")
        new_dist[i] += 1
    else:
        new_dist[i] = 1
        print(i, end=" ")
