import pandas as pd
from flask import (Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response)
import datetime 

app = Flask(__name__)

def parse_datetime(data):
    dt = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
    return dt

ip = pd.read_csv('/home/maddy/programming/python/ip.csv',engine='python',na_values='-',header=None,usecols=[0, 1],names=['ip','count'],converters={'count':int})
df = ip.groupby('ip').sum().sort_values(by='count', ascending=False).reset_index()
@app.route('/ip')
def ip():
    return render_template('simple1.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)    

referer = pd.read_csv('/home/maddy/programming/python/referer.csv',engine='python',na_values='-',header=None,usecols=[0,1,2],names=['link','count'],converters={'count':int})
df = referer.groupby('link').sum().sort_values(by='count',ascending=False).reset_index()
@app.route('/refer')
def refer():
    return render_template('simple2.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)    

request = pd.read_csv('/home/maddy/programming/python/request.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['link','count'],converters={'count':int})
df = request.groupby('link').sum().sort_values(by='count',ascending=False).reset_index()
@app.route('/request')
def request():
    return render_template('simple3.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)    

rate = pd.read_csv('/home/maddy/programming/python/rate.csv',engine='python',na_values='-',header=None,usecols=[1,2,3],names=['ip','time','size'],converters={'time':parse_datetime,'size':int})
df = rate.groupby('time').sum().sort_values(by='size',ascending=False).reset_index()
@app.route('/rate')
def rate():
    return render_template('simple4.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)   

time = pd.read_csv('/home/maddy/programming/python/time.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['time','count'],converters={'time':parse_datetime,'count':int})
df = time.groupby('time').sum().sort_values(by='count',ascending=False).reset_index()
@app.route('/time')
def time():
    return render_template('simple5.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)    


if __name__ == '__main__':
   app.secret_key = 'super secret key'
   app.debug = True
   app.run()