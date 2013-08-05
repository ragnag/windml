"""
Multiple Time Series of Power
-------------------------------------------------------------------------

This example visualizes multiple time series of various wind mills. It is
useful to illustrate differences and correlations of neighboring wind mills.
"""

import numpy as np

from windml.datasets.nrel import NREL
from windml.visualization.plot_multiple_timeseries import plot_multiple_timeseries

ds = NREL()
windpark = ds.get_windpark(NREL.park_id['tehachapi'], 3, 2004)
plot_multiple_timeseries(windpark)
