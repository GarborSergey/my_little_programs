import random

abc = "qwertyuiopasdfghjklzxcvbnm"
ABC = 'QWERTYUIOPASDFGHJKLZXCVBNM'
characters = '`!@#$%^&*(){}[]/.,<>?";_-:'
numbers = '1234567890'

string = abc + ABC + characters + numbers
length = 16
password = ''.join(random.sample(string, length))

print(password)