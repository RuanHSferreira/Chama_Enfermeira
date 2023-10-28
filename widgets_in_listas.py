from ttkbootstrap import ttk, Window
from PIL import Image, ImageTk
import os
from tkinter.font import Font


class Main:

    def __init__(self) -> None:
        self.root = Window()
        self.root.geometry("800x800")
        self.pasta = os.path.dirname(__file__)
        self.my_font = Font(size=50)

        self.carre_img()

        self.wid_dic = {}
        self.imgs_dic = {}
        self.frames_dict = {}
        
        # self.btn_frame()
        self.creat_fr(4, 2)
        # self.creat_fr(8, 3)

        self.root.mainloop()

    def creat_fr(self, lb_quant, num_colunas):

        frame_name = f"Enfermaria {len(self.frames_dict)+1}"
        self.frames_dict[frame_name] = [ttk.Frame(self.root, borderwidth=2, relief='raised')]
        self.frames_dict[frame_name][0].grid(padx=10)

        print(self.frames_dict)

        linha = 0
        for i in range(0, lb_quant):

            print(f"{i%num_colunas}")
            if i != 0 and i%num_colunas == 0:
                linha += 1

            # Eu incurtei a codigo mais aqui seria uma imagem mas tu pode tirar esse image=self.cama_img e passar um text
            self.imgs_dic[f"img 0{str(i+1)}"] = ttk.Label(self.frames_dict[frame_name][0], image=self.cama_img)
            self.imgs_dic[f"img 0{str(i+1)}"].grid(row=i//num_colunas+linha, column=i%num_colunas, padx=15, pady=15)

            self.wid_dic[f"Leito 0{str(i+1)}"] = ttk.Label(self.frames_dict[frame_name][0], text=f"Leito 0{str(i+1)}", font=30)
            self.wid_dic[f"Leito 0{str(i+1)}"].grid(row=i//num_colunas+linha+1, column=i%num_colunas, padx=15, pady=15)

        lb = {f"Label {frame_name}": ttk.Label(self.frames_dict[frame_name][0], text=str(frame_name), font=self.my_font)}
        self.frames_dict[frame_name].append(dict(lb))
        print(self.frames_dict[frame_name])
        self.frames_dict[frame_name][1][f"Label {frame_name}"].grid(columnspan=9)

        del linha

    def carre_img(self):

        self.cama_img = Image.open(self.pasta+'/imgs/maca2.png').resize((150, 150), resample=3)
        self.cama_img = ImageTk.PhotoImage(self.cama_img)

        self.cama_img_vermelha = Image.open(self.pasta+'/imgs/maca.png')
        self.cama_tam_1 = self.cama_img_vermelha.resize((150, 150), resample=3)
        self.cama_tam_2 = self.cama_img_vermelha.resize((160, 160), resample=3)
        self.cama_img_vermelha = ImageTk.PhotoImage(self.cama_tam_1)

        self.cruz = Image.open(self.pasta+'/imgs/cruz.png').resize((25, 25), resample=3)
        self.cruz = ImageTk.PhotoImage(self.cruz)

    # def btn_frame(self):
    #     self.add_leito_btn = ttk.Button(self.root, text="Adicionar", command=self.add_leito)
    #     self.add_leito_btn.grid()

    #     self.codigo_dell = ttk.Entry(self.root, width=100)
    #     self.codigo_dell.grid()

    #     self.dell_leito_btn = ttk.Button(self.root, text='Apagar Leito', command=self.dell_leito)
    #     self.dell_leito_btn.grid()

    # def add_leito(self):
    #     self._quant_leito = len(self.widgets)
    #     self.widgets.append(ttk.Label(self.fr1, text=f"Leito {str(self._quant_leito)}"))
    #     self.widgets[self._quant_leito].grid()

    # def dell_leito(self):
    #     cod = int(self.codigo_dell.get())
    #     self.widgets[cod].destroy()
    #     self.widgets.pop(cod)


Main()
