#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver


def open_web(url):
    """
    打开chrome浏览起
    :return:
    """
    if not url:
        print "未传入你需要打开的网站地址..."
        return None
    browser = webdriver.Chrome()
    browser.get(url)
    return browser

# def find_but_id(browser, find_id):
#     """
#     通过id查找元素
#     :return:
#     """
#     if not browser or not find_id:
#         print "参数错误：browser = {0}, find_id = {1}".format(browser, find_id)
#         return None
#     browser.find_element_by_id(find_id).send_keys(the_selete_key)



def selete_the_key(browser, the_selete_key):
    """
    查找关键词
    :return:
    """
    if not browser or not the_selete_key:
        print "参数错误:browser={0}, the_selete_key={1}...".format(browser, the_selete_key)
        return None
    # 需要查找的关键词
    browser.find_element_by_id("kw").clear()
    browser.find_element_by_id("kw").send_keys(the_selete_key)
    # 点击查找按钮
    selete_but = "su"
    but = browser.find_element_by_id(selete_but)
    if but:
        but.click()
        print "开始查找..."
    else:
        print "未发现按钮：{0}".format(selete_but)
        return None
    return browser

def deal_page_data(borvser):
    """
    处理查找页面结果
    :return:
    """
    # 获取网页源代码
    # html = borvser.page_source
    # 获取所有都查找结果
    all_selete_eles = borvser.find_elements_by_css_selector()
    if len(all_selete_eles) == 0:
        print "获取需要查找都元素失败..."
    else:
        pass


def main():
    """
    开始
    :return:
    """
    # 打开浏览器
    url = "http://www.baidu.com"
    browser = open_web(url)
    # 关键词搜索
    the_selete_key = u"成都"
    borvser = selete_the_key(browser, the_selete_key)
    # 筛选所需要的元素和url
    deal_page_data(borvser)



if __name__ == '__main__':
    main()
