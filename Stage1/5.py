import utils

string = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
print len(string)
HexString = utils.ByteBuffer2HexString(string)
print HexString
print ""
I = utils.HexStringXorWithByte(HexString,'I')
print I
print ""
C = utils.HexStringXorWithByte(I,'C')
print C
print ""
E = utils.HexStringXorWithByte(C,'E')
print E
print ""
ICE_pattern = utils.ByteBuffer2HexString("ICE"*24+"IC")

print utils.HexStringXorFrom2HexStrings(HexString,ICE_pattern)
print len(utils.HexStringXorFrom2HexStrings(HexString,ICE_pattern))

#should be :0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f" :
#is : 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20690a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
#probably because of the new line that should be instad of the " "