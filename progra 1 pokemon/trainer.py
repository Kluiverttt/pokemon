class Trainer: 
    def __init__(self, id : int , first_name: str , last_name: str , age: float , level: float  ) -> None:
        self.id = id 
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age 
        self.level = level 
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} "
    
    def get_id(self): 
        return self.__id
    
    def set_id(self, id): 
        if isinstance(id, int):
            self.__id = id 
        else:
            raise TypeError("El ID debe ser un entero")
        
    
