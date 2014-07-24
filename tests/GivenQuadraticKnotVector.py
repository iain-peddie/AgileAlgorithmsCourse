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
from SplineAlgorithms import splineBasisFunctions
from SplineAlgorithms import splineBasisFunctionsAtSingleParameter

import numpy as np

class WithNoInternalKnots(TestCase):    

    def before(self):
        self.knotVector = (0, 0, 0, 1, 1, 1)
        self.degree = 3 # degree is polynomial order + 1

    def test_then_span_at_0_is_3(self):
        # When
        span = findSpan(self.degree, 0, self.knotVector)
        
        # Then
        expect(span).toEqual(3)

    def test_then_span_beneath_0_is_3(self):
        # When
        span = findSpan(self.degree, -1e-5, self.knotVector)

        # Then
        expect(span).toEqual(3)


    def test_then_span_at_1_is_3(self):
        # When
        span= findSpan(self.degree, 1, self.knotVector)

        # Then
        expect(span).toEqual(3)

    def test_then_span_above_1_is_3(self):
        # When
        span= findSpan(self.degree, 1.0001, self.knotVector)

        # Then
        expect(span).toEqual(3)

    def test_splineBasisFunctions_at_0_equal_bernstein_polynomials_at_0(self):
        # When
        parameter = 0
        span = 3
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)

        # Then
        expectedBasisValues = np.array([1, 0, 0])

        expect(basisValues).toEqual(expectedBasisValues)

    def test_splineBasisFunctions_at_0p5_equal_bernstein_polynomials_at_0p5(self):
        
        # When
        parameter = 0.5
        span = 3
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)

        # Then
        expectedBasisValues = np.array([1/4, 1/2, 1/4])

        expect(basisValues).toEqual(expectedBasisValues)


    def test_splineBasisFunctions_at_1_equal_bernstein_polynomials_at_1(self):
        # When
        parameter = 1
        span = 3
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)

        # Then
        expectedBasisValues = np.array([0, 0, 1])

        expect(basisValues).toEqual(expectedBasisValues)    

    def test_splineBasisFunctions_for_range_0_to_1_with_3_elements(self):
        # When
        parameters = np.linspace(0,1,3)
        basisValues = splineBasisFunctions(parameters, self.degree, self.knotVector)

        # Then
        expectedBasisValues = np.array([[ 1, 0, 0], 
                                        [1/4, 1/2, 1/4],
                                        [0, 0, 1]])
        expect(basisValues).toEqual(expectedBasisValues)



