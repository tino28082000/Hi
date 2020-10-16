#BMI.py

print("BMI計算機")

h = input("請輸入你的身高(cm)： ")
w = input("請輸入你的體重(kg)： ")
h = float(h)
w = float(w)
BMI = w / (h * h / 10000)

print("你的BMI為：" , BMI)

if BMI >= 35 :
	print("重度肥胖")

elif BMI < 35 and BMI >= 30 : 
	print("中度肥胖")

elif BMI < 27 and BMI >= 24 :
	print("輕度肥胖")

elif BMI < 24 and BMI >= 18.5 :
	print("正常")

else :
	print("體重過輕")




