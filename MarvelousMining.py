import pygame, sys, os, random
pygame.init()

FPS = 60
white = (255, 255, 255)
red = (255,0,0)
BG = (239, 93, 96)
winX = 800
winY = 800
scale = 17
screen = pygame.display.set_mode((winX,winY))
center = winX/2 - scale*16/2,winY/2 - scale*16/2
offset = winX/2 - scale*16/2,winY/2 - scale*16/2
frame_counter = 1
money = 0


buttonstate1 = 'buttonUp'
buttonCount = 0
isPresssed1 = False
button1lv = 0
price1 = 500

buttonstate2 = 'buttonUp'
buttonCount2 = 0
isPresssed2 = False
button2lv = 0
price2 = 500

Cash = pygame.font.Font('rainyhearts.ttf', 75)
defaultfont = pygame.font.Font('Minecraft.ttf', 35)

#transparent surface that will move everything dran on in (like when screen is shaking)
display_surface = pygame.Surface((winX,winY), pygame.SRCALPHA, 32)
pygame.display.set_caption('Screen SHAKE!!')

clock = pygame.time.Clock()
screen_shake = 0
Shake_Offset = [0,0]
State_Counter = 0

img = 'stone'
#upgrades
auto = False
speed = FPS/2

luck = 4
luckpubluc = 0
copper = False
iron = False
gold = False
aqua_marine = False


def randomImg():
    global img, luck
    num = random.randint(1,luck)
    if num == 1:
        img = 'stone'
        print('stone1')
    if num == 2:
        img = 'stone2'
        print('stone2')
    if num == 3:
        img = 'coal'
        print('coal1')
    if num == 4:
        img = 'coal2'
        print('coal2')
    if num == 5:
        img = 'copper'
        print('copper')
    if num == 6:
        img = 'iron'
        print('iron')
    if num == 7:
        img = 'gold'
        print('gold')
    if num == 8:
        img = 'aqua'
        print('aqua')

#on mouse clicks
def Change_State():
    global State_Index, State_Counter, screen_shake,money
    if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]: # 0 == left click
                screen_shake = 30 #duration in frames (30 = 0.5s)
            if State_Counter + 1 == 11:
                State_Counter = 0
                if img == 'stone' or img == 'stone2':
                    money += 10
                if img == 'coal' or img == 'coal2':
                    money += 15
                randomImg()
            else:
                State_Counter += 1
            print(State_Counter)

def AUTOMATE():
    global State_Index, State_Counter, screen_shake,money,frame_counter,speed
    
    if frame_counter == speed:
        screen_shake = 30 #duration in frames (30 = 0.5s)
        if State_Counter + 1 == 11:
            State_Counter = 0
            if img == 'stone' or img == 'stone2':
                money += 10
            if img == 'coal' or img == 'coal2':
                money += 15
            if img == 'copper':
                money += 17
            if img == 'iron':
                money += 22
            if img == 'gold':
                money += 30
            if img == 'aqua':
                money += 50
            randomImg()
        else:
            State_Counter += 1
        print(State_Counter)

def DrawCracks(frame):
    if frame == 0:
        display_surface.blit(Crack,(offset),(0,0,0,0))
    if frame == 1:
        display_surface.blit(Crack,(offset),(0,0,16*scale,16*scale))
    if frame == 2:
        display_surface.blit(Crack,(offset),(16*scale*1,0,16*scale,16*scale))
    if frame == 3:
        display_surface.blit(Crack,(offset),(16*scale*2,0,16*scale,16*scale))
    if frame == 4:
        display_surface.blit(Crack,(offset),(16*scale*3,0,16*scale,16*scale))
    if frame == 5:
        display_surface.blit(Crack,(offset),(16*scale*4,0,16*scale,16*scale))
    if frame == 6:
        display_surface.blit(Crack,(offset),(16*scale*5,0,16*scale,16*scale))
    if frame == 7:
        display_surface.blit(Crack,(offset),(16*scale*6,0,16*scale,16*scale))
    if frame == 8:
        display_surface.blit(Crack,(offset),(16*scale*7,0,16*scale,16*scale))
    if frame == 9:
        display_surface.blit(Crack,(offset),(16*scale*8,0,16*scale,16*scale))
    if frame == 10:
        display_surface.blit(Crack,(offset),(16*scale*9,0,16*scale,16*scale))



