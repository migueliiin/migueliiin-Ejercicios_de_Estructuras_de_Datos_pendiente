class Bloque:
    def __init__(self): 
        self.instrucciones = []
 
    def agregarInstruccion(self, instruccion): 
        self.instrucciones.append(instruccion)

    def leerInstruccion(self,que_instruccion):
        if(isinstance(self.instrucciones[que_instruccion],Si)):
            return self.instrucciones[que_instruccion].pintarIf()


class Si: 
    def __init__(self, condicion, entonces, sino): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.sino = sino
    
    def pintarIf(self):
        print( "if ("+self.condicion+"):")
        if(isinstance(self.entonces,Mostrar)):
            self.entonces.pintarMostrar()
        else:
            print("    {}".format(self.entonces))
        print( "else:")
        if(isinstance(self.sino,Mostrar)):
            self.sino.pintarMostrar()
        else:
            print("    {}".format(self.sino))


class MientrasQue:  
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque

 
class Mostrar: 
    def __init__(self, mensaje): 
        self.mensaje = mensaje

    def pintarMostrar(self):
        print(self.mensaje)




def main():
    mostrar_ok = Mostrar('"OK"') 
    mostrar_ko = Mostrar('"KO"') 
    alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
    bloque_alternativa = Bloque() 
    bloque_alternativa.agregarInstruccion(alternativa) 
    bucle = MientrasQue(True, bloque_alternativa) 
    print(bloque_alternativa.leerInstruccion(0))



if __name__=="__main__":
    main()