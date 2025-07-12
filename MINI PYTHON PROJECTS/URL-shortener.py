import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests

def lyhenna_linkit():
    alkuperaiset = syote_teksti.get("1.0", tk.END).strip().splitlines()
    if not alkuperaiset:
        messagebox.showwarning("Virhe", "Anna vähintään yksi linkki.")
        return
    
    lyhennetyt = []
    for url in alkuperaiset:
        if url.strip():
            lyhyt_url = hae_lyhyt_url(url.strip())
            lyhennetyt.append(lyhyt_url)

    tulos_teksti.config(state='normal')
    tulos_teksti.delete("1.0", tk.END)
    tulos_teksti.insert(tk.END, "\n".join(lyhennetyt))
    tulos_teksti.config(state='disabled')

def hae_lyhyt_url(url):
    try:
        api_url = f"https://tinyurl.com/api-create.php?url={url}"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Virhe: {url}"
    
    except Exception as e:
        return f"Virhe: {url} ({e})"
    

root = tk.Tk()
root.title("Linkin lyhennin - TinyURL")
root.geometry("600x500")

otsikko = tk.Label(root, text="Syötä linkit (yksi per rivi):", font=("Arial", 12))
otsikko.pack(pady=10)

syote_teksti = scrolledtext.ScrolledText(root, width=70, height=10)
syote_teksti.pack(padx=10)

nappi = tk.Button(root, text="Lyhennä linkit", command=lyhenna_linkit, font=("Arial", 11), bg="#4CAF50", fg="white")
nappi.pack(pady=10)

tulos_otsikko = tk.Label(root, text="Lyhennetyt linkit:", font=("Arial", 12))
tulos_otsikko.pack(pady=5)

tulos_teksti = scrolledtext.ScrolledText(root, width=70, height=10, state='disabled')
tulos_teksti.pack(padx=10, pady=5)

root.mainloop()