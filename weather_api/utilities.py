from weather_api.temperature import Temperature


def get_temp_info(data, days, city) -> Temperature:
    """This method extracts hourly temperature from the response"""
    weather_data = data.get('forecast', {}).get('forecastday', [])
    day_temperatures = []
    for day in weather_data:
        for hour in day['hour']:
            day_temperatures.append(hour.get('temp_c'))

    temp_data = Temperature(
        city=city,
        days=days,
        data=day_temperatures,
    )
    return temp_data
