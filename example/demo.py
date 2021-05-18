"""
demo.py
The demo of WeReadScan.py
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
"""

from selenium.webdriver import Chrome, ChromeOptions
from WeReadScan import WeRead

# 重要！为webdriver设置headless
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1440,900')

# 启动webdriver(--headless)
headless_driver = Chrome(options=chrome_options)

with WeRead(headless_driver, debug=True) as weread:

    # 重要！登陆
    weread.login()
    # 爬去指定url对应的5图书资源并保存到当前文件夹
    weread.scan2pdf('https://weread.qq.com/web/reader/77c323107210dbf677c5773', keep_color=True)