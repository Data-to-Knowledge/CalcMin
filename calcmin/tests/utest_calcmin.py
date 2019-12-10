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
well_depth_bins1=[0, 20, 10000]
well_depth_bins2=[0, 20, 50, 100, 10000]

output_path = r'C:\ecan\shared\projects\calcmin'

csv1 = 'calcmin_set1_2019-12-11.csv'
csv2 = 'calcmin_set2_2019-12-11.csv'
csv3 = 'calcmin_set3_2019-12-11.csv'
csv4 = 'calcmin_set4_2019-12-11.csv'

###############################
### First run

c1 = calcmin(min_values, quantile, month, start_year, where_in, well_depth_bins1)

c1.to_csv(os.path.join(output_path, csv1), index=False)


###############################
### Second run

c2 = calcmin(min_values, quantile, month, start_year, where_in, well_depth_bins2)

c2.to_csv(os.path.join(output_path, csv2), index=False)


###############################
### Third run

c3 = calcmin(min_values, quantile, month, start_year, where_in, well_depth_bins1, reference_level='msl')

c3.to_csv(os.path.join(output_path, csv3), index=False)

###############################
### Third run

c4 = calcmin(min_values, quantile, month, start_year, where_in, well_depth_bins2, reference_level='msl')

c4.to_csv(os.path.join(output_path, csv4), index=False)




