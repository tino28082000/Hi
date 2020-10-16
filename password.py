#密碼重試程式
x = 2
while True:
	password = input("請輸入密碼")

	if password == "a123456" :
		print("登入成功")
		break

	else :
		print("你還有" , x , "次機會" )
		
		x = x - 1

	if x < 0 :
		break

	

