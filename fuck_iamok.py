import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.blocking import BlockingScheduler

#打卡时间
c_minute="18"
c_hour="3,6,7" #保险起见，打多次卡
# c_week="mon-fri"
 
 
#用户名、密码
zhanghao=""
mima = ''

def work():
    # try:
    browser = webdriver.Chrome()
    browser.get('https://iamok.scut.edu.cn')

    #输入python
    inputs = browser.find_elements_by_class_name('login_box_input')
    button = browser.find_element_by_class_name('landing_btn_bg')

    time.sleep(2)
    inputs[0].send_keys(zhanghao)
    inputs[1].send_keys(mima)
    button.click()

    time.sleep(20)
    browser.find_elements_by_class_name('btn')[0].click()
    time.sleep(10)

    # while(b == []):
    #     b = browser.find_elements_by_class_name('btn')
    # print(browser)

    #退出浏览器
    browser.quit()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Clock Success!")
	# except:
	# 	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Clock Filed!")


if __name__ == '__main__':
    	#添加任务
	scheduler = BlockingScheduler()
	#设置定时任务时间
	scheduler.add_job(work,'cron', minute=c_minute,hour=c_hour)
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Add Task Work!")
	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		scheduler.shutdown()


