data = b"hello"
chk = 0
for b in data: chk ^= b
print("xor_checksum =", chk)
