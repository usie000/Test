#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-06 19:44:40
# @Author  : jm (helloworld135@qq.com)
# @Link    : ${link}
# @Version : $Id$
import os
import pytest
from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import time
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://127.0.0.1:4723/wd/hub'
PLATFORM_VERSION = '6.0'

class TestWebViewAndroid():
	@pytest.fixture(scope="function")
	def driver(self, request):
		desired_caps = {

			'appPackage':'com.hexin.plat.kaihu',

			'appActivity':'com.hexin.plat.kaihu.activity.StartActivity',
			'platformName':'Android',

			'platformVersion':PLATFORM_VERSION,

			'deviceName':'OZ59IZWWAQKRUKYT',

		}
		driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)
		def fin():
			driver.quit()

		request.addfinalizer(fin)
		return driver  # provide the fixture value


	def test_install(self,driver,request):

		time.sleep(5)
		driver.find_element_by_id("com.hexin.plat.kaihu:id/main_tab_open_account").click()
		driver.find_element_by_id("com.hexin.plat.kaihu:id/kaihuBtn").click()
		driver.find_element_by_id("com.hexin.plat.kaihu:id/phone_num").send_keys("0000")

		driver.get_screenshot_as_file('../screenshot/foo.png')
		time.sleep(10)

		#driver.install_app('D:/Program Files/python-3.6.2/projects/to/kaihu_V5.70.01_20170904_e6d4c50_app_release.apk')
if __name__ == '__main__':
	pytest.main("-q test_0906.py")
