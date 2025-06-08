import tkinter as tk
import math
import random
from collections import deque # Deque untuk penambahan/penghapusan efisien dari kedua ujung

# --- Konstanta Game ---
CANVAS_WIDTH = 800  # Lebar kanvas game
CANVAS_HEIGHT = 600 # Tinggi kanvas game
BALL_RADIUS = 20    # Radius bola
SHOOTER_RADIUS = 30 # Radius penembak (katak)
BALL_COLORS = ["red", "green", "blue", "yellow", "purple"] # Warna-warna bola yang tersedia
GAME_SPEED_MS = 30  # Milidetik per frame (nilai lebih kecil = game lebih cepat)
CHAIN_MOVE_SPEED = 2 # Kecepatan pergerakan rantai bola (dalam piksel per frame)
PROJECTILE_SPEED = 15 # Kecepatan bola yang ditembakkan (dalam piksel per frame)

# Definisi jalur: Garis lurus sederhana dari kiri ke kanan
PATH_START_X = -BALL_RADIUS * 5 # Mulai di luar layar di sebelah kiri
PATH_END_X = CANVAS_WIDTH + BALL_RADIUS * 5 # Berakhir di luar layar di sebelah kanan
PATH_Y = CANVAS_HEIGHT // 2 - 50 # Koordinat Y untuk jalur rantai

# Batas Game Over: Jika bola pertama mencapai koordinat X ini
GAME_OVER_X_THRESHOLD = CANVAS_WIDTH - BALL_RADIUS * 2

class Ball:
    """Mewakili satu bola berwarna dalam game."""
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.id = None # ID objek di kanvas Tkinter

    def draw(self, canvas):
        """Menggambar bola di kanvas."""
        x1, y1 = self.x - BALL_RADIUS, self.y - BALL_RADIUS
        x2, y2 = self.x + BALL_RADIUS, self.y + BALL_RADIUS
        if self.id:
            # Jika bola sudah ada, perbarui posisinya
            canvas.coords(self.id, x1, y1, x2, y2)
            canvas.itemconfig(self.id, fill=self.color)
        else:
            # Jika bola baru, buat objek oval baru
            self.id = canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline="black", width=1)

class Projectile:
    """Mewakili bola yang ditembakkan oleh penembak."""
    def __init__(self, color, start_x, start_y, target_x, target_y):
        self.color = color
        self.x = start_x
        self.y = start_y
        self.id = None # ID objek di kanvas Tkinter

        # Hitung vektor arah pergerakan
        dx = target_x - start_x
        dy = target_y - start_y
        dist = math.sqrt(dx**2 + dy**2)
        
        # Normalisasi dan skalakan dengan kecepatan proyektil
        if dist == 0: # Hindari pembagian dengan nol
            self.vx = 0
            self.vy = 0
        else:
            self.vx = (dx / dist) * PROJECTILE_SPEED
            self.vy = (dy / dist) * PROJECTILE_SPEED

    def update(self):
        """Memperbarui posisi proyektil."""
        self.x += self.vx
        self.y += self.vy

    def draw(self, canvas):
        """Menggambar proyektil di kanvas."""
        x1, y1 = self.x - BALL_RADIUS, self.y - BALL_RADIUS
        x2, y2 = self.x + BALL_RADIUS, self.y + BALL_RADIUS
        if self.id:
            # Jika proyektil sudah ada, perbarui posisinya
            canvas.coords(self.id, x1, y1, x2, y2)
            canvas.itemconfig(self.id, fill=self.color)
        else:
            # Jika proyektil baru, buat objek oval baru
            self.id = canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline="white", width=2)

    def is_offscreen(self):
        """Memeriksa apakah proyektil keluar dari area kanvas."""
        return (self.x < -BALL_RADIUS or self.x > CANVAS_WIDTH + BALL_RADIUS or
                self.y < -BALL_RADIUS or self.y > CANVAS_HEIGHT + BALL_RADIUS)

