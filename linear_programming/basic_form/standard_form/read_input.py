

def read(file):
    fi=open(file,'r')
    lines=[]
    for line in fi:
        lines.append(line)
    fi.close()
    return lines

#fi=open('../data/input-1.txt')

def variables(lines):
    for line in lines:
    #print line
        if line.__contains__('variables'):
            #variables_st=line[10:]
            variables_list=line[10:].strip().split(",")
            #print variables_list
    return variables_list


def subject_to(lines):
    ok=0
    subjects=[]
    for line in lines:
        if line.__contains__('subject to:'):
            ok=1
        if ok==1 and line.__contains__('=') and not (line.__contains__('>=') or line.__contains__('<=')):
            #print line
            subjects.append(line.strip())
    return subjects

#subjects=subject_to(fi)
#print subjects

#variables(fi)