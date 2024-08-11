# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:59:59 2018

@author: zhangying
"""

import requests
from logs.log import MyLog
import random


class HtmlDownloader():
    """网页加载器"""

    def __init__(self):
        """构造函数，初始化属性"""
        self.log = MyLog("html_downloader", "logs")

        self.user_agent = [
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE) ",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0) ",
            "Mozilla/5.0 (Windows NT 5.1; zh-CN; rv:1.9.1.3) Gecko/20100101 Firefox/8.0",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        ]

        self.headers = {
            "Host": "sh.lianjia.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "macOS",
            "User-Agent": random.choice(self.user_agent),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            # "Sec-Fetch-Site": "same-origin",
            # "Sec-Fetch-Mode": "navigate",
            # "Sec-Fetch-User": "?1",
            # "Sec-Fetch-Dest": "document",
            "Referer": "https://sh.lianjia.com/chengjiao/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "lianjia_uuid=e00c68cd-991d-4530-a877-45d5649b4d9d; _ga=GA1.2.530741933.1719742564; _ga_00MKBBEWEN=GS1.2.1719742565.1.1.1719742788.0.0.0; _jzqc=1; _smt_uid=6681421d.3dc21291; crosSdkDT2019DeviceId=-a8vsjx-ty21s8-o59d3u4f9mqp8a8-1rxhv3yi6; ftkrc_=a09a4e78-6077-4e32-8d54-6187c1d81d46; lfrc_=63f1cde8-a37d-4aa1-81a2-07c445d1f2f3; _ga_BGW2B8P0NN=GS1.2.1719748545.1.0.1719748545.0.0.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219068c20b39229a-0b8f05288c47d-19525637-1484784-19068c20b3a241c%22%2C%22%24device_id%22%3A%2219068c20b39229a-0b8f05288c47d-19525637-1484784-19068c20b3a241c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; HMACCOUNT=F2D46EACADEF07BA; _ga_XLL3Z3LPTW=GS1.2.1722154734.1.0.1722154734.0.0.0; _ga_NKBFZ7NGRV=GS1.2.1722154734.1.0.1722154734.0.0.0; Qs_lvt_200116=1722165067; Qs_pv_200116=2530248306152801000%2C1046978260940932500%2C653399578516476200; _ga_E91JCCJY3Z=GS1.2.1722165075.1.1.1722165094.0.0.0; _ga_MFYNHLJT0H=GS1.2.1722165075.1.1.1722165094.0.0.0; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1722154729; _ga_KJTRWRHDL1=GS1.2.1722768046.1.0.1722768046.0.0.0; _ga_QJN1VP0CMS=GS1.2.1722768046.1.0.1722768046.0.0.0; select_city=310000; login_ucid=2000000436590591; lianjia_token=2.00145d0d2a44d9b73905f0241bb4fbbc49; lianjia_token_secure=2.00145d0d2a44d9b73905f0241bb4fbbc49; security_ticket=Ys5VrKsp/A/qDD08HcdVNRLCA594eb6wUY5OywZR0nq5yBimjk8H2vJxNbRzZzRqinDRu8QERLCqdnN64i4p8BtulLFSQL2XFX7XU07XIqZYTE1I2zFlckrNxPpAFFNTiMRPTkHT4cFehvdmDAYHgoPA2f28WqKH5rRcQ2deYqw=; _jzqckmp=1; _gid=GA1.2.2015696094.1723278302; _jzqx=1.1719747102.1723301735.6.jzqsr=google%2Ecom|jzqct=/.jzqsr=hip%2Elianjia%2Ecom|jzqct=/; lianjia_ssid=8d6ab20e-f879-4b2c-8ca3-78edcb4356af; _jzqa=1.1502018915332490200.1719747102.1723301735.1723308820.16; hip=lnsQERokK5ttLc9Qf9C1P9kevCFBLdFNW_a1nO_iyPbGsQ4vQ2lNAY3q043RvPAU3ZQbCf3NkYTcQgBQtK2zNZhIcqQ8WPZcCxKihKyepZOT97XlK60NfXhPYlRUGqvz7bHuejw8ppD-tGyaIsQ3pT7iyOPr9mcZmbOv0Lg8ml_U96Sc18mLdo3OtA%3D%3D; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1723309377; _jzqb=1.2.10.1723308820.1; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_LRLL77SF11=GS1.2.1723308830.14.1.1723309384.0.0.0; _ga_GVYN2J1PCG=GS1.2.1723308830.14.1.1723309384.0.0.0"
            }

    def download(self, url):
        """网页下载函数"""
        if url is None:
            self.log.logger.error("页面下载：url为空!!!")
            return None

        # 随机变换user-agent
        # headers = {
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #     "Accept-Encoding": "gzip, deflate, br",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     "Connection": "keep-alive",
        #     "Cookie": "lianjia_uuid=e00c68cd-991d-4530-a877-45d5649b4d9d; _ga=GA1.2.530741933.1719742564; _ga_00MKBBEWEN=GS1.2.1719742565.1.1.1719742788.0.0.0; _jzqc=1; _smt_uid=6681421d.3dc21291; crosSdkDT2019DeviceId=-a8vsjx-ty21s8-o59d3u4f9mqp8a8-1rxhv3yi6; ftkrc_=a09a4e78-6077-4e32-8d54-6187c1d81d46; lfrc_=63f1cde8-a37d-4aa1-81a2-07c445d1f2f3; _ga_BGW2B8P0NN=GS1.2.1719748545.1.0.1719748545.0.0.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219068c20b39229a-0b8f05288c47d-19525637-1484784-19068c20b3a241c%22%2C%22%24device_id%22%3A%2219068c20b39229a-0b8f05288c47d-19525637-1484784-19068c20b3a241c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; HMACCOUNT=F2D46EACADEF07BA; _ga_XLL3Z3LPTW=GS1.2.1722154734.1.0.1722154734.0.0.0; _ga_NKBFZ7NGRV=GS1.2.1722154734.1.0.1722154734.0.0.0; Qs_lvt_200116=1722165067; Qs_pv_200116=2530248306152801000%2C1046978260940932500%2C653399578516476200; _ga_E91JCCJY3Z=GS1.2.1722165075.1.1.1722165094.0.0.0; _ga_MFYNHLJT0H=GS1.2.1722165075.1.1.1722165094.0.0.0; select_city=310000; lianjia_ssid=144909c8-1a2e-4bc3-93c7-15436e5ca45f; _gid=GA1.2.1284536603.1722762565; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1722154729; _jzqckmp=1; _jzqa=1.1502018915332490200.1719747102.1722762606.1722764941.5; _jzqx=1.1719747102.1722764941.2.jzqsr=google%2Ecom|jzqct=/.jzqsr=sh%2Elianjia%2Ecom|jzqct=/ershoufang/beicai/pg1/; login_ucid=2000000436590591; lianjia_token=2.0014dbf3cc445f49df0576dafda04aa658; lianjia_token_secure=2.0014dbf3cc445f49df0576dafda04aa658; security_ticket=l0zG4lv4qMB3jcrlVGo+KrLJ52vVaaqf8RR15lQnvGOLwwxn416grkLvguzJu9bfBjWhGbn8GHWEU/CorYwsoNnv63x81yPc+FeedD6q9VFi5psWzSRhAd7p9tUfKVbOvIld0OFfaKwl+fm8pfdd63YFFDCgTsjMedTb0lmaYhw=; _jzqb=1.22.10.1722764941.1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1722766520; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_LRLL77SF11=GS1.2.1722764948.3.1.1722766522.0.0.0; _ga_GVYN2J1PCG=GS1.2.1722764948.3.1.1722766522.0.0.0",
        #     "Cache-Control": "max-age=0",
        #     "Host": "imapi.lianjia.com",
        #     "User-Agent": random.choice(self.user_agent),
        #
        #
        # }

        r = requests.get(url, headers=self.headers)

        #发送多次请求可能触发人机验证，需要更新cookie
        if r.status_code != 200 or r.text == None:
            self.log.logger.error("页面下载：响应错误：%d" % r.status_code)
            print("May require update cookie")
            #try reset cookie
            new_cookie = input("请输入新的 Cookie: ")

            # 更新 headers 中的 Cookie
            self.headers["Cookie"] = new_cookie

            r = requests.get(url, headers=self.headers)
            if r.text:
                self.log.logger.info("2.2 页面下载：成功!")
                return r.text
            else:
                self.log.logger.info("2.2 页面下载：失败!")
                print("页面下载：失败!")
                return None
        print("2.2 页面下载：成功!")
        self.log.logger.info("2.2 页面下载：成功!")
        return r.text
