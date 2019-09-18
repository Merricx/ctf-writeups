import string
from Crypto.Util.strxor import strxor
from pwn import *

context.log_level = 'warn'

while True:
    r = remote('crypto.chal.csaw.io', 1002)

    print r.recvline()
    #r.sendline('1000000000027013')
    r.sendline('1111111111149781')

    try:
        r.recvuntil('Encrypted flag:\n')

        ciphertext = []
        for _ in range(100):
            cip = r.recvline().strip('\n')
            ciphertext.append(cip)
    except:
        continue

    for i in range(len(ciphertext)):
        for j in range(len(ciphertext)):
            if len(ciphertext[i]) == len(ciphertext[j]) and len(ciphertext[i]) == 48:
                a =  ciphertext[i][-16:]
                b =  ciphertext[j][16:32]
                try:
                    k = strxor(a, '_0n_m3_l1kE_123}')
                    z = strxor(b, k)
                    #if all(c in string.printable for c in z):
                    if z.find('flag') > -1:
                        print z
                except:
                    continue