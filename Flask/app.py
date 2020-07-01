import pandas as pd
from flask import (Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response)
import datetime 

app = Flask(__name__)

def parse_datetime(data):
    dt = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
    return dt

ip_monthly = pd.read_csv('/home/programming/python/ip_monthly.csv',engine='python',na_values='-',header=None,usecols=[0, 1],names=['ip','count'],converters={'count':int})
ip_daily = pd.read_csv('/home/programming/python/ip_daily.csv',engine='python',na_values='-',header=None,usecols=[0, 1],names=['ip','count'],converters={'count':int})
ip = pd.read_csv('/home/programming/python/ip.csv',engine='python',na_values='-',header=None,usecols=[0, 1],names=['ip','count'],converters={'count':int})
ip.append(ip_monthly)
ip.append(ip_daily)
df = ip.groupby('ip').sum().sort_values(by='count', ascending=False).reset_index()
@app.route('/ip')
def ip():
    return render_template('simple1.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)    

referer_monthly = pd.read_csv('/home/programming/python/referer_monthly.csv',engine='python',na_values='-',header=None,usecols=[0,1,2],names=['link','count'],converters={'count':int})
referer_daily = pd.read_csv('/home/programming/python/referer_daily.csv',engine='python',na_values='-',header=None,usecols=[0,1,2],names=['link','count'],converters={'count':int})
referer = pd.read_csv('/home/programming/python/referer.csv',engine='python',na_values='-',header=None,usecols=[0,1,2],names=['link','count'],converters={'count':int})
referer.append(referer_monthly)
referer.append(referer_daily)
df = referer.groupby('link').sum().sort_values(by='count',ascending=False).reset_index()
@app.route('/refer')
def refer():
    return render_template('simple2.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)    

request = pd.read_csv('/home/programming/python/request.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['link','count'],converters={'count':int})
request_daily = pd.read_csv('/home/programming/python/request_daily.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['link','count'],converters={'count':int})
request_monthly = pd.read_csv('/home/programming/python/request_monthly.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['link','count'],converters={'count':int})
request.append(request_monthly)
request.append(request_daily)
df = request.groupby('link').sum().sort_values(by='count',ascending=False).reset_index()
@app.route('/request')
def request():
    return render_template('simple3.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)    

rate = pd.read_csv('/home/programming/python/rate.csv',engine='python',na_values='-',header=None,usecols=[1,2,3],names=['ip','time','size'],converters={'time':parse_datetime,'size':int})
rate_daily = pd.read_csv('/home/programming/python/rate_daily.csv',engine='python',na_values='-',header=None,usecols=[1,2,3],names=['ip','time','size'],converters={'time':parse_datetime,'size':int})
rate_monthly = pd.read_csv('/home/programming/python/rate_monthly.csv',engine='python',na_values='-',header=None,usecols=[1,2,3],names=['ip','time','size'],converters={'time':parse_datetime,'size':int})
rate.append(rate_monthly)
rate.append(rate_daily)
df = rate.groupby('time').sum().sort_values(by='size',ascending=False).reset_index()
@app.route('/rate')
def rate():
    return render_template('simple4.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)   

time = pd.read_csv('/home/programming/python/time.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['time','count'],converters={'time':parse_datetime,'count':int})
time_daily = pd.read_csv('/home/programming/python/time_daily.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['time','count'],converters={'time':parse_datetime,'count':int})
time_monthly = pd.read_csv('/home/programming/python/time_monthly.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['time','count'],converters={'time':parse_datetime,'count':int})
time.append(time_daily)
time.append(time_monthly)
df = time.groupby('time').sum().sort_values(by='count',ascending=False).reset_index()
@app.route('/time')
def time():
    return render_template('simple5.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)    


if __name__ == '__main__':
   app.secret_key = 'super secret key'
   app.debug = True
   app.run()
