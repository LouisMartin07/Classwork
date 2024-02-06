class DMVform:
    def __init__(self, name,email_address,drivers_license_number):
        self.name = name
        self.email_address = email_address
        self.drivers_license_number = drivers_license_number
    
    def form_answer(self):
        print(f'Hello, my name is {self.name}, my email is {self.email_address} and my license number is {self.drivers_license_number}')
        print('Come back in two weeks with 4 forms of ID')

Errick = DMVform('Errick', "errick.theprogrammer@gmail.com, M9840GD64")

Errick.form_answer()
