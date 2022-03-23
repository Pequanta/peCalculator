def num(self, num):
    self.n_entry.insert("end",num)
def clear(self):
    self.n_entry.delete(0,"end")
def back(self):
    i = len(self.n_entry.get()) - 1
    self.n_entry.delete(i,"end")