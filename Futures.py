# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import yahoo_fin.stock_info as si
import pandas as pd

# general futures ticker // could be continuous?
ticker = "AAPL"
                   
# specific contract ticker                   
# ticker = "AAPL"

# request data 
data = si.get_data(ticker, start_date = "01/01/1900",
                   end_date = "01/01/2026")

# access the data
closingPrices = data.adjclose

# quick plot
data.adjclose.plot()


