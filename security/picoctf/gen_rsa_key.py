import sys

# p = sys.argv[1]
# q = sys.argv[2]

p = 67867967
q = 73176001 



n = p * q
print("n calculated : ", n)


phi = (p-1) * (q-1)
print("phi calculated : ", phi)

def factorize(n):
    factors = []
    for i in range(2,int(n/2)+1):
        if(n%i == 0):
            # print("factor of ", n, " : ", i)
            factors.append(i)
    return factors

def isElementNotIn(num, arr):
    for i in arr:
        if(int(num) == int(i)):
            # print("Element is in!")
            return False
    print("Found coprime: ", num)
    return True
    
phi_factors = factorize(phi)
print("phi_factors : ", phi_factors)

def findCoprime(phi=phi, phi_factors=phi_factors):
    for i in range(1, phi):
        # print("finding factor for : ", i)
        e_factors = factorize(i)
        # print("for ", i, ", factors: ",e_factors)
        for e in e_factors:
            if (isElementNotIn(e, phi_factors)):
                return e

e = findCoprime()

print("e : ", e)

# emodphi = e % phi
# print("e mod phi : ", emodphi)

# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def findMulInverse(x,p):
    return pow(x, -1, p)

# def findMultiplicativeInverse(emodphi,phi): 
#     # need to work on
#     # not working
#     for i in range(0, phi):
#         if ((i * emodphi ) % phi == 1 ):
#             return i

d = findMulInverse(e, phi)
print("d : ", d)

print(" publilc key (e, n) : " , (e, n) )
print(" private key (d, n) : ", (d, n))

# output

# misthios@misthios:~/codeplay/coding_interview_questions/security/picoctf$ python3 gen_rsa_key.py 
# n calculated :  117
# phi calculated :  96
# phi_factors :  [2, 3, 4, 6, 8, 12, 16, 24, 32, 48]
# Found coprime:  5
# e :  5
# d :  77
#  publilc key (e, n) :  (5, 117)
#  private key (d, n) :  (77, 117)

    
