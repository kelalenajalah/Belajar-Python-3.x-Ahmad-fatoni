import pygame as game

game.init()
bergerak = True

# membuat windownya 
lebar_window = 500
panjang_window = 500
window = game.display.set_mode((lebar_window, panjang_window))

# posis,ukuran dan kecepatan
posX = 250
posY = 250
pan = 20
leb = 20
sp = 10

# kode programnya
while bergerak:
    game.time.delay(10)

# Program untuk keluar dari windo (Input user)
    for event in game.event.get():
        if event.type == game.QUIT:
            bergerak = False

    # Mengambil kontrol dari keyboard
    tombol = game.key.get_pressed()

    # Code untuk menggerakan
    if tombol[game.K_LEFT] and posX > 0:
        posX -= sp
        
    if tombol[game.K_RIGHT] and posX < lebar_window-leb:
        posX += sp

    if tombol[game.K_DOWN] and posY < panjang_window-pan:
        posY += sp

    if tombol[game.K_UP] and posY > 0:
        posY -= sp

# aset dalam game
    window.fill((255,255,255))
    game.draw.rect(window,(255,125,1),(posX,posY,pan,leb))
    game.display.update()

game.quit()