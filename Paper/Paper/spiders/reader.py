# from PIL import Image
# import os
# import subprocess
# from selenium import webdriver
# import scrapy
# def image_to_string(img, cleanup=True, plus=''):
#     # cleanup为True则识别完成后删除生成的文本文件
#     # plus参数为给tesseract的附加高级参数
#     subprocess.check_output('tesseract ' + img + ' ' +
#                             img + ' ' + plus, shell=True)  # 生成同名txt文件
#     text = ''
#     with open(img + '.txt', 'r') as f:
#         text = f.read().strip()
#     if cleanup:
#         os.remove(img + '.txt')
#     return text
# def Reader(url):
#     n = ''
#     formdata = {
#         'username': ' 18813290978',
#         'password': ' xsy123456',
#         '   checkCode': n,
#         'submit': ' 立即登录',
#     }
#     # url = 'http://login.moneyplat.com/login?service=http%3A%2F%2Fwww.moneyplat.com%2Faccount%2FtoAccount.html'
#     driver = webdriver.PhantomJS()
#     driver.maximize_window()  # 将浏览器最大化
#     driver.get(url)
#     driver.find_element_by_id('username').clear()
#     result = r'E:\Project\Paper\Paper\spiders\result.png'
#     resource = r'E:\Project\Paper\Paper\spiders\resource.png'
#     driver.save_screenshot(resource)  # 截取当前网页，该网页有我们需要的验证码
#     imgelement = driver.find_element_by_id('validate')  # 定位验证码
#     location = imgelement.location  # 获取验证码x,y轴坐标
#     size=imgelement.size  #获取验证码的长宽
#     rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
#     i=Image.open(resource) #打开截图
#     frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
#     frame4=frame4.resize((100,30))
#     frame4.save(result)
#
#     driver.find_element_by_id('username').send_keys('18813290978')
#     driver.find_element_by_id('password').clear()
#     driver.find_element_by_id('password').send_keys('xsy123456')
#     driver.find_element_by_id('checkCode').clear()
#     subprocess.Popen('result.png', shell=True)
#     driver.find_element_by_id('checkCode').send_keys(input('输入验证码'))
#     driver.find_element_by_name('submit').click()
#     cookie_list = driver.get_cookies()
#     cookies = []
#     cookie_dict = {}
#     for cookie in cookie_list:
#         if 'name' in cookie and 'value' in cookie:
#             cookie_dict[cookie['name']] = cookie['value']
#             for key,value in cookie_dict.items():
#                 cookies.append(key+'='+value,)
#     cookies = set(cookies)
#     cookies = ','.join(i for i in cookies)
#     # return cookies
#     print(cookies)
#     # print(cookie_dict)
# Reader('http://login.moneyplat.com/login')
# # text=image_to_string(result).strip() #使用image_to_string识别验证码
# # print(text)
