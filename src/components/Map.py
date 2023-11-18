import googlemaps
from geopy import distance
from TESTintegration import AmadeusClient

API_KEY = "AIzaSyCZzgmKaqun-JuEDQzVNPaexAuBS-5Rq50"
gmaps = googlemaps.Client(key=API_KEY)


def find_nearest_airport(location_name):
    geocode_result = gmaps.geocode(location_name)
    location = geocode_result[0]['geometry']['location'] if geocode_result else None
    airports_iata = ["NGB", "NGO", "KIX", "SHI", "HIJ", "NRT", "TYO", "HND", "OKA", "KMJ", "ISG", "FUK", "NGS", "TAK",
                     "KOJ", "REP", "CJU", "PUS", "ICN", "MNL", "HKT", "BKK", "CNX", "RMQ", "TPE", "KHH", "DAD", "HAN",
                     "CXR"]
    nearest_airport, nearest_distance, nearest_iata = None, None, None
    for iata in airports_iata:
        airport_result = gmaps.places(query=iata + " Airport")
        if airport_result['results']:
            airport_location = airport_result['results'][0]['geometry']['location']
            current_distance = distance.distance((location['lat'], location['lng']),
                                                 (airport_location['lat'], airport_location['lng'])).km
            if not nearest_airport or current_distance < nearest_distance:
                nearest_airport, nearest_distance, nearest_iata = airport_result['results'][0], current_distance, iata

    flight_hotel_data = []
    if location and nearest_airport:
        client = AmadeusClient("jNaE3FNFbCGRRvoDauGu3RZ3cdDrNyNG", "SVfGXtIz9Cw8js7o")
        hotel_data = client.get_hotel_list(nearest_iata, location)
        flights_data = client.get_round_flights(nearest_iata)
        if flights_data:
            for i, flight in enumerate(flights_data):
                check_in_date, check_out_date = flight['departureDate'], flight['returnDate']
                hotel_prices = client.get_hotel_prices(hotel_data, check_in_date, check_out_date)
                flight_hotel_data.append((flight, hotel_prices))

    return {
        'location_coordinates': (
        location['lat'], location['lng']) if location else 'Could not get location coordinates.',
        'nearest_airport': nearest_airport['name'] if nearest_airport else 'No nearby airports found.',
        'iata_code': nearest_iata if nearest_iata else 'No IATA code found.',
        'flight_and_hotel_data': flight_hotel_data if flight_hotel_data else 'Could not fetch hotel and flight data due to invalid location.',
    }