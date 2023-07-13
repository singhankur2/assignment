class Manufacturer():
    def _init_(self, name, location):
        self.name = name
        self.location = location
        self.brands = []

    def add_brand(self, brand):
        """
        Add new brand
        """
        self.brands.append(brand)

    def get_brands(self):
        """
        Returns all the brands
        """
        return self.brands

class Car():

    def _init_(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def get_details(self):
        """
        Add new brand
        """
        print(self.brand, self.model, self.year)

manufacturer_cars = {
    'manufacturer1': {
        "Audi": [
            {"model": "A3", "year": 2020},
            {"model": "Q5", "year": 2021}
        ],
        "BMW": [
            {"model": "X3", "year": 2022}
        ]
    },
    'manufacturer2': {
        "Tata": [
            {"model": "Nexon", "year": 2020}
        ],
        "Hyundai": [
            {"model": "Tucson", "year": 2021}
        ],
    }
}

# Creating two manufacturer objects 
manufacturer1 = Manufacturer(name='Ganpati', location='Delhi')
manufacturer2 = Manufacturer(name='Balaji', location='Noida')

# Adding brands into both manufacturer objects
for brand1 in manufacturer_cars['manufacturer1'].keys():
    manufacturer1.add_brand(brand=brand1)

for brand2 in manufacturer_cars['manufacturer2'].keys():
    manufacturer2.add_brand(brand=brand2)

# Creating Cars objects for all brands
cars = []
for brand in manufacturer1.get_brands():
    for car_details in manufacturer_cars['manufacturer1'][brand]:
        car_obj = Car(brand=brand, **car_details)
        cars.append(car_obj)

for brand in manufacturer2.get_brands():
    for car_details in manufacturer_cars['manufacturer2'][brand]:
        car_obj = Car(brand=brand, **car_details)
        cars.append(car_obj)

# print all cars details
for car in cars:
    car.get_details()