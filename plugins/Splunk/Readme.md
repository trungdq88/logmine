To create Logmine plugin in Splunk, follow these steps ...
1.  Create a custom folder in Splunk installation - <Splunk Install Directory>/etc/apps/Logmine
2.  Under bin directory place Logmine.py
3.  Under default directory place command.conf
4.  Restart Splunk and run -- index=* | head 1000 | Logmine | table *
