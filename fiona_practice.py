# import sys
# import os
# import requests
# import records

import random

import folium
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point


def geotesting():

    p1 = Polygon([(0, 0), (0, -2), (-1, -2), (-2, -1)])
    p2 = Polygon([(0, 0), (2, 0), (2, 1.5), (0, 1)])
    p3 = Polygon([(5, 1), (3, 0), (2, 1), (2, 2)])
    p4 = Point([7, 1])
    g = gpd.GeoSeries([p1, p2, p3, p4])

    print(g)
    print(g.area)

    g.plot()
    plt.show()


def geopandastesting():

    # Polygons take X,Y as parameters
    f = Polygon([(-73.4525, 45.5836), (-73.5325, 45.6336), (-73.5325, 45.5336), (-73.3325, 45.5336)])
    fg = gpd.GeoSeries(f)
    fg.crs = {"init": "epsg:4326"}

    p = []
    for i in range(200):
        x = random.uniform(-73.2500, -73.8500)
        y = random.uniform(45.1500, 45.6500)
        data = Point([x, y])
        p.append(data)
    pg = gpd.GeoSeries(p)
    pg.crs = {"init": "epsg:4326"}

    joined = pg.intersection(fg.unary_union)

    makefolium(fg, pg, joined)

    joined.plot()
    plt.show()


def makefolium(*args):

    # Maps take Y,X as parameters
    m = folium.Map(location=[45.5225, -73.4525])

    for poly in args:
        try:
            folium.GeoJson(poly).add_to(m)
        except (AttributeError, TypeError, ValueError) as e:
            print(poly, e)
            try:
                if poly.is_empty():
                    pass
                else:
                    folium.GeoJson(poly).add_to(m)
            except Exception as e:
                pass

    m.save("index.html")


if __name__ == '__main__':
    # geotesting()
    geopandastesting()