def Button1():
    global isPresssed1, buttonCount, buttonstate1, money
    Button1 = pygame.image.load(f'{buttonstate1}.png').convert_alpha()
    Button1 = pygame.transform.scale(Button1, (32 * scale/2,16 * scale/2))
    header1 = defaultfont.render(f'AUTO mine lv{button1lv}', False, white) 
    subheader1 = defaultfont.render(f'{price1} [1]', False, red) 
    screen.blit(Button1,(25,650))
    screen.blit(header1, (30,600))
    screen.blit(subheader1, (100,690))
    if isPresssed1 == True:
        buttonCount += 1
    if buttonCount == 30:
        buttonstate1 = 'buttonUp'
        isPresssed1 = False
        buttonCount = 0

def Button2():
    global isPresssed2, buttonCount2, buttonstate2, money
    Button2 = pygame.image.load(f'{buttonstate2}.png').convert_alpha()
    Button2 = pygame.transform.scale(Button2, (32 * scale/2,16 * scale/2))
    header2 = defaultfont.render(f'LUCK lv{luckpubluc}', False, white) 
    subheader2 = defaultfont.render(f'{price2} [2]', False, red) 
    screen.blit(Button2,(500,650))
    screen.blit(header2, (550,600))
    screen.blit(subheader2, (575,690))
    if isPresssed2 == True:
        buttonCount2 += 1
    if buttonCount2 == 30:
        buttonstate2 = 'buttonUp'
        isPresssed2 = False
        buttonCount2 = 0




while True:
    screen.fill(BG)
    if frame_counter + 1 == 61:
        frame_counter = 1
    
    cashTEXT = Cash.render(f'${money}', False, white) 
    infoTEXT = defaultfont.render('CLICK TO MINE!!', False, white) 

    Block = pygame.image.load(f'block bases/{img}.png').convert_alpha()
    Block = pygame.transform.scale(Block, (16 * scale,16 * scale))

    Crack = pygame.image.load('block break/BreakSheet.png').convert_alpha()
    Crack = pygame.transform.scale(Crack, (16 * scale*10,16 * scale))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if auto == False:
            Change_State()
        
        key = pygame.key.get_pressed()
        if key [pygame.K_1] and buttonCount == 0 and isPresssed1 == False and money >= price1 and button1lv <3:
            buttonstate1 = "buttonDown"
            money -= price1

            if button1lv == 2:
                price1 = 1000000
                speed = FPS/3
                button1lv += 1
                print('upgrade AUTO 3')
                print(f'button lv {button1lv}')
            if button1lv == 1:
                price1 = 5000
                speed = FPS/12
                button1lv += 1
                print('upgrade AUTO 2')
                print(f'button lv {button1lv}')
            if button1lv == 0:
                price1 = 2000
                button1lv += 1
                auto = True
                print('upgrade AUTO 1')
                print(f'button lv {button1lv}')
            isPresssed1 = True
        if key [pygame.K_2] and buttonCount2 == 0 and isPresssed2 == False and price2 <100000:
            buttonstate2 = "buttonDown"
            money -= price2
    
            if button2lv == 4:
                price2 = 9900000
                button2lv += 1
                luckpubluc +=1
                luck += 1
                print('luck 1')
                print(f'luck lv {luck}')
            if button2lv == 3:
                price2 = 5000
                button2lv += 1
                luckpubluc +=1
                luck += 1
                print('luck 1')
                print(f'luck lv {luck}')
            if button2lv == 2:
                price2 = 2500
                button2lv += 1
                luckpubluc +=1
                luck += 1
                print('luck 1')
                print(f'luck lv {luck}')
            if button2lv == 1:
                price2 = 1000
                button2lv += 1
                luckpubluc +=1
                luck += 1
                print('luck 1')
                print(f'luck lv {luck}')
            if button2lv == 0:
                price2 = 250
                button2lv += 1
                luckpubluc +=1
                luck += 1
                print('luck 1')
                print(f'luck lv {luck}')

            isPresssed2 = True
        if key [pygame.K_3] and buttonCount == 0 and isPresssed3 == False:
            print('upgrade')
            buttonstate3 = "buttonDown"
            isPresssed3 = True
        
    if auto == True:
        AUTOMATE()

    Button1() 
    Button2()
    screen.blit(display_surface, Shake_Offset)
    display_surface.blit(Block,(offset))
    DrawCracks(State_Counter)
    screen.blit(cashTEXT, (10,0))
    screen.blit(infoTEXT, (winX/2 - scale*16/2,winY/2 - scale*16/2 -50))


    #random x and y transformations
    if screen_shake > 0:
        screen_shake -= 1
    if screen_shake:
        Shake_Offset[0] = random.randint(0,8) - 4
        Shake_Offset[1] = random.randint(0,8) - 4

    frame_counter += 1
    pygame.display.update()
    clock.tick(FPS)