import cv2
import numpy


class PolyFiller:

    def __init__(self):
        self._polygons = []

    def addPolygon(self, polygon: list) -> None:
        """
        Add polygon to polygon list

        :param polygon: Added polygon
        :rtype: None
        :return: None
        """

        self._polygons.append(polygon)

    def fill(self) -> None:
        pass
