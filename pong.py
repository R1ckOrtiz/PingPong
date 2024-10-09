import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("HENRIQUE PING PONG")

# Definindo as cores
white = (255, 255, 255)
black = (0, 0, 0)

# Definindo o FPS (Frames per Second)
clock = pygame.time.Clock()
fps = 60

# Posições e tamanhos das barras e da bola
bar_width = 10
bar_height = 100
ball_size = 20

# Posições iniciais das barras
player1_x, player1_y = 50, screen_height // 2 - bar_height // 2
player2_x, player2_y = screen_width - 50 - bar_width, screen_height // 2 - bar_height // 2

# Velocidade das barras
bar_speed = 7

# Posições iniciais da bola
ball_x, ball_y = screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2
ball_speed_x, ball_speed_y = 5, 5

# Pontuações iniciais
score1 = 0
score2 = 0

# Função para desenhar os elementos na tela
def draw_objects():
    # Preenchendo a tela com cor preta
    screen.fill(black)

    # Desenhando as barras
    pygame.draw.rect(screen, white, (player1_x, player1_y, bar_width, bar_height))
    pygame.draw.rect(screen, white, (player2_x, player2_y, bar_width, bar_height))

    # Desenhando a bola
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Desenhando as linhas de divisão
    pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))

    # Desenhando as pontuações
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{score1}   {score2}", True, white)
    screen.blit(score_text, (screen_width // 2 - 40, 20))

# Loop principal do jogo
while True:
    # Verificando eventos (fechar janela, teclas)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas pressionadas para mover as barras
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= bar_speed
    if keys[pygame.K_s] and player1_y < screen_height - bar_height:
        player1_y += bar_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= bar_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - bar_height:
        player2_y += bar_speed

    # Movimento da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisão com as bordas superior e inferior
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    # Colisão com as barras
    if (ball_x <= player1_x + bar_width and player1_y <= ball_y <= player1_y + bar_height) or \
       (ball_x >= player2_x - ball_size and player2_y <= ball_y <= player2_y + bar_height):
        ball_speed_x *= -1

    # Ponto para o jogador 1
    if ball_x >= screen_width:
        score1 += 1
        ball_x, ball_y = screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2
        ball_speed_x *= -1

    # Ponto para o jogador 2
    if ball_x <= 0:
        score2 += 1
        ball_x, ball_y = screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2
        ball_speed_x *= -1

    # Desenhando os objetos na tela
    draw_objects()

    # Atualizando a tela
    pygame.display.flip()

    # Controlando o FPS
    clock.tick(fps)


    

    