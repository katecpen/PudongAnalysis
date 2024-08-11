# -*- coding: utf-8 -*-
"""
Created on 2024-07-28 20:12:11

@author: Kate Yang
@description: This script is used for ...
"""

from url_manager import UrlManager
from logs.log import MyLog
from html_downloader import HtmlDownloader
from property_parser import PropertyParser
from html_outputer import HtmlOutputer

import time
import random



class Spider():
    """爬虫程序主模块"""

    def __init__(self):
        """构造函数，初始化属性"""
        self.urls = UrlManager()
        self.log = MyLog("spider_main", "logs")
        self.downloader = HtmlDownloader()
        self.parser = PropertyParser()
        self.outputer = HtmlOutputer()
        self.testingMode = False
        # self.util=utill.DBConn()

    def craw(self, root_url):
        """爬虫入口函数"""
        if self.testingMode:
            areas = {"huamu":1}
        else:
            areas = {
                "huamu": 51,
                # "beicai": 2，
                # "biyun": 8, "caolu": 8, "chuansha": 8, "datuanzhen": 8,
                # "gaodong": 8, "gaohang": 8, "heqing": 8, "hangtou": 8, "huamu": 8,
                # "huinan": 8, "jinqiao": 8, "jinyang": 8, "kangqiao": 8, "laogangzhen": 8,
                # "lianyang": 8, "lingangxincheng": 8, "lujiazui": 8, "meiyuan": 8, "nanmatou": 8,
                # "nichengzhen": 8, "sanlin": 8, "shibo": 8, "shuyanzhen": 8, "tangqiao": 8,
                # "tangzhen": 8, "waigaoqiao": 8, "wanxiangzhen": 8, "weifang": 8, "xinchang": 8,
                # "xuanqiao": 8, "yangdong": 8, "yangjing": 8, "yangsi": 8, "qiantan": 8,
                # "yuanshen": 8, "yuqiao": 8, "zhangjiang": 8, "zhoupu": 8, "zhuqiao": 8
            }


        # 1、抓取所有二手房详情界面链接，并将所有连接放入URL管理模块
        for area, pg_sum in areas.items():
            for num in range(37, pg_sum + 1):
                # 1.1 拼接页面地址: https://nj.lianjia.com/ershoufang/gulou/pg2/
                pg_url = root_url + area + "/pg" + str(num) + "/"
                self.log.logger.info("1.1 拼接页面地址：" + pg_url)
                print("1.1 拼接页面地址：" + pg_url)
                # 1.2 启动下载器,下载页面.
                try:
                    html_cont = self.downloader.download(pg_url)
                except Exception as e:
                    self.log.logger.error("1.2 下载页面出现异常:" + repr(e))
                    time.sleep(60 * 30)
                else:
                    # 1.3 解析PG页面，获得二手房详情页面的链接,并将所有链接放入URL管理模块
                    try:
                        ershoufang_urls = self.parser.get_property_urls(html_cont)
                    except Exception as e:
                        self.log.logger.error("1.3 页面解析出现异常:" + repr(e))
                    else:
                        self.urls.add_new_urls(ershoufang_urls)
                        # 暂停0~3秒的整数秒，时间区间：[0,3]
                        time.sleep(random.randint(0, 3))

        if self.testingMode:
            time.sleep(60 * 1)
        else:
            time.sleep(60 * 20)
        # 2、解析二手房具体细心页面
        id = 1
        stop = 1
        if self.testingMode:
            stopWithTest = True
        else:
            stopWithTest = False
        while self.urls.has_new_url() and not stopWithTest:
            # 2.1 获取url
            try:
                detail_url = self.urls.get_new_url()
                self.log.logger.info("2.1 二手房页面地址：" + detail_url)
                print("2.1 二手房页面地址：" + detail_url)
            except Exception as e:
                print("2.1 拼接地址出现异常")
                self.log.logger.error("2.1 拼接地址出现异常:" + detail_url)

            # 2.2 下载页面
            try:
                detail_html = self.downloader.download(detail_url)
                time.sleep(random.randint(0, 5))
            except Exception as e:
                self.log.logger.error("2.2 下载页面出现异常:" + repr(e))
                self.urls.add_new_url(detail_url)
                time.sleep(60 * 30)
            else:
                # 2.3 解析页面
                try:
                    property_data = self.parser.parse_sold_property_data(detail_html, id)
                except Exception as e:
                    self.log.logger.error("2.3 解析页面出现异常:" + repr(e))
                else:
                    # 2.4 输出数据
                    try:
                        self.outputer.collect_data(property_data)
                    except Exception as e:
                        self.log.logger.error("2.4 输出数据出现异常:" + repr(e))
                    else:
                        print(id)
                        id = id + 1
                        stop = stop + 1
                        # 暂停0~3秒的整数秒，时间区间：[0,3]
                        time.sleep(random.randint(0, 3))
                        if stop == 1000:
                            stop = 1
                            time.sleep(60 * 20)


if __name__ == "__main__":
    # 设定爬虫入口URL
    root_url = "https://sh.lianjia.com/chengjiao/"
    # 初始化爬虫对象
    obj_spider = Spider()
    # 启动爬虫
    obj_spider.craw(root_url)
