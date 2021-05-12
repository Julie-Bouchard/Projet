# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:06:20 2021

@author: Julie
"""

from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def process(self):
        pass
    
