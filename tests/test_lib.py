from testing.weather import *
def test_weather():
    assert type(search_city('berlin')) == str
