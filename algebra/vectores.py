"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Gerard Escardó Cabrerizo
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
   
    def __mul__(self, other):
        """
        Multiplica dos vectores.
        >>> __mul__(v1 = Vector([1, 2, 3]), v2 = Vector([4, 5, 6]))
        Vector([2, 4, 6])
        """
        return Vector([uno * other for uno in self])
    

    def __rmul__(self, other):
        """
        Multiplica dos vectores, elemento a elemento, por otro vector o un escalar (Producto de Hadamard).
        >>> __rmul__(v1 = Vector([1, 2, 3]), v2 = Vector([4, 5, 6]))
        Vector([4, 10, 18])
        """
        
        return Vector([uno * otro for uno, otro in zip(self, other)])
    

    def __matmul__(self, other):
        """
        Multiplicación matricial de dos vectores.
        >>> __rmul__(v1 = Vector([1, 2, 3]), v2 = Vector([4, 5, 6]))
        32
        """
        return sum(uno @ otro for uno, otro in zip(self, other))
    
    __rmatmul__ = __matmul__
    

    import doctest
    doctest.testmod()