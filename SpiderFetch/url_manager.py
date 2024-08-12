# -*- coding: utf-8 -*-
"""

@author: Kate Yang
"""

""""""

from collections import deque



class UrlManager():
    """url管理模块"""

    def __init__(self):
        """构造函数，初始化属性"""
        self.new_urls = deque()  # use FIFO to follow the original order of urls
        self.old_urls = deque()

    def add_new_url(self, url):
        """向管理器中添加一个URL"""
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)

    def add_new_urls(self, urls):
        """向管理器中添加批量URL"""
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_url(self):
        """从url集合中弹出一个url"""
        new_url = self.new_urls.popleft()
        self.old_urls.append(new_url)
        return new_url

    def has_new_url(self):
        """判断是否还有新的url"""
        return len(self.new_urls) != 0
