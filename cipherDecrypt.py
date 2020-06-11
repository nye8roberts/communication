#!/bin/python2
#decrypt

import random, binascii, os, time

binarySet = [0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1]

encryptedMessage = raw_input('Please write or paste in your encrypted binary message: ')

print 'Input: ' + encryptedMessage
key = input('Please enter key: ')
key = int(key)
print('Processing...')
time.sleep(5)
r = random.Random(key) # the number in the bracket is the key.
a = r.sample(binarySet, len(encryptedMessage) ) # will produce a cipherstream of the length of the user binary number (x)
print len(a)
a2 = ''.join(str(x) for x in a)
print 'Bitstream = ' + a2
xored = int(encryptedMessage, 2) ^ int(a2, 2) #this converts the binary strings to int format and XORs them together.
decrypted =  '{0:b}'.format(xored)
decryptedTwo = decrypted.zfill(len(a))
print 'Decrypted Binary = ' + decryptedTwo
text = ''.join(chr(int(decryptedTwo[i:i+8], 2)) for i in xrange(0, len(decryptedTwo), 8))
print 'Message: ' + text
