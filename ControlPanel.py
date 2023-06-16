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
        self.title("Panel kontrolny inteligentnego domu")

        self.factory_settings_button = tk.Button(self, text="1) Ustawienia fabryczne",
                                                 command=self.apply_factory_settings)
        self.factory_settings_button.pack()

        self.ml_process_button = tk.Button(self, text="2) Zacznij 4-tygodniowy proces uczenia maszynowego",
                                           command=self.start_ml_process)
        self.ml_process_button.pack()

        self.alarm_phone_button = tk.Button(self, text="3) Włącz / wyłącz telefony alarmowe",
                                            command=self.toggle_alarm_phones)
        self.alarm_phone_button.pack()

        self.add_to_routine_button = tk.Button(self, text="4) Dodaj coś ręcznie do rutyny", command=self.add_to_routine)
        self.add_to_routine_button.pack()

        self.hamster_status = tk.Button(self, text="5) Status chomika", command=self.hamster_status)
        self.hamster_status.pack()

        self.close_button = tk.Button(self, text="6) Zamknij opcje", command=self.close_panel)
        self.close_button.pack()

        self.ml_process_running = False
        self.alarm_telephones = False

        self.last_hamster_status = {
            "status": "żywy",
            "power_usage": 25,
            "feeding_status": "ok"
        }

    def apply_factory_settings(self):
        result = messagebox.askyesno("Uwaga", "Czy na pewno chcesz zastosować ustawienia fabryczne?")
        if result:
            # Implementacja logiki dla ustawień fabrycznych
            messagebox.showinfo("Informacja", "Ustawienia fabryczne zostały zastosowane.")

    def start_ml_process(self):
        def format_time_remaining(seconds):
            days = seconds // (24 * 3600)
            hours = (seconds % (24 * 3600)) // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            formatted_time = f"{days} dni, {hours:02d} godzin, {minutes:02d} minut, {seconds:02d} sekund"
            return formatted_time

        # Implementacja logiki dla procesu uczenia maszynowego
        # Sprawdź, czy proces już wystartował i określ ile czasu zostało do końca
        if self.ml_process_running:
            messagebox.showinfo("Informacja", "Proces uczenia maszynowego już trwa.")
            # Oblicz pozostały czas i pokaż użytkownikowi
            time_remaining = ml_process.get_time_remaining()
            formatted_time = format_time_remaining(time_remaining)
            messagebox.showinfo("Informacja", f"Pozostały czas do zakończenia procesu uczenia maszynowego:" 
                                              f" {formatted_time}.")
        else:
            # Rozpocznij proces uczenia maszynowego
            result = messagebox.askyesno("Uwaga", "Czy na pewno chcesz rozpocząć uczenie maszynowe? (Proces potrwa 4 "
                                                  "tygodnie)")
            if result:
                messagebox.showinfo("Informacja", "Proces uczenia maszynowego został rozpoczęty.")
                ml_process.start()
                self.ml_process_running = True

    def toggle_alarm_phones(self):
        if self.alarm_telephones:
            self.alarm_telephones = False
            messagebox.showinfo("Telefony Alarmowe", "Wyłączono telefony alarmowe")
        else:
            self.alarm_telephones = True
            messagebox.showinfo("Telefony Alarmowe", "Włączono telefony alarmowe")
        # Implementacja logiki dla włączania/wyłączania telefonów alarmowych
        # Zmień stan telefonów alarmowych i zaktualizuj interfejs użytkownika
        pass

    def add_to_routine(self):
        # Implementacja logiki dla dodawania czynności do rutyny

        dostepne_czynnosci = ["kawa", "budzik", "światła"]
        dostepne_dni_tygodnia = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]

        while True:
            czynnosc = simpledialog.askstring("Dodaj czynność", "Wprowadź nazwę czynności:")

            if czynnosc is None:
                # Użytkownik kliknął Anuluj, zakończ funkcję bez dodawania czynności
                return

            if czynnosc.lower() in dostepne_czynnosci:
                # Wprowadzona czynność jest poprawna, można ją dodać do rutyny
                break
            else:
                messagebox.showwarning("Błąd", "Wprowadzona czynność jest nieprawidłowa. Proszę spróbować ponownie.")

        while True:
            dzien_tygodnia = simpledialog.askstring("Dodaj czynność", "Wprowadź dzień tygodnia:")

            if dzien_tygodnia is None:
                # Użytkownik kliknął Anuluj, zakończ funkcję bez dodawania czynności
                return

            if dzien_tygodnia.lower() in dostepne_dni_tygodnia:
                # Wprowadzony dzień tygodnia jest poprawny, można kontynuować
                break
            else:
                messagebox.showwarning("Błąd",
                                       "Wprowadzony dzień tygodnia jest nieprawidłowy. Proszę spróbować ponownie.")

        while True:
            godzina = simpledialog.askstring("Dodaj czynność", "Wprowadź godzinę (format HH:MM):")

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
                    messagebox.showwarning("Błąd", "Wprowadzona godzina jest nieprawidłowa. Proszę spróbować ponownie.")
            else:
                messagebox.showwarning("Błąd", "Wprowadzona godzina jest nieprawidłowa. Proszę spróbować ponownie.")

        # Tutaj można wykorzystać pobrane wartości i zaimplementować logikę dodawania czynności do rutyny

        print("Dodano czynność do rutyny:")
        print("Czynność:", czynnosc)
        print("Dzień tygodnia:", dzien_tygodnia)
        print("Godzina:", godzina)

    def hamster_status(self):
        status_chomika = self.last_hamster_status["status"]
        pobor_mocy = self.last_hamster_status["power_usage"]
        status_wyzywienia = self.last_hamster_status["feeding_status"]

        if status_chomika == "martwy":
            messagebox.showinfo("Status chomika", "Chomik jest martwy.")
            return

        if status_wyzywienia != "N/A":
            if status_wyzywienia == "przekarmiony":
                if random.random() < 0.05:
                    status_wyzywienia = "najedzony"
            elif status_wyzywienia == "niedożywiony":
                if random.random() < 0.05:
                    status_wyzywienia = "najedzony"
            else:  # status_wyzywienia == "najedzony"
                if random.random() < 0.05:
                    losowa_wartosc = random.randint(0, 1)
                    if losowa_wartosc == 0:
                        status_wyzywienia = "niedożywiony"
                    else:
                        status_wyzywienia = "przekarmiony"

        zmiana_mocy = random.randint(-10, 10)
        pobor_mocy = max(0, min(100, pobor_mocy + zmiana_mocy))

        if status_chomika == "żywy":
            if random.random() < 0.01:
                status_chomika = "martwy"

        if status_chomika == "martwy":
            status_wyzywienia = "N/A"
            pobor_mocy = "N/A"

        messagebox.showinfo("Status chomika",
                            f"Status chomika: {status_chomika}\n"
                            f"Pobór mocy: {pobor_mocy}\n"
                            f"Status wyżywienia: {status_wyzywienia}")

        self.last_hamster_status["status"] = status_chomika
        self.last_hamster_status["power_usage"] = pobor_mocy
        self.last_hamster_status["feeding_status"] = status_wyzywienia

    def close_panel(self):
        self.destroy()


if __name__ == "__main__":
    app = SmartHomeControlPanel()
    app.mainloop()
