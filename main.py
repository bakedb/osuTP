import tkinter as tk
from tkinter import ttk
import math

def get_diff_name(stars: float) -> str:
    if 0.0 <= stars <= 1.99:
        return "Easy"
    elif 2.0 <= stars <= 2.69:
        return "Normal"
    elif 2.7 <= stars <= 3.99:
        return "Hard"
    elif 4.0 <= stars <= 5.29:
        return "Insane"
    elif 5.3 <= stars <= 6.49:
        return "Expert"
    elif stars >= 6.5:
        return "Expert+"
    else:
        return "Unknown"

def format_song():
    title = title_entry.get()
    artist = artist_entry.get()
    mode = mode_var.get()
    length = length_entry.get()
    
    try:
        stars = float(stars_entry.get())
        diff_name = get_diff_name(stars)
        diff_formatted = f"{diff_name} ({stars:.2f}★)"
    except ValueError:
        diff_formatted = "Invalid stars"
    
    formatted = f'{{ title: "{title}", artist: "{artist}", mode: "{mode}", diff: "{diff_formatted}", length: "{length}" }},'
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, formatted)

def calculate_score():
    try:
        acc = float(acc_entry.get())
        combo = int(combo_entry.get())
        max_combo = int(max_combo_entry.get())
        
        # Base formula
        score = ((0.8 * acc) * 100) + ((0.2 * math.sqrt(combo / max_combo)) * 100)
        
        # Apply mod multiplier
        mod = mod_var.get()
        multipliers = {
            "None": 1.0,
            "Easy (EZ)": 0.50,
            "Hard Rock (HR)": 1.12,
            "Hidden (HD)": 1.05,
            "Flashlight (FL)": 1.10
        }
        score *= multipliers.get(mod, 1.0)
        
        score_output.config(text=f"Score: {score:.2f}")
    except Exception as e:
        score_output.config(text=f"Error: {e}")

# Main window
root = tk.Tk()
root.title("osu! Formatter & Score Calculator")

# --- Section 1: Song Formatter ---
formatter_frame = ttk.LabelFrame(root, text="Song Formatter")
formatter_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(formatter_frame, text="Title:").grid(row=0, column=0, sticky="w")
title_entry = ttk.Entry(formatter_frame, width=30)
title_entry.grid(row=0, column=1)

ttk.Label(formatter_frame, text="Artist:").grid(row=1, column=0, sticky="w")
artist_entry = ttk.Entry(formatter_frame, width=30)
artist_entry.grid(row=1, column=1)

ttk.Label(formatter_frame, text="Mode:").grid(row=2, column=0, sticky="w")
mode_var = tk.StringVar(value="osu")
mode_menu = ttk.Combobox(formatter_frame, textvariable=mode_var, values=["osu", "taiko", "ctb", "mania"], state="readonly")
mode_menu.grid(row=2, column=1)

ttk.Label(formatter_frame, text="Stars:").grid(row=3, column=0, sticky="w")
stars_entry = ttk.Entry(formatter_frame, width=30)
stars_entry.grid(row=3, column=1)

ttk.Label(formatter_frame, text="Length:").grid(row=4, column=0, sticky="w")
length_entry = ttk.Entry(formatter_frame, width=30)
length_entry.grid(row=4, column=1)

format_button = ttk.Button(formatter_frame, text="Format", command=format_song)
format_button.grid(row=5, column=0, columnspan=2, pady=5)

output_text = tk.Text(formatter_frame, height=3, width=60)
output_text.grid(row=6, column=0, columnspan=2, pady=5)

# --- Section 2: Score Calculator ---
score_frame = ttk.LabelFrame(root, text="Score Calculator")
score_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(score_frame, text="Accuracy (to 4SF):").grid(row=0, column=0, sticky="w")
acc_entry = ttk.Entry(score_frame, width=15)
acc_entry.grid(row=0, column=1)

ttk.Label(score_frame, text="Combo:").grid(row=1, column=0, sticky="w")
combo_entry = ttk.Entry(score_frame, width=15)
combo_entry.grid(row=1, column=1)

ttk.Label(score_frame, text="Max Combo:").grid(row=2, column=0, sticky="w")
max_combo_entry = ttk.Entry(score_frame, width=15)
max_combo_entry.grid(row=2, column=1)

ttk.Label(score_frame, text="Mod:").grid(row=3, column=0, sticky="w")
mod_var = tk.StringVar(value="None")
mod_menu = ttk.Combobox(score_frame, textvariable=mod_var, values=["None", "Easy (EZ)", "Hard Rock (HR)", "Hidden (HD)", "Flashlight (FL)"], state="readonly")
mod_menu.grid(row=3, column=1)

calc_button = ttk.Button(score_frame, text="Calculate Score", command=calculate_score)
calc_button.grid(row=4, column=0, columnspan=2, pady=5)

score_output = ttk.Label(score_frame, text="Score: ")
score_output.grid(row=5, column=0, columnspan=2)

root.mainloop()
