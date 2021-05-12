# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:53:45 2021

@author: Julie
"""

from abc import ABC, abstractmethod
from operation import Operation

class Estimateur(Operation):
    def process(self):
        return self.estime(self)
    @abstractmethod
    def estime(self):
        pass
