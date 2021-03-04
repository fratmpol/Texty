from classes.Be import Be

class IP:

    control = False


    def __init__(self, NN, i_be):
        self.int_input = list()
        self.out_input = list()
        self.tell_output = list()
        self.nn = NN
        self.be = i_be

    def processing(self):
        self.int_processing()
        self.out_processing()



    def int_processing(self):
        for i,x in enumerate(self.int_input):
            if x == "/is":
                self.be.be(self.int_input[i - 1], self.int_input[i + 1])
                self.nn = self.be.nn
            elif  x == "/seems":
                self.be.seems(self.int_input[i - 1], self.int_input[i + 1])
                self.nn = self.be.nn

    def out_processing(self):
        for i,x in enumerate(self.out_input):
            if x == "/Tell":
                out = self.be.tell()
                out.append("beT")
                self.tell_output.append(out.copy())
                out.clear()
                self.nn = self.be.nn
            elif  x == "/Ftell":
                out = self.be.force_tell(self.out_input[i-1], self.control)
                out.append("beT")
                self.tell_output.append(out.copy())
                out.clear()
                self.nn = self.be.nn
            elif  x == "/Free":
                out = self.be.free_tell(self.control)
                print(out)
                out.append("beT")
                self.tell_output.append(out.copy())
                out.clear()
                self.nn = self.be.nn

    def clear(self):
        self.int_input.clear()
        self.out_input.clear()
        self.tell_output.clear()

    #REFRATTORI INTERNI
    #dicono che processi interni svolgere