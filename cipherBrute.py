#!/bin/python2
#decrypt

import random, binascii, os


binarySet = [0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1]

encryptedMessage = raw_input('Please write or paste in your encrypted binary message: ')

print 'Input: ' + encryptedMessage

print len(encryptedMessage)

count = 0

while count < 84094082034823480842938402895092854646523354737373757426356236256246462623613545154245949594598438545929598294295482592059258295060363060250295290340258920602498205:


    key = count


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

    count = count + 1


    #os.system("pause")

