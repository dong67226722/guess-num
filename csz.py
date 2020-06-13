import random

i = 0
x = random.randint(1,100)
while True:
	inp = int(input("请猜数字："))
	if inp == x:
		print("猜对了！")
		break
	elif inp > x:
		print("比数字大哦，请重猜！")
	else:
		print("比数字小，重猜！")
	i = i + 1
	print("第", i,"次猜了！")