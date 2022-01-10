import Tools.DirectoryDiscover as DirectoryDiscover
import Tools.Keyloger as Keyloger
import Tools.LoginBruteForce as LoginBruteForce
import Tools.PortScanner as PortScanner
import Tools.ReverseShell as ReverseShell


class HackTools:
    def __init__(self):
        self.DirectoryDiscover = DirectoryDiscover.DirectoryDiscover()
        self.Keyloger = Keyloger.Keyloger()
        self.LoginBruteForce = LoginBruteForce.LoginBruteForce()
        self.PortScanner = PortScanner.PortScanner()
        self.ReverseShell = ReverseShell.ReverseShell()

    def KeylogerInit(self):
        self.save_directory = input("Insert the directory to save de log of the Keyloger. Default options is the root folder of your system: ")
        if self.save_directory == "":
            self.Keyloger.Main()
        else:
            self.Keyloger.Main(self.save_directory)
    
# hack_tools = HackTools()

# hack_tools.Keyloger.Main()