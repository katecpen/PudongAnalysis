# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:00:15 2018

@author: zhangying
"""

from logs.log import MyLog
import csv
import os

class HtmlOutputer():
    """数据输出收集模块"""

    def __init__(self):
        """构造函数，初始化属性"""
        self.log = MyLog("html_outputer", "logs")
        fileName = "property_sold_huamu.csv"
        # 定义文件路径
        output_folder = "output"
        self.path = os.path.join(output_folder, fileName)

        # 创建文件夹，如果它还不存在
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        with open(self.path, "w", newline="") as f:
            data = [
                "id", "小区名称", "所在区域", "总价", "单价",
                "房屋户型", "所在楼层", "建筑面积", "户型结构",
                "套内面积", "建筑类型", "房屋朝向", "建成年代",
                "装修情况", "建筑结构", "供暖方式", "梯户比例",
                "配备电梯", "链家编号", "交易权属", "挂牌时间",
                "房屋用途", "房屋年限", "房权所属"
            ]
            writer = csv.writer(f, dialect='excel')
            writer.writerow(data)


    def collect_data(self, data):
        if data is None:
            self.log.logger.error("页面数据收集：传入数据为空！")
            print("页面数据收集：传入数据为空！")
            return

        with open(self.path, "a", newline="") as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow(data)

        self.log.logger.info("2.4页面数据收集：成功!")
        print("2.4页面数据收集：成功!")