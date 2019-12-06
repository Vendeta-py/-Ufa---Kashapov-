import pygame

pygame.init()
N, K = int(input()), int(input())
size = width, height = N * K * 2, N * K * 2
screen = pygame.display.set_mode(size)
red, green, blue = True, False, False
circle_radius = N
circle_width = 0
for i in range(K):
    if red:
        pygame.draw.circle(screen, pygame.Color('red'), (width // 2, height // 2), circle_radius, circle_width)
        red, green = False, True
    elif green:
        pygame.draw.circle(screen, pygame.Color('green'), (width // 2, height // 2), circle_radius, circle_width)
        green, blue = False, True
    elif blue:
        pygame.draw.circle(screen, pygame.Color('blue'), (width // 2, height // 2), circle_radius, circle_width)
        blue, red = False, True
    circle_width += N
    circle_radius += N
    pygame.display.flip()


while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()