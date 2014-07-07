def findSpan(degree, u, knotVector):
    numKnots = len(knotVector)
    numSpans = numKnots - (degree - 1)

    if u >= knotVector[numSpans]:
        return numSpans

    return degree
    
