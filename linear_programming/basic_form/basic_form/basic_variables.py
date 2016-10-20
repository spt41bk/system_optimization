
def basisSet(basicVariables,variables):
    basic_set=[]
    nonbasic_set=[]
    indexes=[]
    nonindexes=[]
    basic_vars=basicVariables.strip().split(' ')
    for var in variables:
        if basic_vars.__contains__(var):
            basic_set.append(var)
            indexes.append(variables.index(var))
        else:
            nonbasic_set.append(var)
            nonindexes.append(variables.index(var))
    basis_set=[]
    basis_set.append(basic_set)
    basis_set.append(nonbasic_set)
    basis_set.append(indexes)
    basis_set.append(nonindexes)
    return basis_set

def basis(basisSet):
    return basisSet[0]

def nonbasis(basisSet):
    return basisSet[1]

def indexes(basisSet):
    return basisSet[2]

def nonindexes(basisSet):
    return basisSet[3]