class WithOneEvenlySpacedInternalKnot(TestCase):    

    def before(self):
        self.knotVector = (0, 0, 0, 0.5, 1, 1, 1)
        self.degree = 3 # degree is polynomial order + 1

    def test_then_span_at_0_is_3(self):
        # When
        span = findSpan(self.degree, 0, self.knotVector)
        
        # Then
        expect(span).toEqual(3)

    def test_then_span_beneath_0_is_3(self):
        # When
        span = findSpan(self.degree, -1e-5, self.knotVector)

        # Then
        expect(span).toEqual(3)

    def test_then_span_just_beneath_internal_knot_is_3(self):
        # When
        span = findSpan(self.degree, 0.5-1e-5, self.knotVector)

        # Then
        expect(span).toEqual(3)

    def test_then_span_just_at_internal_knot_is_4(self):
        # When
        span = findSpan(self.degree, 0.5+1e-5, self.knotVector)

        # Then
        expect(span).toEqual(4)

    def test_then_span_just_below_final_knot_is_4(self):
        # When
        span = findSpan(self.degree, 1-1e-5, self.knotVector)

        # Then
        expect(span).toEqual(4)


    def test_then_span_at_1_is_4(self):
        # When
        span= findSpan(self.degree, 1, self.knotVector)

        # Then
        expect(span).toEqual(4)

    def test_then_span_above_1_is_4(self):
        # When
        span= findSpan(self.degree, 1.0001, self.knotVector)

        # Then
        expect(span).toEqual(4)

    def test_splineBasisFunctions_at_0_equal_bernstein_polynomials_at_0(self):
        # When
        parameter = 0
        span = 3
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)

        # Then
        expectedBasisValues = np.array([1, 0, 0])

        expect(basisValues).toEqual(expectedBasisValues)

    def test_splineBasisFunctions_just_under_0p25_equal_bernstein_polynomials_at_0p5(self):
        
        # When
        parameter = 0.25
        span = 3
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)        

        # Then

        # (1-2u)^2 2u(2-3u) 2u^2

        expectedBasisValues = np.array([2/8, 5/8, 1/8])

        expect(basisValues).toEqual(expectedBasisValues)


    def test_splineBasisFunctions_at_0p5_equal_bernstein_polynomials_at_1(self):
        # When
        parameter = 0.5
        span = 3
        
        basisValues = splineBasisFunctionsAtSingleParameter(span, parameter, self.degree, self.knotVector)

        # Then
        # (1-2u)^2 2u(2-3u) 2u^2
        expectedBasisValues = np.array([0, 1/2, 1/2])

        expect(basisValues).toEqual(expectedBasisValues)    

    def test_splineBasisFunctions_for_range_0_to_1_with_5_elements(self):
        # When
        parameters = np.linspace(0,1,5)
        basisValues = splineBasisFunctions(parameters, self.degree, self.knotVector)

        # Then
        # (1-2u)^2, 2u(2-3u), 2u^2, 0 for 0 <= u < 1/2
        # 0, 2(1-u)^2, 2(1-u)(3u-1), (2u-1)^2 for 1/2 <= u < 1
        expectedBasisValues = np.array([[ 1, 0, 0, 0], 
                                        [2/8, 5/8, 1/8, 0],
                                        [0, 1/2, 1/2, 0],
                                        [0, 1/8, 5/8, 2/8], 
                                        [0, 0, 0, 1]])
        expect(basisValues).toEqual(expectedBasisValues)


    
class WithOneEvenlySpacedInternalDegenerateKnot(TestCase):    
    def before(self):
        self.knotVector = (0, 0, 0, 0.5, 0.5, 1, 1, 1)
        self.degree = 3 # degree is polynomial order + 1


    def test_then_span_at_0_is_3(self):
        # When
        span = findSpan(self.degree, 0, self.knotVector)
        
        # Then
        expect(span).toEqual(3)

    def test_then_span_beneath_0_is_3(self):
        # When
        span = findSpan(self.degree, -1e-5, self.knotVector)

        # Then
        expect(span).toEqual(3)

    def test_then_span_just_beneath_internal_knot_is_3(self):
        # When
        span = findSpan(self.degree, 0.5-1e-5, self.knotVector)

        # Then
        expect(span).toEqual(3)

    def test_then_span_just_at_internal_knot_is_5(self):
        # When
        span = findSpan(self.degree, 0.5+1e-5, self.knotVector)

        # Then
        expect(span).toEqual(5)

    def test_then_span_just_below_final_knot_is_5(self):
        # When
        span = findSpan(self.degree, 1-1e-5, self.knotVector)

        # Then
        expect(span).toEqual(5)


    def test_then_span_at_1_is_5(self):
        # When
        span= findSpan(self.degree, 1, self.knotVector)

        # Then
        expect(span).toEqual(5)

    def test_then_span_above_1_is_5(self):
        # When
        span= findSpan(self.degree, 1.0001, self.knotVector)

        # Then
        expect(span).toEqual(5)

    def test_splineBasisFunctions_for_range_0_to_1_with_5_elements(self):
        # When
        parameters = np.linspace(0,1,5)
        basisValues = splineBasisFunctions(parameters, self.degree, self.knotVector)

        # Then
        # (1-2u)^2, 4u(1-2u), (2u)^2, 0, 0 for 0 <= u < 1/2
        # 0, 0, [2(1-u)]^2, 4(1-u)(2u-1), (2u-1)^2 for 1/2 <= u < 1
        expectedBasisValues = np.array([[ 1, 0, 0, 0, 0],                                         
                                        [1/4, 1/2, 1/4, 0, 0],
                                        [0, 0, 1, 0, 0],
                                        [0, 0, 1/4, 1/2, 1/4], 
                                        [0, 0, 0, 0, 1]])
        expect(basisValues).toEqual(expectedBasisValues)

