import pytest
import os
import glob
import cv2
from polyfiller_g4 import PolyFiller
from itertools import chain
from utilspy_g4 import compareFrames


def _removeTempFiles() -> None:
    """
    Remove temp files
    :rtype: None
    :return: None
    """

    removeFiles = glob.iglob('tests/images/*.fill.*')
    removeFiles = chain(removeFiles, glob.iglob('tests/images/*.fill2.*'))

    for _file in removeFiles:
        os.remove(_file)


def test_1():
    pf = PolyFiller()

    assert pf._ext == 'fill'
    assert pf._color == 0
    assert pf._polygons == []


def test_2():
    pf = PolyFiller('new_ext', (200, 100, 250))

    assert pf._ext == 'new_ext'
    assert pf._color == (200, 100, 250)
    assert pf._polygons == []


def test_3():
    pf = PolyFiller(color=(200, 100, 250), ext='new_ext')

    assert pf._ext == 'new_ext'
    assert pf._color == (200, 100, 250)
    assert pf._polygons == []


def test_4():
    pf = PolyFiller()

    pf.addPolygon([[10, 15], [25, 20], [15, 50]])
    assert pf._polygons == [[[10, 15], [25, 20], [15, 50]]]


def test_5():
    pf = PolyFiller()

    pf.addPolygon([[10, 15], [25, 20], [15, 50]])
    pf.addPolygon([[1, 2], [3, 4], [5, 6], [7, 8]])
    assert pf._polygons == [[[10, 15], [25, 20], [15, 50]], [[1, 2], [3, 4], [5, 6], [7, 8]]]


def test_6():
    _removeTempFiles()

    pf = PolyFiller()

    pf.fill('tests/images/frame_1.png')
    assert os.path.exists('tests/images/frame_1.fill.png') == True


def test_7():
    _removeTempFiles()

    pf = PolyFiller(ext='fill2')

    pf.fill('tests/images/frame_1.png')
    assert os.path.exists('tests/images/frame_1.fill2.png') == True


def test_8():
    _removeTempFiles()

    pf = PolyFiller()

    pf.fill('tests/images/frame_1.png')

    assert compareFrames('tests/images/frame_1.png', 'tests/images/frame_1.fill.png') == True


def test_9():
    _removeTempFiles()

    pf = PolyFiller()
    pf.addPolygon([[750, 500], [850, 500], [800, 600]])
    pf.addPolygon([[1000, 600], [1100, 650], [1200, 800], [900, 650]])
    pf.fill('tests/images/frame_1.png')

    frameFill = cv2.imread('tests/images/frame_1.fill.png')

    (b, g, r) = frameFill[530, 800]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameFill[640, 970]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameFill[730, 1123]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameFill[551, 771]
    assert int(r) + int(g) + int(b) == 309

    (b, g, r) = frameFill[564, 824]
    assert int(r) + int(g) + int(b) == 321

    (b, g, r) = frameFill[711, 1007]
    assert int(r) + int(g) + int(b) == 456

    (b, g, r) = frameFill[672, 1123]
    assert int(r) + int(g) + int(b) == 477

    _removeTempFiles()


def test_10():
    _removeTempFiles()

    pf = PolyFiller(color=(100, 250, 50))
    pf.addPolygon([[750, 500], [850, 500], [800, 600]])
    pf.addPolygon([[1000, 600], [1100, 650], [1200, 800], [900, 650]])
    pf.fill('tests/images/frame_1.png')

    frameFill = cv2.imread('tests/images/frame_1.fill.png')

    (b, g, r) = frameFill[530, 800]
    assert int(r) + int(g) + int(b) == 400

    (b, g, r) = frameFill[640, 970]
    assert int(r) + int(g) + int(b) == 400

    (b, g, r) = frameFill[730, 1123]
    assert int(r) + int(g) + int(b) == 400

    (b, g, r) = frameFill[551, 771]
    assert int(r) + int(g) + int(b) == 309

    (b, g, r) = frameFill[564, 824]
    assert int(r) + int(g) + int(b) == 321

    (b, g, r) = frameFill[711, 1007]
    assert int(r) + int(g) + int(b) == 456

    (b, g, r) = frameFill[672, 1123]
    assert int(r) + int(g) + int(b) == 477

    _removeTempFiles()


def test_11():
    _removeTempFiles()

    pf = PolyFiller(color=(100, 250, 50))
    pf.addPolygon([[750, 500], [850, 500], [800, 600]])
    pf.addPolygon([[1000, 600], [1100, 650], [1200, 800], [900, 650]])
    pf.fill('tests/images/frame_1.png')
    pf.fill('tests/images/frame_2.png')

    frameFill = cv2.imread('tests/images/frame_2.fill.png')


    (b, g, r) = frameFill[530, 800]
    assert int(r) + int(g) + int(b) == 400

    (b, g, r) = frameFill[640, 970]
    assert int(r) + int(g) + int(b) == 400

    (b, g, r) = frameFill[730, 1123]
    assert int(r) + int(g) + int(b) == 400

    (b, g, r) = frameFill[551, 771]
    assert int(r) + int(g) + int(b) == 318

    (b, g, r) = frameFill[564, 824]
    assert int(r) + int(g) + int(b) == 315

    (b, g, r) = frameFill[711, 1007]
    assert int(r) + int(g) + int(b) == 438

    (b, g, r) = frameFill[672, 1123]
    assert int(r) + int(g) + int(b) == 483

    _removeTempFiles()
