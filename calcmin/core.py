# -*- coding: utf-8 -*-
"""

"""
import os
import pandas as pd
from pdsql import mssql
from scipy.stats import rankdata
import yaml


pd.options.display.max_columns = 10
run_time_start = pd.Timestamp.today()

###########################################
#### Parameters

base_dir = os.path.realpath(os.path.dirname(__file__))

with open(os.path.join(base_dir, 'parameters.yml')) as param:
    param = yaml.safe_load(param)

to_date = run_time_start.floor('H')
from_date = (to_date - pd.DateOffset(days=7)).round('D')



###########################################
### Functions


class CalcMin(object):
    """

    """

    def __init__(self, min_values=5, where_in=None, quantile=0.2):
        """

        """
        ## Get sites and summary data
        sites1 = mssql.rd_sql(param['input']['ts_server'], param['input']['ts_database'], param['input']['sites_table'], ['ExtSiteID', 'NZTMX', 'NZTMY', 'Altitude', 'CatchmentName', 'CatchmentGroupName', 'SwazName', 'SwazGroupName', 'GwazName', 'CwmsName'], where_in=where_in)
        sites2 = sites1[sites1.ExtSiteID.str.contains('[A-Z]+\d+/\d+')]

        summ1 = mssql.rd_sql(param['input']['ts_server'], param['input']['ts_database'], param['input']['ts_summ_table'], ['ExtSiteID', 'Min', 'Median', 'Mean', 'Max', 'Count', 'FromDate', 'ToDate'], where_in={'DatasetTypeID': [param['input']['ts_dataset']]})
        summ2 = summ1[summ1.Count >= min_values].copy()

        sites3 = sites2[sites2.ExtSiteID.isin(summ2.ExtSiteID)].copy()

        ## Get TS data
        tsdata1 = mssql.rd_sql(param['input']['ts_server'], param['input']['ts_database'], param['input']['ts_table'], ['ExtSiteID', 'DateTime', 'Value'], where_in={'ExtSiteID': sites3.ExtSiteID.tolist(), 'DatasetTypeID': [param['input']['ts_dataset']], 'QualityCode': param['input']['ts_quality_codes']})
        tsdata1.DateTime = pd.to_datetime(tsdata1.DateTime)

        # Summarise by month
        tsdata1['mon'] = tsdata1.DateTime.dt.month
        tsdata1['year'] = tsdata1.DateTime.dt.year
        tsdata2 = tsdata1.loc[tsdata1['mon'].isin([5])].groupby(['ExtSiteID', 'year', 'mon']).mean().reset_index()

        tsmon1 = tsdata2.groupby(['ExtSiteID', 'mon']).Value.count()
        tsmon2 = tsmon1.groupby(level='ExtSiteID').max()
        good_sites = tsmon2[tsmon2 >= min_values]
        tsdata3 = tsdata2.loc[tsdata2.ExtSiteID.isin(good_sites.index)]

        ## Calc percentiles
        quant1 = tsdata3.groupby('ExtSiteID')['Value'].quantile(quantile)













































