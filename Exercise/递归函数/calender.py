import calendar
'''
日历模块

'''
#返回指定年月的日历
print(calendar.month(2018,7))

#返回指定一年的日历
print(calendar.calendar(2018))

#判断闰年  是闰年返回True 否则返回False
print(calendar.isleap(2000))

#返回某个月的weekday的第一天和这个月的天数
print(calendar.monthrange(2018,7))

#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2018,7))




