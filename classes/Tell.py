class Tell:

    def __init__(self):
        self.input = list()
        self.output = "Answer:"

    def answer_construction(self):
        for x in self.input:
            if "beT" in x:
                self.output = self.output + f' {x[0]} is {x[1]} .'
            else:
                self.output = self.output + f' {x} .'

    def answer(self):
        self.answer_construction()
        return(self.output)

    def clear(self):
        self.input.clear()
        self.output = "Answer:"
