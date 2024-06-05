import time


def passwd():
   CT=time.localtime()
   yr=str(CT.tm_year)
   day=str(CT.tm_mday)
   month=str(CT.tm_mon)
   print(yr,day,month)
   time_list=[2024,6,1]
   P_yr=str(time_list[0])
   P_month=str(time_list[1])
   P_day=str(time_list[2])
   if P_yr == yr and P_month == month:
      if P_day == day:
        print("yes")

passwd()

#make sure code to get localtime() runs once the user opens tab
#so comparison can take place.