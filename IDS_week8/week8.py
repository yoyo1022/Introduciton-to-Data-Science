player_height = float(input("請輸入球員身高(公尺):"))
player_weight = float(input("請輸入球員體重(公斤):"))
player_bmi = player_weight / player_height**2
bmi_label = None
if player_bmi > 30:
    bmi_label = 'Obese'
if player_bmi <= 30 and player_bmi > 25:
    bmi_label = 'Overweight'
if player_bmi <= 25 and player_bmi > 18.5:
    bmi_label = 'Normal weight'
if player_bmi <= 18.5:
    bmi_label = 'Underweight'
print(player_bmi)
print(bmi_label)

if True:
    print("First branch")
elif True:
    print("Second branch")
elif True:
    print("Third branch")

user_int = int(input("請輸入一個正整數:"))
if user_int % 3 == 0:
    print("Fizz")
if user_int % 5 == 0:
    print("Buzz")

user_int = int(input("請輸入一個正整數:"))
if user_int % 15 == 0:
    print("Fizz Buzz")
elif user_int % 5 == 0:
    print("Buzz")
elif user_int % 3 == 0:
    print("Fizz")
else:
    print(user_int)

i = 1
counter = 0
while i <= 10:
    counter += 1
    i += 1
print(counter)

i = 1
counter = 0
while i <= 10:
    if i % 2 == 0:
        counter += 1
    i += 1
print(counter)

i = 1
summation = 0
while i <= 100:
    summation += i
    i += 1
print(summation)

x = int(input("請輸入起始的正整數:"))
y = int(input("請輸入終止的正整數"))
i = x
while i <= y:
    print(i)
    i += 1

x = int(input("請輸入起始的正整數:"))
y = int(input("請輸入終止的正整數"))
i = x
while i <= y:
    if i % 2 == 1:
        print(i)
    i += 1 