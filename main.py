a = input()
b = input()
if a==b:
    print("Ок")
else:
    print("Не принято")

def p():
 "2"
a = int(input("Введите номер вашего места:"))
if a%2==0 and a<=36:
    print("Ваше место верхнее")
elif a%2!=0 and a<=36:
    print("Ваше место нижнее")
elif a%2 == 0 and a > 36 and a <= 54:
    print("Ваше место боковое сверху")
else:
    print("Ваше место боковое снизу")


def p2():
    "3"
    yer = int(input("Введите год:"))
    if yer % 4 == 0 and yer % 100 != 0:
        print("Год ", yer, " - високосный")
    else:
        print("Этот год не високосный")
    if yer % 400 == 0:
        print("Год ", yer, " - високосный")

"4"
def p3():

    a = input ("Введите один из трех цветов (красный, синиий, желтый):")
b = input ("Введите один из трех цветов (красный, синиий, желтый):")
r = 'красный'
bl = 'синий'
y = 'желтый'
if a == b:
    print ("Цвет не изменился!")
elif a == r and b == bl:
    print ("Получился фиолетовый!")
elif a == r and b == y:
    print ("Получился оранжевый!")
elif a == bl and b == y:
    print ("Получился зеленый!")
elif b == r and a == bl:
    print("Получился фиолетовый!")
elif b == r and a == y:
    print("Получился оранжевый!")
elif b == bl and a == y:
    print("Получился зеленый!")
else:
    print("Что-то пошло не так(")

p(), p2(), p3()