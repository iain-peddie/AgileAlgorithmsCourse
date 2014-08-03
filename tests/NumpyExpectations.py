from WellBehavedPython.Expectations.BaseExpect import BaseExpect
from WellBehavedPython.api import expect

class NumpyExpectations(BaseExpect):

    def __init__(self, actual, stategy, reverseExpecter):
        BaseExpect.__init__(self, actual, stategy, reverseExpecter)
        self.tolerance = 1e-5

    def withTolerance(self, tolerance):
        self.tolerance = tolerance
        return self

    def toEqual(self, expected):
        if self.actual.shape != expected.shape:
            message = "Sapes are not the same {}, {}".format(self.actual.shape, expected.shape)
            self.fail(message)
            return

        shape = expected.shape

        if len(shape) == 1:
            for i in range(0, shape[0]-1):
                ai = self.actual[i]
                ei = expected[i]
                if ai == 0 and ei == 0:
                    continue
                if abs(ai - ei) / (abs(ai) + abs(ei) ) > self.tolerance:
                    self.fail("first difference at {}\n {} != {} with tolerance {}".format(
                        i, self.actual.tolist(), expected.tolist(), self.tolerance))
        elif len(shape) == 2:
            for i in range(0, shape[0]-1):
                for j in range(0, shape[1]-1):
                    aij = self.actual[i,j]
                    eij = expected[i,j]
                    if aij == 0 and eij == 0:
                        continue
                    if abs(aij - eij) / (abs(aij) + abs(eij)) > self.tolerance:
                        self.fail("first difference at [{},{}]\n {} != {} with tolerance {}".format(
                            i, j, self.actual.tolist(), expected.tolist(), self.tolerance))
        else:
            self.fail("Can only cope with 1d and 2d arrays at the moment")

        self.success("Arrays appear the same")

