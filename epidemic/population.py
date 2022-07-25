from selenium import webdriver
import pandas as pd
import time

fileNameStr = 'population.csv'

'''定义爬虫类'''
class mySpider(object):
    '''设置爬取网址'''
    def __init__(self):
        self.url = "https://baike.baidu.com/item/%E4%B8%96%E7%95%8C%E5%90%84%E5%9B%BD%E4%BA%BA%E5%8F%A3%E6%8E%92%E5%90%8D/23333799"
        self.browser=webdriver.Edge("E:\CODE\msedgedriver.exe")

    '''打开网页'''
    def get_html(self):
        self.browser.get(self.url)
        time.sleep(3)

    '''爬取'''
    def parse(self):
        item={}
        result=[]
        file = open(fileNameStr, mode='w', encoding='utf-8')
        flag=0;

        '''找到人口数据栏'''
        li=self.browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div/div[2]/table/tbody/tr')
        for each in li:
            flag+=1
            if flag==1:
                continue    #表头不读取
            info_list=each.text.split('\n')

            '''单独处理中国一项，将大陆及港澳台人口合并'''
            if info_list[1]=='中华人民共和国':
                item['country'] = '中国'
                item['population'] = int(info_list[3].replace(',',''))
            elif info_list[0]=='中国香港' or info_list[0]=='中国澳门' or info_list[0]=='中国台湾':
                item['country'] = '中国'
                item['population'] += int(info_list[1].replace(',', ''))
            else:
                '''其余国家正常读取'''
                item['country'] = info_list[1]
                item['population'] = int(info_list[2].replace(',', ''))
            print(item)
            result.append(str(item['country'])+','+str(item['population']))

        '''写入文件'''
        for items in result:
            file.write(items)
            file.write('\n')
        file.close

    def main(self):
        self.get_html()
        self.parse()

if __name__ == '__main__':
    spider=mySpider()
    spider.main()

# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()

# country:
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[2]/div/a
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[7]/td[2]/div/a
#
# population:
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[6]/td[3]/div
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[7]/td[3]/div

# 中华人民共和国：
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/a
#
# 中国人口：
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/div[2]
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/div[2]
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/div[2]
# /html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/div[2]