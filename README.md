# Scheduled Log Analyser

The log analysis tool is a setup that can be used to check the following properties of a live server(live server with very high traffic) without rendering any significant loss or specialised data management. 
this is a system that provides HTTP APIs for obtaining the following stats on a *live* Apache / Nginx webserver logfile:

   a) (host, request-count) tuples for the top-10 frequent hosts

   b) (HTTP-status-code, count) tuples, sorted by count

   c) the hour with the highest request count, along with the count

   d) the hour with the highest total number of bytes served, along with the total

   e) the first & last path name components of top-10 most frequently accessed resources
   
Pre-req:
Ubuntu Server (preferably 16.04 LTS), please edit the following configurations around your predefined ones(if any).
 1) install the following: pandas, Flask,wsgi.
 ```
 sudo apt update
sudo apt install pandas numpy libapache2-mod-wsgi-py3 python-dev python3  
python3 install pip
```

2) First adjust the logrotate, (which in default condition) for the daily.
   go to ``` /etc/cron.daily``` copy the logrotate file and paste it into ``` /etc/cron.hourly```, then paste apache2 into ```/etc/logrotate.d```

3) make sure the file are placed in the home directory as they are path specific and must be editted in case of any change.

4) open the cron tab from the terminal using ``` crontab -e ``` and paste the data inside the crontab file,save it and restart crontab .

5) move into the Flask Folder add these folder into the server site and make sure to open the ```app.py``` to ensure that there is no link mishap.

6) Then restart the server.

7) Check for updates in the corresponding pages.

N.B the above process only updates to a maximum of a month and after that the data file it creates shall grow considerably.
but if the process needs to be extended into a months. place the pandas_monthly.py file accordingly in cron.monthly.
