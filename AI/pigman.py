import pygame

# init game
pygame.init()
# command untuk menjalankan game
isRun = True

# untuk ukuran dari window game
panjang_window = 500
lebar_window = 500
window = pygame.display.set_mode((panjang_window, lebar_window))

# poisis dari objek
x = 250
y = 250

# untuk kecepatan gerak
speed = 20

# kode utama program
while True:
    pygame.time.delay(10)

    # Tombol dari input user
    for gerakan in pygame.event.get():
        if gerakan.type == pygame.QUIT:
            isRun = False

    # Mengambil control dari keyboward
    analog = pygame.key_pressed()

    # ambil ke kiri
    if analog[pygame.K_LEFT] and x > 0:
        x -= speed
    
    if analog[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed

    if analog[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed

    if analog[pygame.K_UP] and y > 0:
        y -= speed






pygame.quit()
