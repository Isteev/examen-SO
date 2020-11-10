class datos:
    _id = int
    _nombre: str
    _apellido: str
    _tempEntrada: str
    _tempSalida: str
    _fecha: str

    def __init__(self, data):
        self._id = data[0]
        self._nombre= data[1]
        self._apellido = data[2]
        self._tempEntrada = data[3]
        self._tempSalida = data[4]
        self._fecha = data[5]
