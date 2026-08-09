class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        """
        Constructor de la clase CuentaBancaria

        Args:
            titular (str): Nombre del titular de la cuenta
            saldo (float): Saldo inicial de la cuenta (por defecto 0)
        """
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self):
        """Propiedad de solo lectura: no se permite modificar el titular."""
        return self._titular

    @property
    def saldo(self):
        """Getter del saldo."""
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        """Setter del saldo: no permite valores negativos."""
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = nuevo_saldo

    def depositar(self, cantidad):
        """
        Incrementa el saldo si la cantidad es positiva.

        Args:
            cantidad (float): Cantidad a depositar

        Returns:
            bool: True si el depósito fue exitoso, False en caso contrario
        """
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """
        Disminuye el saldo si hay suficiente dinero disponible.

        Args:
            cantidad (float): Cantidad a retirar

        Returns:
            bool: True si el retiro fue exitoso, False en caso contrario
        """
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False


# Prueba de la clase CuentaBancaria
def main():
    # Crear una cuenta con saldo inicial
    cuenta1 = CuentaBancaria("Juan Pérez", 1000)
    cuenta2 = CuentaBancaria("Ana Gómez")  # saldo por defecto = 0

    print("=== Información inicial de las cuentas ===")
    print(f"Titular: {cuenta1.titular}, Saldo: {cuenta1.saldo}")
    print(f"Titular: {cuenta2.titular}, Saldo: {cuenta2.saldo}")
    print("\n")

    # Intentar modificar el titular (no debería ser posible)
    print("=== Intento de modificar el titular ===")
    try:
        cuenta1.titular = "Otro Nombre"
    except AttributeError as e:
        print(f"Error: no se puede modificar el titular ({e})")
    print("\n")

    # Depósitos
    print("=== Depósitos ===")
    print(f"Depositar 500 en cuenta1: {cuenta1.depositar(500)}")
    print(f"Depositar -100 en cuenta1 (inválido): {cuenta1.depositar(-100)}")
    print(f"Saldo actual cuenta1: {cuenta1.saldo}")
    print("\n")

    # Retiros
    print("=== Retiros ===")
    print(f"Retirar 300 de cuenta1: {cuenta1.retirar(300)}")
    print(f"Retirar 10000 de cuenta1 (sin fondos suficientes): {cuenta1.retirar(10000)}")
    print(f"Saldo actual cuenta1: {cuenta1.saldo}")
    print("\n")

    # Intentar asignar un saldo negativo directamente
    print("=== Intento de asignar saldo negativo ===")
    try:
        cuenta2.saldo = -50
    except ValueError as e:
        print(f"Error: {e}")
    print("\n")

    # Asignar un saldo válido directamente mediante el setter
    print("=== Asignación válida de saldo ===")
    cuenta2.saldo = 200
    print(f"Nuevo saldo de cuenta2: {cuenta2.saldo}")


if __name__ == "__main__":
    main()