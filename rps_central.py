import paho.mqtt.client as mqtt
import random
from getpass import getpass
import time

player1 = ""
player2 = ""
result = ""
player1_score = 0
player2_score = 0

def on_connect(central, userdata, flags, rc):
    print(print("Connection returned result: " + str(rc)))
    central.subscribe("PLAYER1", qos=1)
    central.subscribe("PLAYER2", qos=1)
    print("Sending the prompt...")
    central.publish("PROMPT", "\nWelcome to Rock-Paper-Scissors Game!\n Press:\n r for Rock\n p for Paper\n s for scissors\n")

def on_disconnect(central, userdata, rc):
    if rc!=0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
def on_message(central, userdata, message):
    global player1
    global player2
    global result

    choice = message.payload.decode("utf-8")
    if choice == "r":
        choice = "Rock"
    elif choice == "s":
        choice = "Scissors"
    elif choice == "p":
        choice = "Paper"
    else:
        print("invalid input")
    
    if message.topic == "PLAYER1":
        player1 = choice
        print("player1: " + player1)
    else: 
        player2 = choice
        print("player2: " + player2)

    if player1 != "" and player2 != "":
        result = rps_game(player1, player2)
        print(result)
        central.publish("RESULT", result + " p1: " + player1 + ", p2: " + player2 + " | Score: p1: " + str(player1_score) + " vs p2: " + str(player2_score))
        player1 = ""
        player2 = ""

def rps_prompt():
    print("Sending the prompt...")
    central.publish("PROMPT", "Choose Rock Paper or Scissors!")

def rps_game(player_1, player_2):
    
    global result
    global player1_score
    global player2_score
    if player1 == player2:
        result = "Draws!"
    elif player1 == "Rock" and player2 == "Paper":
        player2_score += 1
        result = "Player2 wins!"
    elif player1 == "Rock" and player2 == "Scissors":
        player1_score += 1
        result = "Player1 wins!"
    elif player1 == "Paper" and player2 == "Rock":
        player1_score += 1
        result = "Player1 wins!"
    elif player1 == "Paper" and player2 == "Scissors":
        player2_score += 1
        result = "Player2 wins!"
    elif player1 == "Scissors" and player2 == "Rock":
        player2_score += 1
        result = "Player2 wins!"
    else:
        player1_score += 1
        result = "Player1 wins!"

    return result

central = mqtt.Client()

central.on_connect = on_connect
central.on_disconnect = on_disconnect
central.on_message = on_message

central.connect_async("mqtt.eclipseprojects.io")

central.loop_start()

while True:
    pass

central.loop_stop()
central.disconnect()


    