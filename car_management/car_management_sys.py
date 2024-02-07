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
        return CarManager.all_cars
    
    #returns a number of the total amount of cars
    @classmethod
    def view_total_num_of_cars(cls):
        return CarManager.total_cars
    
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
        else:  # This else belongs to the for loop, executed if the loop completes normally (no break)
            print(f"No car found with ID {car_id}.")
    
    #just adds whatever service you want by appending it to the existing list
    def set_car_service(self):
        new_services = input("what service would you like done to your vehichle? ")
        self.services.append(new_services)
        
    #Updates the mileage for a vehichle a specific vehicle
    def set_mileage(self):
        new_mileage = input("what is the new mileage for the vehicle? ")
        self.mileage = new_mileage

    #Takes input for what option the user would like to utilize and runs the corresponding function
    @staticmethod
    def goodbye():
        print("Have a brutal day")

#======== Code essential to the Main Loop =======#
        
    option_list = [
        {"option": 1, "description": "Add a car", "function": add_a_car},
        {"option": 2, "description": "View all cars", "function": view_cars},
        {"option": 3, "description": "View total number of cars", "function": view_total_num_of_cars},
        {"option": 4, "description": "See a car's details", "function": print_car_by_id},
        {"option": 5, "description": "Service a car", "function": set_car_service},
        {"option": 6, "description": "Update mileage", "function": set_mileage},
        {"option": 7, "description": "Quit", "function": goodbye}
    ]     
    
       
#you have to utilize this as a class method or it wont properly understand what the functions are you are calling in the option_list
    @classmethod
    def handle_option(cls, input_number):
        for option in cls.option_list:
            if option["option"] == input_number:
                # Call the function directly if it's a normal class method or static method
                if callable(option["function"]):
                    # Special handling for option 7 (Quit), or any function that doesn't need extra arguments
                    if input_number == 7:
                        option["function"]()  # Call the goodbye function without needing 'cls'
                    else:
                        option["function"](cls)  # Assuming other functions are class methods and require 'cls'
                return  # Exit the method after handling the valid option
        else:
            print("Invalid option selection.")
    
#======== Main Loop =======#
        
    print(f"----  WELCOME  ----\n Below is a list of our options")
    for option in option_list:
        print(f'{option["option"]}: {option["description"]}')

user_input = int(input("Enter an option number: "))
CarManager.handle_option(user_input)
        
