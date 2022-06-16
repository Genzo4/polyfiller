from polyfiller_g4 import PolyFiller


pf = PolyFiller()
print(pf._polygons)
pf.addPolygon([[10, 10], [500, 300], [400, 150]])
print(pf._polygons)
