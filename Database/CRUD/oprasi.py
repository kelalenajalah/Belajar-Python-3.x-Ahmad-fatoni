from time import time 
from . import database
from .util import random_string
import time

def dataAwal():
    penulis = input("Penulis : ")
    judul = input("Penulis : ")
    tahun = input("tahun : ")

    data = database.Template.copy()

    data["pk"] = random_string
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah Gagal booooos")

def read():
    try:
        with open(database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False
    