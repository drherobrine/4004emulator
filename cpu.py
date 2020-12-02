from nybble import Nybble as n

rom = open('mem.rom', 'rb')

accumulator = rom.read()
rom.close()
print(accumulator)
