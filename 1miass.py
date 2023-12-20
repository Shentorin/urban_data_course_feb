# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

python -m venv /path/to/new/virtual/environment

import sys
import os
import numpy as np
import pandas as pd

folder = "/Users/myopic/Documents/CityGeoTools_course_IDU-master"

from metrics.data import CityInformationModel as BaseModel
#from metrics.calculations import CityMetricsMethods as CityMetrics

city_model = BaseModel.CityInformationModel(city_name="Miass", city_crs=32641, cwd="../")
print(city_model.Buildings)

print(city_model)