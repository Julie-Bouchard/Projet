# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:17:45 2021

@author: Julie
"""

from abc import ABC, abstractmethod
from operation import Operation

class Transformation(Operation):
    def process(self):
        return self.transforme(self)
    @abstractmethod
    def transforme(self):
        pass
        
