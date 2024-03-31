class Operator:
    def m1(self):
        print('add')

    def m2(self):
        print('sub')

    def m3(self):
        print('multi')


class Symbol(Operator):
    def n1(operator):
        print("athorate")


class Res(Operator):
    def o1(self):
        print("result")


class Done(Symbol, Res):
    def one(self):
        print("done")


t1 = Done()
t1.m1()
t1.m2()
t1.m3()
t1.n1()
t1.o1()
t1.one()
