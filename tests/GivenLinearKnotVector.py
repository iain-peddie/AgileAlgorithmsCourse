#!/usr/bin/env python3

# Copyright 2014 Iain Peddie iain.peddie@tessella.com
# 
#    This file is part of AgileAgorithmsCourse
#
#    WellBehavedPython is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    WellBehavedPython is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with AgileAlgorithmsCourse. If not, see <http://www.gnu.org/licenses/>.

from WellBehavedPython.Engine.TestCase import TestCase
from WellBehavedPython.api import *
from SplineAlgorithms import findSpan
from SplineAlgorithms import splineBasisFunctionsAtSingleParameter

import numpy as np

class WithNoInternalKnots(TestCase):    

    def before(self):
        self.knotVector = (0, 0, 1, 1)
        self.degree = 2 # degree is polynomial order + 1

    def test_then_span_at_0_is_2(self):
        # When
        span = findSpan(self.degree, 0, self.knotVector)
        
        # Then
        expect(span).toEqual(2)

    def test_then_span_beneath_0_is_2(self):
        # When
        span = findSpan(self.degree, -1e-5, self.knotVector)

        # Then
        expect(span).toEqual(2)

    def test_then_span_at_1_is_2(self):
        # When
        span= findSpan(self.degree, 1, self.knotVector)

        # Then
        expect(span).toEqual(2)

    def test_then_span_above_1_is_2(self):
        # When
        span= findSpan(self.degree, 1.0001, self.knotVector)

        # Then
        expect(span).toEqual(2)

    def test_splineBasisFunctions_at_0_equal_bernstein_polynomials_at_0(self):
        # When
        parameter = 0
        span = 2
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)

        # Then
        expectedBasisValues = np.array([1, 0])

        expect(basisValues).toEqual(expectedBasisValues)

    def test_splineBasisFunctions_at_0p5_equal_bernstein_polynomials_at_1(self):
        # When
        parameter = 0.5
        span = 2
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)

        # Then
        expectedBasisValues = np.array([0.5, 0.5])

        expect(basisValues).toEqual(expectedBasisValues)


    def test_splineBasisFunctions_at_1_equal_bernstein_polynomials_at_1(self):
        # When
        parameter = 1
        span = 2
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)

        # Then
        expectedBasisValues = np.array([0, 1])

        expect(basisValues).toEqual(expectedBasisValues)


    
