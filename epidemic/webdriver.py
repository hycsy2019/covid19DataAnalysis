from selenium import webdriver
import time
import pandas as pd
import datetime

'''根据日期给csv文件命名'''
today = datetime.date.today()
fileNameStr = 'epidemic' + str(today) + '.csv'

'''定义爬虫类'''


class mySpider(object):
    '''设置爬取网址'''

    def __init__(self):
        self.url = "https://sa.sogou.com/new-weball/page/sgs/epidemic?type_page=VR"
        self.browser = webdriver.Edge("E:\CODE\msedgedriver.exe")

    '''转到要爬取的网页'''

    def get_html(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(
            '//*[@id="async"]/div/div[1]/div[3]/div[1]/div/div[1]/a[2]').click()  # 点击“国外疫情”按钮
        self.browser.find_element_by_xpath('//*[@id="tab-pane-column_0"]/div[3]/a').click()  # 点击“查看更多”按钮
        time.sleep(3)

    '''单独爬取中国数据'''

    def China(self, file):
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_xpath(
            '//*[@id="async"]/div/div[1]/div[3]/div[1]/div/div[1]/a[1]'))  # 点击“国内疫情”按钮
        time.sleep(3)
        file.write('中国,')
        file.write(self.browser.find_element_by_xpath(
            '//*[@id="async"]/div/div[1]/div[3]/div[1]/div/ul/li[1]/span[1]/strong/span').text)
        file.write(',')
        file.write(self.browser.find_element_by_xpath('//*[@id="async"]/div/div[1]/div[3]/div[1]/div/ul/li[1]/em').text)
        file.write(',')
        file.write(self.browser.find_element_by_xpath('//*[@id="async"]/div/div[1]/div[3]/div[1]/div/ul/li[2]/em').text)
        file.write(',')
        file.write(self.browser.find_element_by_xpath('//*[@id="async"]/div/div[1]/div[3]/div[1]/div/ul/li[4]/em').text)
        file.write('\n')

    def parse(self):
        item = {}
        result = []
        file = open(fileNameStr, mode='w', encoding='utf-8')

        '''爬取国外数据所有条目'''
        li = self.browser.find_elements_by_xpath('//*[@id="overseasChart"]/div')
        for each in li:
            result_item = each.text.split(',')
            info_list = each.text.split('\n')
            item['country'] = info_list[0]
            item['new'] = info_list[1]
            item['total'] = info_list[2]
            item['cured'] = info_list[3]
            item['death'] = info_list[4]
            # print(item)
            result.append(result_item)
        for items in result:
            file.write("".join(items).replace('\n', ','))
            file.write('\n')

        '''爬取中国数据'''
        self.China(file)

        file.close

    def main(self):
        self.get_html()
        self.parse()


if __name__ == '__main__':
    spider = mySpider()
    spider.main()

# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()

# country
# //*[@id="overseasChart"]/div[1]/div[1]/span[1]
# //*[@id="overseasChart"]/div[2]/div[1]/span[1]
#
# new
# /html/body/div[5]/div/div[9]/div[2]/div[1]/div/span[2]
# /html/body/div[5]/div/div[9]/div[2]/div[2]/div/span[2]
#
# total
# /html/body/div[5]/div/div[9]/div[2]/div[1]/div/span[3]
# /html/body/div[5]/div/div[9]/div[2]/div[2]/div/span[3]
#
# cured
# /html/body/div[5]/div/div[9]/div[2]/div[1]/div/span[4]
# /html/body/div[5]/div/div[9]/div[2]/div[2]/div/span[4]
#
# death
# /html/body/div[5]/div/div[9]/div[2]/div[1]/div/span[5]
# /html/body/div[5]/div/div[9]/div[2]/div[2]/div/span[5]
