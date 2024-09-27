
class Logic:

    def logics(self, successful_delivery):
        base_pay = 5000

        if successful_delivery < 0 or successful_delivery > 100:
            raise ValueError("Invalid number of deliveries")

        elif successful_delivery <= 50:
            return successful_delivery * 160 + base_pay
        elif 51 < successful_delivery < 59:
            return successful_delivery * 200 + base_pay
        elif 60 < successful_delivery < 69:
            return successful_delivery * 250 + base_pay
        elif 70 < successful_delivery >= 100:
            return successful_delivery * 500 + base_pay
