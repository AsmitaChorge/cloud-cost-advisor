import json


class PricingService:

    def __init__(self):
        with open("data/pricing_cache.json", "r") as file:
            self.pricing = json.load(file)

    def get_price(self, service, region, instance, operating_system ):

        return self.pricing[service][region][instance][operating_system]