import pygame
import random
import time
from random import randint
from time import sleep

import threading

pygame.init()

# Створюємо вікно програми
back = (255, 255, 255)  # колір фону меню
back1 = (255, 255, 255)  # колір фону (background)
mw = pygame.display.set_mode((700, 400))  # вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()
pygame.display.set_caption("Fast Clicker")

# клас прямокутник
class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямокутник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # обводка існуючого прямокутника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):  # перевірка на дотик до картки
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def set_text1(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def set_text2(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    def draw_text(self, shift_x=0, shift_y=0):
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    def draw_text1(self, shift_x=0, shift_y=20):
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def draw_text2(self, shift_x=0, shift_y=30):
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    def draw_text3(self, shift_x=0, shift_y=40):
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    def draw_text4(self, shift_x=0, shift_y=40):
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Picture(Area):
    def __init__(self, filename, x=0, y=0,width=10, height=10, color=None):
        Area.__init__(self, x, y, width, height, color)
        self.image = pygame.image.load(filename)

    def draw_picture(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

#Створення меню та об'єктів для нього

menu_start = Picture("images/knSTART.png", 150, 50, 250, 66 )
menu_settings = Picture("images/KnSettings.png", 200, 170, 250, 100)
menu_exit = Picture("images/knQuit.png",150, 270, 250, 100)

#Створення тексту для меню налаштувань
sett_info = Label(25,50,100,50)
sett_info1 = Label(25,50,100,50)
sett_info2 = Label(25,60,100,50)
sett_info3 = Label(25,70,100,50)
sett_info4 = Label(25,320,100,50)
sett_info.set_text("Ціль гри набрати 5 очків , набрати ці очки можна натиснувши на жовту картку з написом 'CLICK' (+1 очко) ")
sett_info1.set_text1("Якщо ви натисните на картку без напису 'CLICK' у вас відніметься 1 очко (Якщо ви натисните картку коли")
sett_info2.set_text2("у вас буде 0 очків ваші очки будуть відмінусовуватись далі) ")
sett_info3.set_text2("Якщо ви не встигните набрати 5 очків за 10 секунд або ваші очки будуть -11 ви програєте")
sett_info4.set_text2("Автор:Ярослав Сапожкін")
#Створення об'єктів для меню налаштувань
sett_back = Picture("images/BtBack.png", 450, 300, 300, 100)
sett_back1 = Picture("images/BtBack1.png", 450, 300, 300, 100)

#Створення музики для додавання музики
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

#Шлях до файлу з музикою
music_file = 'sound/night_city_knigh.mp3'
play_music(music_file)

# Запуск музики у окремому потоці
music_thread = threading.Thread(target=play_music, args=(music_file,))
music_thread.start()

# Створення екрана меню
screen = "menu"
while True:
    mw.fill(back)
    if screen == "menu":
        menu_start.draw_picture()
        menu_settings.draw_picture()
        menu_exit.draw_picture()
        for event in pygame.event.get():
            #Створення анімації при наведені курсором на кнопку старт
            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos
                if menu_start.rect.collidepoint(x,y):
                    menu_start = Picture("images/knSTART1.png", 160, 50, 385, 85)

                else:
                    menu_start = Picture("images/knSTART.png", 150, 50, 385, 85)
            #Створення анімації при наведені курсором на кнопку налаштувань
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if menu_settings.rect.collidepoint(x, y):
                    menu_settings = Picture("images/KnSettings1.png", 200, 170, 298, 78)

                else:
                    menu_settings = Picture("images/KnSettings.png", 200, 170, 298, 78)
            #Створення анімації при наведені курсором на кнопку виходу
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if menu_exit.rect.collidepoint(x, y):
                    menu_exit = Picture("images/KnQuit1.png", 160, 280, 250, 100)

                else:
                    menu_exit = Picture("images/KnQuit.png", 150, 270, 250, 100)
            if event.type == pygame.QUIT:
                exit()
        #Функціонал кнопок меню
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if menu_settings.rect.collidepoint(x, y):
                screen = "settings"
            if menu_exit.rect.collidepoint(x, y):
                exit()
            if menu_start.rect.collidepoint(x, y):
                screen = "start"
            if sett_back.rect.collidepoint(x, y):
                screen = "menu"
    #Екран налаштувань
    elif screen == "settings":
        #Текст меню налаштувань
        sett_info.draw_text()
        sett_info1.draw_text1()
        sett_info2.draw_text2()
        sett_info3.draw_text3()
        sett_info4.draw_text4()
        #Кнопка назад для меню налаштувань
        sett_back.draw_picture()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if sett_back.rect.collidepoint(x, y):
                    sett_back = Picture("images/BtBack1.png", 450, 300, 230, 70)

                else:
                    sett_back = Picture("images/BtBack.png", 450, 300, 230, 70)

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if sett_back1.rect.collidepoint(x, y) or sett_back.rect.collidepoint(x, y):
                    screen = "menu"
    #Екран старту гри
    elif screen == "start":
        mw.fill(back1)
        class Area():
            def __init__(self, x=0, y=0, width=10, height=10, color=None):
                self.rect = pygame.Rect(x, y, width, height)  # прямокутник
                self.fill_color = color

            def color(self, new_color):
                self.fill_color = new_color

            def fill(self):
                pygame.draw.rect(mw, self.fill_color, self.rect)

            def outline(self, frame_color, thickness):  # обводка існуючого прямокутника
                pygame.draw.rect(mw, frame_color, self.rect, thickness)

            def collidepoint(self, x, y):  # перевірка на дотик до картки
                return self.rect.collidepoint(x, y)


        '''клас напис'''


        class Label(Area):
            def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
                self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

            def draw(self, shift_x=0, shift_y=0):
                self.fill()
                mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

        RED = (255, 0, 0)
        GREEN = (0, 255, 51)
        YELLOW = (255, 255, 0)
        DARK_BLUE = (0, 0, 100)
        BLUE = (80, 80, 255)
        LIGHT_GREEN = (200, 255, 200)
        LIGHT_RED = (250, 128, 114)

        cards = []
        num_cards = 4
        x = 70

        start_time = time.time()
        cur_time = start_time
        cur_time = time.time()

        time_text = Label(0, 0, 50, 50, back)
        time_text.set_text('Час:', 40, DARK_BLUE, )
        time_text.draw(10, 20)

        timer = Label(100, 20, 50, 40, back)
        timer.set_text('0', 40, DARK_BLUE)
        timer.draw(0, 0)

        score_text = Label(400, 0, 50, 50, back)
        score_text.set_text('Рахунок:', 30, DARK_BLUE)
        score_text.draw(5, 20)

        score = Label(550, 20, 50, 40, back)
        score.set_text('0', 30, DARK_BLUE)
        score.draw(0, 0)

        for i in range(num_cards):  # для кожного елемента з списку
            new_card = Label(x, 170, 70, 100, YELLOW)
            new_card.outline(BLUE, 10)
            new_card.set_text('CLICK', 18)
            cards.append(new_card)
            x = x + 100

        wait = 0  # змінну-лічильник wait для підрахунку кадрів.
        points = 0  # кількісь балів
        from random import randint

        while True:

            if wait == 0:
                wait = 20  # Скільки кліків напис буде на одному місці
                click = randint(1, num_cards)
                for i in range(num_cards):
                    cards[i].color(YELLOW)
                    if (i + 1) == click:
                        cards[i].draw(10, 40)
                    else:
                        cards[i].fill()
            else:
                wait -= 1

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    for i in range(num_cards):
                        # шукаємо, до якої карти потрапив клік
                        if cards[i].collidepoint(x, y):
                            if i + 1 == click:  # якщо на карті є напис перефарбовуємо в зелений плюс очко
                                cards[i].color(GREEN)
                                points += 1
                            else:  # інакше перефарбовуємо в червоний, мінус очко
                                cards[i].color(RED)
                                points -= 1

                            cards[i].fill()
                            score.set_text(str(points), 30, DARK_BLUE)
                            score.draw(0, 0)

            elapsed_time = cur_time - start_time
            new_time = time.time()
            if new_time - start_time >= 10:
                win = Label(0, 0, 700, 400, LIGHT_RED)
                win.set_text("Час вийшов!", 60, DARK_BLUE)
                win.draw(150, 150)
                cur_time = time.time()
            if int(new_time) - int(cur_time) == 1:
                timer.set_text(str(int(new_time - start_time)), 40, DARK_BLUE)
                timer.draw(0, 0)
                cur_time = new_time

            if points >= 5:
                cur_time = start_time
                cur_time = time.time()
                win = Label(0, 0, 700, 400, LIGHT_GREEN)
                win.set_text("ТИ ВИГРАВ!", 60, DARK_BLUE)
                win.draw(150, 150)

            if points <= -11:
                win = Label(0, 0, 700, 400, LIGHT_RED)
                win.set_text("ТИ ПРОГРАВ!", 60, DARK_BLUE)
                win.draw(150, 150)

            pygame.display.update()
            clock.tick(40)
        pygame.display.update()
        menu_pause.draw_picture()
    pygame.display.update()
    clock.tick(40)
