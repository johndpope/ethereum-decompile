#!/usr/bin/python3

import sys
import opcodes

def fetchByte():
	return sys.stdin.buffer.read(2)

def bytes():
	while True:
		byte=fetchByte()
		if not byte:
			break
		yield byte

for x in bytes():
	if(x==b'\n'):
		break
	code=int(x.decode(),16)
	# if we have a push instruction, we must read bytes from the byte array for its argument
	arg=''.join(["0x%s"%fetchByte().decode()for i in range(0x60,code+1)])if(0x60<=code<=0x7f)else''
	print(
		hex(code),
		opcodes.opcodes[code][0],
		"\t|\t",
		arg,
		"\t;\t",
		opcodes.opcodes[code][1])
