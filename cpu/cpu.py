from cpu.registers import Registrador

class CpuMIC1:
    def __init__(self):
        self.registradores = {
            "PC": Registrador("PC"),
            "MAR": Registrador("MAR"),
            "MDR": Registrador("MDR"),
            "MBR": Registrador("MBR"),
            "SP": Registrador("SP"),
            "LV": Registrador("LV"),
            "CPP": Registrador("CPP"),
            "TOS": Registrador("TOS"),
            "OPC": Registrador("OPC"),
            "H": Registrador("H")
        }
    
    def reset(self):
        for registrador in self.registradores.values():
            registrador.reset()
    
    def getRegister(self, nome):
        return self.registradores[nome]
    
    def dumpRegisters(self):
        for registrador in self.registradores.values():
            print(registrador)