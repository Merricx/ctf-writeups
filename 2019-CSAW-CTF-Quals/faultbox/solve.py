import gmpy, random
from pwn import *
from Crypto.Util.number import *

def encrypt_flag():
    r.recvuntil('4. encrypt\n====================================\n')
    r.sendline('1')
    return int(r.recvline().strip('\n'), 16)

def encrypt_fake_flag_crt():
    r.recvuntil('4. encrypt\n====================================\n')
    r.sendline('3')
    return int(r.recvline().strip('\n'), 16)

def encrypt(plaintext):
    r.recvuntil('4. encrypt\n====================================\n')
    r.sendline('4')
    r.recvuntil('input the data:')
    r.sendline(plaintext)

    return int(r.recvline().strip('\n'), 16)

def get_modulus():
    e = 0x10001
    print "[+] Leaking Modulus..."
    try:
        m_list = [2, 3, 5, 7]
        mod_list = [(encrypt(long_to_bytes(m_list[i]))) - (m_list[i]**e) for i in range(4)]
        _GCD = mod_list[0]
        for i in range(4):
            _GCD = GCD(_GCD, mod_list[i])
        return _GCD
    except Exception as ex:
        print "[-] Exception: ", ex

def get_p(N):
    print "[+] Performing RSA-CRT Fault Attack..."
    fault_c = encrypt_fake_flag_crt()
    for i in range(50, 500):
        fake_flag = 'fake_flag{%s}' % (('%X' % i).rjust(32, '0'))
        c = encrypt(fake_flag)
        check = GCD(fault_c - c, N)
        if isPrime(check) and check != 2:
            return check

    print "[-] p not found :("
    return None



while True:
    try:
        r = remote('crypto.chal.csaw.io', 1001)
        #r = remote('0.0.0.0', 23333)

        N = get_modulus()
        print N

        p = get_p(N)

        if p is None:
            exit()
        print p

        q = N // p
        phi = (p-1) * (q-1)
        d = inverse(0x10001, phi)

        enc_flag = encrypt_flag()
        print "[+] Encypted flag:", enc_flag

        flag = pow(enc_flag, d, N)

        print "[+] FLAG:", long_to_bytes(flag)
        exit()
    except:
        continue