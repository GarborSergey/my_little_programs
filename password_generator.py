import random

abc = "qwertyuiopasdfghjklzxcvbnm"
ABC = 'QWERTYUIOPASDFGHJKLZXCVBNM'
characters = '`!@#$%^&*(){}[]/.,<>?";_-:'
numbers = '1234567890'

list_abc = list(abc)
list_ABC = list(ABC)
list_characters = list(characters)
list_numbers = list(numbers)

random.shuffle(list_abc)
random.shuffle(list_ABC)
random.shuffle(list_numbers)
random.shuffle(list_characters)

password_lenght = 12
list_password = []
for i in range(5):
    list_password.append(list_abc[i])
for i in range(3):
    list_password.append(list_ABC[i])
for i in range(3):
    list_password.append(list_characters[i])
list_password.append(list_numbers[0])
random.shuffle(list_password)
password = "".join(list_password)
print(password)
