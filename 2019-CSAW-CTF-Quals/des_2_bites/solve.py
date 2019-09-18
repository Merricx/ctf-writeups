from Crypto.Cipher import DES
from itertools import izip, cycle

def xor(c, key):
    return "".join(chr(ord(x) ^ ord(y)) for (x,y) in izip(c, cycle(key)))

hexDict = {
    '0913334009133337':'0',
    '0913334009133338':'1',
    '0913334009133339':'2',
    '0913334009133340':'3',
    '0913334009133341':'4',
    '0913334009133342':'5',
    '0913334009133343':'6',
    '0913334009133344':'7',
    '0913334009133345':'8',
    '0913334009133346':'9',
    '0913334309133338':'a',
    '0913334309133339':'b',
    '0913334309133340':'c',
    '0913334309133341':'d',
    '0913334309133342':'e',
    '0913334309133343':'f'
}

def desDecrypt(input,key):
	cipher = DES.new(key, DES.MODE_OFB, '13371337')
	msg = cipher.decrypt(input)
	return msg

ciphertext = open('FLAG.enc').read()

ciphertext = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

decoded = ''
for c in ciphertext:
    decoded += hexDict[c]

decoded = decoded.decode('hex')

keys = [
    '0101010101010101',
    'fefefefefefefefe',
    'e0e0e0e0f1f1f1f1',
    '1f1f1f1f0e0e0e0e',
    '011F011F010E010E',
    '01E001E001F101F1',
    '01FE01FE01FE01FE',
    '1FE01FE00EF10EF1',
    '1FFE1FFE0EFE0EFE',
    'E0FEE0FEF1FEF1FE',
    '1F011F010E010E01',
    'E001E001F101F101',
    'FE01FE01FE01FE01',
    'E01FE01FF10EF10E',
    'FE1FFE1FFE0EFE0E',
    'FEE0FEE0FEF1FEF1',
    '01011F1F01010E0E',
    '0101E0E00101F1F1',
    '0101FEFE0101FEFE',
    '011F1F01010E0E01',
    '011FE0FE010EF1FE',
    '011FFEE0010EFEF1',
    '01E01FFE01F10EFE',
    'FE01E01FFE01F10E',
    '01E0E00101F1F101',
    '01E0FE1F01F1FE0E',
    '01FE1FE001FE0EF1',
    '01FEE01F01FEF10E',
    '01FEFE0101FEFE01',
    '1F01011F0E01010E',
    '1F01E0FE0E01F1FE',
    '1F01FEE00E01FEF1',
    '1F1F01010E0E0101',
    '1F1FE0E00E0EF1F1',
    '1F1FFEFE0E0EFEFE',
    '1FE001FE0EF101FE',
    '1FE0E01F0EF1F10E',
    '1FE0FE010EF1FE01',
    '1FFE01E00EFE01F1',
    '1FFEE0010EFEF101',
    '1FFEFE1F0EFEFE0E',
    'E00101E0F10101F1',
    'E0011FFEF1010EFE',
    'E001FE1FF101FE0E',
    'E01F01FEF10E01FE',
    'E01F1FE0F10E0EF1',
    'E01FFE01F10EFE01',
    'E0E00101F1F10101',
    'E0E01F1FF1F10E0E',
    'E0E0FEFEF1F1FEFE',
    'E0FE011FF1FE010E',
    'E0FE1F01F1FE0E01',
    'E0FEFEE0F1FEFEF1',
    'FE0101FEFE0101FE',
    'FE011FE0FE010EF1',
    'FE1F01E0FE0E01F1',
    'FE1FE001FE0EF101',
    'FE1F1FFEFE0E0EFE',
    'FEE0011FFEF1010E',
    'FEE01F01FEF10E01',
    'FEE0E0FEFEF1F1FE',
    'FEFE0101FEFE0101',
    'FEFE1F1FFEFE0E0E',
    'FEFEE0E0FEFEF1F1'
]

for i in keys:
    for j in keys:
        a = desDecrypt(decoded, i.decode('hex'))
        b = desDecrypt(a, j.decode('hex'))

        if b.find('flag') > -1:
            print b
            exit()