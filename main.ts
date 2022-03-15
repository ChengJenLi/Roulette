function 編號關燈 (燈號: number) {
    LX = 燈號 % 5
    LY = 燈號 / 5
    led.unplot(LX, LY)
}
input.onButtonPressed(Button.A, function () {
    亂數 = randint(0, 15)
    PA = true
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    PA = false
})
function 編號點燈 (燈號2: number) {
    LX = 燈號2 % 5
    LY = 燈號2 / 5
    led.plot(LX, LY)
}
let PA = false
let 亂數 = 0
let LY = 0
let LX = 0
let list2 = [
0,
1,
2,
3,
4,
9,
14,
19,
24,
23,
22,
21,
20,
15,
10,
5
]
basic.forever(function () {
    if (PA) {
        for (let index = 0; index <= 亂數; index++) {
            編號點燈(list2[index])
            basic.pause(100)
            編號關燈(list2[index])
        }
        編號點燈(list2[亂數])
    } else {
        for (let index = 0; index <= 15; index++) {
            編號點燈(list2[index])
            basic.pause(100)
            編號關燈(list2[index])
        }
    }
})
