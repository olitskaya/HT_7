# Програма-банкомат.
# Створити програму з наступним функціоналом:
# - підтримка 3-4 користувачів, які валіються парою ім'я/пароль (файл <users.data>);
# - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>)
# та історію транзакцій (файл <{username}_transactions.data>);
# - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених
# даних (введено число; знімається не більше, ніж є на рахунку).
# Особливості реалізації:
# - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру
# з балансом);
# - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець
# файла;
# файл з користувачами: тільки читається.
# Якщо захочете реалізувати функціонал додавання нового корситувача - не стримуйте
# себе :)
# Особливості функціонала:
# - за кожен функціонал відповідає окрема функція;
# - основна функція - <start()> - буде в собі містити весь workflow банкомата:
# - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні
# - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім
# вже закінчити роботу - все на ентузіазмі :) )
# - потім - елементарне меню типа:
# Введіть дію:
# 1. Продивитись баланс
# 2. Поповнити баланс
# 3. Вихід
# - далі - фантазія і креатив :)

import json

def users():
	user1 = {'login': 'Alex', 'password': '1111'}
	user2 = {'login': 'Anna', 'password': '2222'}
	user3 = {'login': 'Mark', 'password': '3333'}
	users = [user1, user2, user3]
	filename = 'users.data'
	with open(filename, 'w') as f:
		json.dump(users, f)

def balance():
	balance1 = 0
	filename = 'Alex_balance.data'
	with open(filename, 'w') as f:
		json.dump(balance1, f)
	balance2 = 100
	filename = 'Anna_balance.data'
	with open(filename, 'w') as f:
		json.dump(balance2, f)
	balance3 = 1000
	filename = 'Mark_balance.data'
	with open(filename, 'w') as f:
		json.dump(balance3, f)
	
def login_check(login):
	filename = 'users.data'
	with open(filename) as f:
		users = json.load(f)
	for user in users:
		if login == user['login']:
			return user	

def password_check(login, password):
	if password == login['password']:
		return True
	return False
	
def check_balance(user):
	filename = '{user}_balance.data'
	with open(filename) as f:
		balance = json.load(f)
	return balance

def withdraw(user, summ):
	filename = '{user}_balance.data'
	with open(filename) as f:
		balance = json.load(f)
	digit = summ.isdigit()
	if digit and summ > 0:
		if balance - summ >= 0:
			balance = balance - summ
			with open(filename, 'w') as f:
				json.dump(balance, f)
			return 'You withdrew {summ}.'
		else:
			return 'Not enough money!'
	else:
		print('Enter a positive number!')    

def replenishment(user, summ):
	filename = '{user}_balance.data'
	with open(filename) as f:
		balance = json.load(f)
	digit = summ.isdigit()
	if digit and summ > 0:
		balance = balance + summ
		with open(filename, 'w') as f:
			json.dump(balance, f)
		return 'You have deposited the amount {summ}.'
	else:
		print('Enter a positive number!')

def user_choice(choice, user):
    if choice == 1:
        print(f'Your balance: {check_balance(user)}.')
    elif choice == 2:
        summ = input('Amount to be withdraw:')
        trans = withdraw(user, summ)
        filename = '{user}_transactions.data'
        with open(filename, 'w') as f:
        	json.dump(summ, f)
        	f.write('\n')
        print(trans)
    elif choice == 3:
        summ = input('Enter the replenishment sum:')
        trans = g(user, summ)
        filename = '{user}_transactions.data'
        with open(filename, 'w') as f:
        	json.dump(summ, f)
        	f.write('\n')
        print(trans)     

def start():
	users()
	balance()
	login_test = str(input('Enter login:'))
	user = login_check(login_test)
	password_test = str(input('Enter password:'))
	if password_check(user, password_test):
		while True:
			choice = int(input('Select item:\n1. Check balance\n2. Withdraw money\n3. Deposit cash\n4. Exit\n\nYour choice:'))
			if choice == 4:
				break
			user_choice(choice, user)
	else:
		print('User {user} not found!')

start()
