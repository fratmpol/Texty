class NNG:

    def __init__(self, NN):
        self.nn = NN

    def save(self):
        SAVE = ""
        for x in self.nn:
            SAVE = SAVE + f'{x}\n'
        memory = open('memory/memory.txt', 'w')
        memory.write(SAVE)
        memory.close()

    def load(self):
        memory = open('memory/memory.txt', 'r').readlines()
        # rimozione degli \n
        for ind, dex in enumerate(memory):
            memory[ind] = dex.split('\n')[0]
        for x in memory:
            self.nn.append(x)

