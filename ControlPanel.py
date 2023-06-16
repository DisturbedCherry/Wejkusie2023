import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime
import re
import random


class MachineLearningProcess:
    def __init__(self):
        self.process_start = None
        self.process_finish = 0

    def start(self):
        if self.process_start is None:
            self.process_start = datetime.now()
        else:
            print("Proces uczenia maszynowego już został uruchomiony.")

    def get_time_remaining(self):
        if self.process_start is not None:
            time_elapsed = datetime.now() - self.process_start
            time_remaining = 4 * 7 * 24 * 60 * 60 - time_elapsed.total_seconds()
            return max(0, int(time_remaining))
        else:
            return 0

    def finish(self):
        if self.process_start is not None:
            self.process_finish = 1
            self.process_start = None
            print("Proces uczenia maszynowego został zakończony.")
        else:
            print("Proces uczenia maszynowego nie został jeszcze uruchomiony.")


# Przykład użycia klasy MachineLearningProcess

ml_process = MachineLearningProcess()

ml_process.start()  # Uruchamia proces uczenia maszynowego

time_remaining = ml_process.get_time_remaining()  # Pobiera pozostały czas w sekundach
print("Pozostały czas do zakończenia procesu uczenia maszynowego:", time_remaining, "sekund.")

ml_process.finish()  # Zakańcza proces uczenia maszynowego


class SmartHomeControlPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart home control panel")

        self.factory_settings_button = tk.Button(self, text="1) Factory settings",
                                                 command=self.apply_factory_settings)
        self.factory_settings_button.pack()

        self.ml_process_button = tk.Button(self, text="2) Start a 4-week machine learning process",
                                           command=self.start_ml_process)
        self.ml_process_button.pack()

        self.alarm_phone_button = tk.Button(self, text="3) Enable/disable emergency calls",
                                            command=self.toggle_alarm_phones)
        self.alarm_phone_button.pack()

        self.add_to_routine_button = tk.Button(self, text="4) Add something manually to your routine",
                                               command=self.add_to_routine)
        self.add_to_routine_button.pack()

        self.hamster_status = tk.Button(self, text="5) Hamster status", command=self.hamster_status)
        self.hamster_status.pack()

        self.close_button = tk.Button(self, text="6) Close the menu", command=self.close_panel)
        self.close_button.pack()

        self.ml_process_running = False
        self.alarm_telephones = False

        self.last_hamster_status = {
            "status": "alive",
            "power_usage": 25,
            "feeding_status": "ok"
        }

    def apply_factory_settings(self):
        result = messagebox.askyesno("Warning", "Are you sure you want to apply factory settings?")
        if result:
            # Implementacja logiki dla ustawień fabrycznych
            messagebox.showinfo("Info", "The factory settings have been applied.")

    def start_ml_process(self):
        def format_time_remaining(seconds):
            days = seconds // (24 * 3600)
            hours = (seconds % (24 * 3600)) // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            formatted_time = f"{days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds"
            return formatted_time

        # Implementacja logiki dla procesu uczenia maszynowego
        # Sprawdź, czy proces już wystartował i określ ile czasu zostało do końca
        if self.ml_process_running:
            messagebox.showinfo("Info", "The machine learning process is already underway.")
            # Oblicz pozostały czas i pokaż użytkownikowi
            time_remaining = ml_process.get_time_remaining()
            formatted_time = format_time_remaining(time_remaining)
            messagebox.showinfo("Info", f"Remaining time to complete the machine learning process:" 
                                              f" {formatted_time}.")
        else:
            # Rozpocznij proces uczenia maszynowego
            result = messagebox.askyesno("Warning", "Are you sure to start machine learning? (Proccess will last 4 "
                                                    "weeks)")
            if result:
                messagebox.showinfo("Info", "Machine learning started.")
                ml_process.start()
                self.ml_process_running = True

    def toggle_alarm_phones(self):
        if self.alarm_telephones:
            self.alarm_telephones = False
            messagebox.showinfo("Emergency numbers", "Turned off emergency calls")
        else:
            self.alarm_telephones = True
            messagebox.showinfo("Emergency numbers", "Turned on emergency calls")
        # Implementacja logiki dla włączania/wyłączania telefonów alarmowych
        # Zmień stan telefonów alarmowych i zaktualizuj interfejs użytkownika
        pass

    def add_to_routine(self):
        # Implementacja logiki dla dodawania czynności do rutyny

        dostepne_czynnosci = ["coffee", "alarm", "lights"]
        dostepne_dni_tygodnia = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        while True:
            czynnosc = simpledialog.askstring("Add routine", "Please add routine:")

            if czynnosc is None:
                # Użytkownik kliknął Anuluj, zakończ funkcję bez dodawania czynności
                return

            if czynnosc.lower() in dostepne_czynnosci:
                # Wprowadzona czynność jest poprawna, można ją dodać do rutyny
                break
            else:
                messagebox.showwarning("Error", "Incorrect action, please try again.")

        while True:
            dzien_tygodnia = simpledialog.askstring("Add routine", "Enter the day:")

            if dzien_tygodnia is None:
                # Użytkownik kliknął Anuluj, zakończ funkcję bez dodawania czynności
                return

            if dzien_tygodnia.lower() in dostepne_dni_tygodnia:
                # Wprowadzony dzień tygodnia jest poprawny, można kontynuować
                break
            else:
                messagebox.showwarning("Error",
                                       "Incorrect day, try again.")

        while True:
            godzina = simpledialog.askstring("Add to routine", "Enter the hour (format HH:MM):")

            if godzina is None:
                # Użytkownik kliknął Anuluj, zakończ funkcję bez dodawania czynności
                return

            if re.match(r'^\d{2}:\d{2}$', godzina):
                # Wprowadzona godzina jest w odpowiednim formacie
                godzina_split = godzina.split(":")
                hour = int(godzina_split[0])
                minute = int(godzina_split[1])

                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    # Wprowadzona godzina jest w prawidłowym zakresie
                    break
                else:
                    messagebox.showwarning("Error", "Incorrect time, try again.")
            else:
                messagebox.showwarning("Error", "Incorrect time, try again.")

        # Tutaj można wykorzystać pobrane wartości i zaimplementować logikę dodawania czynności do rutyny

        print("Adding to routine:")
        print("Action:", czynnosc)
        print("Day:", dzien_tygodnia)
        print("Hour:", godzina)

    def hamster_status(self):
        status_chomika = self.last_hamster_status["status"]
        pobor_mocy = self.last_hamster_status["power_usage"]
        status_wyzywienia = self.last_hamster_status["feeding_status"]

        if status_chomika == "martwy":
            messagebox.showinfo("Hamster status", "Hamster is dead.")
            return

        if status_wyzywienia != "N/A":
            if status_wyzywienia == "overfed":
                if random.random() < 0.05:
                    status_wyzywienia = "fed"
            elif status_wyzywienia == "starving":
                if random.random() < 0.05:
                    status_wyzywienia = "fed"
            else:  # status_wyzywienia == "najedzony"
                if random.random() < 0.05:
                    losowa_wartosc = random.randint(0, 1)
                    if losowa_wartosc == 0:
                        status_wyzywienia = "starving"
                    else:
                        status_wyzywienia = "overfed"

        if status_chomika == "alive":
            zmiana_mocy = random.randint(-10, 10)
        if status_chomika == "alive":
            pobor_mocy = max(0, min(100, pobor_mocy + zmiana_mocy))

        if status_chomika == "alive":
            if random.random() < 0.01:
                status_chomika = "dead"

        if status_chomika == "dead":
            status_wyzywienia = "N/A"
            pobor_mocy = "N/A"

        messagebox.showinfo("Hamster",
                            f"Hamster status: {status_chomika}\n"
                            f"Power usage: {pobor_mocy}\n"
                            f"Feed status: {status_wyzywienia}")

        self.last_hamster_status["status"] = status_chomika
        self.last_hamster_status["power_usage"] = pobor_mocy
        self.last_hamster_status["feeding_status"] = status_wyzywienia

    def close_panel(self):
        self.destroy()


if __name__ == "__main__":
    app = SmartHomeControlPanel()
    app.mainloop()
