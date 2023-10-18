s = 'spam'
#s[1] = 'b'  # Ошибка
s = s[0] + 'b' + s[2:]
print(s)
