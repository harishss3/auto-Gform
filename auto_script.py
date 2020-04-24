'''
*******************
*AUTHOR: harishss3*
*******************
'''

import requests
for i in range(100):
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSdt4al2U8TTWbtjwYNGV3cSOdhaWdPu58QyRtjm0e7Z6M0FVw/formResponse'
    form_data = {'entry.1156409':'Harish Adsule',
                'entry.210055283':190070,
                'entry.192452008':'Yes',
                'entry.446099277':'https://github.com/harishss3/auto-Gform.git'}
    r = requests.post(url, data=form_data)