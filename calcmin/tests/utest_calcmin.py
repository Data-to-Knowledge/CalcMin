# -*- coding: utf-8 -*-
"""
Created on Wed May  9 15:12:14 2018

@author: MichaelEK
"""
import pandas as pd
import os
from calcmin import calcmin

###############################
### Parameters

min_values=5
quantile=0.2
month=5
start_year='2000'
where_in=None
well_depth_bins=[0, 20, 10000]

output_path = r'E:\ecan\shared\projects\calcmin\calcmin_2019-08-26.csv'

###############################
### Tests

c1 = calcmin(min_values, quantile, month, start_year, where_in, well_depth_bins)

c1.to_csv(output_path, index=False)













