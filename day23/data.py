"""
data
"""

from datetime import date, datetime
import calendar


def print_mydata(mydata):
    print(f'今天是:{mydata}\n')

    year_calendar_str = calendar.calendar(mydata.year)
    print(f"{mydata.year}年的日历图：{year_calendar_str}\n")

    is_leap = calendar.isleap(mydata.year)
    print_leap_str = "%s年是闰年" if is_leap else "%s年不是闰年\n"
    print(print_leap_str % mydata.year)

    month_calendar_str = calendar.month(mydata.year, mydata.month)
    print(f"{mydata.year}年-{mydata.month}月的日历图：{month_calendar_str}\n")

    weekday, days = calendar.monthrange(mydata.year, mydata.month)
    print(f'{mydata.year}年-{mydata.month}月的第一天是那一周的第{weekday}天\n')
    print(f'{mydata.year}年-{mydata.month}月共有{days}天\n')

    month_first_day = date(mydata.year, mydata.month, 1)
    print(f'当月第一天：{month_first_day}\n')

    month_last_day = date(mydata.year, mydata.month, days)
    print(f'当月最后一天：{month_last_day}\n')


print_mydata(date.today())
