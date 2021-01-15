# public key
e = 11
n = 117

# private key
d = 35
n = 117

# message
m = 10
print("Mesaage: ", m)
#operation
#m^e mod n
c = pow(m, e) % n
print("Encryption: ", c)

#decryption
#c^e mod n
print("Decryption: ", pow(c, e)% n)


