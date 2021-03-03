

class Read:

    def __init__(self):
        self.input = ""
        self.in_output = list()
        self.IP_int_output = list()
        self.IP_out_output = list() #pezzi di testo che devono essere elaborati da tell.py

    def subdivider(self):
        self.in_output = self.input.split(" ")
        to_add = ["ç", "ç"]
        for i, x in enumerate(self.in_output):
            if "." in x or ":" in x or "," in x or ";" or "?" in x or "!" in x:
                if "." in x:
                    to_add = x.split(".")
                if ":" in x:
                    to_add = x.split(":")
                if "," in x:
                    to_add = x.split(",")
                if ";" in x:
                    to_add = x.split(";")
                if "!" in x:
                    to_add = x.split("?")
                if "?" in x:
                    to_add = x.split("!")
                if to_add[0] != "ç":
                    self.in_output.remove(x)
                    if len(self.in_output) == i:
                        self.in_output.append(to_add[0])
                        self.in_output.append(to_add[1])
                    else:
                        self.in_output.insert(i, to_add[1])
                        self.in_output.insert(i, to_add[0])


    # METODO REFRATTORI TEMPORANEO

    def refractor(self):
        for i,x in enumerate(self.in_output):
            if x == "/is":
                self.IP_int_output.append(self.in_output[i - 1])
                self.IP_int_output.append(x)
                self.IP_int_output.append(self.in_output[i + 1])
            elif  x == "/seems":
                self.IP_int_output.append(self.in_output[i-1])
                self.IP_int_output.append(x)
                self.IP_int_output.append(self.in_output[i+1])
            elif x == "/Tell":
                self.IP_out_output.append(x)
            elif  x == "/Ftell":
                self.IP_out_output.append(x)
                self.IP_out_output.append(self.in_output[i-1])
            elif  x == "/Free":
                self.IP_out_output.append(x)

    def read(self):
        self.subdivider()
        self.refractor()

    def clear(self):
        self.in_output.clear()
        self.IP_int_output.clear()
        self.IP_out_output.clear()

