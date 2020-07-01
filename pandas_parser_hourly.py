from datetime import datetime
import pandas as pd


def parse_str(data):
    return data[1:-1]

def parse_datetime(data):
    dt = datetime.strptime(data[1:-13], '%d/%b/%Y:%H')
    return dt

data = pd.read_csv('access.log',sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])', engine='python', na_values='-', header=None, usecols=[0, 3, 4, 5, 6, 7, 8], names=['ip', 'time', 'request', 'status', 'size', 'referer', 'user_agent'], converters={'time': parse_datetime,'request': parse_str,'status': int,'size': int,'referer': parse_str,'user_agent': parse_str})
dk = data.groupby(['ip','time']).agg({'size': "sum"}).reset_index()
s_dk = dk.sort_values(by =['size'],ascending=False)
dt = [s_dk.iloc[0]['ip'],s_dk.iloc[0]['time'],s_dk.iloc[0]['size']]
referer = {
 'count':data['referer'].value_counts()[:10]
}
ip = {
'count':data['ip'].value_counts()[:10]
}
request = {
    'count':data['request'].value_counts()[:10]
}
time = {
   'count':data['time'].value_counts()[:10] 
}
rate = {
    'count':dt
}
df = pd.DataFrame (referer)
df.to_csv (r'/home/programming/python/referer.csv', mode='a', header=False)
df = pd.DataFrame (ip)
df.to_csv (r'/home/programming/python/ip.csv', mode='a', header=False)
df = pd.DataFrame (request)
df.to_csv (r'/home/programming/python/request.csv', mode='a', header=False)
df = pd.DataFrame (rate)
df = df.transpose()
df.to_csv (r'/home/programming/python/rate.csv', mode='a', header=False)
df = pd.DataFrame (time)
df.to_csv (r'/home/programming/python/time.csv', mode='a', header=False)
