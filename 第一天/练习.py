from time import sleep
from  selenium import webdriver
dirver = webdriver.Chrome()
dirver.get('file:///C:/Users/86183/Desktop/课堂素材/注册A.html')

# 1绝对路径
# dirver.find_element_by_xpath('/html/body/form/div/fieldset/p[@id="p1"]/input').send_keys('admin')

# 2相对路径
dirver.find_element_by_xpath('//input[@id="userA"]').send_keys('w')
dirver.find_element()


sleep(3)
dirver.quit()
