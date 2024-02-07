class CarManager:
    all_cars = []
    total_cars  = 0
    
    def __init__(self,make,model,year,mileage=0,services=[]):
        self.id = CarManager
        CarManager.total_cars +=1
        #incriments total_cars and sets id to total_cars, but not sure why I need ID
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage 
        self.services = services
        #maybe input it as a dictionary then throw in whatever informations id want to to reference across all the class created
        CarManager.all_cars.append(self)

    def __str__(self):
        return f"Id{self.id}, Make:{self.make}, Model:{self.model}, year:{self.year}, Mileage:{self.mileage}, Services:{self.services}"
    
    def __repr__(self):
        return str(self)
    

Erricks_Whip = CarManager("Toyota","Prius","1990",100000,[1,1,1])
print(CarManager.all_cars)
print(CarManager.total_cars)

print(f"----  WELCOME  ----\nPlease enter a number based on one of the following options")
option_list = [{1: 'Add a car'},{2:'View all cars'},{3:'View total number of cars'},{4:'See a cars details'},{5:'Service a car'},{6:'Update mileage'},{7:'Quit'}]
#Change to only print values
print(option_list)


