import standard_form
from standard_form import read_input
from standard_form import coefficient_matrix

#file_input='../data/input-1.txt'
file_input='../data/input-2.txt'

#variables list
lines=read_input.read(file_input)
variables=read_input.variables(lines)
subjects=read_input.subject_to(lines)

sizes=coefficient_matrix.matrix_size(subjects,variables)
row=coefficient_matrix.matrix_row_size(sizes)
column=coefficient_matrix.matrix_col_size(sizes)

param0=coefficient_matrix.extract_param(subjects[0],variables)
param1=coefficient_matrix.extract_param(subjects[1],variables)
param2=coefficient_matrix.extract_param(subjects[2],variables)

coeff_matrix=coefficient_matrix.coeff_matrix(subjects,variables)
coeff_matrix_printer=coefficient_matrix.print_matrix(coeff_matrix)

print ('variables: %s'%variables)
print ('subjects: %s'%subjects)
print ('matrix sizes: %s'%sizes)
print ('row: %s'%row)
print ('column: %s'%column)

print('')

#coefficient matrix
#print ('params 0: %s'%param0)
#print ('params 1: %s'%param1)
#print ('params 2: %s'%param2)

print ('coefficient matrix:\n%s' % coeff_matrix_printer)


#----------------
#variables params
x1_params=coefficient_matrix.variable_params("x1",variables,coeff_matrix)
x2_params=coefficient_matrix.variable_params("x2",variables,coeff_matrix)
y1_params=coefficient_matrix.variable_params("y1",variables,coeff_matrix)
y2_params=coefficient_matrix.variable_params("y2",variables,coeff_matrix)
y3_params=coefficient_matrix.variable_params("y3",variables,coeff_matrix)

#print ('x1 params: %s'%x1_params)
#print ('x2 params: %s'%x2_params)
#print ('y1 params: %s'%y1_params)
#print ('y2 params: %s'%y2_params)
#print ('y3 params: %s'%y3_params)
