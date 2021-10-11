# 產生一個隨機數字1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random

r = random.randint(1, 100)
count = 0

while True:
	count += 1 # count = count + 1
	num = input('請輸入一個1~100的整數: ')
	num = int(num)
	if num == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif r > num:
		print('太小了，猜大一點的數字!')
	else:
		print('太大了，猜小一點的數字!')
	print('這是你猜的第', count, '次')

