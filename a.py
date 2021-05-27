import requests
import json
import csv
import time
import calendar
import pyautogui
import random
from playsound import playsound
# from fbchat import Client
# from fbchat.models import *
# email = 'nvlong.18it2@vku.udn.vn'
# password='112223344'
# client = Client(email, password)
money = 500
chuoi= [0,5,10,25,40,20]
delay=0.2
ran = random.randint(0, 1)
level = 1
sleepTime = 20

def Num(num):
    for x in range(int(num/50)):
        # dat 50k
        pyautogui.click(170, 510)
        time.sleep(delay)
    for x in range(int(num%100%50/10)):
        # dat 10k
        pyautogui.click(130, 510)
        time.sleep(delay)
    for x in range(int(num%10)):
        # dat 1k
        pyautogui.click(90, 510)
        time.sleep(delay)

def Click(state, number):
    if state==0:
        print("Dat Tai")
        pyautogui.click(120, 450)
        time.sleep(delay)
        Num(number)
    if state==1:
        print("Dat Xiu")
        pyautogui.click(330, 450) 
        time.sleep(delay)
        Num(number)
    pyautogui.click(230, 550)

while True:
    try:
        
        response = requests.get("https://api-agent.gowsazhjo.tv/glms/v1/notify/taixiu")
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        data = json.loads(text)
        employee_data = data['data']
        print(employee_data)
        # for emp in employee_data:
        #     if(emp['cmd']==1003):
        #         if(emp['d1']+emp['d2']+emp['d3']<=10):
        #             kq = 1
        #             if (ran==kq):
        #                 money+=chuoi[level]
        #                 cuoc = chuoi[1]
        #                 level = 1
        #                 message = 'an tien dat:' + str(cuoc) + 'k'
        #                 print(message)
        #                 # client.sendMessage(message, thread_id=client.uid, thread_type=ThreadType.USER)
        #                 playsound('ring.mp3')
        #             else:
        #                 money-=chuoi[level]
        #                 level +=1
        #                 if (level < len(chuoi)):
        #                     cuoc = chuoi[level]

        #                 else:
        #                     level = 1
        #                     cuoc = chuoi[level]
        #                     playsound('toetoe.mp3')
        #                 message = 'thua tien dat:' + str(cuoc) + 'k'
        #                 print(message)
        #                 # client.sendMessage(message, thread_id=client.uid, thread_type=ThreadType.USER)
        #                 playsound('fail.mp3')
        #             print("money:",money)
        #             time.sleep(sleepTime)
                    
        #         if(emp['d1']+emp['d2']+emp['d3']>10):
        #             kq = 0
        #             if (ran==kq):
        #                 money+=chuoi[level]
        #                 cuoc = chuoi[1]
        #                 level = 1
        #                 message = 'an tien dat:' + str(cuoc) + 'k'
        #                 print(message)
        #                 # client.sendMessage(message, thread_id=client.uid, thread_type=ThreadType.USER)
        #                 playsound('ring.mp3')
        #             else:
        #                 money-=chuoi[level]
        #                 level +=1
        #                 if (level < len(chuoi)):
        #                     cuoc = chuoi[level]

        #                 else:
        #                     level = 1
        #                     cuoc = chuoi[level]
        #                     playsound('toetoe.mp3')
        #                 message = 'thua tien dat:' + str(cuoc) + 'k'
        #                 print(message)
        #                 # client.sendMessage(message, thread_id=client.uid, thread_type=ThreadType.USER)
        #                 playsound('fail.mp3')
        #             print("money:",money)
        #             time.sleep(sleepTime)
        #         ran = random.randint(0, 1)
        #         Click(ran, cuoc)
                

    except:
        print("Error")
        time.sleep(3)
    

                
            
  