from ttkbootstrap import Window, Label, ttk
from serial_python import serialApp
from threading import Thread as thread
from PIL import Image, ImageTk
import os
from tkinter.font import Font


class WidgetsFuncResp(object):

    def func_pisca1(self, leito_press, atv):

        serial_respost = str(self.resposta.decode().replace('\n', ''))

        if serial_respost == leito_press['stop']:

            leito_press['OBJ']['image'] = self.cama_img

        else:

            if atv == 1:

                leito_press['OBJ']['image'] = self.cama_img
                leito_press['OBJ'].after(500, self.func_pisca1, leito_press, 0)

            else:

                leito_press['OBJ']['image'] = self.cama_verm
                leito_press['OBJ'].after(500, self.func_pisca1, leito_press, 1)


class WidgetsTk(object):

    def creat_fr(self, lb_quant, num_colunas, index_column=0, index_line=0):

        frame_name = f"Enfermaria {len(self.frames_dict)+1}"
        self.frames_dict[frame_name] = [ttk.Frame(self.root, borderwidth=2, relief='raised')]
        if index_column > 0 or index_line > 0:
            self.frames_dict[frame_name][0].grid(padx=10, column=index_column, row=index_line)
        else:
            self.frames_dict[frame_name][0].grid(padx=10)

        self.imgs_dic[f"{frame_name}"] = {}
        self.times_cron[f"{frame_name}"] = {}
        self.wid_dic[f"{frame_name}"] = {}

        linha = 0
        for i in range(0, lb_quant):

            if i != 0 and i%num_colunas == 0:
                # Conforme a quantidade de widgets que tiver aumentar o numero!
                linha += 2

            #print(str(f"{len(self.frames_dict)}{i+1}1"))

            # Eu incurtei a codigo mais aqui seria uma imagem mas tu pode tirar esse image=self.cama_img e passar um text
            self.imgs_dic[f"{frame_name}"][f"img 0{str(i+1)}"] = {"OBJ": ttk.Label(self.frames_dict[frame_name][0], image=self.cama_img), "start": str(f"{len(self.frames_dict)}{i+1}1"), "stop": str(f"{len(self.frames_dict)}{i+1}2")}
            self.imgs_dic[f"{frame_name}"][f"img 0{str(i+1)}"]["OBJ"].grid(row=i//num_colunas+linha, column=i%num_colunas, padx=15, pady=5)

            self.times_cron[f"{frame_name}"][f"Leito 0{str(i+1)}"] = ttk.Label(self.frames_dict[frame_name][0], text="00:00", font=Font(size=20), foreground='red')
            self.times_cron[f"{frame_name}"][f"Leito 0{str(i+1)}"].grid(row=i//num_colunas+linha+1, column=i%num_colunas)

            self.wid_dic[f"{frame_name}"][f"Leito 0{str(i+1)}"] = ttk.Label(self.frames_dict[frame_name][0], text=f"Leito 0{str(i+1)}", font=Font(size=10))
            self.wid_dic[f"{frame_name}"][f"Leito 0{str(i+1)}"].grid(row=i//num_colunas+linha+2, column=i%num_colunas, padx=15, pady=5)

        lb = {f"Label {frame_name}": ttk.Label(self.frames_dict[frame_name][0], text=str(frame_name), font=self.my_font)}
        self.frames_dict[frame_name].append(dict(lb))
        self.frames_dict[frame_name][1][f"Label {frame_name}"].grid(columnspan=9)

        del linha
        del lb


class Main(WidgetsTk, WidgetsFuncResp):

    def __init__(self) -> None:

        self.root = Window()
        self.configs()
        self.carre_img()

        self.times_cron = {}
        self.wid_dic = {}
        self.imgs_dic = {}
        self.frames_dict = {}

        self.creat_fr(4, 2)
        self.creat_fr(4, 2, 1)
        self.creat_fr(4, 2, 2)
        self.creat_fr(4, 2, 3)

        print(self.imgs_dic)

        self.connect_serial()
        self.root.mainloop()

    def configs(self):

        self.pasta = os.path.dirname(__file__)
        self.root.geometry("1920x1080")
        self.root.title("Chama Enfermeira")
        self.desliga_list = [11, 22, 33, 44]

        self.my_font = Font(size=20)

        # self.fr1 = ttk.Frame(self.root, borderwidth=2, relief='raised')
        # self.fr1.grid(padx=10)

        # self.fr2 = ttk.Frame(self.root, borderwidth=2, relief='raised')
        # self.fr2.grid(padx=10, row=0, column=1)

    def carre_img(self):

        self.cama_img = Image.open(self.pasta+'/imgs/maca2.png').resize((70, 70), resample=3)
        self.cama_img = ImageTk.PhotoImage(self.cama_img)

        self.cama_verm = Image.open(self.pasta+'/imgs/maca.png').resize((70, 70), resample=3)
        self.cama_verm = ImageTk.PhotoImage(self.cama_verm)

    def connect_serial(self):
        self.ser = serialApp()
        self.ser.updatePort()
        self.ser.serialPort.port = 'COM2'
        self.ser.serialPort.baudrate = 9600
        self.ser.connectSerial()
        self.on_th()

    def recv_serial(self):

        while True:

            self.resposta = self.ser.readSerial()
            self._rsp = self.resposta.decode().replace('\n', '')

            if self._rsp == self.imgs_dic.get(f"Enfermaria {self._rsp[0]}").get(f"img 0{self._rsp[1]}").get("start"):
                    self._obj_img = self.imgs_dic.get(f"Enfermaria {self._rsp[0]}").get(f"img 0{self._rsp[1]}").get("OBJ")
                    self._obj_img.after(500, self.func_pisca1, self.imgs_dic.get(f"Enfermaria {self._rsp[0]}").get(f"img 0{self._rsp[1]}"), 0)

            # if self._rsp == '1':
                
            #     # self.myimg.after(500, self.func_pisca1, self.myimg, 0)
            #     self._obj_img = self.imgs_dic.get(f"Enfermaria {self._rsp}").get(f"img 0{self._rsp}")
            #     self._obj_img.after(500, self.func_pisca1, self._obj_img, 0)

            # elif self.resposta.decode().replace('\n', '') == '2':
                
            #     self.myimg2.after(500, self.func_pisca1, self.myimg2, 0)

            # elif self.resposta.decode().replace('\n', '') == '3':
                
            #     self.myimg2.after(500, self.func_pisca1, self.myimg3, 0)

            # elif self.resposta.decode().replace('\n', '') == '4':
                
            #     self.myimg2.after(500, self.func_pisca1, self.myimg4, 0)

    def on_th(self):
        self.servidor = thread(target=self.recv_serial, daemon=True)
        self.servidor.start()


Main()
