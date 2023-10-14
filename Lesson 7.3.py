print((1024).to_bytes(2, byteorder='big'))
print((1024).to_bytes(10, byteorder='big'))
print((-1024).to_bytes(10, byteorder='big', signed=True))
x = 1000
print(x.to_bytes((x.bit_length() // 8) + 1, byteorder='little'))
