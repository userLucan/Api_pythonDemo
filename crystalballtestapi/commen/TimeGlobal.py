from datetime import date, timedelta


def day_time(yestday):
    # 时间参数公共方法
    # 获取今天或者前七天时间
    day = "yestday"
    if yestday == day:
        day = (date.today() + timedelta(days=-7)).strftime("%Y%m%d")
    else:
        day = (date.today()).strftime("%Y%m%d")
    return day


def year_time():
    # 获取当前年时间
    year = (date.today()).strftime("%Y")
    return year


def get_token():
    # token参数公共变量方法
    token = "0acc34be-56d0-4927-8ee2-1281fc8bce4f"
    return token


def today_time():
    # 获取当前日时间天
    year = (date.today()).strftime("%d")
    return year


def January_time():
    # 获取当前上一个月时间
    day = (date.today() + timedelta(days=-31)).strftime("%m")
    return day


def Lastmonth_time(yestmonth):
    # 获取当前年当前月的上一月以及本月日期
    day = "yestmonth"
    if yestmonth == day:
         day = (date.today() + timedelta(days=-31)).strftime("%Y%m")
    else:
         day = (date.today() + timedelta(days=-1)).strftime("%Y%m")
    return day


if __name__ == '__main__':
    # login = "crystalBall-web/overall/TotolUsers"
    # sss=TestGlobal()
    # print(sss.test_url()+login)
    print(day_time(yestday="yestday"))
    # print(sss.get_token())
    # url = "crystalBall-web/overall/TotolUsers"
    # data = {"TimeVender": "03",
    #         "Year":TestGlobal().year_time(),
    #         "Type": "02",
    #         "region": "10",
    #         "line": "3",
    #         "column": "0",
    #         "token":TestGlobal().get_token()}
    # print (TestGlobal ( ).get_token ( ))
    print(day_time('day'))
    print(today_time())
    # response = requests.post(url=TestGlobal().test_url()+url,data=data)
    print(January_time())
    print(Lastmonth_time(yestmonth="month"))
