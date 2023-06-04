# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 10:24:27 2023

@author: Otavi
"""


import time
import zmq
import random


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:
             
           
             peso = random.randrange(30, 100, 5)
    #  Wait for next request from client
             message = socket.recv()
             print(f"Pedido recebido: {message}")

             #  Do some 'work'
             time.sleep(1)
             print (peso)
             if  30<peso<50:
             #  Send reply back to client
                 socket.send(b"compra ação intel")   
             elif peso>50:
                 socket.send(b"Vender ação intel")
             else:
                 socket.send(b"Manter ação intel")
                 


           
    