# use Tkinter to show a digital clock
# tested with Python24    vegaseat    10sep2006
# https://www.daniweb.com/software-development/python/code/216785/tkinter-digital-clock-python
# http://en.sharejs.com/python/19617

# Anders E. Wallin, 2015-04-24
# GPLv3 license.
#
# added: UTC, localtime, date, MJD, DOY, week
from tkinter import *
import time
import datetime,requests
#import math

#import jdutil # https://gist.github.com/jiffyclub/1294443
#import gpstime



def tianqi():
	r2= requests.get('http://www.weather.com.cn/data/cityinfo/101120201.html') #http://www.weather.com.cn/data/cityinfo/101121005.html

	#r.encoding = 'utf-8'
	r2.encoding = 'utf-8'


	TQ=r2.json()['weatherinfo']

	#print(r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp']) 

	TXT=" \n"+TQ['city']+"   温度："+TQ['temp2']+"-"+TQ['temp1']+" "+TQ['weather']+"  更新时间："+TQ['ptime']
	return TXT



def tail(txt):
    aa=int(txt[-1])%4
    if aa >1:
        return txt[:5].replace(":"," : ")
    else:
        return txt[:5].replace(":"," . ")











root = Tk()
root.attributes("-fullscreen", True)
root.attributes('-alpha', 0.9) #透明度
# this should make Esc exit fullscrreen, but doesn't seem to work..
#root.bind('<Escape>',root.attributes("-fullscreen", True))
root.configure(background='black')
ziti= "LED Board-7"              #"courier new"      #"Inconsolata"

#root.geometry("1280x1024") # set explicitly window size
scale=0.8 # scale all fonts
time1 = ''
clock_lt = Label(root, font=(ziti, int(scale*250), ), fg='grey',bg='black')
clock_lt.pack()

# date_iso = Label(root, font=(ziti, int(scale*75), 'bold'), fg='grey',bg='black')
# #date_iso.pack()

date_etc = Label(root, font=("Monaco", int(scale*40), ), fg='grey',bg='black')
date_etc.pack()

clock_tq = Label(root, font=('幼圆', int(scale*50), ),fg='grey', bg='black')
clock_tq.config(text=tianqi())
clock_tq.pack()

# clock_gps = Label(root, font=(ziti, int(scale*40), 'bold'),fg='grey', bg='black')
# #clock_gps.pack()

# clock_tai = Label(root, font=(ziti, int(scale*40), 'bold'),fg='grey', bg='black')
# #clock_tai.pack()

    


    
def tick():
    global time1
    dt =datetime.datetime.utcnow()
    time2 = time.strftime('%I:%M:%S')#time.strftime('%H:%M:%S') # local
    #time_utc = time.strftime('%H:%M:%S', time.gmtime()) # utc
    # MJD
    #date_iso_txt = time.strftime('%Y-%m-%d', time.gmtime()) + "    %.5f" % jdutil.mjd_now()
    # day, DOY, week
    date_etc_txt = "\n\n %s    %s " % (time.strftime('%p  星期%w'), time.strftime('%Y年 %m月%d日'))
    #date_etc_txt=tail22(date_etc_txt)
    #leap_secs = 37
    #gps_leap_secs = leap_secs - 19
    
    #(gps_week, gps_s_w, gps_day, gps_s_day) = gpstime.gpsFromUTC(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, leapSecs=gps_leap_secs)
    #gps_hours = math.floor( gps_s_day / 3600.0 )
    #gps_minutes = math.floor( ( gps_s_day - gps_hours*3600.0 ) / 60.0 )
    #gps_seconds = gps_s_day - gps_hours*3600.0  - gps_minutes*60.0
    #gps_txt = " GPS Time %02d:%02d:%02d \nGPS Week.Day %d.%d" % (gps_hours,gps_minutes,gps_seconds,gps_week, gps_day)
    #dt_tai = dt + datetime.timedelta( seconds = leap_secs )
    #tai_txt = " TAI %02d:%02d:%02d" % (dt_tai.hour, dt_tai.minute, dt_tai.second)
    if time2 != time1: # if time string has changed, update it
        time1 = time2
        
        #showtime=time2+tail(time2[-1])
        clock_lt.config(text=tail(time2))
        
        #date_iso.config(text=date_iso_txt)
        date_etc.config(text=date_etc_txt)
        #clock_gps.config(text=gps_txt)
        #clock_tai.config(text=tai_txt)

    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock_lt.after(20, tick)

#root.bind("<Escape>", quit)
root.bind('<Key>',quit)
root.bind('<Motion>',quit)
tick()
root.mainloop()
