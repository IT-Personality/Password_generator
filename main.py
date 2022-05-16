import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
num = input('Введите количество паролей: ')
leng = input('Введите длину пароля: ')
num = int(num)
leng = int(leng)

for n in range(num):
	password = ''
	for i in range(leng):
		password += random.choice(chars)

	print(password)