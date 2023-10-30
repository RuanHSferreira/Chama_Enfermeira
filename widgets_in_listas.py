from ttkbootstrap import ttk, Window
from PIL import Image, ImageTk
import os
from tkinter.font import Font


class Main:

    def __init__(self) -> None:
        self.root = Window()
        self.root.geometry("800x800")
        #self.root.state("zoomed")
        #self.root.attributes('-fullscreen', True)
        self.pasta = os.path.dirname(__file__)
        self.my_font = Font(size=20)

        self.carre_img()

        self.times_cron = {}
        self.wid_dic = {}
        self.imgs_dic = {}
        self.frames_dict = {}
        
        # self.btn_frame()
        self.creat_fr(4, 2)
        self.creat_fr(4, 2)

        self.root.mainloop()

    def creat_fr(self, lb_quant, num_colunas):

        frame_name = f"Enfermaria {len(self.frames_dict)+1}"
        self.frames_dict[frame_name] = [ttk.Frame(self.root, borderwidth=2, relief='raised')]
        self.frames_dict[frame_name][0].grid(padx=10)

        print(self.frames_dict)

        linha = 0
        for i in range(0, lb_quant):

            if i != 0 and i%num_colunas == 0:
                # Conforme a quantidade de widgets que tiver aumentar o numero!
                linha += 2

            # Eu incurtei a codigo mais aqui seria uma imagem mas tu pode tirar esse image=self.cama_img e passar um text
            self.imgs_dic[f"img 0{str(i+1)}"] = ttk.Label(self.frames_dict[frame_name][0], image=self.cama_img)
            self.imgs_dic[f"img 0{str(i+1)}"].grid(row=i//num_colunas+linha, column=i%num_colunas, padx=15, pady=5)

            self.times_cron[f"Leito 0{str(i+1)}"] = ttk.Label(self.frames_dict[frame_name][0], text="00:00", font=Font(size=20), foreground='red')
            self.times_cron[f"Leito 0{str(i+1)}"].grid(row=i//num_colunas+linha+1, column=i%num_colunas)

            self.wid_dic[f"Leito 0{str(i+1)}"] = ttk.Label(self.frames_dict[frame_name][0], text=f"Leito 0{str(i+1)}", font=Font(size=10))
            self.wid_dic[f"Leito 0{str(i+1)}"].grid(row=i//num_colunas+linha+2, column=i%num_colunas, padx=15, pady=5)

        lb = {f"Label {frame_name}": ttk.Label(self.frames_dict[frame_name][0], text=str(frame_name), font=self.my_font)}
        self.frames_dict[frame_name].append(dict(lb))
        self.frames_dict[frame_name][1][f"Label {frame_name}"].grid(columnspan=9)

        del linha
        del lb

    def carre_img(self):

        self.cama_img = Image.open(self.pasta+'/imgs/maca2.png').resize((70, 70), resample=3)
        self.cama_img = ImageTk.PhotoImage(self.cama_img)

        self.cama_img_vermelha = Image.open(self.pasta+'/imgs/maca.png')
        self.cama_tam_1 = self.cama_img_vermelha.resize((100, 100), resample=3)
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
