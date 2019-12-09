country = input('請問你是哪國人：')
age = input('請輸入年齡：')
age = int(age)
if country == '台灣':   ##要是國籍是台灣 如果不是那就部會印出任何東西
  if age >= 18:
    print('你可以考駕照')
  else: 
    print('你還不能考駕照')
elif country == '美國':   ##要是國籍是美國 如果不是那就部會印出任何東西
  if age >= 16:
    print('你可以考駕照')
  else: 
    print('你還不能考駕照')
