import tkinter as tk
import psutil


class App:

    def __init__(self, root):

        self.root = root
        root.title("Check Charging App")
        root.geometry("300x100")
        self.check_button = tk.Button(root, text="Check charging", command=lambda:self.check_charging())
        self.check_button.pack()
        self.charging_text = tk.Label(root, text="button to check the battery status.")
        self.charging_text.pack()
        self.battery_percent = tk.Label(root, text="")
        self.battery_percent.pack()

    def check_charging(self):
        battery = psutil.sensors_battery()
        charging_status = "Charging" if battery.power_plugged else "Not charging"
        self.charging_text["text"] = charging_status
        self.battery_percent["text"] = str(battery.percent) + "%"


def main():
    root = tk.Tk()
    app = App(root)
    app.root.mainloop()


if __name__ == "__main__":
    main()