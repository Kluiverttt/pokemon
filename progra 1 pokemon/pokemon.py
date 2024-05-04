class Pokemon: 
    def  __init__(self, id : int, name: str, weight: float, altura: float, type: str, trainer: str ) -> None:   #self : utilizara la misma clase en este caso 'pokemon'
        self.id = id         
        self.name = name            #init: inicia el construtor 
        self.weight = weight
        self.altura = altura
        self.type = type
        self.trainer = trainer 
    
    def _str_(self) -> str:
        return self.name

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("El ID debe ser un entero")
