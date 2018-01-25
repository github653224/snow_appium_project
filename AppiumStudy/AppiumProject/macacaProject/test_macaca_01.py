# -*- coding:utf-8 -*-
from macaca import WebDriver

desired_caps = {
    'browserName': 'Baidu', # Electon, Safari(iOS).
    'platformName': 'Android', # iOS, Android.
    'platformVersion': '*',
    'autoAcceptAlerts': True # Accept the Alerts in page automaticalliy.
}

# server_url = 'http://127.0.0.1:3456/wd/hub/'
server_url = 'http://127.0.0.1:3456/wd/hub/'

# You can omit the server_url if you use the default url above.
driver = WebDriver(desired_caps, server_url)

# You can also use a dict to represent the url.
driver = WebDriver(desired_caps, {
    'protocol': 'https',
    'hostname': '127.0.0.1',
    'port': 5678,
    'username': 'macaca',
    'password': '123456',
    'path': '/hub'
})

# Defaults
{
    'protocol': 'http',
    'hostname': '127.0.0.1',
    'port': 3456,
    'path': '/wd/hub'
}

# Which equals to
driver = WebDriver(desired_caps, 'https://macaca:123456@127.0.0.1:5678/hub')
driver.init()
driver.get("https://www.baidu.com")