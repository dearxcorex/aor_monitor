import serial
import time
usb_port = '/dev/tty.usbserial-1110'







# power_on_of("ZP")
class ARDVController:
    def __init__(self,port,baudrate=115200,timeout=0.050):
        self.ser = serial.Serial(usb_port, baudrate, timeout=timeout)
        time.sleep(2)

    def send_command(self,command,value=''):
        full_command = f"{command}{value}\r"
        self.ser.write(full_command.encode())
        response = self.ser.readline().decode().strip()
        return response
    
    def power_on_of(self,command):
        # if command not in ["ZP","QP"]:
        #     raise ValueError('Invalid command. Only "ZP" and "QP" are supported.')
        # return self.send_command(command)
        if command == "ZP":
            return self.send_command(command)
        elif command == "QP":
            return self.send_command(command,00)
    def close(self):
        self.ser.close()

    #process
    def fix_frequency(self):
        pass 

    def serach_frequency(self):
        pass 


#Using  the class 
controller = ARDVController(usb_port)

try:
    response = controller.power_on_of('QP')
    print('Response',response)
finally:
    controller.close()