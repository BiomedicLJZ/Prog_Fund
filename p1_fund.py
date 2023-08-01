class operaciones():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def suma(self):
        return self.a + self.b
    def multiplicacion(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    
    
    test = operaciones(5,6)
    test.suma()
    
    test2 = operaciones(21.2,13)
    test2.multiplicacion()
    
class operaciones_avanzadas(operaciones):
    def __init__(self,a,b):
        super().__init__(a,b)
    def potencia(self):
        return self.a ** self.b
    def raiz(self):
        return self.a ** (1/self.b)
    
    test3 = operaciones_avanzadas(5,6)
    test3.potencia()
    
    test4 = operaciones_avanzadas(21.2,13)
    test4.raiz()
    
    test5 = operaciones_avanzadas(21.2,13)
    test5.div()
    
    test6 = operaciones_avanzadas(21.2,13)
    test6.suma()
    
    test7 = operaciones_avanzadas(21.2,13)
    test7.multiplicacion()
    
    test8 = operaciones_avanzadas(21.2,13)
    test8.potencia()
    
    test9 = operaciones_avanzadas(21.2,13)
    test9.raiz()
    
    test10 = operaciones_avanzadas(21.2,13)
    test10.div()
    
    test11 = operaciones_avanzadas(21.2,13)
    test11.suma()
    
    test12 = operaciones_avanzadas(21.2,13)
    test12.multiplicacion()
    
    test13 = operaciones_avanzadas(21.2,13)
    test13.potencia()
    
    test14 = operaciones_avanzadas(21.2,13)
    test14.raiz()
    
    test15 = operaciones_avanzadas(21.2,13)
    test15.div()
    
    test16 = operaciones_avanzadas(21.2,13)
    test16.suma()
    
    test17 = operaciones_avanzadas(21.2,13)
    test17.multiplicacion()
    
    test18 = operaciones_avanzadas(21.2,13)
    test18.potencia()
    
    test19 = operaciones_avanzadas(21.2,13)
    test19.raiz()
    
    test20 = operaciones_avanzadas(21.2,13)
    test20.div()
    
    test21 = operaciones_avanzadas(21.2,13)
    test21.suma()
    
    test22 = operaciones_avanzadas(