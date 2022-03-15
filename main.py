def 編號關燈(燈號: number):
    global LX, LY
    LX = 燈號 % 5
    LY = 燈號 / 5
    led.unplot(LX, LY)

def on_button_pressed_a():
    global 亂數, PA
    亂數 = randint(0, 15)
    PA = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def doSomething(DELAY: number):
    for index in range(16):
        編號點燈(list2[index])
        basic.pause(DELAY)
        編號關燈(list2[index])

def on_button_pressed_b():
    global PA
    basic.clear_screen()
    PA = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def 編號點燈(燈號2: number):
    global LX, LY
    LX = 燈號2 % 5
    LY = 燈號2 / 5
    led.plot(LX, LY)
PA = False
亂數 = 0
LY = 0
LX = 0
list2: List[number] = []
list2 = [0, 1, 2, 3, 4, 9, 14, 19, 24, 23, 22, 21, 20, 15, 10, 5]

def on_forever():
    if PA:
        index2 = 0
        while index2 <= 亂數:
            編號點燈(list2[index2])
            basic.pause(100)
            編號關燈(list2[index2])
            index2 += 1
        編號點燈(list2[亂數])
    else:
        for index3 in range(1001):
            doSomething(index3)
basic.forever(on_forever)
