import asyncio
import serial
import time
usb_port = '/dev/tty.usbserial-1110'


# power_on_of("ZP")
class ARDVController:
    def __init__(self,port,baudrate=115200,timeout=0.050):
        self.ser = serial.Serial(usb_port, baudrate, timeout=timeout)
        time.sleep(2)
    def decoding_mode(self,modulation=None):
        #mod fm
        if modulation == "FM":
            self.send_command("MD0F0") 
            time.sleep(2)
            self.send_command("IF0")
        #send auto decode     
        elif modulation == "DA":
            self.send_command("MD00")
        
    def send_command(self,command,value=''):
        full_command = f"{command}{value}\r"
        self.ser.write(full_command.encode())
        response =self.ser.readline().decode().strip()
        return response
    
    def power_on_off(self,command):
        #turn on
        if command == "ZP":
            return self.send_command(command)
        #shut down
        elif command == "QP":
            return self.send_command(command,00)
    def close(self):
        self.ser.close()

    #process
    def fixed_frequency(self,revceive_freq,modulation):
        self.decoding_mode(modulation)
        
        return self.send_command("RF",revceive_freq)
    
    def search_freq(self,start,stop,step,modulation):
        self.send_command(f"VFB RF{stop} ST{step} {modulation}")
        time.sleep(2)                
        return self.send_command(f"VFA RF{start} ST{step} {modulation}")
        
        
                


    

#Using  the class 
controller = ARDVController(usb_port)
#EX close remote
#VS ativate vfo search

try:
    # response =  controller.fixed_frequency(151.125,"FM")
    # response = controller.search_freq(130.00,135.00,12.5,"MD00")
    response = controller.send_command("VS")
    print('Response',response)
finally:
    controller.close()


