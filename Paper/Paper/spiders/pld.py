# -*- coding: utf-8 -*-
import scrapy
import re
import time
from Paper.items import Item,VIPItem
# from selenium import webdriver
import pymongo

client = pymongo.MongoClient('localhost')
paper = client['paper']
Item_n = paper['Item']
class PldSpider(scrapy.Spider):
    name = 'pld'
    allowed_domains = ['moneyplat.com']
    start_urls = ['http://www.moneyplat.com/bonds/bondsInvestList.html']

    def start_requests(self):
        url = 'https://www.moneyplat.com/show/toVipInvest.html?peroid=0&pageNo=1413&pageSize=10'
        # url = 'http://www.moneyplat.com/bonds/bondsInvestList.html?rate=&money=&pageNo=705&pageSize=10'
        yield scrapy.Request(url,callback=self.index_parse)

    def index_parse(self, response):
        item = Item()
        base_url = 'https://www.moneyplat.com'
        url=response.css('a[href*=invest]::attr(href)').extract()
        # url = url[2:]
        # next = base_url + re.search(r'<a class="nav" .*onclick=(.*?)>下一页',response.text,flags=re.S).group(1).lstrip('"studio_open_url(').rstrip(')"').strip("'")
        next = base_url + re.search(r'<a class="nav" .*onclick="studio_open_url\(\'(.+)\'\)">下一页',response.text,flags=re.S).group(1).lstrip('"studio_open_url(').rstrip(')"').strip("'")
        # tag = re.search(r'<a href=.*class="(listatz.*?)">', response.text, flags=re.S).group(1)
        for i in url :
            item['url'] = base_url+i
            item['no'] = re.search(r'pageNo=(\d+)',next,flags=re.S).group(1)
            yield item
            time.sleep(0.5)
        urls = Item_n.find()
        for i in urls:
            yield scrapy.Request(i['url'],callback=self.content_parse)
            # Item_n.delete_one({'url':i['url']})
        if next:
            yield scrapy.Request(next,callback=self.index_parse)
    def content_parse(self,response):
        data = response.css('div.jiben-info').extract_first()
        gender = re.search(r'性别：(.*?)<',data,flags=re.S).group(1).strip()
        education = re.search(r'最高学历：(.*?)<',data,flags=re.S).group(1).strip()
        age = re.search(r'年龄：(\d*?)<',data,flags=re.S).group(1).strip()
        house = re.search(r'住宅情况：(.*?)<',data,flags=re.S).group(1).strip()
        marriage = re.search(r'婚姻状况：(.*?)<',data,flags=re.S).group(1).strip()
        description = re.search(r'<li class="info-last">借款描述：(.*?)<',data,flags=re.S).group(1).strip()
        data_1 = response.css('div.income-lt').extract_first()
        rate = re.search(r'历史年化利率.*?(\d+\.*\d*).*</span>%</li>',data_1,flags=re.S).group(1).strip()
        period = re.search(r'投资期限.*?(\d+)</span>个月</li>',data_1,flags=re.S).group(1).strip()
        count = re.search(r'逾期笔数：(\d+)<', response.text, flags=re.S).group(1).strip()
        count_1 = re.search(r'正常还款笔数：(\d+)<', response.text, flags=re.S).group(1).strip()
        amount = re.search(r'项目本金：.*>(\d+\.\d+元)</span></p>', response.text, flags=re.S).group(1).strip()
        item = VIPItem()
        for field in item.fields:
            item[field] = eval(field)
        yield item
        # print(gender,education,age,house,description,count,amount,rate,period,marriage)

    # def Reader(self,url):
    #     n = ''
    #     # url = 'http://login.moneyplat.com/login?service=http%3A%2F%2Fwww.moneyplat.com%2Faccount%2FtoAccount.html'
    #     driver = webdriver.PhantomJS()
    #     driver.maximize_window()  # 将浏览器最大化
    #     driver.get(url)
    #     driver.find_element_by_id('username').clear()
    #     result = r'E:\Project\Paper\Paper\result.png'
    #     resource = r'E:\Project\Paper\Paper\resource.png'
    #     driver.save_screenshot(resource)  # 截取当前网页，该网页有我们需要的验证码
    #     imgelement = driver.find_element_by_id('validate')  # 定位验证码
    #     location = imgelement.location  # 获取验证码x,y轴坐标
    #     size = imgelement.size  # 获取验证码的长宽
    #     rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
    #               int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    #     i = Image.open(resource)  # 打开截图
    #     frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    #     frame4 = frame4.resize((100, 30))
    #     frame4.save(result)
    #
    #     driver.find_element_by_id('username').send_keys('18813290978')
    #     driver.find_element_by_id('password').clear()
    #     driver.find_element_by_id('password').send_keys('xsy123456')
    #     driver.find_element_by_id('checkCode').clear()
    #     a = Image.open(result)
    #     a.show()
    #     driver.find_element_by_id('checkCode').send_keys(input('输入验证码'))
    #
    #     driver.find_element_by_name('submit').click()
    #     cookie_list = driver.get_cookies()
    #     cookies = []
    #     cookie_dict = {}
    #     for cookie in cookie_list:
    #         if 'name' in cookie and 'value' in cookie:
    #             cookie_dict[cookie['name']] = cookie['value']
    #             for key, value in cookie_dict.items():
    #                 cookies.append(key + '=' + value, )
    #     cookies = set(cookies)
    #     cookies = ','.join(i for i in cookies)
    #     return cookies
