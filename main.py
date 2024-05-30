import tkinter as tk
from tkinter import ttk


class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Conversion rates
        self.cad_to_usd = 0.73
        self.cad_to_aud = 1.1

        self.amount_label = ttk.Label(root, text="Amount in CAD:")
        self.amount_label.grid(column=0, row=0, padx=10, pady=10)

        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(column=1, row=0, padx=10, pady=10)

        self.convert_to_label = ttk.Label(root, text="Convert to:")
        self.convert_to_label.grid(column=0, row=1, padx=10, pady=10)

        self.currency_var = tk.StringVar(value="USD")
        self.convert_to_combobox = ttk.Combobox(root, textvariable=self.currency_var)
        self.convert_to_combobox['values'] = ('USD', 'AUD')
        self.convert_to_combobox.grid(column=1, row=1, padx=10, pady=10)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def convert_currency(self):
        try:
            amount_cad = float(self.amount_entry.get())
            target_currency = self.currency_var.get()

            if target_currency == "USD":
                converted_amount = amount_cad * self.cad_to_usd
                result_text = f"{amount_cad} CAD = {converted_amount:.2f} USD"
            elif target_currency == "AUD":
                converted_amount = amount_cad * self.cad_to_aud
                result_text = f"{amount_cad} CAD = {converted_amount:.2f} AUD"
            else:
                result_text = "Invalid currency selected"

            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="Please enter a valid amount")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
