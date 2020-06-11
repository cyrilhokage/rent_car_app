import datetime

class Rental():
    
    def __init__(self, rent_id, vehicle, start_date, end_date, distance):
        
        self.rent_id = rent_id
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.distance = distance
        self.commission = dict()
        
        #Calculate number of days
        diff_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') - datetime.datetime.strptime(start_date, '%Y-%m-%d') #Calculate the number of days
        self.nb_days = diff_date.days + 1
        self.base_price = self.vehicle.get_rental_price(self.nb_days, distance) #Set the rental price 
     
    
        #Share rental revenues between car owner, the company, the insurance & the roadside assistance

        # For Assistance_fee, it is say in the instructions that it is 1€ per day of reservation
        # but to match the output file expectations,
        # i have to multiply it by 100
                
          # for drivy_fee, we assume the commission will
          # always be positive, if not it will count
          # as a company loss or debt
        
        self.commission = {
            "insurance_fee": self.base_price * 0.3 * 0.5,
            "assistance_fee": self.nb_days * 100,
            "drivy_fee": self.base_price * 0.3 - self.base_price * 0.3 * 0.5 - self.nb_days * 100 
         }
        
        
        #For Level 5 : Additional options
        self.options = []
        self.gps_fee = 0
        self.baby_seat_fee = 0
        self.add_insurance_fee = 0
        
        
        
    #Level 4 : Actions
        driver_debit = self.base_price 
        owner_fee = self.base_price * 0.7
        insurance_fee = self.commission["insurance_fee"]
        assistance_fee = self.commission["assistance_fee"]
        drivy_fee = self.commission["drivy_fee"]
        
        self.set_actions(driver_debit = driver_debit,
                         owner_fee = owner_fee,
                         insurance_fee = insurance_fee,
                         assistance_fee = assistance_fee,
                         drivy_fee = drivy_fee)
        
    
    def set_actions(self, driver_debit, owner_fee, insurance_fee,
                    assistance_fee, drivy_fee):
        
        #Level 4 : Actions
        self.actions =  [
            {
              "who": "driver",
              "type": "debit",
              "amount": driver_debit
            },
            {
              "who": "owner",
              "type": "credit",
              "amount": owner_fee
            },
            {
              "who": "insurance",
              "type": "credit",
              "amount": insurance_fee
            },
            {
              "who": "assistance",
              "type": "credit",
              "amount": assistance_fee
            },
            {
              "who": "drivy",
              "type": "credit",
              "amount": drivy_fee
            }
          ]
    
    #Level5 : Additional options
    def add_options(self, options=[]):
        
        self.options = options
        
        #Level 5 Additional options
        self.gps_fee = 500 * self.nb_days if("gps" in self.options) else 0
        self.baby_seat_fee = 200 * self.nb_days if("baby_seat" in self.options) else 0
        self.add_insurance_fee = 1000 * self.nb_days if("additional_insurance" in self.options) else 0
        
        driver_debit = self.base_price + self.gps_fee + self.baby_seat_fee + self.add_insurance_fee 
        owner_fee = self.base_price * 0.7 + self.gps_fee + self.baby_seat_fee
        insurance_fee = self.commission["insurance_fee"]
        assistance_fee = self.commission["assistance_fee"]
        drivy_fee = self.commission["drivy_fee"] + self.add_insurance_fee
    
        
        self.set_actions(driver_debit = driver_debit,
                         owner_fee = owner_fee,
                         insurance_fee = insurance_fee,
                         assistance_fee = assistance_fee,
                         drivy_fee = drivy_fee)
        
        
        