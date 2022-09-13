M = input("import Message\n")
#print(M)
K = input("input Your key Code\n")
C = ""
D = ""

K*=int(len(M)/len(K)+1)
#print(K)

for i in range(len(M)):
    code_num = ord(M[i])
    #print(code_num, "codenum")
    if code_num == 32:
        C+= " "
    else:
        encode_num = code_num + ord(K[i])-97
        if encode_num >122:
            encode_num -=26
        #print(encode_num, "encodenum")
        C+= chr(encode_num)

print("Encryped PSW: ", C)

for i in range(len(M)):
    ept_num = ord(C[i])
