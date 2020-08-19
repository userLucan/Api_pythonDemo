from datetime import date,timedelta

class TestGlobal():
    def test_url(self):
    #url公共方法
        url = "http://crystalball.wasu.com/"
        return url
    def day_time(self,yestday):
        #时间参数公共方法
        #获取今天或者前七天时间
        day ="yestday"
        if yestday== day:
            day = (date.today() + timedelta(days=-7)).strftime("%Y%m%d")
        else:
            day = (date.today() ).strftime("%Y%m%d")
        return day
    def year_time(self):
        #获取当前年时间
        year = (date.today() ).strftime("%Y")
        return year
    def get_token(self):
        #token参数公共变量方法
        token = "901e17c4-6f5c-4466-95c4-4c379453e206"
        return token
    def today_time(self):
        #获取当前日时间天
        year = (date.today ( )).strftime ("%d")
        return year
    def January_time(self):
        #获取当前上一个月时间
        day = (date.today() + timedelta(days=-31)).strftime("%m")
        return day
    def Lastmonth_time(self,yestmonth):
        #获取当前年当前月的上一月以及本月日期
        day = "yestmonth"
        if yestmonth==day:
            month = day = (date.today() + timedelta(days=-31)).strftime("%Y%m")
        else:
            month = day = (date.today ( ) + timedelta (days=-1)).strftime ("%Y%m")
        return day

if __name__ == '__main__':
    # login = "crystalBall-web/overall/TotolUsers"
    # sss=TestGlobal()
    # print(sss.test_url()+login)
    print(TestGlobal().day_time(yestday="yestday"))
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
    print(TestGlobal().year_time())
    print (TestGlobal ( ).today_time ( ))
    # response = requests.post(url=TestGlobal().test_url()+url,data=data)
    print (TestGlobal().January_time())
    print(TestGlobal().Lastmonth_time(yestmonth="yestmonth"))