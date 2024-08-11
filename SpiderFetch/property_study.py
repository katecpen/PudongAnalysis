# -*- coding: utf-8 -*-
"""
Created on 2024-08-11 19:04:33

@author: Kate Yang
@description: This script is used for ...
"""

import pandas as pd
import os

class PropertyStudy():
    def __init__(self):
        """构造函数，初始化属性"""
        self.study = "mm"

    def read_csv(self):
        fileName = "property_sold_huamu.csv"
        output_folder = "output"
        path = os.path.join(output_folder, fileName)
        df = pd.read_csv(path)

