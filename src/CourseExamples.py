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

import numpy as np
from NacaCurves import create4DigitNacaAerofoil

def generateExampleData(exampleNumber):
    """Generates the given example"""

    examples = (generateExampleData1,
                generateExampleData2,
                generateExampleData3)

    return examples[exampleNumber - 1]()

def generateExampleData1():
    """Creates the data for the first example.
    
    Returns
    --------
    Returns
    --------
    A dictionary with the following fields:
       upperSurface : The upper surface points, a 2d array (x and y)
       lowerSurface : The lower surface points, a 2d array 
       anticlockwise: The full points, anticlockwise from the trailing edge
       camber : The camber profile, as a 2d array ( x and camber at that x)
       thickness : The thickness distribution as as a 2d array ( x and thickness at that x)"""

    x = np.linspace(0,1,501)
    return create4DigitNacaAerofoil(0,0,12,x)

def generateExampleData2():
    """Creates the data for the second example.
    
    Returns
    --------
    A dictionary with the following fields:
       upperSurface : The upper surface points, a 2d array (x and y)
       lowerSurface : The lower surface points, a 2d array 
       anticlockwise: The full points, anticlockwise from the trailing edge
       camber : The camber profile, as a 2d array ( x and camber at that x)
       thickness : The thickness distribution as as a 2d array ( x and thickness at that x)"""

    theta = np.linspace(0,np.pi,101)
    x = (1-np.cos(theta))/2
    return create4DigitNacaAerofoil(4,4,12,x)

def generateExampleData3():
    """Creates the data for the third example.
    
    Returns
    --------
    A dictionary with the following fields:
       upperSurface : The upper surface points, a 2d array (x and y)
       lowerSurface : The lower surface points, a 2d array 
       anticlockwise: The full points, anticlockwise from the trailing edge
       camber : The camber profile, as a 2d array ( x and camber at that x)
       thickness : The thickness distribution as as a 2d array ( x and thickness at that x)"""


    theta = np.linspace(0,np.pi,101)
    x = np.power((1-np.cos(theta))/2, 2)
    return create4DigitNacaAerofoil(9,5,16,x)

