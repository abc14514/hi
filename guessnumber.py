import random

ans = random.randint(1,100)

x = 0

while True:
	x = x + 1
	guess = input('請輸入整數1~100 :')
	guess = int(guess)

	if ans == guess:
		print('終於猜對了!')
		print('這是第', x , '次猜數字')
		break		
	elif ans >= guess:
		print('比答案小')
	else:	
		print('比答案大')
		
	print('這是第', x , '次猜數字')