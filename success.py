#Songsuggestion des Tages: Lingus von Snarky Puppy 
import pygame
pygame.init()
screen = pygame.display.set_mode((1366, 768)) 
pygame.display.set_caption("Apenture Science - Huge Success")
clock = pygame.time.Clock()

class String_data:
    def __init__(self, scale_factor, content, coords, text_or_number, special_property): #Wo die variable wohl gut für ist :?
        self.scale_factor = scale_factor
        self.char_list = self.init_char_images()
        self.content = content #Kann eine Zahl oder ein Text sein
        self.coords = coords
        self.text_or_number = text_or_number
        self.special_property = special_property


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
        if self.text_or_number == "Text":
            space_between_letters = 6 * self.scale_factor
            x, y = self.coords[0], self.coords[1]
            for i in range(len(self.content)):
                self.blit_char_from_string(self.content[i], x, y)
                x += space_between_letters
        if self.text_or_number == "Number":
            space_between_letters = 6 * self.scale_factor
            x, y = self.coords[0], self.coords[1]
            for i in range(len(self.content)):
                self.blit_char_from_string(self.content[i], x, y)
                x += space_between_letters
    
    def do_special_property(self):
        if self.special_property == "None":
            return
        if self.special_property == "Count_up":
            x = int(self.content)
            if x < 5:
                x += 1
            elif x < 32: 
                x += 7
            elif x < 65:
                x += 1
            elif x < 90: 
                x += 3
            else: x = 100
            self.content = str(x) 

#Hier alle Objekte:
#(self, scale_factor, text, coords, style):
object_list = [
    String_data(24, ":)", [50, 50], "Text", "None"),
    String_data(3, "Your PC ran into a success and can continue. We are just", [100, 250], "Text", "None"),
    String_data(3, "collecting some success info and then we will continue for you.", [100, 300], "Text", "None"),
    String_data(3, "(   % Complete)", [100, 350], "Text", "None"),
]

Percentage = String_data(3, "0", [117, 350], "Number", "Count_up")

def blit_all_strings():
    for string_data in object_list:
        string_data.blit_string()
        string_data.do_special_property()

    Percentage.blit_string()
    Percentage.do_special_property()

def blit_loading_bar(percentage):
    width = percentage * 10
    height = 30
    outline = pygame.Rect((1366 - 1010) / 2, 495, 1010, height + 10) #Ich kann nicht mehr rechnen heute
    rect = pygame.Rect((1366 - 1000) / 2, 500, width, height)
    pygame.draw.rect(screen, (0, 0, 0), outline)
    pygame.draw.rect(screen, (255, 255, 255), rect)

running = 15
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((210, 108, 0))
    blit_all_strings()
    blit_loading_bar(int(Percentage.content))
    if Percentage.content == "100":
        running -= 1
    pygame.display.flip() 
    clock.tick(4) 

pygame.quit() 

