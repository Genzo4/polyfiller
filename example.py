from polyfiller_g4 import PolyFiller

pf = PolyFiller()
pf.addPolygon([[0, 0], [1919, 0], [1919, 682], [1277, 385], [951, 374], [0, 615]])
pf.fill('images/frame_1.png')
pf.fill('images/frame_2.png')
pf.fill('images/frame_3.png')
