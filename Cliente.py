# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 10:24:34 2023

@author: Otavi
"""



import zmq
import random


context = zmq.Context()


print("Bolsa de valores...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket2 = context.socket(zmq.REQ)
socket2.connect("tcp://localhost:7777")




for request in range(10):
    print(f"sevidor 1  Número da chamada{request} …")
    socket.send(b"VitaSonho")

    message = socket.recv()
    print(f"Resposta do servidor1 Número da chamada {request} :{message}")
    
    print(f"sevidor 2 Número da chamada {request} …")
    socket2.send(b"Vit")

    
    message = socket2.recv()
    print(f"Resposta sevidor 2 Número da chamada {request}:{message}")