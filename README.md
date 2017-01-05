### NOCtools
Tools used by NOC members created by UW student assistant Brandon Kinard

**Contains**:

Updated script to reserve IP addresses which accounts for changes implemented to snstatus during Autumn Quarter 2016 in  
* find_useable.py

Supplementary script to determine time since an IP has been used
* time_since.py


Script to split records (typically used to split requests contains IP addresses and hostnames in form -> xxx.xxx.xxx.xxx  foo.bar.uw.edu
* record_split.py


**_[Scripts using Selenium]_**

To reserve IP addresses
* reserve_address.py


Commonly used selenium functions for web automation in
* selenium_functions.py

To use the selenium scripts you need to login to your MyUW account. I created a simple script to accomplish this. You will need to replace the text fields in username and password with your information. Script can be found in
* login_uw.py
