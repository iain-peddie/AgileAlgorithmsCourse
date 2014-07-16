import numpy as np

def findSpan(degree, u, knotVector):
    """Counts spans in a knot vector.
    
    Given a parameter value, and a set of knots corresponding to a paremteric curve
    of a given degree, calculate the span in the knot vector.

    See the Nurbs book. This is a variant of Algorithm A2.1 (with different handling if
    the parameter is outside the knot span).

    Inputs
    ------
    degree : The degree of the curve this knot vector corresponds to. degree = polynomial order + 1,
             so degree is 2 for a linear curve, 3 for quadratic etc.
    u : The value of the line parameter
    knotVector : The sequence of knots. Expected that the values never decreates, that is 
                 U(i+1) >= U(i).

    Returns
    -------
    The span, that is the maximum i, such that U(i) <= u <= U(i+1). Returns degree if u< U(1) and the last span if u < U(-1).
"""
    numKnots = len(knotVector)
    numSpans = numKnots - (degree - 1)

    if u >= knotVector[numSpans]:
        return numSpans - 1

    if knotVector[0] > u:
        return degree

    i = 0;
    for knot in knotVector:
        if knot > u:
            return i
        i = i + 1


    return numSpans
    
def splineBasisFunctionsAtSingleParameter(span, u, degree, knotVector):
    """Evaluates the full set of non-zero spline basis functions at a given parmeter
    value.
    
    Inputs
    ------
    span: The span of the parameter value in the given knot vector
    u : The parameter value to evaluate the basis functions at
    degree: The degree of the curve
    knotVector: The knot vector being operated on
    
    Returns
    -------
    A row vector of the non-zero basis functions evaluated at the given parameter value."""

    basis = np.zeros([degree])
    left = np.zeros([degree])
    right = np.zeros([degree])
    basis[0] = 1

    for j in range(1, degree):
        left[j] = u - knotVector[span - j]
        right[j] = knotVector[span -1 + j] - u
        saved = 0.0;
        for r in range(0, j):
            num = basis[r]
            denom = right[r+1] + left[j-r]
            temp = basis[r] / (right[r+1]+left[j-r])

            basis[r] = saved + right[r+1]*temp
            saved = left[j-r] * temp
        
        basis[j] = saved

    return basis
