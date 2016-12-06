# ethereum-decompile
Decompiles ethereum bytecode into (marginally) more readable assembly

Will be updated with more detailed descriptions of the opcodes
## How to use:
* Clone this repo
* `cd` into its directory
* `cat <bytecode> | python3 decomp.py` to print helpful descriptions to stdout

The bytecode can be generated with `solcjs contract.sol --bin` or similar.
