from time import sleep
from selenium import webdriver
dirver = webdriver.Firefox()
dirver.get('file:///C:/Users/86183/Desktop/课堂素材/注册A.html')
dirver.find_element_by_tag_name('input').send_keys('admmin')
dirver.find_element_by_id('passwordA').send_keys('1')
dirver.find_element_by_id('telA').send_keys('12345666')
dirver.find_element_by_id('emailA').send_keys('1@qq.com')

# 1标签名 tag_name()
# dirver.find_element_by_tag_name('button').click()

# 2模糊超链接 partial_link_text()
# dirver.find_element_by_partial_link_text('访问').click()

# 3精准超链接 link_text()
# dirver.find_element_by_link_text('访问 新浪 网站').click()

sleep(3)
dirver.quit()
from time import sleep
from selenium import webdriver
dirver = webdriver.Firefox()
dirver.get('file:///C:/Users/86183/Desktop/课堂素材/注册A.html')
dirver.find_element_by_tag_name('input').send_keys('admmin')
dirver.find_element_by_id('passwordA').send_keys('1')
dirver.find_element_by_id('telA').send_keys('12345666')
dirver.find_element_by_id('emailA').send_keys('1@qq.com')

# 1标签名 tag_name()
# dirver.find_element_by_tag_name('button').click()

# 2模糊超链接 partial_link_text()
# dirver.find_element_by_partial_link_text('访问').click()

# 3精准超链接 link_text()
# dirver.find_element_by_link_text('访问 新浪 网站').click()

sleep(3)
dirver.find_element_by_id('passwordA').send_keys('1')
dirver.find_element_by_id('telA').send_keys('12345666')
dirver.find_element_by_id('emailA').send_keys('1@qq.com')

# 1标签名 tag_name()
# dirver.find_element_by_tag_name('button').click()

# 2模糊超链接 partial_link_text()
# dirver.find_element_by_partial_link_text('访问').click()

# 3精准超链接 link_text()
# dirver.find_element_by_link_text('访问 新浪 网站').click()

sleep(3)
dirver.quit()
