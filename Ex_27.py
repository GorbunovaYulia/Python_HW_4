'''
Задача №27. Общее обсуждение
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите,
сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells.
Output: 13
'''
user_list = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".upper().split()
print(user_list)
new_list = set(user_list)
print(len(new_list))