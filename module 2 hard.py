from random import randint

field1 = randint(3, 20)
print('ПОЛЕ №1 : ', field1)
print('ПОЛЕ №2 - пароль :  ', end='')
for x in range(1, field1):
    for y in range(1, field1):
        if field1 % (x + y) == 0:
            if x < y:
                result = (str(x)+str(y))
                print(result, end='')
