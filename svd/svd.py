import itertools
import random

import sympy as s
mp = s.mpmath
import numpy as np

flatten = lambda l: [x for x in itertools.chain(*l)]

def dot(l,r):
    l = np.array(l)
    r = np.array(l)
    if (1 in l.shape) or (1 in r.shape):
        return l*r
    else:
        return np.dot(l,r)

def SVD_np(A):
    A = np.matrix(A)
    U,Sp,V = np.linalg.svd(A)
    n = U.shape[0]
    m = V.shape[0]
    S = np.zeros((n,m))
    S[:min(n,m),:min(n,m)] = np.diag(Sp)
    return (U,S,V)

def randomUnitVector(n):
    unnormalized = [random.normalvariate(0, 1) for _ in range(n)]
    theNorm = np.sqrt(sum(x * x for x in unnormalized))
    return [x / theNorm for x in unnormalized]

def svd_1d(A, epsilon=1e-10):
    ''' The one-dimensional SVD '''
    A = np.matrix(A)
    n, m = A.shape
    x = randomUnitVector(m)
    lastV = None
    currentV = x

    if n > m:
        B = dot(A.T, A)
    else:
        B = dot(A, A.T)

    iterations = 0
    while True:
        iterations += 1
        lastV = currentV
        currentV = dot(B, lastV)
        currentV = currentV / np.linalg.norm(currentV)
        if np.greater(abs(dot(currentV, lastV)),  1 - epsilon).all():
            print("converged in {} iterations!".format(iterations))
            return currentV


def svd(A, k=None, epsilon=1e-10):
    '''
        Compute the singular value decomposition of a matrix A
        using the power method. A is the input matrix, and k
        is the number of singular values you wish to compute.
        If k is None, this computes the full-rank decomposition.
    '''
    A = np.matrix(A)
    n, m = A.shape
    svdSoFar = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrixFor1D = A.copy()

        for singularValue, u, v in svdSoFar[:i]:
            matrixFor1D -= singularValue * np.outer(u, v)

        v = svd_1d(matrixFor1D, epsilon=epsilon)  # next singular vector
        u_unnormalized = dot(A, v)
        sigma = np.linalg.norm(u_unnormalized)  # next singular value
        u = u_unnormalized / sigma

        svdSoFar.append((sigma, u, v))

    singularValues, us, vs = [np.array(x) for x in zip(*svdSoFar)]
    return us.T, singularValues, vs

def SVD_s(A): # -> U, S, V
    A = s.Matrix(A)
    (n,m) = A.shape
    AAT = A*A.T # nxn
    ATA = A.T*A # mxm
    AAT_eigs = sorted(AAT.eigenvects(simplify=True), reverse=True)
    ATA_eigs = sorted(ATA.eigenvects(simplify=True), reverse=True)
    AAT_bases = [basis for (eigenval, multiplicity, basis) in AAT_eigs]
    U = s.Matrix([x for x in flatten(AAT_bases)]).reshape(n,n)
    assert U.shape == (n,n)
    ATA_bases = [basis for (eigenval, multiplicity, basis) in ATA_eigs]
    V = s.Matrix([x for x in flatten(ATA_bases)]).reshape(m,m)
    assert V.shape == (m,m)
    S = s.zeros(n,m)
    S[:min(n,m),:min(n,m)] = s.diag(*flatten([[s.sqrt(eigenval)]*multiplicity for (eigenval,multiplicity, basis) in ATA_eigs]))
    # normalize by your largest magnitude such that U*S*V is fixed
    U /= S[0]
    return (U,S,V)

def SVD_m(A):
    A = mp.matrix([x for x in A])
    m = A.cols
    n = A.rows
    (U,Sp,V) = mp.svd(A, full_matrices = True)
    S = mp.zeros(n,m)
    S[:min(n,m),:min(n,m)] = mp.diag(Sp)
    return (U, S, V)

A = range(1,4)

fm = lambda x: x[0]*(x[1]*x[2])

print(fm(SVD_np(A)))
print(fm(SVD_s(A)))
print(SVD_m(A))
print(svd_1d(A))
