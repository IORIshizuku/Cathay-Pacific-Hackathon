from openai import OpenAI
from Map import find_nearest_airport
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_query(query, client):
    # Check if the query should be handled by the scripts
    if 'plan my trip to' in query.lower():
        # Extract the destination from the query
        destination = query.split('to')[-1].strip()

        try:
            trip_data = find_nearest_airport(destination)
            nearest_airport = trip_data['nearest_airport']
            flight_and_hotel_data = trip_data['flight_and_hotel_data']
        except Exception as e:
            return f"Sorry, I couldn't process your request. {str(e)}"

        # Combine the flight and hotel information into a response
        response = f"Here's a travel plan for {destination}:\n"
        # Add logic to format flight_and_hotel_data into the response

        # Format the nearest airport info to be more presentable
        airport_info = f"The nearest airport to your location is {nearest_airport}."
        airport_prompt = f"I have found some useful information for your trip: {airport_info}"
        airport_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": airport_prompt
                }
            ]
        )
        response += airport_response['choices'][0]['message']['content'].strip()

        return response

    else:
        # If not, send the query to GPT-3
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        )
        return response['choices'][0]['message']['content'].strip()

while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        break

    response = handle_query(user_input, client)
    print("Bot: ", response)