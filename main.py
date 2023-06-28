#cosas por hacer:
#1. ver el tema del puntaje ✓
#2. ver la coalision para el game over (falta la pantalla del game over)
#3. crear un menu de inicio
#4. mejorar las colisión ✓

import pygame
import random

#inicializacion
pygame.init()

#configuraciones
WIDTH, HEIGHT = 1080, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paredon")

#variables
ball_radius = 20
player_width = 200
player_height = 20
PLAYER_SPEED = 9
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
#variables de texto
score = 0
game_font = pygame.font.Font("advanced_pixel-7.ttf", 42)
#sonido
colision_sound = pygame.mixer.Sound("collision.wav")
score_sound = pygame.mixer.Sound("score.wav")

#Pygame Rectangles
player1_pos = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10, player_width, player_height)
ball_pos = pygame.Rect(WIDTH // 2 - ball_radius // 2, HEIGHT // 2 - ball_radius // 2, ball_radius, ball_radius)

player_speed = 0


#loop del juego
running = True
clock = pygame.time.Clock()

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball_pos.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))

def ball():
    global ball_speed_x, ball_speed_y, score
    ball_pos.x += ball_speed_x
    ball_pos.y += ball_speed_y
    #colisión del balon con la pared
    if ball_pos.left <= 0 or ball_pos.right >= WIDTH:
        ball_speed_x *= -1
        pygame.mixer.Sound.play(colision_sound)
    if ball_pos.top <= 0:
        ball_speed_y *= -1
        score += 1
        pygame.mixer.Sound.play(score_sound)
    if ball_pos.bottom >= HEIGHT:
        ball_restart()
        score = 0
    #colisión del balon con jugador
    if ball_pos.colliderect(player1_pos) and ball_speed_y > 0:
        if abs(ball_pos.top - ball_pos.bottom) < 50:
            ball_speed_y *= -1 
            pygame.mixer.Sound.play(colision_sound)
        elif abs(ball_pos.right - ball_pos.left) < 50 and ball_speed_x > 0:
            ball_speed_x *= -1 
            pygame.mixer.Sound.play(colision_sound)
        elif abs(ball_pos.left - ball_pos.right) < 50 and ball_speed_x < 0:
            ball_speed_x *= -1
            pygame.mixer.Sound.play(colision_sound)

def player():
    #actualizar posicion del jugador
    player1_pos.x += player_speed
    if player1_pos.left < 0:
        player1_pos.left = 0
    elif player1_pos.right > WIDTH:
        player1_pos.right = WIDTH

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed = -PLAYER_SPEED            #!!!
                print("izq")
            elif event.key == pygame.K_RIGHT:
                player_speed = PLAYER_SPEED
                print("der")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key  == pygame.K_RIGHT:
                player_speed = 0

    ball()
    player()
    #pantalla
    screen.fill('black')
    #formas
    pygame.draw.rect(screen, 'white', player1_pos)
    pygame.draw.ellipse(screen, 'white', ball_pos)
    player_text = game_font.render(f"Puntaje: {score}", False, "white")
    screen.blit(player_text, (940, 10))
    #actualizar display y frames
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    
