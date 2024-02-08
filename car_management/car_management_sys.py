class CarManager:
    all_cars = []
    total_cars  = 0
    
    def __init__(self,make,model,year,mileage=0,services=[]):
        CarManager.total_cars +=1
        self.id = CarManager.total_cars
        #incriments total_cars and sets id to total_cars so each car has a specific number referencing it
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage 
        self.services = services
        #maybe input it as a dictionary then throw in whatever informations id want to to reference across all the class created
        CarManager.all_cars.append(self)   
        on = True

    def __str__(self):
        return f"Id{self.id}, Make:{self.make}, Model:{self.model}, year:{self.year}, Mileage:{self.mileage}, Services:{self.services}"
    
    def __repr__(self):
        return str(self)
    
    @classmethod
    def add_a_car(cls):
        make = input('What is the make of the vehicle? ')
        model = input('What is the model of the vehicle? ')
        year = input('What is the year of the vehicle? ')
        mileage = int(input('What is the mileage of the vehicle? '))
        services_input = input('What, if any, services have been done on the vehicle? ')
        services = services_input.split(', ') if services_input else []
        cls(make,model,year,mileage,services)
        print("Car added successfully")
    
    #returns a list view of all of the instantiated vehicles
    @classmethod
    def view_cars(cls):
        print(cls.all_cars)
    
    #returns a number of the total amount of cars
    @classmethod
    def view_total_num_of_cars(cls):
        print(cls.total_cars)
    
    #returns all of a vehicles information based on the number selected from view_all_cars()
    @classmethod
    def print_car_by_id(cls,car_id):
        for car in cls.all_cars:
            if car.id == car_id:
                print(f"Car ID: {cls.id}")
                print(f"Make: {cls.make}")
                print(f"Model: {cls.model}")
                print(f"Year: {cls.year}")
                print(f"Mileage: {cls.mileage}")
                if car.services:
                    print("Services: " + ", ".join(car.services))
                else:
                    print("Services: None")
                break
        else: 
            print(f"No car found with ID {car_id}.")
    
    #just adds whatever service you want by appending it to the existing list
    def set_car_service(self):
        new_services = input("what service would you like done to your vehicle? ")
        self.services.append(new_services)
        print("The service has been added, have a brutal day!")
        
    #Updates the mileage for a vehichle a specific vehicle
    def set_mileage(self):
        new_mileage = input("what is the new mileage for the vehicle? ")
        self.mileage = new_mileage
        print("The mileage has been updated, have a brutal day!")

    #Takes input for what option the user would like to utilize and runs the corresponding function
    @staticmethod
    def goodbye():
        print("Have a brutal day")

#======== Code essential to the Main Loop =======#
        
    #you have to utilize this as a class method or it wont properly understand what the functions are you are calling in the option_list
    @classmethod
    def handle_option(cls, input_number):
        terminal_on = True
        while terminal_on:
            for option in cls.option_list:
                if option["option"] == input_number:
                    function = option["function"]
                    # Check if the function requires the class ('cls') as an argument
                    if input_number == 7:
                        function()
                        terminal_on = False
                        break
                    # the exception is 5 and 6 which require cls since they are isntance methods
                    if input_number < 5:  
                        function()
                        user_input = int(input("Please enter another option number: "))
                        CarManager.handle_option(user_input)
                    # the exception is 5 and 6 which require cls since they are instance methods
                    else:
                        car_id = int(input("Please specify a car ID "))
                        car = CarManager.all_cars[car_id]
                        function(car)
                        user_input = int(input("Please enter another option number: "))
                        CarManager.handle_option(user_input)

            else:
                print("Invalid option selection.")
                user_input = int(input("Please enter another option number: "))
                CarManager.handle_option(user_input)

CarManager.option_list = [
    {"option": 1, "description": "Add a car", "function": CarManager.add_a_car},
    {"option": 2, "description": "View all cars", "function": CarManager.view_cars},
    {"option": 3, "description": "View total number of cars", "function": CarManager.view_total_num_of_cars},
    {"option": 4, "description": "See a car's details", "function": CarManager.print_car_by_id},
    {"option": 5, "description": "Service a car", "function": CarManager.set_car_service},
    {"option": 6, "description": "Update mileage", "function": CarManager.set_mileage},
    {"option": 7, "description": "Quit", "function": CarManager.goodbye}
]     
#======== Sample Object ============#
Erricks_car = CarManager("Mobile","Home","1997",1000000000,["Added Spinners"])   
#======== Initiate Main Loop =======#

print(f"----  WELCOME  ----\n Below is a list of our options")
for option in CarManager.option_list:
    print(f'{option["option"]}: {option["description"]}')

user_input = int(input("Enter an option number: "))
CarManager.handle_option(user_input)