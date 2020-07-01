from datetime import datetime
import pandas as pd


def parse_datetime(data):
    dt = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
    return dt
ip = pd.read_csv('/home/maddy/programming/python/ip.csv',engine='python',na_values='-',header=None,usecols=[0, 1],names=['ip','count'],converters={'count':int})
df = ip.groupby('ip').sum().sort_values(by='count', ascending=False).reset_index()
df.to_csv(r'/home/maddy/programming/ip_daily.csv',mode='a',header=False)

referer = pd.read_csv('/home/maddy/programming/python/referer.csv',engine='python',na_values='-',header=None,usecols=[0,1,2],names=['link','count'],converters={'count':int})
df = referer.groupby('link').sum().sort_values(by='count',ascending=False).reset_index()
df.to_csv(r'/home/maddy/programming/referer_daily.csv',mode='a',header=False)

request = pd.read_csv('/home/maddy/programming/python/request.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['link','count'],converters={'count':int})
df = request.groupby('link').sum().sort_values(by='count',ascending=False).reset_index()
df.to_csv(r'/home/maddy/programming/request_daily.csv',mode='a',header=False)

rate = pd.read_csv('/home/maddy/programming/python/rate.csv',engine='python',na_values='-',header=None,usecols=[1,2,3],names=['ip','time','size'],converters={'time':parse_datetime,'size':int})
df = rate.groupby('time').sum().sort_values(by='size',ascending=False).reset_index()
df.to_csv(r'/home/maddy/programming/rate_daily.csv',mode='a',header=False)

time = pd.read_csv('/home/maddy/programming/python/time.csv',engine='python',na_values='-',header=None,usecols=[0,1],names=['time','count'],converters={'time':parse_datetime,'count':int})
df = time.groupby('time').sum().sort_values(by='count',ascending=False).reset_index()
df.to_csv(r'/home/maddy/programming/time_daily.csv',mode='a',header=False)
