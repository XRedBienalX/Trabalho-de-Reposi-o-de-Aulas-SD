# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:02:56 2023

@author: Otavi
"""

import time
import zmq
import random


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:7777")


while True:
             
           
             peso = random.randrange(15, 100, 5)
    
             message = socket.recv()
             print(f"Pedido recebido: {message}")

             
             time.sleep(1)
             print (peso)
             if  15<peso<40:
                 socket.send(b"compra ação amd")   
             elif peso>60:
                 socket.send(b"Vender ação amd")
             else:
                 socket.send(b"Manter ação amd")