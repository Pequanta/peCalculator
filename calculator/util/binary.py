import math 
def equal(self,operation,first_num):
    if operation == "sum":
        self.n_entry.get()
        second_num = self.n_entry.get()
        self.n_entry.delete(0,"end")
        self.n_entry.insert(str(first_num + second_num))


def handler(self):
    equal(self, operation,container)

def un_equal(self,operation,num):
    if operation == "sin":
        self.n_entry.delete(0,"end")
        sine = math.sin(math.radians(num))
        self.n_entry.insert("end",sine)
    elif operation == "cos":
        self.n_entry.delete(0, "end")
        cos = math.tan(math.radians(num))
        self.n_entry.insert("end", cos)
    elif operation == "tan":
        self.n_entry.delete(0, "end")
        tan = math.tan(math.radians(num))
        self.n_entry.insert("end", tan)
    elif operation == "log10":
        self.n_entry.delete(0, "end")
        log10 = math.log(math.radians(num),10)
        self.n_entry.insert("end", log10)
    elif operation == "sqrt":
        self.n_entry.delete(0, "end")
        sqrt = math.sqrt(num)
        self.n_entry.insert("end", sqrt)
def bi_equal(self):
    num_cont= self.n_entry.get()
    if num_cont.isdigit():
        first_number = num_cont
    else:
        print("Invalid input")
