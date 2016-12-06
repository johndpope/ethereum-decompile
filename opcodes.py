#!/usr/bin/python3

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

opcodes={
#0s: Stop and Arithmetic Operations

0x00:	["STOP","Halts execution"],
0x01:	["ADD","Addition operation"],
0x02:	["MUL","Multiplication operation"],
0x03:	["SUB","Subtraction operation"],
0x04:	["DIV","Integer division operation"],
0x05:	["SDIV","Signed integer"],
0x06:	["MOD","Modulo"],
0x07:	["SMOD","Signed modulo"],
0x08:	["ADDMOD","Modulo"],
0x09:	["MULMOD","Modulo"],
0x0a:	["EXP","Exponential operation"],
0x0b:	["SIGNEXTEND","Extend length of two's complement signed integer"],

#10s: Comparison & Bitwise Logic Operations

0x10:	["LT","Lesser-than comparison"],
0x11:	["GT","Greater-than comparison"],
0x12:	["SLT","Signed less-than comparison"],
0x13:	["SGT","Signed greater-than comparison"],
0x14:	["EQ","Equality  comparison"],
0x15:	["ISZERO","Simple not operator"],
0x16:	["AND","Bitwise AND operation"],
0x17:	["OR","Bitwise OR operation"],
0x18:	["XOR","Bitwise XOR operation"],
0x19:	["NOT","Bitwise NOT operation"],
0x1a:	["BYTE","Retrieve single byte from word"],

#20s: SHA3

0x20:	["SHA3","Compute Keccak-256 hash"],

#30s: Environmental Information

0x30:	["ADDRESS","Get address of currently executing account"],
0x31:	["BALANCE","Get balance of the given account"],
0x32:	["ORIGIN","Get execution origination address"],
0x33:	["CALLER","Get caller address. This is the address of the account that is directly responsible for this execution"],
0x34:	["CALLVALUE","Get deposited value by the instruction/transaction responsible for this execution"],
0x35:	["CALLDATALOAD","Get input data of current environment"],
0x36:	["CALLDATASIZE","Get size of input data in current environment"],
0x37:	["CALLDATACOPY","Copy input data in current environment to memory This pertains to the input data passed with the message call instruction or transaction"],
0x38:	["CODESIZE","Get size of code running in current environment"],
0x39:	["CODECOPY","Copy code running in current environment to memory"],
0x3a:	["GASPRICE","Get price of gas in current environment"],
0x3b:	["EXTCODESIZE","Get size of an account's code"],
0x3c:	["EXTCODECOPY","Copy an account's code to memory"],

#40s: Block Information

0x40:	["BLOCKHASH","Get the hash of one of the 256 most recent complete blocks"],
0x41:	["COINBASE","Get the block's beneficiary address"],
0x42:	["TIMESTAMP","Get the block's timestamp"],
0x43:	["NUMBER","Get the block's number"],
0x44:	["DIFFICULTY","Get the block's difficulty"],
0x45:	["GASLIMIT","Get the block's gas limit"],

#50s Stack, Memory, Storage and Flow Operations

0x50:	["POP","Remove item from stack"],
0x51:	["MLOAD","Load word from memory"],
0x52:	["MSTORE","Save word to memory"],
0x53:	["MSTORE8","Save byte to memory"],
0x54:	["SLOAD","Load word from storage"],
0x55:	["SSTORE","Save word to storage"],
0x56:	["JUMP","Alter the program counter"],
0x57:	["JUMPI","Conditionally alter the program counter"],
0x58:	["PC","Get the value of the program counter prior to the increment"],
0x59:	["MSIZE","Get the size of active memory in bytes"],
0x5a:	["GAS","Get the amount of available gas, including the corresponding reduction"],
0x5b:	["JUMPDEST","Mark a valid destination for jumps"],

#60s & 70s: Push Operations

0x60:	["PUSH1","Place 1-byte item on stack"],
0x61:	["PUSH2","Place 2-byte item on stack"],
0x62:	["PUSH3","Place 3-byte item on stack"],
0x63:	["PUSH4","Place 4-byte item on stack"],
0x64:	["PUSH5","Place 5-byte item on stack"],
0x65:	["PUSH6","Place 6-byte item on stack"],
0x66:	["PUSH7","Place 7-byte item on stack"],
0x67:	["PUSH8","Place 8-byte item on stack"],
0x68:	["PUSH9","Place 9-byte item on stack"],
0x69:	["PUSH10","Place 10-byte item on stack"],
0x6a:	["PUSH11","Place 11-byte item on stack"],
0x6b:	["PUSH12","Place 12-byte item on stack"],
0x6c:	["PUSH13","Place 13-byte item on stack"],
0x6d:	["PUSH14","Place 14-byte item on stack"],
0x6e:	["PUSH15","Place 15-byte item on stack"],
0x6f:	["PUSH16","Place 16-byte item on stack"],
0x70:	["PUSH17","Place 17-byte item on stack"],
0x71:	["PUSH18","Place 18-byte item on stack"],
0x72:	["PUSH19","Place 19-byte item on stack"],
0x73:	["PUSH20","Place 20-byte item on stack"],
0x74:	["PUSH21","Place 21-byte item on stack"],
0x75:	["PUSH22","Place 22-byte item on stack"],
0x76:	["PUSH23","Place 23-byte item on stack"],
0x77:	["PUSH24","Place 24-byte item on stack"],
0x78:	["PUSH25","Place 25-byte item on stack"],
0x79:	["PUSH26","Place 26-byte item on stack"],
0x7a:	["PUSH27","Place 27-byte item on stack"],
0x7b:	["PUSH28","Place 28-byte item on stack"],
0x7c:	["PUSH29","Place 29-byte item on stack"],
0x7d:	["PUSH30","Place 30-byte item on stack"],
0x7e:	["PUSH31","Place 31-byte item on stack"],
0x7f:	["PUSH32","Place 32-byte (full word) item on stack"],

#80s: Duplication Operations

0x80:	["DUP1","Duplicate 1st stack item"],
0x81:	["DUP2","Duplicate 2nd stack item"],
0x82:	["DUP3","Duplicate 3rd stack item"],
0x83:	["DUP4","Duplicate 4th stack item"],
0x84:	["DUP5","Duplicate 5th stack item"],
0x85:	["DUP6","Duplicate 6th stack item"],
0x86:	["DUP7","Duplicate 7th stack item"],
0x87:	["DUP8","Duplicate 8th stack item"],
0x88:	["DUP9","Duplicate 9th stack item"],
0x89:	["DUP10","Duplicate 10th stack item"],
0x8a:	["DUP11","Duplicate 11th stack item"],
0x8b:	["DUP12","Duplicate 12th stack item"],
0x8c:	["DUP13","Duplicate 13th stack item"],
0x8d:	["DUP14","Duplicate 14th stack item"],
0x8e:	["DUP15","Duplicate 15th stack item"],
0x8f:	["DUP16","Duplicate 16th stack item"],

#90s: Exchange Operations

0x90:	["SWAP1","Exchange 1st and 2nd stack items"],
0x91:	["SWAP2","Exchange 1st and 3rd stack items"],
0x92:	["SWAP3","Exchange 1st and 4th stack items"],
0x93:	["SWAP4","Exchange 1st and 5th stack items"],
0x94:	["SWAP5","Exchange 1st and 6th stack items"],
0x95:	["SWAP6","Exchange 1st and 7th stack items"],
0x96:	["SWAP7","Exchange 1st and 8th stack items"],
0x97:	["SWAP8","Exchange 1st and 9th stack items"],
0x98:	["SWAP9","Exchange 1st and 10th stack items"],
0x99:	["SWAP10","Exchange 1st and 11th stack items"],
0x9a:	["SWAP11","Exchange 1st and 12th stack items"],
0x9b:	["SWAP12","Exchange 1st and 13th stack items"],
0x9c:	["SWAP13","Exchange 1st and 14th stack items"],
0x9d:	["SWAP14","Exchange 1st and 15th stack items"],
0x9e:	["SWAP15","Exchange 1st and 16th stack items"],
0x9f:	["SWAP16","Exchange 1st and 17th stack items"],

#a0s: Logging Operations

0xa0:	["LOG0","Append log record with no topics"],
0xa1:	["LOG1","Append log record with one topic"],
0xa2:	["LOG2","Append log record with two topics"],
0xa3:	["LOG3","Append log record with three topics"],
0xa4:	["LOG4","Append log record with four topics"],

#f0s: System operations

0xf0:	["CREATE","Create a new account with associated code"],
0xf1:	["CALL","Message-call into an account"],
0xf2:	["CALLCODE","Message-call into this account with alternative account's code"],
0xf3:	["RETURN","Halt execution returning output data"],
0xf4:	["DELEGATECALL","Message-call into this account with an alternative account's code, but persisting the current values for `sender` and `value`"],

#Halt Execution, Mark for deletion

0xff:	["SUICIDE","Halt execution and register account for later deletion"]}

