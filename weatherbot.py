from weather import Weather, Unit
from geotext import GeoText
import nltk

print('This is a very simple chatbot, it does not employ machine learning at all and just a little bit of NLP')
print('Please install weather-api and geotext libraries')
print("Please provide a city name always otherwise api won't be able to give a proper answer, "
      "also this chatbot gives only current information and not on forecasting")
print('To exit the bot, just press enter without typing anything\n')

# Give me a working demo of bots from which I can ask about the weather. My question will be " How is the weather' ?

# You can send me the link and also make sure that demo can answer couple of more questions, like how is the weather in
# New delhi  ? Is it going to rain today ? it is sunshine ?

chat_input = ['Hi', 'Hello', 'Hey']
weather = Weather(unit=Unit.CELSIUS)

while True:
    inp = input('User: ')
    if inp == '':
        break
    inp = inp.title()
    if inp in chat_input:
        print('Bot: Hello, what can I do for you?')
    else:
        places = GeoText(inp)
        city = places.cities
        if city:
            lookup = weather.lookup_by_location(city[0])
            condition = lookup.condition
            condition_text = condition.text
            condition_text = condition_text.replace('rain', 'rainy')
            condition_text = condition_text.replace('Showers', 'rainy')
            tokenized_words = nltk.word_tokenize(inp.lower())
            weather_condition = list({'cloudy', 'sunny', 'rainy'}.intersection(tokenized_words))
            if weather_condition:
                if weather_condition[0] in condition_text.lower():
                    print('Bot: Yes')
                    continue
                else:
                    print('Bot: No')
                    continue
            print('Bot: It is ' + condition.text.lower() + ' and ' + condition.temp + 'C now in ' + city[0])
        else:
            print('Bot: Could not understand the query')
