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
from NacaCurves import create4DigitNacaAerofoil
from SplineAlgorithms import bernsteinFunctions

import numpy as np

class GivenNothing(TestCase):
    def test_that_first_order_bernstein_polynomials_look_linear(self):
        # Where
        u = np.linspace(0,1,3)
        order = 1
        degree = order + 1

        # When
        values = bernsteinFunctions(u, 2)

        # Then
        expectedValues = np.array([[1, 0],
                                     [1/2,1/2],
                                     [0, 1]])
        expect(values).toEqual(expectedValues)


    def test_that_second_order_bernstein_polynomials_look_quadratic(self):
        # When
        parameters = np.linspace(0,1,3)
        order = 2
        degree = order + 1
        values = bernsteinFunctions(parameters, degree)

        # Then
        expectedValues = np.array([[ 1, 0, 0], 
                                   [1/4, 1/2, 1/4],
                                   [0, 0, 1]])
        expect(values).toEqual(expectedValues)

    def test_that_00xx_naca_curve_is_symmetric(self):
        # Where
        x = np.linspace(0, 1, 11)
        
        # When
        aerofoil = create4DigitNacaAerofoil(0, 0, 12, x)

        # Then
        
        upperY = aerofoil['upper'][:, 1]
        lowerY = aerofoil['lower'][:, 1]

        upperX = aerofoil['upper'][:, 0]
        lowerX = aerofoil['lower'][:, 0]
        meanY = upperY + lowerY

        expect(-upperY).toEqual(lowerY)
        expect(upperX).toEqual(lowerX)

    def test_that_yzxx_naca_curve_is_asymmetric(self):
        # Where
        x = np.linspace(0, 1, 11)
        
        # When
        aerofoil = create4DigitNacaAerofoil(4, 4, 12, x)

        # Then
        
        upperY = aerofoil['upper'][:, 1]
        lowerY = aerofoil['lower'][:, 1]

        upperX = aerofoil['upper'][:, 0]
        lowerX = aerofoil['lower'][:, 0]
        meanY = upperY + lowerY

        expectedCamber= np.array([0, 0.035, 0.06, 0.075, 0.0799, 0.077, 0.0711, 0.06, 0.0444, 0.0244, 0.0])

        # low tolerance to match precision of output in avove array
        expect(upperY + lowerY).toBeCloseTo(expectedCamber, absoluteTolerance = 1e-2) 

        # x_U and x_L get shifted by compensating amounts: x{U,L} = x \pm t sin\theta, so xU + xL = 2x
        expect((upperX+lowerX)/2).toBeCloseTo(x, absoluteTolerance = 1e-3)
