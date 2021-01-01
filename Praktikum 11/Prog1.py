from datetime import date
import datetime

 
def diffdate(x):
     dt_now = str(date.today())

     print('Tanggal Hari Ini    :', dt_now)

     dt_in = str(x)

     print('Tanggal Sebelumnya  :', dt_in)
     
     add_days = date.today() - datetime.datetime.strptime(x, '%Y-%m-%d').date() ;
 
     print('Maka selisih hari   :', str(add_days.days))

diffdate("2020-12-24")
