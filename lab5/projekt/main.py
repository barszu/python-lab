import time
import triangle_game
import tkinter as tk
from threading import Thread
import Options

def main():
    root = tk.Tk()
    root.title("Aplikacja z grą")
    root.geometry("900x720")

    # Ustaw tło na ciemnoszare
    root.configure(bg='darkgrey')

    # Dodaj padding do okna głównego
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    # Stylizuj etykietę powitalną
    welcome_label = tk.Label(root, text="Witaj w mojej grze!", font=("Helvetica", 18), bg='darkgrey', fg='white')
    welcome_label.pack(pady=10)

    # Stylizuj etykietę z informacją o grze
    game_rules_label = tk.Label(root, text=Options.rules_label_text, font=("Helvetica", 14), bg='darkgrey', fg='white')
    game_rules_label.pack(pady=20)

    slider_label1 = tk.Label(root, text="Wybierz rozmiar planszy:", font=("Helvetica", 12), bg='darkgrey', fg='white')
    slider_label1.pack(pady=10)

    slider1 = tk.Scale(root, from_=3, to=7, orient=tk.HORIZONTAL, length=200, font=("Helvetica", 12))
    slider1.pack()

    slider_label2 = tk.Label(root, text="Wybierz ilosc kolorow:", font=("Helvetica", 12), bg='darkgrey', fg='white')
    slider_label2.pack(pady=10)

    slider2 = tk.Scale(root, from_=2, to=len(Options.colours), orient=tk.HORIZONTAL, length=200, font=("Helvetica", 12))
    slider2.pack()

    slider_label3 = tk.Label(root, text="Wybierz ilosc poczatkowych ruchow komputera:", font=("Helvetica", 12), bg='darkgrey', fg='white')
    slider_label3.pack(pady=10)

    slider3 = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, length=200, font=("Helvetica", 12))
    slider3.pack()

    start_button_label = tk.Label(root, text="Kliknij przycisk, aby rozpocząć grę z trojkatami", font=("Helvetica", 14), bg='darkgrey', fg='white')
    start_button_label.pack(pady=10)

    start_button = tk.Button(root, text="Uruchom grę", bg='green', fg='white', font=("Helvetica", 14), padx=10, pady=10)
    start_button.pack()

    is_game_running = False

    def start_game():
        nonlocal start_button, is_game_running
        is_game_running = True
        params = {
            'size': int(slider1.get()),
            'colors_no': int(slider2.get()),
            'shuffle_moves_no': int(slider3.get())
        }
        triangle_game.main(params)
        start_button.config(state='normal')  # Włącz przycisk z powrotem
        is_game_running = False

    def on_bttn_clicked():
        nonlocal start_button
        start_button.config(state='disabled')


        if not is_game_running:
            Thread(target=start_game).start()
        else:
            print('Gra już trwa!')


    start_button.config(command=on_bttn_clicked)  # Przypisz funkcję start_game do przycisku

    root.mainloop()


if __name__ == "__main__":
    main()



