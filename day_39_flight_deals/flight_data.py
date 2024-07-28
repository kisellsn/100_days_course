def find_cheapest_flight(data):
    if data is None or len(data) == 0:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A")

    first_flight = data[0]
    print(first_flight)
    lowest_price = first_flight["price"]["grandTotal"]
    departure_city_code = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination_city_code = first_flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    is_direct = len(first_flight["itineraries"][0]["segments"]) < 1
    cheapest_flight = FlightData(lowest_price, departure_city_code,
                                 destination_city_code, departure_date,
                                 is_direct)

    for flight in data:
        if flight["price"]["grandTotal"] < lowest_price:
            lowest_price = flight["price"]["grandTotal"]
            departure_city_code = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination_city_code = flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
            departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            is_direct = len(first_flight["itineraries"][0]["segments"]) < 1
            cheapest_flight = FlightData(lowest_price, departure_city_code,
                                         destination_city_code, departure_date,
                                         is_direct)
    return cheapest_flight


class FlightData:
    def __init__(self, price, departure_airport_code, destination_airport_code, departure_date,
                 is_direct=True,
                 return_date=None):
        self.price = price
        self.departure_city_code = departure_airport_code
        self.destination_city_code = destination_airport_code
        self.departure_date = departure_date
        self.is_direct = is_direct
        self.return_date = return_date
