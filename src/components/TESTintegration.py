import requests
import googlemaps
from geopy import distance

class AmadeusClient:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.access_token = self.get_access_token()

    def get_access_token(self):
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(self.auth_url, data=auth_data)
        response_data = response.json()
        if "access_token" in response_data:
            return response_data["access_token"]
        else:
            print(f"Failed to get access token: {response_data}")
            return None

    def get_hotel_list(self, cityCode, user_location):
        if self.access_token is None:
            print("Cannot get hotel list without access token.")
            return None

        search_url = "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        params = {
            "cityCode": cityCode,
        }
        response = requests.get(search_url, params=params, headers=headers)

        if response.status_code == 500:
            return None

        data = response.json()

        gmaps = googlemaps.Client(key="AIzaSyCZzgmKaqun-JuEDQzVNPaexAuBS-5Rq50")
        hotels_with_distances = []

        for hotel in data.get('data', []):
            hotel_result = gmaps.geocode(hotel['name'])
            try:
                hotel_location = hotel_result[0]['geometry']['location']
                hotel_distance = distance.distance((user_location['lat'], user_location['lng']),
                                                   (hotel_location['lat'], hotel_location['lng'])).km
                hotels_with_distances.append((hotel['name'], hotel_distance, hotel['hotelId']))
            except IndexError:
                next

        hotels_with_distances.sort(key=lambda x: x[1])
        return hotels_with_distances[:5]

    def get_round_flights(self, destination):
        if self.access_token is None:
            print("Cannot get round flights without access token.")
            return None

        search_url = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }

        round_flights = []

        for place in ["HKG", destination]:
            params = {
                "origin": place,
            }
            response = requests.get(search_url, params=params, headers=headers)

            if response.status_code != 200:
                print(f"Error getting data: {response.json()}")
                return None

            data = response.json()
            filtered_data = [flight for flight in data.get("data", []) if
                             flight.get("destination") == ("HKG" if place != "HKG" else destination)]

            round_flights.extend(filtered_data)

        return round_flights

    def get_hotel_prices(self, hotel_names, check_in, check_out):
        if self.access_token is None:
            print("Cannot get hotel prices without access token.")
            return None

        search_url = "https://test.api.amadeus.com/v3/shopping/hotel-offers"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }

        hotel_prices = []
        for hotel in hotel_names:
            params = {
                "hotelIds": hotel[2],
                "checkInDate": check_in,
                "checkOutDate": check_out,
                "hotelName": hotel[0],
            }
            response = requests.get(search_url, params=params, headers=headers)

            if response.status_code != 200:
                print(f"Error getting data: {response.json()}")
                return None

            data = response.json()

            if 'data' in data:
                for hotel_offer in data['data']:
                    if 'offers' in hotel_offer and isinstance(hotel_offer['offers'], list) and len(
                            hotel_offer['offers']) > 0:
                        price = hotel_offer['offers'][0].get('price', {}).get('total', "Price not available")
                        hotel_id = hotel_offer['hotel'].get('hotelId', "ID not available")
                        hotel_name = hotel_offer['hotel'].get('name', "Name not available")
                    else:
                        price = "Price not available"
                        hotel_id = "ID not available"
                        hotel_name = "Name not available"
                    hotel_prices.append((hotel_id, hotel_name, price))

        return hotel_prices