#!/usr/bin/env python3

from WellBehavedPython.Runners.VerboseConsoleTestRunner import VerboseConsoleTestRunner

import GivenQuadraticKnotVector


case = GivenQuadraticKnotVector.WithOneEvenlySpacedInternalKnot()
case.configureTest("test_then_span_just_below_final_knot_is_4")

runner = VerboseConsoleTestRunner()
runner.run(case)

print(results.summary())
