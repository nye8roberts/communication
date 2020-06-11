#!/bin/python2

import random, smtplib
#cipherstream

binarySet = [0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1]

print len(binarySet)

test = raw_input('Enter text to be converted: ')

x = ' '.join(format(ord(x), 'b').zfill(8) for x in test) #converts text to binary, seperated into bytes.

x = x.replace(' ', '') #the spaces need removing from the binary sequence. This is how.

print x.zfill(len(x)) #this prints the binary sequence, without the spaces.
print len(x)
#x2 = list(x) #the binary sequence is converted to a list called x2. This means that both cipherstream and binary message can be XORed later.

key = int(raw_input('Enter Key: '))

#print x2

r = random.Random(key) # the number in the bracket is the key.

a = r.sample(binarySet, len(x) ) # will produce a cipherstream of the length of the user binary number (x)



a2 = ''.join(str(x) for x in a) #this converts the set to a string and joins the binary digits together so they are in the same format as x, the users binary input.

#a2.zfill(len(x))

xored = int(x, 2) ^ int(a2, 2) #this converts the binary strings to int format and XORs them together.

ciphertext =  '{0:b}'.format(xored) #makes sure ciphertext is in binary format.

ciphertextTwo = ciphertext.zfill(len(x)) #ensures leading zeros are not missing

print ciphertextTwo

print len(ciphertextTwo)

#decrypt = int(ciphertext, 2) ^ int(a2, 2)

#decrypt2 = '{0:b}'.format(decrypt)

#print decrypt2

#---------------------------------------------------------------------------------
#server = smtplib.SMTP('smtp.gmail.com', 587)

#server.starttls()

#passwd = raw_input('Enter password: ')

#message = ciphertext

#server.login('nye8roberts@gmail.com', passwd)

#server.sendmail('nye8roberts@gmail.com', 'nye8roberts@protonmail.com', message)

