import math

def handler(self,operation,event = None):
    self.operation = operation
    simple = ['mult','div','sum','diff','^']
    unary = ['sin','cos','tan','log10','sqrt']
    self.act = str()
    if operation in simple:
        self.n_entry.get()
        self.first_num = self.n_entry.get()
        self.n_entry.delete(0,"end")
        self.act = str(operation)
        self.tool = []
        self.tool.append(self.act)
        self.tool.append(self.first_num)
        return self.tool

    elif operation in unary:
        self.n_entry.get()
        number = self.n_entry.get()
        self.n_entry.delete(0,"end")
        if self.operation == "sin":
            self.n_entry.insert(0,math.sin(math.radians(float(number))))
        elif self.operation == "cos":
            self.n_entry.insert(0,math.cos(math.radians(float(number))))
        elif self.operation == "tan":
            self.n_entry.insert(0,math.tan(math.radians(float(number))))
        elif self.operation == "log10":
            self.n_entry.insert(0,math.log10(float(number)))
        elif self.operation == "sqrt":
            self.n_entry.insert(0,math.sqrt(float(number)))
        else:
            return
    elif operation == "equal":
        if self.tool[0] == "sum":
            self.n_entry.get()
            second_num = self.n_entry.get()
            result = int(self.first_num) + int(second_num)
            self.n_entry.delete(0,"end")
            self.n_entry.insert(0,result)
        elif self.tool[0] == "mult":
            self.n_entry.get()
            second_num = self.n_entry.get()
            result = int(self.first_num) * int(second_num)
            self.n_entry.delete(0,"end")
            self.n_entry.insert(0,result)

        elif self.tool[0] == "div":
            self.n_entry.get()
            second_num = self.n_entry.get()
            result = int(self.first_num) / int(second_num)
            self.n_entry.delete(0,"end")
            self.n_entry.insert(0,result)
        elif self.tool[0] == "diff":
            self.n_entry.get()
            second_num = self.n_entry.get()
            result = int(self.first_num) - int(second_num)
            self.n_entry.delete(0,"end")
            self.n_entry.insert(0,result)
        elif self.tool[0] == "^":
            self.n_entry.get()
            second_num = self.n_entry.get()
            result = int(self.first_num) ** int(second_num)
            self.n_entry.delete(0,"end")
            self.n_entry.insert(0,result)
        else:
            return
