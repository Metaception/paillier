#!/usr/bin/env python
import sys
from paillier.paillier import *

pub = PublicKey.from_n(234211556871988559712772050416031298747)
priv = SpecialPrivateKey(234211556871988559682003437006366349696, 45032584017729125702641811226061628591)

if sys.argv[1] == 'encrypt':
	x = int(sys.argv[2], 16)
	print("x =", x)
	cx = encrypt(pub, x)
	print("cx =", cx)

if sys.argv[1] == 'decrypt':
	cx = int(sys.argv[2], 16)
	print("cx =", cx)
	x = decrypt(priv, pub, cx)
	print("x =", x)
