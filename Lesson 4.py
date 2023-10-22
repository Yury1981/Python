# Инструкция if-elif-else, проверка истинности, трехместное выражение if/else

if 1:
    print("true")
else:
    print("false")
input()

a = int(input())
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')
input()

A = 't' if 'spam' else 'f'
print(A)
