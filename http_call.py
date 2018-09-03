import requests
import random

def sync_webcall(pid):
        r = requests.get('https://webhook.site/6a0cc4e9-3ffd-40e7-b972-ec191f421cf0')
        print (r.headers['Date'])

def main():
    for i in range(1, 4):
        sync_webcall(i)

main()
