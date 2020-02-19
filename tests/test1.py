""" Test for function 1"""
from EskomFunctions.function1 import dictionary_of_metrics




assert dictionary_of_metrics([1,2,3,4,5]) == {'mean': 3.0,
                                                'median': 3.0,
                                                'variance': 2.0,
                                                'min': 1,
                                                'max': 5,
                                                'standard deviation': 1.41}