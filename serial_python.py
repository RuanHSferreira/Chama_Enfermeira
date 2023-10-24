import serial
import serial.tools.list_ports


class serialApp():

    def __init__(self):
        self.serialPort = serial.Serial()
        print(self.serialPort.get_settings())
        self.baudrate = [9600, 115200]
        self.portlist = []

    def updatePort(self):
        self.portlist = [port.device for port in serial.tools.list_ports.comports()]
        print(self.portlist)

    def connectSerial(self):
        try:
            self.serialPort.open()
        except:
            print("Houve um erro")

    def readSerial(self):
        #dataRead = self.serialPort.read(4).decode("utf-8")
        # dataRead = self.serialPort.read_all()
        dataRead = self.serialPort.readline()
        #print(dataRead)
        #print("-"*30)
        return dataRead

    def sendSerial(self, data):
        if self.serialPort.isOpen():
            dadoSend = str(self.data)
            self.serial.Port.write(dadoSend.encode())
            self.serial.Port.flushOutpu()

    def closeSerial(self):
        self.serialPort.close()


# ser = serialApp()

# ser.updatePort()
# ser.serialPort.port = 'COM2'
# ser.serialPort.baudrate = 9600
# ser.connectSerial()
# contador = 0

# while True:
#     ser.readSerial()
#     if contador >= 2:
#         break
#     contador += 1

# ser.closeSerial()
