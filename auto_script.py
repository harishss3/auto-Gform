'''
*******************
*AUTHOR: harishss3*
*******************
'''

import requests
    url = '' # Enter the URL of the google doc. Make sure to change 'viewform' to 'formResponse'
    gform_data = {'entry.1':value1,
                'entry.2':value2,
                'entry.3':value3}      # Entry name can be found by inspecting the required element or from a pre-filled link 
    r = requests.post(url, data=gform_data)
'''
This can be used to fill a form multiple times by using a for loop. 
'''
