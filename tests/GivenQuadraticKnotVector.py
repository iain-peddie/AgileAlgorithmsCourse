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
    


