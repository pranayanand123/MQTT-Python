# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:36:38 2018

@author: pranay
"""

import paho.mqtt.client as mqttClient
import time
import pyttsx3
import json, requests 
bank = False
def say(s):
        engine = pyttsx3.init()
        voices= engine.getProperty('voices')
        engine.setProperty('rate', 150)
        #voices= engine.getProperty('voices')
        #for voice in voices:                                                                                    
        engine.setProperty('voice', voices[1])
        #print voice.id                                                                                          
        engine.say(s)
        a = engine.runAndWait() #blocks
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
def on_message(client, userdata, message):
    print("Message received: "  + message.payload.decode('utf-8'))
    global bank
    if message.payload.decode('utf-8')=='banking mode on':
        say('Welcome to State Bank Of India. How can i help you?')
        bank = True
    elif message.payload.decode('utf-8')=='menu':
        say('Banking mode off')
        bank = False
    else:
        print(bank)
        if bank==True:
            url = requests.get('http://codeglobal.in/chatbot/chatbot/conversation_start.php?say='+message.payload.decode('utf-8')) 
            root= json.loads(url.text)
            bot = root['botsay']
            print(bot)
            say(bot)
        else:
            say('sorry, I dont understand')
Connected = False   #global variable for the state . the connection
  
broker_address= "broker.mqttdashboard.com"  #Broker address
port = 1883                        #Broker port
user = "yourUser"                    #Connection username
password = "yourPassword"            #Connection password
 
client = mqttClient.Client("bjhfsdfhafiwbfwfnfwadmwndfnasdj")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message         #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("inayaA13vb4yj7dhjqad7")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()