import random
l = input("請輸入猜數字下限: ")
h = input("請輸數猜數字上限: ")
count = 0
l = int(l)
h = int(h)


r = random.randint(l, h)

while True :
	num = input("請猜數字：")
	num = int(num)
	count += 1
	if num == r :
			print("恭喜你猜對了！")
			print("你最後猜了", count, "次！" )
			break

	elif num > r :
			print("再低一點")

	else :
			print("再高一點")

	print("你已經猜了", count, "次了！" )		

