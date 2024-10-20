from geolocation import get_user_info
from forecast_metadata import get_forecast_metadata
from business_logic import API_HEADER
from forecast import get_forecast

def get_one_day_forecast():
    # Call get_user_info with parameters to get back PersonalInfo{lat, long}
    personal_info = get_user_info(address = "Hood River, Oregon")
    # print(personal_info.latitude, personal_info.longitude)

    #Use header, lat, long to get relevant weather station metadata & forecast endpoint
    forecast_metadata = get_forecast_metadata(personal_info.latitude, personal_info.longitude)
    forecast_url = forecast_metadata.forecast_url

    #Ping forecast endpoint to get forecast as .json
    forecast = get_forecast(forecast_url=forecast_url)
    todays_forecast = forecast[0].detailed_forecast
    return todays_forecast



