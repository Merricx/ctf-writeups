from pwn import *
import pollardsrho
from common import inverse_mod, tinycurve as curve

r = remote('crypto.chal.csaw.io', 1000)

r.recvuntil('a = ')
a = int(r.recvline().strip('\r\n'))
r.recvuntil('b = ')
b = int(r.recvline().strip('\r\n'))
r.recvuntil('p = ')
p = int(r.recvline().strip('\r\n'))
r.recvuntil('n = ')
n = int(r.recvline().strip('\r\n'))
r.recvuntil('Public key: (')
q = r.recvuntil(')').strip(')').replace(' ', '').split(',')
q[0] = int(q[0])
q[1] = int(q[1])
print 'Public key:', q

for i in range(1, 7919):
    coba = curve.mult(i, curve.g)
    if coba[0] == q[0] and coba[1] == q[1]:
        print 'Secret', i
        break

print r.interactive()