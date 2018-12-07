from city import City
from timeit import timeit

class Snowplough():
	"""
		Super high-tech snowplough that must clean all the city
	"""

	@timeit
	def clean_city(self, city: City):
		while sum([house[1] for house in city.houses]):
			break