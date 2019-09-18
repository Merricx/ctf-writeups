from pwn import *

def split_block(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

r = remote('crypto.chal.csaw.io', 1003)

def encrypt(s):
    r.recvline()
    r.recvuntil('Tell me something: ')
    r.sendline(s+'\n')
    r.recvline()
    r.recvline()
    response = r.recvline().strip('\r\n')

    return response

# get block length
print '[*]', 'Get prefix offset...'
offset = 1
prefix_pad = ''
prev_first_block = ''
flag_len = 45
while True:
    response = encrypt('a'*offset)
    blocks = split_block(response, 32)
    if prefix_pad == '' and prev_first_block == blocks[0]:
        prefix_pad = 'A' * (offset-1)

    prev_first_block = blocks[0]

    if len(blocks) > 4:
        break
    offset += 1
    
# Enumerating flag
n = 29+13
flag = 'flag{y0u_kn0w_h0w_B10cks_Are_n0T_r31iab13'
while True:
    no_found = True
    current_block_pos = 4
    dummy = 'A' * (64 - n)

    for k in '_abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}!@#$%^&*-?/,.<>;':

        payload = prefix_pad + dummy + flag + k + dummy
        response = encrypt(payload)

        blocks = split_block(response, 32)
        if blocks[current_block_pos] == blocks[current_block_pos+4]:
            flag += k
            print '[+] FLAG:', flag
            no_found = False
            break

    n += 1
    if no_found:
        break

print '[+] FLAG: ',flag