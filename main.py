from city import City
from snowplough import Snowplough

#small_city = City(100, (-500, 500))
medium_city = City()
#big_city = City(10000, (-50000, 50000))
#mega_city = City(1000000, (-5000000, 5000000))

print(medium_city)

snowplough = Snowplough()
snowplough.clean_city(medium_city)

print(medium_city)