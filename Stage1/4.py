import utils

fd = open('4.txt','r')

line_idx = 0
matches = 0
for line in fd:
	line_idx = line_idx + 1
	HexString = line.rstrip()
	for i in range(0,255):
		if utils.isStringMakesSense(utils.HexString2ByteBuffer(utils.HexStringXorWithByte(HexString,chr(i)))):
			print utils.HexString2ByteBuffer(utils.HexStringXorWithByte(HexString,chr(i))),line_idx,i,chr(i)
			matches = matches + 1
			
print matches


#Now that the party is jumping line:171 byte:53 char:5