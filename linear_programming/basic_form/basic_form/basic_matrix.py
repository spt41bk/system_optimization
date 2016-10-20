

def basis_matrix(indexes,coeff_matrix):
    matrix=[]
    for row in coeff_matrix:
        basis_row=[]
        for index in indexes:
            basis_row.append(row[index])
        matrix.append(basis_row)
    return matrix