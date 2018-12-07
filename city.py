from random import sample
from enum import Enum

class City():
	nb_houses = 0
	min_distance = 0
	max_distance = 0
	houses = None
	position_range = None

	def __init__(self, nb_houses=1000, position_range=(-5000, 5000)):
		houses_position = None
		houses_state = None

		self.nb_houses = nb_houses
		self.position_range = position_range

		# Generates a sorted list of unique random relatives integers
		self.houses_position = sorted(sample(range(*position_range), nb_houses))

		# 0 for cleaned, 1 for snowy
		# This form of initialization for same element is way faster than list comprehension
		self.houses_state = [1] * nb_houses

		# Associate each position with a state (houses is a list of tuples)
		self.houses = [elem for elem in zip(self.houses_position, self.houses_state)]

	def __str__(self):
		houses_cleared = self.nb_houses - sum([house[1] for house in self.houses])
		return "Map of {} houses reparted from {} to {}. {} house{} cleared".format(
				self.nb_houses,
				*self.position_range,
				houses_cleared,
				"s" if houses_cleared != 1 else ""
			)