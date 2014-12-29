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

import sys

from WellBehavedPython.Engine.TestSuite import TestSuite
from WellBehavedPython.Runners.VerboseConsoleTestRunner import VerboseConsoleTestRunner
from WellBehavedPython.api import registerExpectationClass, discoverTests
from WellBehavedPython.Expectations.Numpy.ArrayExpectations import ArrayExpectations

import numpy as np

def main(suite):
    try:

        registerExpectationClass(lambda actual: isinstance(actual, np.ndarray),
                                 ArrayExpectations)
                
        suite = createSuite()
        
        buffer = True

        runner = VerboseConsoleTestRunner(bufferOutput = buffer)
        results = runner.run(suite)

        sys.__stdout__.flush()
        sys.__stderr__.flush()

        exit(results.countFailures() + results.countErrors() > 0)
    except Exception as ex:        
    
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        traceback.print_exc(file = sys.stdout)
        
    
def createSuite():

    suite = TestSuite("WellBehavedPythonTests")
    nothingSuite = discoverTests("GivenNothing")
    linearKnotSuite = discoverTests("GivenLinearKnotVector")
    quadraticKnotSuite = discoverTests("GivenQuadraticKnotVector")

    suite.add(linearKnotSuite)
    suite.add(quadraticKnotSuite)
    suite.add(nothingSuite)
    
    return suite

if __name__ == "__main__":
    main(createSuite())

