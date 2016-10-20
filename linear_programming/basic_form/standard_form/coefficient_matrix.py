import re

def matrix_size(subjects,variables):
    sizes=[]
    sizes.append(len(subjects))
    sizes.append(len(variables))
    return sizes

def matrix_row_size(sizes):
    return sizes[0]

def matrix_col_size(sizes):
    return sizes[1]

def extract_param(subject,variables):
    vars_list=subject.split(' ')
    #print vars
    params=[]
    for vari in variables:
        param=0
        for var in vars_list:
            if var.__contains__(vari):
                #print var
                param=var[:(len(var)-len(vari))]
                if param.__contains__("+"):
                    param=param.replace("+","")
                elif param.__contains__('-') and len(param)== 1:
                    param='-1'
                if len(param)==0:
                    param='1'
        #print param
        param=int(param)
        params.append(param)
    return params

def coeff_matrix(subjects,variables):
    matrix=[]
    for subject in subjects:
        matrix.append(extract_param(subject,variables))
    return matrix

def print_matrix(matrix):
    printer=''
    for row in matrix:
        for element in row:
            #print('%s\t'%element)
            printer+=('%s\t'%element)
        printer+=('\n')
    return printer

def variable_params(variable,variables,matrix):
    index=variables.index(variable)
    params=[]
    for row in matrix:
        params.append(row[index])
    return params

def constraint(subject):
    index=subject.index('=')
    return int(subject[index+1:])

def constraints(subjects):
    constraint_list=[]
    for subject in subjects:
        constraint_list.append(constraint(subject))
    return constraint_list

#subject_st='x1 +2x2 +y1 = 3'
#constraint=constraint(subject_st)
#print constraint