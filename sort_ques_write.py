f1 = open("Python_Assignment (1).txt", "r")

text = f1.read();

ques_posn = []

i = 1

while True:
    var = text.find('Q' + str(i) + ')')
    if var == -1:
        break;
    else:
        ques_posn.append(var)
        i+= 1
    
    
rel_posn = sorted(ques_posn)


f2 = open("Output_q1.txt", "w")

maxm = max(ques_posn)

for x in ques_posn:
    if x == maxm:
        f2.write(text[x:])
    else:
        f2.write(text[x:rel_posn[rel_posn.index(x)+1]])
        


f2.close()
f1.close()

raw_input()