height = input('請輸入身高: ')
weight = input("請輸入體重: ")
h = int(height)/100
w = int(weight)

BMI = w/(h**2)
BMI = round(BMI, 2)

print('您的BMI為: ', BMI)

if BMI < 18.5:
    print('過輕')
elif 18.5 <= BMI < 24:
    print('正常')
elif 24 <= BMI < 27:
    print('過重')
elif 27 <= BMI < 30:
    print('輕度肥胖')
elif 30 <= BMI < 35:
    print('中度肥胖')
else:
    print('重度肥胖')    
