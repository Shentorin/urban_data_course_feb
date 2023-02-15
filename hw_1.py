# -*- coding: utf-8 -*-
"""HW 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-JhSaeBOx6xDfpEmvow5FVnRYO1OeBIh
"""

!pip install numpy==1.22.0
!pip install geopandas mapclassify
!pip install keplergl
!pip install osmnx

from keplergl import KeplerGl
import osmnx as ox

from google.colab import output
output.enable_custom_widget_manager()

TERITORY_NAME = 'Невский район, Санкт-Петербург'

territory = ox.geocode_to_gdf(TERITORY_NAME)
territory.explore(tiles="CartoDB positron")

tags = {'building': True}  # building=*
buildings = ox.geometries_from_polygon(territory.unary_union, tags)
buildings.head()

buildings.explore(tiles="CartoDB positron")

buildings.reset_index(inplace=True)
buildings.head()

map = KeplerGl(height=500)
map.add_data(data=buildings.copy(), name='buildings')
map.add_data(data=territory.copy(), name='territory')
map