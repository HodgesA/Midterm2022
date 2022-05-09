from datetime import date
import holidays

us_holidays = holidays.US()
ni_holidays = holidays.NI()
ng_holidays = holidays.NG()
# the below is the same, but takes a string:
us_holidays = holidays.country_holidays('US')
ng_holidays = holidays.country_holidays('NG')
ni_holidays = holidays.country_holidays('NI')

date(2022, 1, 1) in us_holidays 
date(2022, 1, 2) in us_holidays 
date(2022, 4, 14) in ni_holidays
date(2022, 10, 14) in ni_holidays
date(2022, 5, 1) in ng_holidays
date(2022, 5, 9) in ng_holidays
us_holidays.get('2022-01-01') 
ni_holidays.get('2022-04-14')
ng_holidays.get('2022-05-01')

