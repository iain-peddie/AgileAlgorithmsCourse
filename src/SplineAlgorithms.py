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
        return numSpans

    # we do a binary search to speed this up
    low = degree
    high = numSpans
    mid = int((low + high)/2); # need to use floor, since python doesn't have integer arithmetic                    
    if knotVector[0] > u:
        return degree

    i = 0;
    for knot in knotVector:
        if knot > u:
            return i
        i = i + 1


    return numSpans
    
