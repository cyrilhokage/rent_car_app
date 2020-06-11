class Vehicle():
    
    def __init__(self, p_id, price_per_day, price_per_km):
        self.car_id = p_id
        self.price_per_day = price_per_day
        self.price_per_km = price_per_km
        
        
    def calculate_ndays_fees(self, n_days):
        paliers = [1, 3, 6, 10e4]
        i = 0
        list_days = [0, 0, 0, 0]

        while(n_days > paliers[i]):
            n_days = n_days - paliers[i]
            list_days[i] = paliers[i]
            i += 1
        list_days[i] = n_days

        return list_days
    
        
    def get_rental_price(self, nb_days, nb_km):
        
        # Get different days with particular discount rates
        list_ndays = self.calculate_ndays_fees(nb_days)
        discount_rates = [1, 0.9, 0.7, 0.5]
        
        # Calculate price with nb_km
        price = nb_km * self.price_per_km 
        
        # Calculate price with nb_days and different discount rates
        for i in range(len(discount_rates)):
            price += list_ndays[i] * discount_rates[i] * self.price_per_day

        return price
        