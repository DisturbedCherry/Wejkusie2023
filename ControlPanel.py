import tkinter as tk
from tkinter import messagebox
from datetime import datetime


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

        self.close_button = tk.Button(self, text="5) Zamknij opcje", command=self.close_panel)
        self.close_button.pack()

        self.ml_process_running = False
        self.alarm_telephones = False

    def apply_factory_settings(self):
        result = messagebox.askyesno("Uwaga", "Czy na pewno chcesz zastosować ustawienia fabryczne?")
        if result:
            # Implementacja logiki dla ustawień fabrycznych
            messagebox.showinfo("Informacja", "Ustawienia fabryczne zostały zastosowane.")

    def start_ml_process(self):
        # Implementacja logiki dla procesu uczenia maszynowego
        # Sprawdź, czy proces już wystartował i określ ile czasu zostało do końca
        if self.ml_process_running:
            messagebox.showinfo("Informacja", "Proces uczenia maszynowego już trwa.")
            # Oblicz pozostały czas i pokaż użytkownikowi
        else:
            # Rozpocznij proces uczenia maszynowego
            messagebox.showinfo("Informacja", "Proces uczenia maszynowego został rozpoczęty.")

    def toggle_alarm_phones(self):
        if self.alarm_telephones:
            self.alarm_telephones = False
        else:
            self.alarm_telephones = True
        # Implementacja logiki dla włączania/wyłączania telefonów alarmowych
        # Zmień stan telefonów alarmowych i zaktualizuj interfejs użytkownika
        pass

    def add_to_routine(self):
        # Implementacja logiki dla dodawania czynności do rutyny
        # Pobierz nazwę urządzenia / czynności, dzień tygodnia i godzinę od użytkownika
        # Dodaj czynność do rutyny i zaktualizuj interfejs użytkownika
        pass

    def close_panel(self):
        self.destroy()


if __name__ == "__main__":
    app = SmartHomeControlPanel()
    app.mainloop()
