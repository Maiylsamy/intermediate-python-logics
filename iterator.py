class Mulof4:
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        if self.count <=24 :
            x=self.count
            self.count +=4
            return x
        else:
            raise StopIteration
obj1=Mulof4()
x=iter(obj1)
for i in x:
    print(i)

a =[12,34,5,686,98]
it=iter(a)
for m in it:
    print(m)
