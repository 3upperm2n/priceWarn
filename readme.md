### Software
* googlefinance (https://github.com/hongtaocai/googlefinance)
```bash
pip install googlefinance
```

* send emails using python

* run the script using crontab
I am using anaconda for python env. Thus, I need to load the env in crontab file. 
```bash
vim /etc/crontab 
```


```bash
SHELL=/bin/sh                                                                   
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/home/leiming/anaconda2/bin
PYTHONPATH=/home/leiming/anaconda2/lib/python2.7/site-packages

@reboot root /home/leiming/Dropbox/20_finance/priceWarn/check_price.py > /tmp/check_price_reboot.log 2>&1
*/1 9-16 * * 1-5 root /home/leiming/Dropbox/20_finance/priceWarn/check_price.py > /tmp/check_price.log 2>&1
#
```
