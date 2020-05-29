# -*- coding: utf-8 -*-
"""
Created on Mon May 18 08:27:02 2020

@author: Marcin
"""

import numpy as np
import timeit
from memory_profiler import profile

@profile(precision=6)
def execute_all():
    seq_len = 35
    sensors_num = 11
    time_len = 80
    full_time_len = 200
    
    
    raw_features = np.zeros((full_time_len,sensors_num), dtype = float)
    for i, value in np.ndenumerate(raw_features):
        raw_features[i] = sum(i)
        
        
        
    start = timeit.default_timer()
    x = raw_features.flatten()
    stop = timeit.default_timer()
    print((stop-start)*1.0e6)

execute_all()
#features = np.zeros((seq_len, time_len,sensors_num), dtype = float)
