#EJERCICIO USUARIOS CON CUENTAS BANCARIAS
class CuentaBancaria:
    cuentas = []
    def __init__(self, banco, tasa_interes = 0.01, balance = 0):
        self.banco = banco
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    #Método de depósito:
    def deposito(self, amount, is_transfer=False):
        self.balance += amount
        if not is_transfer:
            print(f"Ha realizado un depósito de ${amount} en su cuenta bancaria en la institución: {self.banco},")
            print(f"ahora su cuenta tiene un saldo de: ${self.balance}.")
        return self

    #Método de retiro:
    def retiro(self, amount, is_transfer=False):
        if self.balance - amount < 0:
            self.balance -= 5
            print(f"Usted ha intentado realizar un retiro por ${amount} dólares, el cual no se ha concretado,")
            print("por fondos insuficientes, se ha cobrando una tarifa de $5,")
            print(f"ahora su cuenta en la institución: {self.banco} tiene un saldo de: ${self.balance} dólares.")
        elif self.balance >= amount:
            self.balance -= amount
            if not is_transfer:
                print(f"Ha realizado un retiro de ${amount} dólares en su cuenta bancaria en la institución: {self.banco},")
                print(f"ahora su cuenta tiene un saldo de: ${self.balance} dólares.")
        return self

    #Método de mostrar información del balance de la cuenta:
    def mostrar_info_cuenta(self):
        print(f"Balance de cuenta: ${self.balance} dólares,")
        print(f"en la institución: {self.banco}.")
        return self

    #Método de generar intereses:
    def generar_interes(self):
        if self.balance > 0:
            interes_generado = self.balance * self.tasa_interes
            self.balance += interes_generado
            print(f"Su actual tasa de interés en {self.banco} es de {self.tasa_interes}, por lo que")
            print(f"ha generado un interés de: ${'{:.1f}'.format(interes_generado)} dólares en su cuenta bancaria.")
        else:
            print("Debido a que su balance no ha sido positivo, usted no ha acumulado intereses,")
            print(f"en su cuenta en la institución {self.banco}.")
        return self
    
    @classmethod
    def mostrar_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()
    
class Usuario:
    def __init__(self, name, email, cuentas):
        self.name = name
        self.email = email
        self.cuentas = cuentas
    
    #Usuario hace un retiro
    def hacer_retiro (self, cuenta_index, amount):
        print(f"- El usuario {self.name}:")
        cuenta = self.cuentas[cuenta_index]
        cuenta.retiro(amount)
        return self
    
    #Usuario hace un deposito
    def hacer_deposito (self, cuenta_index, amount):
        print(f"- El usuario {self.name}:")
        cuenta = self.cuentas[cuenta_index]
        cuenta.deposito(amount)
        return self
    
    #Usuario hace una transferencia
    def transfer_dinero(self, cuentaor_index, other_user, cuentades_index, amount):
        cuenta_origen = self.cuentas[cuentaor_index]
        cuenta_destino = other_user.cuentas[cuentades_index]
        if cuenta_origen.balance - amount < 0:
            print(f"- El usuario{self.name} tiene un saldo insuficiente para transferir.")
        else:
            cuenta_origen.retiro(amount, is_transfer=True)
            cuenta_destino.deposito(amount, is_transfer=True)
            print(f"- El usuario {self.name} ha realizado una transferencia por ${amount} dólares,")
            print(f"desde su cuenta en {cuenta_origen.banco}, a la cuenta de {other_user.name} en {cuenta_destino.banco}.")
            print(f"- El usuario {other_user.name} ha recibido una transferencia de {self.name}, por ${amount} dólares,")
            print(f"en su cuenta bancaria en {cuenta_destino.banco}.")
            return self

    #Usuario quiere ver sus saldos
    def mostrar_saldos (self, cuenta_index):
        print(f"- El usuario {self.name}:")
        cuenta = self.cuentas[cuenta_index]
        cuenta.mostrar_info_cuenta()
        return self
    
    #Usuario quiere ver su reporte de intereses mensual
    def mostrar_reporte (self, cuenta_index):
        print(f"- Reporte mensual de intereses de la cuenta de usuario {self.name}:")
        cuenta = self.cuentas[cuenta_index]
        cuenta.generar_interes()
        return self





#Instancias cuenta
cuenta_uno = CuentaBancaria("Banco Internacional POO", 0.01, 2000)
cuenta_dos = CuentaBancaria("Banco Nacional Python", 0.01, 500)
cuenta_tres = CuentaBancaria("Banco Python de América", 0.015, 800)
cuenta_cuatro = CuentaBancaria("National Dojo Bank", 0.01, 1000)
cuenta_cinco = CuentaBancaria("Banco Internacional POO", 0.01, 200)
cuenta_seis = CuentaBancaria("Banco Python de América", 0.018, 800)


#Instancias usuario
usuario_uno = Usuario("Karli Acuña", "karli.am@gmail.com", [cuenta_uno, cuenta_cuatro])
usuario_dos = Usuario("Nicolás Gutiérrez", "nicomg@gmail.com", [cuenta_dos, cuenta_cinco])
usuario_tres = Usuario("Ruth Main", "ruthm@gmail.com", [cuenta_tres])
usuario_cuatro = Usuario("Juan Mongo", "mongodb@gmail.com", [cuenta_seis])


#IMPRIMIR:
print("------------------INICIO------------------")
usuario_uno.hacer_retiro (0, 200).hacer_deposito(1,150).transfer_dinero(1,usuario_dos, 0, 500).mostrar_saldos(0).mostrar_saldos(1)
print("----------------SIG CUENTA----------------")
usuario_dos.mostrar_saldos(0).mostrar_saldos(1).transfer_dinero(0,usuario_cuatro,0,100).hacer_retiro(1,50).mostrar_saldos(0).mostrar_saldos(1)
print("----------------SIG CUENTA----------------")
usuario_tres.transfer_dinero(0,usuario_uno,1,5).hacer_deposito(0,200).mostrar_saldos(0)
print("----------------SIG CUENTA----------------")
usuario_cuatro.hacer_deposito(0,500).hacer_retiro(0,400).hacer_deposito(0,1000).mostrar_saldos(0).transfer_dinero(0,usuario_dos,1,280).mostrar_saldos(0)
print("-------------------FINAL------------------")
usuario_uno.mostrar_reporte(0).mostrar_reporte(1)