import sys

domainKnown = False
domainLength  = 53

message = 'mCHPybBvPcbgrrjHUjePgPvBkwrjPvhGvyByhyBsHPcBwbjVPugvPhvjfePGhyPuBybPgPvk'


def bf(message, domain):
    print('Taking domain to be: ', domain)
    for key in range(len(domain)):
        translated = ""
        for i in message:
            if (i == " "):
                translated += " "
            else: 
                try: 
                    index = domain.index(i)
                    rotated_index  =  (index + key) % len(domain)
                    translated += domain[rotated_index]
                except Exception as e:
                    print(e)
                    print("message char ", i , " not found in domain! exiting.")
                    #sys.exit()
                    break
    
        print("For key value ", key, ", message : ", translated)





if(domainKnown):
    domain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bf(message, domain)
else :
    # if domain is unknown
    # we will have to brute force domain also
    for i in range(0, 128-domainLength):
        domain = "".join([chr(x) for x in range(i, i + domainLength) ])
        bf(message, domain)



        

