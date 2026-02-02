#Songsuggestion des Tages: Lingus von Snarky Puppy 
import pygame
pygame.init()
screen = pygame.display.set_mode((1366, 768)) 
pygame.display.set_caption("Apenture Science - Huge Success")
clock = pygame.time.Clock()

class String_data:
    def __init__(self, scale_factor, text, coords, style):
        self.scale_factor = scale_factor
        self.char_list = self.init_char_images()
        self.text = text
        self.coords = coords
        self.style = style

    def get_char_index(self, char):
        if char == " ":
            return 0
        index = ord(char) - 32
        if index > 0 and index < 95:
            return index
        else:
            print("error in get_char_index. Index out of bounds")

    def get_char_pos(self, index):#Position of letter on spritesheet
        x_pos = 7 * (index % 18) * self.scale_factor # Die Buchstaben Map hat 18 Zeichen pro
        y_pos = 9 * (index // 18) * self.scale_factor # Zeile und jeder Buchstabe ist 7 * 9 Pixel breit
        return x_pos, y_pos

    def init_char_images(self):
        char_width = 7 * self.scale_factor
        char_hight = 9 * self.scale_factor
        char_list = []
        sheet = pygame.image.load("letters.png").convert_alpha()
        sheet = pygame.transform.scale(sheet, (128 * self.scale_factor, 64 * self.scale_factor))
        for i in range(0, 95):
            x, y = self.get_char_pos(i)
            rect = pygame.Rect(x, y, char_width, char_hight)
            char = sheet.subsurface(rect)
            char_list.append(char)
        return char_list

    def blit_char_from_string(self, char, x, y):
        index = self.get_char_index(char) 
        screen.blit(self.char_list[index], (x, y))

    def blit_string(self):
        if self.style == "normal":
            space_between_letters = 2 * self.scale_factor
            x, y = self.coords[0], self.coords[1]
            for i in range(len(self.text)):
                self.blit_char_from_string(self.text[i], x, y)
                x += space_between_letters


#Hier alle Objekte:
#(self, scale_factor, text, coords, style):
object_list = [
    String_data(15, ": )", [150, 150], "normal")
]


def blit_all_strings():
    for string_data in object_list:
        string_data.blit_string()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((210, 108, 0))
    blit_all_strings()
    pygame.display.flip() 
    clock.tick(60) 

pygame.quit() 

