import os
import time
from threading import Thread

def animate_text(text, speed):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()  # baris baru

def sing_lyric(lyric, delay, speed, line_delay=0):
    time.sleep(delay)
    animate_text(lyric, speed)
    time.sleep(line_delay)

def sing_song():
    lyrics = [
        ("Kau begitu sempurna...", 0.08),
        ("Di mataku kau begitu indah...", 0.08),
        ("Kau membuat diriku...", 0.08),
        ("Akan slalu memujamu...", 0.08),
        ("Disetiap langkahku...", 0.09),
        ("Kukan slalu memikirkan dirimu...", 0.09),
        ("Tak bisa kubayangkan hidupku tanpa cintamu...", 0.07),
        ("Janganlah kau tinggalkan diriku...", 0.08),
        ("Takkan mampu menghadapi semua...", 0.09),
        ("Hanya bersamamu ku akan bisa...", 0.1),
        ("Kau adalah darahku...", 0.1),
        ("Kau adalah jantungku...", 0.1),
        ("Kau adalah hidupku...", 0.1),
        ("Lengkapi diriku...", 0.1),
        ("Oh sayangku kau begitu...", 0.08),
        ("Sempurna...", 0.12)
    ]

    delays = [0, 3, 6, 9, 12, 15, 19, 22, 25, 29, 32, 35, 38, 41, 44, 47]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

# Bersihkan layar terminal sebelum mulai
os.system('cls' if os.name == 'nt' else 'clear')

sing_song()
