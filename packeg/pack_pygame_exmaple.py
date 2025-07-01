import pygame

# Inisialisasi Pygame
pygame.init()

# Konfigurasi window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Puzzle Game: Cari Jalan Keluar")

# Warna
WHITE = (255, 255, 255)
ORANGE = (255, 120, 0)
RED = (255, 0, 0)  # Warna untuk rintangan
GREEN = (0, 255, 0)  # Warna untuk tujuan

# Objek game (persegi panjang pemain)
x = 20
y = 20
RECT_WIDTH = 20
RECT_HEIGHT = 20
SPEED = 10

# Daftar rintangan (x, y, width, height)
obstacles = [
    (100, 100, 200, 20),  # Dinding horizontal
    (100, 200, 20, 200),  # Dinding vertikal
    (300, 300, 100, 20),  # Dinding horizontal pendek
    (200, 50, 20, 100)    # Dinding vertikal pendek
]

# Tujuan (exit)
exit_rect = (WINDOW_WIDTH - 40, WINDOW_HEIGHT - 40, 20, 20)  # Persegi panjang hijau di kanan bawah

# Inisialisasi font untuk pesan kemenangan
font = pygame.font.SysFont("arial", 36)

# Kontrol frame rate
clock = pygame.time.Clock()
FPS = 60  # Frame per second

# Status game
is_running = True
game_won = False

while is_running:
    # Atur frame rate
    clock.tick(FPS)

    # Tangani event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    if not game_won:
        # Ambil input keyboard
        keys = pygame.key.get_pressed()

        # Simpan posisi sebelumnya untuk rollback jika tabrakan
        prev_x, prev_y = x, y

        # Gerakan persegi panjang dengan batasan
        if keys[pygame.K_LEFT] and x > 0:
            x -= SPEED
        if keys[pygame.K_RIGHT] and x < WINDOW_WIDTH - RECT_WIDTH:
            x += SPEED
        if keys[pygame.K_UP] and y > 0:
            y -= SPEED
        if keys[pygame.K_DOWN] and y < WINDOW_HEIGHT - RECT_HEIGHT:
            y += SPEED

        # Buat rect untuk pemain
        player_rect = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)

        # Cek tabrakan dengan rintangan
        for obs in obstacles:
            obstacle_rect = pygame.Rect(obs)
            if player_rect.colliderect(obstacle_rect):
                # Kembalikan ke posisi sebelumnya jika menabrak
                x, y = prev_x, prev_y
                break

        # Cek apakah pemain mencapai tujuan
        exit_rect_obj = pygame.Rect(exit_rect)
        if player_rect.colliderect(exit_rect_obj):
            game_won = True

    # Update tampilan
    window.fill(WHITE)  # Bersihkan layar dengan warna putih

    # Gambar rintangan
    for obs in obstacles:
        pygame.draw.rect(window, RED, obs)

    # Gambar tujuan (exit)
    pygame.draw.rect(window, GREEN, exit_rect)

    # Gambar pemain
    pygame.draw.rect(window, ORANGE, (x, y, RECT_WIDTH, RECT_HEIGHT))

    # Jika menang, tampilkan pesan
    if game_won:
        win_text = font.render("You Win!", True, (0, 0, 255))
        window.blit(win_text, (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 18))

    # Perbarui tampilan
    pygame.display.update()

# Keluar dari Pygame
pygame.quit()