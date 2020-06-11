import json
from Vehicle import Vehicle
from Rental import Rental


class Test():

	def __init__(self):
		pass


	#Load cars
	def load_cars(self, input_data_cars):
	    list_cars = []

	    for car in input_data_cars:
	        veh = Vehicle(car['id'], car['price_per_day'], car['price_per_km'])
	        list_cars.append(veh)
	    
	    return list_cars


	#Load rentals
	def load_rentals(self, input_data, list_cars):
	    
	    #Load rentals
	    list_rentals = []

	    for rental in input_data['rentals']:

	        #Get rental vehicle
	        for car in list_cars:
	            if(car.car_id == rental['car_id']):
	                rent_veh = car 

	        rent = Rental(rental['id'], rent_veh, rental['start_date'], rental['end_date'], rental['distance'])
	        
	        #Load options
	        if "options" in input_data.keys():
	            rental_options = []
	            for option in input_data["options"]:
	                if(option["rental_id"] == rent.rent_id):
	                    rental_options.append(option["type"])
	            
	            rent.add_options(rental_options)
	        
	        list_rentals.append(rent)
	        
	    return list_rentals


	def load_data(self, filename):
		with open(filename) as inputfile:
			input_data = json.load(inputfile)
	    
	    
		list_cars = self.load_cars(input_data["cars"])
		list_rentals = self.load_rentals(input_data, list_cars)
	    
		return list_cars, list_rentals

	def write_output(self, list_rentals, output_file):
		list_output_rentals = []

		for rental in list_rentals : 
			output_rental = {
		        "id": rental.rent_id,
		        "options": rental.options,
		        "actions": rental.actions
		      }

		list_output_rentals.append(output_rental)

		output = {
	        	"rentals" : list_output_rentals
	    }

		with open(output_file, 'w') as fp:
			json.dump(output, fp)

	
	def test(self, input_file, output_name):
		list_cars, list_rentals = self.load_data(input_file)
		self.write_output(list_rentals, output_name)