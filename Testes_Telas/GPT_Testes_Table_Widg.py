import tkinter as tk
from tkinter import ttk


class InicialConfigs:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Tabela de Quantidade de Leitos")

        # Frame para conter a entrada, botões e Treeview
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10, anchor="w")

        # Entrada para inserir o nome da enfermaria
        self.entry_name = ttk.Entry(self.input_frame)
        self.entry_name.grid(row=0, column=0, padx=5, pady=5)

        # Botão para adicionar o item à Treeview
        self.add_button = ttk.Button(self.input_frame, text="Adicionar", command=self.add_row)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Treeview para exibir os dados
        self.tree = ttk.Treeview(self.root, columns=("Quantity"))
        self.tree.heading('#0', text='Nome')
        self.tree.heading('#1', text='Quantidade de Leitos')

        self.tree.column('#0', width=150, stretch=tk.YES)
        self.tree.column('#1', width=150, stretch=tk.YES)

        self.tree.pack(padx=10, pady=10)

        # Entrada para alterar a quantidade de leitos
        self.quantity_entry = ttk.Entry(self.root)
        self.quantity_entry.pack(padx=10, pady=5)

        # Botão para atualizar a quantidade de leitos
        self.update_button = ttk.Button(self.root, text="Atualizar Quantidade", command=self.update_quantity)
        self.update_button.pack(pady=10)

        # Botão para excluir a linha selecionada
        self.delete_button = ttk.Button(self.root, text="Excluir", command=self.delete_row)
        self.delete_button.pack(pady=5)

        self.salvar = ttk.Button(self.root, text='Salvar')
        self.salvar.pack(side='right')

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.root.mainloop()

    def add_row(self):
        name = self.entry_name.get()
        quantity = "0"  # Valor padrão
        self.tree.insert('', 'end', text=name, values=(quantity,))

    def on_select(self, event):
        selected_item = self.tree.focus()
        item_values = self.tree.item(selected_item, 'values')
        if item_values:
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, item_values[0])

    def update_quantity(self):
        selected_item = self.tree.focus()
        new_quantity = self.quantity_entry.get()
        self.tree.item(selected_item, values=(new_quantity,))

    def delete_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)

