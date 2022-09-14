import random

ans = random.randint(1,100)

while True:
	guess = input('請輸入整數1~100 :')
	guess = int(guess)

	if ans == guess:
		print('終於猜對了!')
		break
	elif ans >= guess:
		print('比答案小')
	else:
		print('比答案大')