from pygame.gfxdraw import rectangle
from pygame.key import get_pressed
from pygame.constants import *
from all_colors import *
from random import *
import pygame
pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Рисовалка')
bg_color = (255, 255, 255)
brush_color = (0, 0, 0)
brush_width = 5

BORDER_COLOR = (0, 0, 0)
CUR_INDEX = 0

canvas = pygame.Surface(screen.get_size())
canvas.fill(bg_color)

size = 50
palette_rect = pygame.Rect(10, 10, size * 15, size)
palette = pygame.Surface(palette_rect.size)

drag = False

Rectangle_color = choice(colors)
top_left = (0, 0)
SIZE = (0, 0)
dragging = False

rectangles = []

colors = [Black, White, DarkSlateGrey, SlateGrey, Red, Green, Blue, Orange, Yellow, Navy, Grey, GreenYellow,
          Brown, RosyBrown, SandyBrown, SaddleBrown, Lime, LimeGreen, Tan, Peru, Cyan, LightCyan, DarkCyan,
          Salmon, DarkSalmon, LightSalmon, Linen, Silver, DimGrey,LightGrey, DarkGrey, Ivory, Beige, Azure,
          Snow, Aqua, Teal, Olive, SeaGreen, Sienna, Chocolate, Maroon, Wheat, Purple, Indigo, Violet, Plum,
          Magenta, Pink, Gold, Coral, Tomato, Khaki, LightSlateGrey, Gainsboro, MistyRose, LavenderBlush,
          SkyBlue, RoyalBlue, DarkRed, OldLace, FloralWhite, AntiqueWhite, Seashell, WhiteSmoke, GhostWhite,
          AliceBlue, MintCream, Honeydew, MidnightBlue, DarkBlue, MediumBlue, MediumSlateBlue, CornflowerBlue,
          DodgerBlue, DeepSkyBlue, LightSkyBlue, LightBlue, PowderBlue, LightSteelBlue, SteelBlue, CadetBlue]

def create_palett():
    palette.fill(bg_color)
    for i in range(15):
        color_rect = pygame.Rect(i * size, 0, size, size)
        pygame.draw.rect(palette, colors[i], color_rect)

    border_rect = pygame.Rect(CUR_INDEX * size, 0, size, size)
    pygame.draw.rect(palette, BORDER_COLOR, border_rect, width=3)
    screen.blit(palette, palette_rect.topleft)

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if palette_rect.collidepoint(event.pos):
                drag = True
                offset = (event.pos[0] - palette_rect.left,
                          event.pos[1] - palette_rect.top)
            else:
                drag = False

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            drag = False

    mouse_pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        if palette_rect.collidepoint(mouse_pos):
            selected_index = ((mouse_pos[0] - palette_rect.left) // size)
            CUR_INDEX = selected_index
            brush_color = colors[CUR_INDEX]
        else:
            pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)

    if drag:
        new_pos = (mouse_pos[0] - offset[0],
                   mouse_pos[1] - offset[1])
        palette_rect.topleft = new_pos

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        top_left = event.pos
        SIZE = 0, 0
        dragging = True
    elif event.type == pygame.MOUSEMOTION and dragging:
        right_bottom = event.pos
        SIZE = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
        right_bottom = event.pos
        SIZE = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
        dragging = False
        rect = pygame.Rect(top_left, SIZE)
        color = choice(colors)
        rectangles.append((rect, color))

    screen.blit(canvas, (0, 0))
    create_palett()

    pygame.draw.rect(screen, Rectangle_color, (top_left, SIZE), 1)
    for rectangle, color in rectangles:
        pygame.draw.rect(screen, color, rectangle, 1)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()