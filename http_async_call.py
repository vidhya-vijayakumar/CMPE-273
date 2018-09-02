import ast
from requests_futures.sessions import FuturesSession

async_call = FuturesSession()

# First http call request to Webhook
web_call1 = async_call.get('https://webhook.site/6a0cc4e9-3ffd-40e7-b972-ec191f421cf0')

# Second http call request to webhook
web_call2 = async_call.get('https://webhook.site/6a0cc4e9-3ffd-40e7-b972-ec191f421cf0')

#Thrid http call request to webhook
web_call3 = async_call.get('https://webhook.site/6a0cc4e9-3ffd-40e7-b972-ec191f421cf0')

#Caching the result for three web callsg
result_web_call1 = web_call1.result()
result_web_call2 = web_call2.result()
result_web_call3 = web_call3.result()

#Collecting the results to a dictonary
temp_result_web_call1 = format(result_web_call1.headers)
temp_result_web_call2 = format(result_web_call2.headers)
temp_result_web_call3 = format(result_web_call3.headers)

#Converting to dictionary
dict_temp_result_web_call1= ast.literal_eval(temp_result_web_call1)
dict_temp_result_web_call2= ast.literal_eval(temp_result_web_call2)
dict_temp_result_web_call3= ast.literal_eval(temp_result_web_call3)

#Date output for http call
for keys,values in dict_temp_result_web_call1.items():
    if keys == 'Date':
        print(keys,values) 

for keys,values in dict_temp_result_web_call2.items():
    if keys == 'Date':
        print(keys,values) 

for keys,values in dict_temp_result_web_call3.items():
    if keys == 'Date':
        print(keys,values) 
