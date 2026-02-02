import pygame
pygame.init()
screen = pygame.display.set_mode((1366, 768)) 
pygame.display.set_caption("Apenture Science - Huge Success")
clock = pygame.time.Clock()


def get_char_index(char):
    if char == " ":
        return 0
    index = ord(char) - 32
    if index > 0 and index < 95:
        return index
    else:
        print("error in get_char_index. Index out of bounds")

def get_char_pos(index):#Position of letter on spritesheet
    x_pos = 7 * (index % 18) * letter_scale # Die Buchstaben Map hat 18 Zeichen pro
    y_pos = 9 * (index // 18) * letter_scale # Zeile und jeder Buchstabe ist 7 * 9 Pixel breit
    return x_pos, y_pos

def init_char_images(letter_scale):
    char_width = 7 * letter_scale
    char_hight = 9 * letter_scale
    char_list = []
    sheet = pygame.image.load("letters.png").convert_alpha()
    sheet = pygame.transform.scale(sheet, (128 * letter_scale, 64 * letter_scale))
    for i in range(0, 95):
        x, y = get_char_pos(i)
        rect = pygame.Rect(x, y, char_width, char_hight)
        char = sheet.subsurface(rect)
        char_list.append(char)
    return char_list

def blit_char_from_string(char, x_pos, y_pos):
    index = get_char_index(char) 
    screen.blit(char_list[index], (x_pos, y_pos))

def blit_string(char_list, string, x, y, style):
    if style == "normal":
        space_between_letters = 8 * letter_scale
        for i in range(len(string)):
            blit_char_from_string(string[i], x, y)
            x += space_between_letters


char_list_15 = init_char_images(15) #lettersize
char_list_3 = init_char_images(3)
mystring = ":)"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((210, 108, 0))
    blit_string(char_list_3, mystring, 100, 100, "normal")
    pygame.display.flip() 
    clock.tick(60) 

pygame.quit() 

