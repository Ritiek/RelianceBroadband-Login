#!/usr/bin/env python

import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

sign_in = browser.open("http://reliancebroadband.co.in/reliance/startportal_isg.do")
browser.select_form(name = "form1")

# replace 'user_id' and 'password' with your credentials
browser["userId"] = '<user_id>'
browser["password"] = '<password>'

browser.submit()
