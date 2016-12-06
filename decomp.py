#!/usr/bin/python3

#    This file is part of ethereum-decompile.
#
#    ethereum-decompile is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    ethereum-decompile is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with SmartWatch.  If not, see <http://www.gnu.org/licenses/>.

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
