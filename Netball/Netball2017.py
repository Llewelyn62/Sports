# -*- coding: utf-8 -*-

import pandas as pd

# Pandas version check
from pkg_resources import parse_version
if parse_version(pd.__version__) != parse_version('0.20.2'):
    raise RuntimeError('Invalid pandas version')

from catalyst.pandas.convert import to_int
import re

# Read HTML from
url = 'https://anzpremiership.co.nz/fixtures-and-results/ladder'
#url= 'http://www.superxv.com/results/2017-super-rugby-results/'
data_frame = pd.read_html(url, header=None,
                    skiprows=0, match='.+')[0]

# Type conversion for the following columns: 1, 4
# for column in ['1', '4']:
#     data_frame[column] = to_int(data_frame[column])
