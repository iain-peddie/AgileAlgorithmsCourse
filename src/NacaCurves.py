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

def create4DigitNacaAerofoil(camber, position, thickness, xValues):
    """Creates a data sampling around a naca 4-digit aerofoil.
    
    Inputs
    ------
    camber : The maximum camber, as a percentage of a chord. That is,
             4 will correspond to a camber height 4%, ie camber/chord = 0.04
    position: The position of maximum camber, in 10 percents if chord
    thickness: The thickness as a percent of a chord
    xValues: A ndarray containing the x coordinates to evaluate the curve at, 
             in chord length scaled coordinates. That is these should all be
             in the range [0, 1]

    Returns
    --------
    A dictionary with the following fields:
       upperSurface : The upper surface points, a 2d array (x and y)
       lowerSurface : The lower surface points, a 2d array 
       anticlockwise: The full points, anticlockwise from the trailing edge
       camber : The camber profile, as a 2d array ( x and camber at that x)
       thickness : The thickness distribution as as a 2d array ( x and thickness at that x)
    
    Notes
    -----
    The inputs look a little strange because they are written in the form of the
    digits of the NACA 4 digit series, e.g. craete_4_digit_naca_aerofoil(4, 4, 12)
    would then create the points on the NACA4412 shape."""

    
    xValues.sort()

    xt = _createThicknessDistribution(thickness, xValues)
    xc = _createCamberDistribution(position, camber, xValues)
    theta = _createThetaDistribution(position, camber, xValues)

    x = xValues.transpose()

    xu = x - xt[:,1] * np.sin(theta)
    yu = xc[:,1] + xt[:,1] * np.cos(theta)

    xl = x + xt[:,1] * np.sin(theta)
    yl = xc[:,1] - xt[:,1] * np.cos(theta)

    upperSurface = _combineSurface(xu, yu)
    lowerSurface = _combineSurface(xl, yl)

#    upperSurface = np.vstack((xu, yu)).transpose()
#    lowerSurface = np.vstack((xl, yl)).transpose()

    

    anticlockwise = _combineSurfaces(upperSurface, lowerSurface)

    return { 'thickness' : xt,
             'camber' : xc, 
             'upper' : upperSurface, 
             'lower' : lowerSurface, 
             'anticlockwise' : anticlockwise }

def _combineSurface(xValues, yValues):
    """Combines xValues and yValues into a single array.
    
    Inputs
    ------
    xValues : An array of x values  This should have the same shape as yVales.
    yValues : An array of y values. This should have the same shape as xValues."""

    x0 = min(xValues)
    x1 = max(xValues)

    chordLength = x1 - x0

    xOnChord = (xValues - x0)/chordLength;
    yOnChord = yValues / chordLength;

    return np.vstack((xOnChord, yOnChord)).transpose()

def _createCamberDistribution(position, maximum, x):
    m = maximum / 100
    p = position / 10

    beforeJink = x < p

    if p != 0:
        camberBefore = m * x/(p*p) * (2*p - x)
    else:
        camberBefore = 0 * x

    camberAfter = m * (1-x) / pow(( 1 - p), 2) * ( 1 + x  - 2*p)

    final = np.where(beforeJink, camberBefore, camberAfter)

    return np.vstack((x, final)).transpose()

def _createThetaDistribution(position, maximum, x):
    x_dcdx = _createDerivativeCamberDistribution(position, maximum, x)

    return np.arctan(x_dcdx)

def _createDerivativeCamberDistribution(position, maximum, x):
    m = maximum / 100
    p = position / 10


    
    beforeJink = x < p    
    if p != 0:
        derivativeBefore = 2*m /(p*p) * (p - x)
    else:
        derivativeBefore = 0 * x

    derivativeAfter = 2*m / pow(( 1 - p), 2) * ( p - x)

    return np.where(beforeJink, derivativeBefore, derivativeAfter)
    

def _createThicknessDistribution(thickness, xValues):
    """Evaluates the thickness distribution at xVales

    Inputs
    ------
    thickness : The thickness distribution. This has the same meaning as 
                for create_4digit_naca_aerofoil.
    xValues : The xValues to evaluate at.

    Returns
    -------
    The evaluated thickness distribution."""

    x = xValues
    x2 = np.power(x, 2)
    x3 = np.power(x, 3)
    x4 = np.power(x, 4)
    rootX = np.sqrt(x)

    # Thickness equation taken from Wikipedia naca page...
    y = 5*thickness/100 * ( 0.2969 * rootX - 0.1260 * x - 0.3516 * x2 + 0.2843 * x3 - 0.1015 * x4 )

    xy = np.vstack((x,y))
    return xy.transpose()
    

def _combineSurfaces(upperSurface, lowerSurface):
    """Combines the two surfaces into an anticlockwise surface

    Inputs
    ------
    upperSurface : ndarray containing the upper surface points. The first index
                   is expected to correspond to point number, and the second index
                   to dimension. That is three points would look like [[0 0],[0.5 0.1],[1 0]]
    lowerSurface : ndarray containing the lower surface points, with the same index 
                   meaning as for the inputs.

    Outputs
    -------
    single array, with the points reversed along the uppers surface, with the same index
    meaning as for the inputs."""

    upperReverse = np.flipud(upperSurface);
    
    # remove the last point from the  upper surface, as it should be the same as
    # the first point on the lower surface
    return np.vstack([upperReverse[0:-1, :], lowerSurface])
    
   
