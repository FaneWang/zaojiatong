# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger


class ZaojiatongDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self, timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        return cls(timeout=crawler.settgings.get('SELENIUM_TIMEOUT'))

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        self.logger.debug('Chrome is Starting')
        cookie_str = 'lastHost=hubei.zjtcn.com; lastHost=hubei.zjtcn.com; mainHost=hubei.zjtcn.com; fac_mat=; REF_SEARCH_COUNT=0; GOV_SEARCH_COUNT=1940928; ASK_SEARCH_COUNT=2871919; SHOP_SEARCH_COUNT=80934; GUESSINGHD=2018%2F11%2F5; jsid=83467ea6-55da-46c9-bee6-889c8000683f; Hm_lvt_a01b74f783ea1eda2c633ceefd483123=1540264556,1541149549,1541378015,1541388275; cookie_indexScroll=; cookie_indexScroll_date=; lastHost=gd.zjtcn.com; mainHost=gd.zjtcn.com; userLoginCookie=0; user_uid=18502827757; Hm_lpvt_a01b74f783ea1eda2c633ceefd483123=1541393031'

        list1 = cookie_str.split('; ')
        list2 = [li.split('=') for li in list1]
        dict1 = {li[0]: li[1] for li in list2}
        self.browser.add_cookie(dict1)
        try:
            self.browser.get(request.url)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-box .clearfix')))
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, request=request, status=500)
