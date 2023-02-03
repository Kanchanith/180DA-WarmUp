import paho.mqtt.client as mqtt
import pygame
import button

from pygame.locals import(
    K_r,
    K_p,
    K_s,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

message_topic = ""
promptX = 50
promptY = 10
resultX = 5
resultY = 10
prompt_intro = ""
result = ""
font = pygame.font.SysFont('arial', 15)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("P1 Rock Paper Scissors")

rock_img = pygame.image.load('rock_btn.png').convert_alpha()
paper_img = pygame.image.load('paper_btn.png').convert_alpha()
scissors_img = pygame.image.load('scissors_btn.png').convert_alpha()

rock_button = button.Button(70, 200, rock_img, 100, 155)
paper_button = button.Button(200, 200, paper_img, 100, 155)
scissors_button = button.Button(330, 200, scissors_img, 100, 155)

def on_connect(player1, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    player1.subscribe("PROMPT", qos=1)
    player1.subscribe("RESULT", qos=1)
    player1.subscribe("SCORE", qos=1)

def on_disconnect(player1, userdata, rc):
    if rc!=0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")

def on_message(player1, userdata, message):
    global message_topic
    message_topic = message.topic
    # if message_topic == "PROMPT":
    #     if rock_button.draw(screen):
    #         print("Rock")
    #         message = "r"
    #         player1.publish("PLAYER1", message, qos=1)
    if message_topic == "RESULT":
        global result
        result = str(message.payload.decode("utf-8"))
        # print("Here's the result: " + message.payload.decode("utf-8"))

def prompt(x, y):
    global prompt_intro
    prompt_intro = font.render("Choose Rock Paper or Scissors!", True, (26, 56, 28))
    screen.blit(prompt_intro, (x,y))

def show_result(message, x, y):
    result_img = font.render(str(message), True, (26, 56, 28))
    screen.blit(result_img, (x,y))

player1 = mqtt.Client()

player1.on_connect = on_connect
player1.on_disconnect = on_disconnect
player1.on_message = on_message

player1.connect_async("mqtt.eclipseprojects.io")

player1.loop_start()

running = True
while running:
    screen.fill((188,228,230))

    if rock_button.draw(screen):
        print("rock")
        player1.publish("PLAYER1", "r", qos=1)
    elif paper_button.draw(screen):
        print("paper")
        player1.publish("PLAYER1", "p", qos=1)
    elif scissors_button.draw(screen):
        print("scissors")
        player1.publish("PLAYER1", "s", qos=1)

    if message_topic == "PROMPT":
        prompt(promptX, promptY)
    elif message_topic == "RESULT":
        show_result(result, resultX, resultY)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
    

    pygame.display.flip()
    pygame.display.update()

pygame.quit()

player1.loop_stop()
player1.disconnect()