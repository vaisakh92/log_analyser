# Scheduled Log Analyser

The log analysis tool is a setup that can be used to check the following properties of a live server(live server with very high traffic) without rendering any significant loss or specialised data management. 
this is a system that provides HTTP APIs for obtaining the following stats on a *live* Apache / Nginx webserver logfile:

   a) (host, request-count) tuples for the top-10 frequent hosts

   b) (HTTP-status-code, count) tuples, sorted by count

   c) the hour with the highest request count, along with the count

   d) the hour with the highest total number of bytes served, along with the total

   e) the first & last path name components of top-10 most frequently accessed resources
   
Pre-req:
Ubuntu Server (preferably 14.04 LTS), please edit the following configurations around your predefined ones(if any).
 1) install the following: pandas, Flask,wsgi.
 ```
 sudo apt update
sudo apt install pandas numpy libapache2-mod-wsgi-py3 python-dev python3  
python3 install pip
```
2) First adjust the logrotate, (which in default condition) for the daily.

