""" Test for function 2"""
from EskomFunctions.function1 import dictionary_of_metrics



assert dictionary_of_metrics([1,2,3,4,5]) == {'median': 3.0, 
                                             'min': 1, 
                                             'max': 5, 
                                             'q1': 2.0, 
                                             'q3': 4.0 }
     
    
          