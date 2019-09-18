from Crypto.Cipher import DES
import binascii

IV = '13371337'

def getNibbleLength(offset):	
	if str(offset)[0]=="9":
		return len(str(offset))+1
	return len(str(offset))

def duck(aChr):
	try:
		return int(aChr)
	except:
		return "abcdef".index(aChr)+11

def encodeText(plainText,offset):
	hexEncoded = plainText.encode("hex")
	nibbleLen = getNibbleLength(offset)
	output = ""
	for i in range(0,len(hexEncoded),2):
		hexByte = hexEncoded[i:i+2]
		try: 
			output += str(duck(hexByte[0]) + offset).rjust(nibbleLen,"0")
			output += str(duck(hexByte[1]) + offset).rjust(nibbleLen,"0")
		except:
			continue
	return output

def padInput(input):
	bS = len(input)/8
	if len(input)%8 != 0:
		return input.ljust((bS+1)*8,"_")	
	return input
	
def desEncrypt(input,key):
	cipher = DES.new(key, DES.MODE_OFB, IV)
	msg = cipher.encrypt(padInput(input))
	return msg
		
def createKey(hex,fileName):
	with open(fileName, 'wb') as f:
		f.write(binascii.unhexlify(hex))

def createChallenge():
	createKey("0101010101010101","key1")
	createKey("fefefefefefefefe","key2")

	plainText = open('DES2Bytes.txt').read()
	key1 = open('key1').read()

	byte = desEncrypt(plainText,key1)
	print byte.encode('hex')
	key2 = open('key2').read()

	cipherText = desEncrypt(byte,key2)
	print cipherText.encode('hex')
	cipherText = encodeText(binascii.hexlify(cipherText),9133337)
	with open('DES2Bytes.enc2', 'w') as f:
		f.write(cipherText)

createChallenge()