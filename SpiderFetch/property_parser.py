# -*- coding: utf-8 -*-
"""
Created on 2024-07-28 20:12:11

@author: Kate Yang
@description: This script is used for ...
"""

from bs4 import BeautifulSoup
from logs.log import MyLog


class PropertyParser():
    """网页解析模块"""

    def __init__(self):
        """构造函数，初始化属性"""
        self.log = MyLog("html_parser", "logs")

    def parse_sold_property_data(self, html_cont, id):
        if html_cont is None:
            self.log.logger.error("页面解析(detail)：传入页面为空！")
            print("页面解析(detail)：传入页面为空！")
            return

        property_data = []
        communityName = "None"
        areaName = "None"
        total_price = "None"
        unit_price = "None"

        bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        try:
            # 处理所在区域和小区名称
            deal_bread_div = bsObj.find('div', class_='deal-bread')
            if deal_bread_div:
                links = deal_bread_div.find_all('a')
                if len(links) >= 2:
                    areaName = links[-2].get_text().replace('二手房成交', '')
                    communityName = links[-1].get_text().replace('二手房成交', '')

            # 处理总价
            total_price_element = bsObj.find('span', class_='dealTotalPrice')
            if total_price_element:
                total_price = total_price_element.i.get_text()

            # 处理单价
            unit_price_element = bsObj.find('div', class_='price')
            if unit_price_element:
                unit_price = unit_price_element.b.get_text()

            property_data.append(id)
            property_data.append(communityName)
            property_data.append(areaName)
            property_data.append(total_price)
            property_data.append(unit_price)

            counta = 13
            for a_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "base"}).find("div", {
                "class": "content"}).ul.findAll("li"):
                # print(child1)
                [s.extract() for s in a_child("span")]
                property_data.append(a_child.get_text())
                counta = counta - 1

            while counta > 0:
                property_data.append("null")
                counta = counta - 1

            countb = 6
            for b_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "transaction"}).find("div", {
                "class": "content"}).ul.findAll("li"):
                [s.extract() for s in b_child("span")]
                property_data.append(b_child.get_text())
                countb = countb - 1

            while countb > 0:
                property_data.append("null")
                countb = countb - 1

            self.log.logger.info("2.3 页面解析(detail)：页面解析成功！")
            print("2.3 页面解析(detail)：页面解析成功！")
        except Exception as e:
            print(f"2.3 发生错误: {e}")

        return property_data

    # def get_ershoufang_data(self, html_cont, id):
    #     """获取二手房页面详细数据"""
    #     if html_cont is None:
    #         self.log.logger.error("页面解析(detail)：传入页面为空！")
    #         print("页面解析(detail)：传入页面为空！")
    #         return
    #
    #     ershoufang_data = []
    #     communityName = "null"
    #     areaName = "null"
    #     total = "null"
    #     unitPriceValue = "null"
    #
    #     bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
    #
    #     tag_com = bsObj.find("div", {"class": "communityName"}).find("a")
    #     if tag_com is not None:
    #         communityName = tag_com.get_text()
    #     else:
    #         self.log.logger.error("页面解析(detail)：找不到communityName标签！")
    #
    #     tag_area = bsObj.find("div", {"class": "areaName"}).find("span", {"class": "info"}).find("a")
    #     if tag_area is not None:
    #         areaName = tag_area.get_text()
    #     else:
    #         self.log.logger.error("页面解析(detail)：找不到areaName标签！")
    #
    #     tag_total = bsObj.find("span", {"class": "total"})
    #     if tag_total is not None:
    #         total = tag_total.get_text()
    #     else:
    #         self.log.logger.error("页面解析(detail)：找不到total标签！")
    #
    #     tag_unit = bsObj.find("span", {"class": "unitPriceValue"})
    #     if tag_unit is not None:
    #         unitPriceValue = tag_unit.get_text()
    #     else:
    #         self.log.logger.error("页面解析(detail)：找不到total标签！")
    #
    #     ershoufang_data.append(id)
    #     ershoufang_data.append(communityName)
    #     ershoufang_data.append(areaName)
    #     ershoufang_data.append(total)
    #     ershoufang_data.append(unitPriceValue)
    #
    #     # print(bsObj.find("div",{"class":"introContent"}).find("div",{"class":"base"}).find("div",{"class":"content"}).ul)
    #     counta = 12
    #     for a_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "base"}).find("div", {
    #         "class": "content"}).ul.findAll("li"):
    #         # print(child1)
    #         [s.extract() for s in a_child("span")]
    #         ershoufang_data.append(a_child.get_text())
    #         counta = counta - 1
    #
    #     while counta > 0:
    #         ershoufang_data.append("null")
    #         counta = counta - 1
    #
    #     countb = 8
    #     for b_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "transaction"}).find("div", {
    #         "class": "content"}).ul.findAll("li"):
    #         information = b_child.span.next_sibling.next_sibling.get_text()
    #         ershoufang_data.append(information)
    #         countb = countb - 1
    #
    #     while countb > 0:
    #         ershoufang_data.append("null")
    #         countb = countb - 1
    #
    #     self.log.logger.info("2.3 页面解析(detail)：页面解析成功！")
    #     print("2.3 页面解析(detail)：页面解析成功！")
    #     return ershoufang_data

    def get_property_urls(self, html_cont):
        if html_cont is None:
            self.log.logger.error("页面解析(page)：pg页面为空！")
            print("页面解析(page)：pg页面为空！")
            return

        property_urls = set()
        bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        # sellListContent = bsObj.find("ul", {"class": "sellListContent"})
        list_items = bsObj.select('ul.listContent > li')

        if list_items is not None:
            for item in list_items:
                # if child["class"][0] == "clear":
                link = item.find('a', class_='img')['href']
                if link:
                    property_urls.add(link)
                    self.log.logger.info(link)
                    # print(child.find("a",{"class":"img"})["href"])
        else:
            self.log.logger.error("页面解析(page)：找不到sellListContent标签！")

        self.log.logger.info("1.3 PG页面解析：pg页面解析成功！")
        print("1.3 页面解析：pg页面解析成功！")
        return property_urls