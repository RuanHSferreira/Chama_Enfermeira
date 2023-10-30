from ttkbootstrap import Window, Label, ttk
from serial_python import serialApp
from threading import Thread as thread
from PIL import Image, ImageTk
import os
from tkinter.font import Font


class WidgetsFuncResp(object):

    def func_pisca1(self, leito_press, atv):

        serial_respost = int(self.resposta.decode().replace('\n', ''))
        print(leito_press)
        if str(leito_press) == '.!frame.!label' and serial_respost == 11:

            leito_press['image'] = self.cama_img
            self.add_cr.grid_forget()

        elif str(leito_press) == '.!frame.!label4' and serial_respost == 22:

            leito_press['image'] = self.cama_img

        elif str(leito_press) == '.!frame.!label6' and serial_respost == 33:
            
            leito_press['image'] = self.cama_img

        elif str(leito_press) == '.!frame.!label8' and serial_respost == 44:
            
            leito_press['image'] = self.cama_img

        else:

            if atv == 1:

                leito_press['image'] = self.cama_img
                self.add_cr.grid_forget()
                leito_press.after(500, self.func_pisca1, leito_press, 0)

            else:

                leito_press['image'] = self.cama_img_vermelha
                self.add_cr.grid(row=0, rowspan=2, sticky='S', pady=50)
                leito_press.after(500, self.func_pisca1, leito_press, 1)


class WidgetsTk(object):

    def enfermaria_1_frame(self):

        self.myimg = Label(self.fr1, image=self.cama_img)
        self.myimg.grid(padx=15, pady=15)
        self.label1 = Label(self.fr1, text='Leito 1', font=30)
        self.label1.grid(padx=15, pady=15)

        print(self.label1.winfo_class())

        self.add_cr = Label(self.fr1, image=self.cruz)
        self.add_cr.grid(row=0, rowspan=2, sticky='S', pady=50)
        self.add_cr.grid_forget()

        self.myimg2 = Label(self.fr1, image=self.cama_img)
        self.myimg2.grid(padx=15, pady=15, row=0, column=1)
        self.label2 = Label(self.fr1, text='Leito 2', font=30)
        self.label2.grid(padx=15, pady=15, row=1, column=1)

        self.myimg3 = Label(self.fr1, image=self.cama_img)
        self.myimg3.grid(padx=15, pady=15)
        self.label3 = Label(self.fr1, text='Leito 3', font=30)
        self.label3.grid(padx=15, pady=15)

        self.myimg4 = Label(self.fr1, image=self.cama_img)
        self.myimg4.grid(padx=15, pady=15, row=2, column=1)
        self.label4 = Label(self.fr1, text='Leito 4', font=30)
        self.label4.grid(padx=15, pady=15, row=3, column=1)

        self.enfer_title = Label(self.fr1, text="Enfermaria 01", font=self.my_font)
        self.enfer_title.grid(columnspan=9)

    def enfermaria_2_frame(self):

        self.myimg_fr2 = Label(self.fr2, image=self.cama_img)
        self.myimg_fr2.grid(padx=15, pady=15)
        self.label1_fr2 = Label(self.fr2, text='Leito 1', font=30)
        self.label1_fr2.grid(padx=15, pady=15)

        self.myimg2_fr2 = Label(self.fr2, image=self.cama_img)
        self.myimg2_fr2.grid(padx=15, pady=15, row=0, column=1)
        self.label2_fr2 = Label(self.fr2, text='Leito 2', font=30)
        self.label2_fr2.grid(padx=15, pady=15, row=1, column=1)

        self.myimg3_fr2 = Label(self.fr2, image=self.cama_img)
        self.myimg3_fr2.grid(padx=15, pady=15)
        self.label3_fr2 = Label(self.fr2, text='Leito 3', font=30)
        self.label3_fr2.grid(padx=15, pady=15)

        self.myimg4_fr2 = Label(self.fr2, image=self.cama_img)
        self.myimg4_fr2.grid(padx=15, pady=15, row=2, column=1)
        self.label4_fr2 = Label(self.fr2, text='Leito 4', font=30)
        self.label4_fr2.grid(padx=15, pady=15, row=3, column=1)


        self.enfer_title = Label(self.fr2, text="Enfermaria 02", font=self.my_font)
        self.enfer_title.grid(columnspan=9)

    def efermmaria_3_frame(self):

        self.myimg_fr2 = Label(self.fr2, image=self.cama_img)
        self.myimg_fr2.grid(padx=15, pady=15)
        self.label1_fr2 = Label(self.fr2, text='Leito 1', font=30)
        self.label1_fr2.grid(padx=15, pady=15)

        self.myimg2_fr2 = Label(self.fr2, image=self.cama_img)
        self.myimg2_fr2.grid(padx=15, pady=15, row=0, column=1)
        self.label2_fr2 = Label(self.fr2, text='Leito 2', font=30)
        self.label2_fr2.grid(padx=15, pady=15, row=1, column=1)

        self.myimg3_fr2 = Label(self.fr2, image=self.cama_img)
        self.myimg3_fr2.grid(padx=15, pady=15, row=0, column=2)
        self.label3_fr2 = Label(self.fr2, text='Leito 3', font=30)
        self.label3_fr2.grid(padx=15, pady=15, row=1, column=2)

        self.myimg4_fr2 = Label(self.fr2, image=self.cama_img)
        self.myimg4_fr2.grid(padx=15, pady=15, row=0, column=3)
        self.label4_fr2 = Label(self.fr2, text='Leito 4', font=30)
        self.label4_fr2.grid(padx=15, pady=15, row=1, column=3)


