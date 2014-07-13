#!/usr/bin/env python3

from WellBehavedPython.Runners.VerboseConsoleTestRunner import VerboseConsoleTestRunner

import GivenQuadraticKnotVector


case = GivenQuadraticKnotVector.WithOneEvenlySpacedInternalDegenerateKnot()
case.configureTest("test_then_span_just_at_internal_knot_is_5")

runner = VerboseConsoleTestRunner()
runner.run(case)

print(results.summary())
