from appium import webdriver
desired_caps = {}
#平台名称，版本
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] ="9.0"
desired_caps['deviceName'] = "Android Emulator"
desired_caps['appActivity'] = "com.lemon.lemonban"
desired_caps['appPackage'] = "com.lemon.lemonban.activity.WelcomeActivity"
desired_caps['automationName'] = "UiAutomator2"

#与appium进行连接并发送要操作的apk信息
webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)