class Main(WidgetsTk, WidgetsFuncResp):

    def __init__(self) -> None:

        self.root = Window()
        self.configs()
        self.carre_img()
        self.enfermaria_1_frame()
        self.enfermaria_2_frame()
        
        self.connect_serial()
        self.root.mainloop()

    def configs(self):

        self.pasta = os.path.dirname(__file__)
        self.root.geometry("1920x1080")
        self.root.title("Chama Enfermeira")
        self.desliga_list = [11, 22, 33, 44]

        self.my_font = Font(size=50)

        self.fr1 = ttk.Frame(self.root, borderwidth=2, relief='raised')
        self.fr1.grid(padx=10)

        self.fr2 = ttk.Frame(self.root, borderwidth=2, relief='raised')
        self.fr2.grid(padx=10, row=0, column=1)

    def carre_img(self):

        self.cama_img = Image.open(self.pasta+'/imgs/maca2.png').resize((150, 150), resample=3)
        self.cama_img = ImageTk.PhotoImage(self.cama_img)

        self.cama_img_vermelha = Image.open(self.pasta+'/imgs/maca.png')
        self.cama_tam_1 = self.cama_img_vermelha.resize((150, 150), resample=3)
        self.cama_tam_2 = self.cama_img_vermelha.resize((160, 160), resample=3)
        self.cama_img_vermelha = ImageTk.PhotoImage(self.cama_tam_1)

        self.cruz = Image.open(self.pasta+'/imgs/cruz.png').resize((25, 25), resample=3)
        self.cruz = ImageTk.PhotoImage(self.cruz)

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
            if self.resposta.decode().replace('\n', '') == '1':
                
                self.myimg.after(500, self.func_pisca1, self.myimg, 0)

            elif self.resposta.decode().replace('\n', '') == '2':
                
                self.myimg2.after(500, self.func_pisca1, self.myimg2, 0)

            elif self.resposta.decode().replace('\n', '') == '3':
                
                self.myimg2.after(500, self.func_pisca1, self.myimg3, 0)

            elif self.resposta.decode().replace('\n', '') == '4':
                
                self.myimg2.after(500, self.func_pisca1, self.myimg4, 0)

    def on_th(self):
        self.servidor = thread(target=self.recv_serial, daemon=True)
        self.servidor.start()


Main()
