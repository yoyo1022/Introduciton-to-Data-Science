print(False) # off
print(True) # on

print(7.7 > 8)
print(7.7 > 7)

print(type(False))
print(type(True))

print(type(7.7 > 8))
print(type(7.7 > 7))

print(7.7 == 8)
print(7.7 != 8)

id_last_digit = 7
id_last_digit % 2 != 0

print(not True)
print(not False)

print(not 7.7 != 8)
print(not 7.7 == 8)

print(5566.00 == 5566)
print(type(5566.00))
print(type(5566))

print(156 < 120) # False
print(7.7 > 7) # True

print(156 < 120 and 7.7 > 7)
print(156 < 120 or 7.7 > 7)

city = input("請輸入您所在的城市：")
weather = input("請輸入現在的天氣：")
print("我在{}，天氣{}".format(city, weather))

city = input("請輸入您所在的城市：")
weather = input("請輸入現在的天氣：")
tempc = input("請輸入現在的攝氏氣溫：")
tempc = int(tempc)
tempf = tempc*9/5 + 32

print("我在{}，天氣{}，攝氏{}度，華氏{}度".format(city, weather, tempc, tempf))

id_last_digit = input("請輸入您身分證字號的尾數：")
id_last_digit = int(id_last_digit)
print(id_last_digit)
print(type(id_last_digit))
modulo = id_last_digit % 2
ans = modulo == 1
print(ans)

print(float('5566'))
print(int('5566'))

print(int(False))
print(int(True))

print(float(False))
print(float(True))

print(bool(0))
print(bool(1))
print(bool(5566))
print(bool(55.66))

print(bool('False'))
print(bool('True'))

help(bin)

help(ord)

ord('A')

bin(ord('A'))