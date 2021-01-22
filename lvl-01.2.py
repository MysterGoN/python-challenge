# Start page: http://www.pythonchallenge.com/pc/def/274877906944.html

# 2. Decrypt by string.maketrans

cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
transtab = str.maketrans(intab, outtab)

print(cipher.translate(transtab))

# 3. Decrypt url
cipher = 'map'

print(cipher.translate(transtab))
