code = input("code: ")
code = '0' * (7 - len(code)) + code
s1 = (int(code[0]) + int(code[2]) + int(code[4]) + int(code[-1])) % 2
s2 = (int(code[1]) + int(code[2]) + int(code[-2]) + int(code[-1])) % 2
s3 = (int(code[-4]) + int(code[-3]) + int(code[-2]) + int(code[-1])) % 2
S = str(s3) + str(s2) + str(s1)
if int(S,2) == 0:
    print("no error in code")
else:
    c = int(S,2)
    cl_code = code
    cl_code = cl_code[:c - 1] + str((int(code[c-1]) + 1) % 2) + cl_code[c:]

    print("error in cell number ", c,"\nclear code: ", cl_code)


