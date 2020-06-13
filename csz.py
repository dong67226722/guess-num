import random

start = input("请输入猜数字的开始值:")
end = input("请输入猜数字的结束值:")
start = int(start)
end = int(end)

i = 0
x = random.randint(start, end)
while True:
	i = i + 1
	inp = int(input("请猜数字："))
	if inp == x:
		print("猜对了！")
		print("这是第", i,"次猜了！")
		break
	elif inp > x:
		print("比数字大哦，请重猜！")
	else:
		print("比数字小，重猜！")
	print("这是第", i,"次猜了！")