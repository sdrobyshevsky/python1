import controller

if __name__ == '__main__':

    controller.start() 
   
class Human:
   def __init__(self, name: str = 'Человек', age: int = 18, work: str = 'GB'): 
      self.name = name
      self.age = age
      self.work = work 

def greetings(self):
      return f'{self.name} приветствую тебя'  

def _str_ (self): 
      return f'Человек по имени {self.name}, {self.age} лет от роду, трудиться на {self.work}'  
 
 
stone = Human('Стоун', 39, work = 'Работа') 
andrey = Human('Андрей', 18)    
stone.name = 'STONE' 

print(stone) 
print(andrey)

print(stone.greetings())
print(andrey.greetings()) 
   


