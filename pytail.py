import time
import subprocess
import select


def apache_output(line):
    
    split_line = line.split()
    ip_count[split_line[0]] = ip_count.get(split_line[0],0)+1
    global bytes_size 
    bytes_size += int(split_line[9])
    request_count[split_line[8]] = request_count.get(split_line[8],0)+1
    
f = subprocess.Popen(['tail','-f','/var/log/apache2/access.log'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)
ip_count = {}
request_count = {}
bytes_size = 0
while True:
    if p.poll(1):
        _str =  f.stdout.readline()
        apache_output(_str.decode("utf-8"))
    time.sleep(0.5)
    print(ip_count)
    print(request_count)
    print(bytes_size)