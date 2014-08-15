import struct
import re

def HexString2ByteBuffer(hex_str):
	buffer = ""
	for i in range(0,len(hex_str)/2):	
		cur_byte = hex_str[i*2:i*2+2]
		#print cur_byte,int(cur_byte,16),ord(struct.pack('B',int(cur_byte,16)))
		buffer = buffer + str(struct.pack('B',int(cur_byte,16)))
	return buffer

def ByteBuffer2HexString(byte_buff):
	buffer = ""
	for i in range(0,len(byte_buff)):
		buffer = buffer + str(hex(ord(byte_buff[i])))[2:]
	return buffer
	
def HexStringXorFrom2HexStrings(hex_str1,hex_str2):
	buffer = ""
	byte_buf1 = HexString2ByteBuffer(hex_str1)
	byte_buf2 = HexString2ByteBuffer(hex_str2)
	if len(byte_buf1) != len(byte_buf2):
		return buffer
		
	
	for i in range(0,len(byte_buf1)):
		xor_char = str(hex(ord(byte_buf1[i])^ord(byte_buf2[i])))[2:]
		if len(xor_char) == 2 :
			buffer = buffer + xor_char
		elif len(xor_char) == 1:
			buffer = buffer + '0' + xor_char
		
	return buffer
	
def HexStringXorWithByte(hex_str1,byte):
	buffer = ""
	byte_buf1 = HexString2ByteBuffer(hex_str1)

	for i in range(0,len(byte_buf1)):
		#print i
		xor_char = str(hex(ord(byte_buf1[i])^ord(byte)))[2:]
		if len(xor_char) == 2 :
			buffer = buffer + xor_char
		elif len(xor_char) == 1:
			buffer = buffer + '0' + xor_char
			
		#print str(hex(ord(byte_buf1[i])^ord(byte))),len(buffer)
	#print ord(byte)
	return buffer

def ByteStringXorWithByte(byte_buf1,byte):
	buffer = ""
	
	for i in range(0,len(byte_buf1)):
		buffer = buffer + str(hex(ord(byte_buf1[i])^ord(byte)))[2:]
	#print ord(byte)
	return buffer
	
def isStringMakesSense(byte_buf):
	m = re.match('([a-zA-Z0-9\']+\s){2,}',byte_buf)
	if m is not None and  m.group(0) is not None and len(m.group(0))>0:
		#print m.group(0)
		return True

