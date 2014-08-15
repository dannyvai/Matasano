import base64
import utils


HexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print "Starting with : " + HexString
buff = utils.HexString2ByteBuffer(HexString)
print "After HexString2ByteBuffer : " + buff
print "After base64Encode : " + base64.b64encode(buff)
print "After base64Decode : " + base64.b64decode(base64.b64encode(buff))
print "After base64Decode+ByteBuffer2HexString : \n" + utils.ByteBuffer2HexString(base64.b64decode(base64.b64encode(buff)))
#SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

