from cpu.cpu import CpuMIC1
from gui.mainWindow import MainWindow

def main():
    cpu = CpuMIC1()

    cpu.getRegister("PC").write(10)
    cpu.getRegister("SP").write(200)
    cpu.getRegister("LV").write(500)

    janela = MainWindow(cpu)
    janela.rodar()

if __name__ == "__main__": main()