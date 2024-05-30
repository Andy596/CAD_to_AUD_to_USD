import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.cad_to_usd = 0.73
        self.cad_to_aud = 1.1
        self.usd_to_cad = 1 / self.cad_to_usd
        self.aud_to_cad = 1 / self.cad_to_aud

        self.create_widgets()

    def create_widgets(self):
        self.amount_label = ttk.Label(self.root, text="Amount:")
        self.amount_label.grid(column=0, row=0, padx=10, pady=10)

        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.grid(column=1, row=0, padx=10, pady=10)
        self.amount_entry.bind('<KeyRelease>', self.convert_currency)

        self.currency_var = tk.StringVar(value="CAD")
        self.currency_combobox = ttk.Combobox(self.root, textvariable=self.currency_var)
        self.currency_combobox['values'] = ('USD', 'CAD', 'AUD')
        self.currency_combobox.grid(column=2, row=0, padx=10, pady=10)
        self.currency_combobox.bind('<<ComboboxSelected>>', self.convert_currency)

        self.usd_label = ttk.Label(self.root, text="USD:")
        self.usd_label.grid(column=0, row=1, padx=10, pady=10)
        self.usd_result = ttk.Label(self.root, text="0.00")
        self.usd_result.grid(column=1, row=1, padx=10, pady=10)

        self.cad_label = ttk.Label(self.root, text="CAD:")
        self.cad_label.grid(column=0, row=2, padx=10, pady=10)
        self.cad_result = ttk.Label(self.root, text="0.00")
        self.cad_result.grid(column=1, row=2, padx=10, pady=10)

        self.aud_label = ttk.Label(self.root, text="AUD:")
        self.aud_label.grid(column=0, row=3, padx=10, pady=10)
        self.aud_result = ttk.Label(self.root, text="0.00")
        self.aud_result.grid(column=1, row=3, padx=10, pady=10)

    def convert_currency(self, event=None):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.currency_var.get()

            if from_currency == "CAD":
                usd_amount = amount * self.cad_to_usd
                aud_amount = amount * self.cad_to_aud
                cad_amount = amount
            elif from_currency == "USD":
                cad_amount = amount * self.usd_to_cad
                aud_amount = cad_amount * self.cad_to_aud
                usd_amount = amount
            elif from_currency == "AUD":
                cad_amount = amount * self.aud_to_cad
                usd_amount = cad_amount * self.cad_to_usd
                aud_amount = amount
            else:
                usd_amount = 0
                cad_amount = 0
                aud_amount = 0

            self.usd_result.config(text=f"{usd_amount:.2f}")
            self.cad_result.config(text=f"{cad_amount:.2f}")
            self.aud_result.config(text=f"{aud_amount:.2f}")

        except ValueError:
            self.usd_result.config(text="0.00")
            self.cad_result.config(text="0.00")
            self.aud_result.config(text="0.00")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
