import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Kinder Süt Dilimi Endeksleyicisi")

content = requests.get("https://www.sokmarket.com.tr/kinder-sut-dilimi-28-g-p-5835")
çorba = BeautifulSoup(content.text, "html.parser")
a = çorba.find('div', class_='CPriceBox-module_priceContainer__ZROpc')
para = a.get_text(strip=True)
para = float(para[:-1].replace(',', '.'))

entry = tk.Entry(root)
entry.pack(pady=5)

def alisahin():
    try:
        ürün = float(entry.get())
        sonuç = ürün / para
        result_label.config(text=f"{ürün} lira ile {sonuç:.2f} adet Süt Dilimi alabilirsiniz.")
    except ValueError:
        messagebox.showerror("Input Error", "Geçerli bir fiyat girin.")

calculate_button = tk.Button(root, text="Hesapla", command=alisahin)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
