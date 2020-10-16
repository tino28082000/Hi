#密碼重試程式
x = 3
password = "a123456"
while x > 0:
	pwd = input("請輸入密碼")

	if pwd == password :
		print("登入成功!")
		break

	else :
		x = x - 1
		print("登入失敗，你還有" , x , "次機會" )
	
	

	

