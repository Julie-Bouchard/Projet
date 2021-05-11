# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:36:38 2021

@author: id1776
"""

from transformation import Transformation
import json


class ChargementDeDonneesjson(Transformation):
    def __init__(self,emplacement_fichier):
        self.emplacement_fichier=emplacement_fichier
    def transforme(self):
        with open(self.emplacement_fichier) as json_file :
            data = json.load(json_file)
        return data