class AplikasiZuma:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Game Zuma")
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="darkgreen")
        self.canvas.pack()

        self.game_over = False
        self.score = 0
        # Teks skor di sudut kiri atas
        self.score_text_id = self.canvas.create_text(10, 10, anchor="nw", text=f"Skor: {self.score}", fill="white", font=("Arial", 16, "bold"))

        self.chain_y = PATH_Y # Koordinat Y untuk rantai lurus
        self.ball_chain = deque() # Menggunakan deque untuk rantai bola

        self.projectile = None
        self.shooter_x = CANVAS_WIDTH // 2 # Posisi X penembak (tengah bawah)
        self.shooter_y = CANVAS_HEIGHT - SHOOTER_RADIUS * 2 # Posisi Y penembak

        # Inisialisasi warna bola berikutnya yang akan ditembakkan
        self.shooter_next_color = random.choice(BALL_COLORS)
        # Gambar penembak (lingkaran abu-abu)
        self.shooter_id = self.canvas.create_oval(
            self.shooter_x - SHOOTER_RADIUS, self.shooter_y - SHOOTER_RADIUS,
            self.shooter_x + SHOOTER_RADIUS, self.shooter_y + SHOOTER_RADIUS,
            fill="grey", outline="black", width=2
        )
        self.shooter_ball_id = None # ID untuk bola yang ditampilkan di dalam penembak
        self.update_shooter_display() # Perbarui tampilan bola di penembak

        # Ikat klik mouse kiri untuk menembakkan bola
        self.canvas.bind("<Button-1>", self.shoot_ball)

        self.init_chain(15) # Mulai dengan 15 bola di rantai
        self.game_loop() # Mulai loop game

    def update_shooter_display(self):
        """Memperbarui warna bola yang ditampilkan di dalam penembak."""
        if self.shooter_ball_id:
            self.canvas.delete(self.shooter_ball_id) # Hapus bola sebelumnya
        
        # Gambar bola kecil di dalam penembak untuk menunjukkan warna bola berikutnya
        offset = SHOOTER_RADIUS - BALL_RADIUS // 2 
        self.shooter_ball_id = self.canvas.create_oval(
            self.shooter_x - offset, self.shooter_y - offset,
            self.shooter_x + offset, self.shooter_y + offset,
            fill=self.shooter_next_color, outline="white", width=1
        )
        self.canvas.tag_raise(self.shooter_ball_id, self.shooter_id) # Pastikan bola di atas penembak

    def init_chain(self, num_balls):
        """Menginisialisasi rantai bola dengan jumlah bola yang ditentukan."""
        # Tempatkan bola secara berurutan dari kiri ke kanan, dimulai di luar layar
        for i in range(num_balls):
            color = random.choice(BALL_COLORS)
            # Posisi X bola, dengan sedikit celah antar bola
            x_pos = PATH_START_X + i * (BALL_RADIUS * 2 + 2) 
            ball = Ball(color, x_pos, self.chain_y)
            self.ball_chain.append(ball)
            ball.draw(self.canvas)

    def shoot_ball(self, event):
        """Menangani klik mouse untuk menembakkan proyektil."""
        if self.projectile: # Hanya izinkan satu proyektil dalam satu waktu
            return
        if self.game_over: # Jangan tembak jika game over
            return

        target_x, target_y = event.x, event.y # Dapatkan koordinat klik mouse
        # Buat proyektil baru dengan warna bola berikutnya
        self.projectile = Projectile(self.shooter_next_color, self.shooter_x, self.shooter_y, target_x, target_y)
        self.shooter_next_color = random.choice(BALL_COLORS) # Dapatkan warna bola berikutnya untuk ditembakkan
        self.update_shooter_display() # Perbarui tampilan penembak

    def update_game(self):
        """Memperbarui logika game untuk setiap frame."""
        if self.game_over:
            return

        # Gerakkan rantai bola
        if self.ball_chain:
            for ball in self.ball_chain:
                ball.x += CHAIN_MOVE_SPEED # Gerakkan bola ke kanan
                ball.draw(self.canvas) # Gambar ulang bola di posisi baru

            # Periksa kondisi game over (bola pertama mencapai batas)
            if self.ball_chain[0].x >= GAME_OVER_X_THRESHOLD:
                self.game_over = True
                self.display_game_over("GAME OVER!", "red")
                return

        # Perbarui dan gambar proyektil
        if self.projectile:
            self.projectile.update() # Perbarui posisi proyektil
            self.projectile.draw(self.canvas) # Gambar proyektil
            
            if self.projectile.is_offscreen():
                self.canvas.delete(self.projectile.id) # Hapus proyektil jika keluar layar
                self.projectile = None
            else:
                self.check_projectile_collision() # Periksa tabrakan

        # Periksa kondisi menang (rantai kosong)
        if not self.ball_chain and not self.projectile:
            self.game_over = True
            self.display_game_over("ANDA MENANG!", "gold")
            return

    def check_projectile_collision(self):
        """Memeriksa apakah proyektil bertabrakan dengan bola di rantai."""
        if not self.projectile:
            return

        for i, ball in enumerate(self.ball_chain):
            # Hitung jarak antara proyektil dan bola di rantai
            dist = math.sqrt((self.projectile.x - ball.x)**2 + (self.projectile.y - ball.y)**2)

            if dist < BALL_RADIUS * 2: # Tabrakan terdeteksi (dua radius bola)
                self.insert_and_match(self.projectile, i) # Sisipkan dan periksa kecocokan
                self.canvas.delete(self.projectile.id) # Hapus proyektil
                self.projectile = None
                return

    def insert_and_match(self, projectile, collision_index):
        """Menyisipkan proyektil ke dalam rantai dan memeriksa kecocokan."""
        # Buat objek Bola baru dari proyektil yang bertabrakan
        new_ball = Ball(projectile.color, projectile.x, projectile.y)
        
        # Sisipkan bola baru di posisi tabrakan (sebelum bola yang ditabrak)
        self.ball_chain.insert(collision_index, new_ball)
        new_ball.draw(self.canvas) # Gambar bola yang baru disisipkan

        # Atur ulang posisi semua bola di rantai untuk menjaga jarak yang konsisten
        self.reposition_chain()

        # Periksa kecocokan di sekitar posisi bola yang baru disisipkan
        self.check_for_matches(collision_index)

    def reposition_chain(self):
        """Mengatur ulang posisi semua bola di rantai untuk menjaga jarak yang konsisten."""
        if not self.ball_chain:
            return
        
        # Posisi X bola pertama (kepala rantai) tetap pada posisinya saat ini
        current_x = self.ball_chain[0].x
        self.ball_chain[0].draw(self.canvas) # Pastikan bola pertama digambar di posisi X-nya saat ini

        # Atur posisi bola-bola berikutnya relatif terhadap bola sebelumnya
        for i in range(1, len(self.ball_chain)):
            current_x += (BALL_RADIUS * 2 + 2) # Tambahkan diameter bola + sedikit celah
            self.ball_chain[i].x = current_x
            self.ball_chain[i].y = self.chain_y # Pastikan tetap di jalur Y
            self.ball_chain[i].draw(self.canvas)

    def check_for_matches(self, inserted_index):
        """Memeriksa kecocokan 3 atau lebih bola berwarna sama di sekitar bola yang disisipkan."""
        if not self.ball_chain:
            return

        # Dapatkan warna bola yang baru disisipkan
        match_color = self.ball_chain[inserted_index].color
        
        # Temukan awal segmen kecocokan potensial (bergerak ke kiri dari bola yang disisipkan)
        match_start = inserted_index
        while match_start > 0 and self.ball_chain[match_start - 1].color == match_color:
            match_start -= 1
        
        # Temukan akhir segmen kecocokan potensial (bergerak ke kanan dari bola yang disisipkan)
        match_end = inserted_index
        while match_end < len(self.ball_chain) - 1 and self.ball_chain[match_end + 1].color == match_color:
            match_end += 1
        
        match_length = match_end - match_start + 1 # Hitung panjang kecocokan

        if match_length >= 3:
            # Hapus bola yang cocok
            for _ in range(match_length):
                ball_to_remove = self.ball_chain.pop(match_start) # Hapus dari awal segmen kecocokan
                self.canvas.delete(ball_to_remove.id) # Hapus objek dari kanvas
            
            self.score += match_length * 10 # Tingkatkan skor
            self.canvas.itemconfig(self.score_text_id, text=f"Skor: {self.score}") # Perbarui tampilan skor

            # Setelah penghapusan, atur ulang posisi rantai yang tersisa untuk menutup celah
            self.reposition_chain()

    def display_game_over(self, message, color):
        """Menampilkan pesan game over atau menang."""
        # Hapus pesan game sebelumnya jika ada
        self.canvas.delete("game_message")
        
        # Tampilkan pesan utama
        self.canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2 - 20, text=message, fill=color, font=("Arial", 40, "bold"), tags="game_message")
        # Tampilkan skor akhir
        self.canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2 + 30, text=f"Skor Akhir: {self.score}", fill="white", font=("Arial", 24), tags="game_message")
        
        # Tambahkan tombol "Mulai Ulang"
        self.restart_button = tk.Button(self.root, text="Mulai Ulang", command=self.reset_game, font=("Arial", 18), bg="#4CAF50", fg="white", relief="raised", bd=3)
        # Tempatkan tombol di kanvas
        self.canvas.create_window(CANVAS_WIDTH/2, CANVAS_HEIGHT/2 + 100, window=self.restart_button)

    def reset_game(self):
        """Mengatur ulang status game."""
        # Hapus semua objek dari kanvas
        self.canvas.delete("all")
        
        # Reset variabel game
        self.game_over = False
        self.score = 0
        self.ball_chain = deque()
        self.projectile = None
        
        # Gambar ulang teks skor dan penembak
        self.score_text_id = self.canvas.create_text(10, 10, anchor="nw", text=f"Skor: {self.score}", fill="white", font=("Arial", 16, "bold"))
        self.shooter_id = self.canvas.create_oval(
            self.shooter_x - SHOOTER_RADIUS, self.shooter_y - SHOOTER_RADIUS,
            self.shooter_x + SHOOTER_RADIUS, self.shooter_y + SHOOTER_RADIUS,
            fill="grey", outline="black", width=2
        )
        self.shooter_next_color = random.choice(BALL_COLORS)
        self.update_shooter_display()

        # Inisialisasi ulang rantai bola
        self.init_chain(15)
        
        # Hapus tombol restart jika ada (penting agar tidak ada tombol duplikat)
        # Menggunakan try-except untuk menangani kasus di mana tombol mungkin sudah dihancurkan
        try:
            if self.restart_button.winfo_exists(): # Periksa apakah widget masih ada
                self.restart_button.destroy() 
        except AttributeError:
            pass # Tombol belum dibuat atau sudah dihancurkan

        # Mulai ulang loop game
        self.game_loop()

    def game_loop(self):
        """Loop game utama untuk animasi dan pembaruan."""
        self.update_game() # Panggil fungsi pembaruan game
        if not self.game_over:
            # Jadwalkan panggilan berikutnya ke game_loop setelah GAME_SPEED_MS milidetik
            self.root.after(GAME_SPEED_MS, self.game_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiZuma(root)
    root.mainloop()
