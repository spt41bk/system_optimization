import standard_form
from standard_form import coefficient_matrix
from standard_form import read_input

import basic_form
from basic_form import basic_variables
from basic_form import basic_matrix

file_input='../data/input-1.txt'

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


#----------------------
basic_str='x1 x2 y2'
basis_set=basic_variables.basisSet(basic_str,variables)
basis=basic_variables.basis(basis_set)
nonbasis=basic_variables.nonbasis(basis_set)
indexes=basic_variables.indexes(basis_set)

print ('basis: %s'%basis)
print ('nonbasis: %s'%nonbasis)
print ('indexes: %s'%indexes)

#
print '---------------------BASIC FORM---------------------'
basis_matrix=basic_matrix.basis_matrix(indexes,coeff_matrix)
basis_matrix_printer=coefficient_matrix.print_matrix(basis_matrix)
print ('basis matrix: B=\n%s' % basis_matrix_printer)


nonindexes=basic_variables.nonindexes(basis_set)
nonbasis_matrix=basic_matrix.basis_matrix(nonindexes,coeff_matrix)
nonbasis_matrix_printer=coefficient_matrix.print_matrix(nonbasis_matrix)
print ('non basis matrix: N=\n%s' % nonbasis_matrix_printer)


print ('basis: xb=%s'%basis)
print ('nonbasis: xn=%s'%nonbasis)

constrains=coefficient_matrix.constraints(subjects)
print ('constraints: b=%s'%constrains)
print('fucntion: B xB + N xN = b')
print ('xB + B-1 N xN = B-1 b')
print ('[I | B-1 N] [xB / xN] = B-1 b')
