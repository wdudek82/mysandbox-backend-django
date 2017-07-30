from django.db import models
from behaviors.behaviors import Timestamped


# TODO: Add weather and smog information
# TODO: Write tools for reading this information from proper apis
# TODO: Use Celery to periodically synchonize data
class Smog(Timestamped):
    """
    Information about pollution levels in one of 24 Polish Cities recognized by id (Krakow id: 1)
    http://powietrze.malopolska.pl/_powietrzeapi/api/dane?act=danemiasta&ci_id=01
    """
    pass


class Weather(Timestamped):
    """
    Weather info from external API (https://openweathermap.org/api)
    synched using Celery
    """
    pass