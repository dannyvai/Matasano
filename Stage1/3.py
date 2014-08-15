import utils

HexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
#print utils.HexString2ByteBuffer(HexString)
for i in range(0,255):
	if utils.isStringMakesSense(utils.HexString2ByteBuffer(utils.HexStringXorWithByte(HexString,chr(i)))) :
		print utils.HexString2ByteBuffer(utils.HexStringXorWithByte(HexString,chr(i)))
	
#print utils.HexString2ByteBuffer(utils.HexStringXorWithByte(HexString,'X'))