import tkinter as tk
import numpy as np

def fft(data):
    N = len(data)
    
    # Condition d'arrêt de la récursion
    if N <= 1:
        return data
    
    # Séparation des parties paire et impaire
    even = fft(data[0::2])
    odd = fft(data[1::2])
    
    # Calcul de la transformée de Fourier discrète à 2 points
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N//2):
        angle = -2j * np.pi * k / N
        e = even[k]
        o = odd[k]
        X[k] = e + np.exp(angle) * o
        X[k + N//2] = e - np.exp(angle) * o
    
    return X

def get_x_values():
    N = int(n_entry.get())
    if not N or N & (N - 1) != 0:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Veuillez entrer une puissance de 2 pour N.")
        return
    
    # Effacer les champs d'entrée existants
    for entry in x_entries:
        entry.destroy()
    
    # Créer de nouveaux champs d'entrée pour les valeurs de x
    x_entries.clear()
    for i in range(N):
        label = tk.Label(window, text=f"x[{i+1}]:")
        label.grid(row=i+3, column=0, sticky="e", padx=10, pady=5)
        
        entry = tk.Entry(window)
        entry.grid(row=i+3, column=1, padx=10, pady=5)
        
        x_entries.append(entry)
    
    calculate_button.config(state=tk.NORMAL)

def calculate_fft():
    data = []
    for entry in x_entries:
        value = entry.get()
        if not value:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "Erreur : Veuillez entrer toutes les valeurs de x.")
            return
        try:
            data.append(float(value))
        except ValueError:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "Erreur : Les valeurs de x doivent être des nombres.")
            return
    
    # Calcul de la transformée de Fourier discrète
    result = fft(data)
    
    # Affichage des résultats dans l'interface utilisateur
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Sortie X :\n")
    for k, value in enumerate(result):
        output_text.insert(tk.END, f"X[{k}] = {value}\n")

# Couleurs
bg_color = "#f0f0f0"
label_color = "#333333"
button_color = "#4c94ff"
entry_bg_color = "white"
entry_fg_color = "black"
output_bg_color = "white"
output_fg_color = "black"

# Style de police
font = ("Arial", 12)

# Configuration de la fenêtre
window = tk.Tk()
window.title("Calcul de la Transformée de Fourier Discrète")
window.configure(bg=bg_color)

# Titre de l'application
title_label = tk.Label(window, text="Transformée de Fourier Discrète", font=("Arial", 18), bg=bg_color, fg=label_color)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Nombre de données
n_frame = tk.Frame(window, bg=bg_color)
n_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

n_label = tk.Label(n_frame, text="Nombre de données (N) :", font=font, bg=bg_color, fg=label_color)
n_label.pack(side="left")

n_entry = tk.Entry(n_frame, font=font, bg=entry_bg_color, fg=entry_fg_color)
n_entry.pack(side="left", padx=10)

get_x_values_button = tk.Button(window, text="OK", font=font, bg=button_color, fg="white", command=get_x_values)
get_x_values_button.grid(row=1, column=1, padx=10)

# Nota Bene
nota_bene_label = tk.Label(window, text="Nota Bene: N doit être une puissance de 2", font=("Arial", 10), bg=bg_color, fg=label_color)
nota_bene_label.grid(row=2, column=0, columnspan=2, pady=5)

# Valeurs de x
x_frame = tk.Frame(window, bg=bg_color)
x_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

x_entries = []
x_labels = []

def clear_x_entries():
    for entry in x_entries:
        entry.destroy()
    for label in x_labels:
        label.destroy()

def create_x_entries():
    clear_x_entries()
    
    N = int(n_entry.get())
    if not N or N & (N - 1) != 0:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Veuillez entrer une puissance de 2 pour N.")
        return
    
    for i in range(N):
        label = tk.Label(x_frame, text=f"x[{i+1}]:", font=font, bg=bg_color, fg=label_color)
        label.grid(row=i, column=0, sticky="e", padx=10, pady=5)
        x_labels.append(label)
        
        entry = tk.Entry(x_frame, font=font, bg=entry_bg_color, fg=entry_fg_color)
        entry.grid(row=i, column=1, padx=10, pady=5)
        x_entries.append(entry)
    
    calculate_button.config(state=tk.NORMAL)

get_x_values_button.config(command=create_x_entries)

# Bouton Calculer
calculate_button = tk.Button(window, text="Calculer", font=font, bg=button_color, fg="white", command=calculate_fft, state=tk.DISABLED)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Sortie X
output_frame = tk.Frame(window, bg=bg_color)
output_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

output_label = tk.Label(output_frame, text="Sortie X :", font=font, bg=bg_color, fg=label_color)
output_label.grid(row=0, column=0, sticky="w")

output_text = tk.Text(output_frame, font=font, bg=output_bg_color, fg=output_fg_color, width=30, height=10)
output_text.grid(row=1, column=0, pady=5)

# Lancement de la boucle principale
window.mainloop()
