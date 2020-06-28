import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
	def __init__(self, width: int, height: int):
		self.width, self.height = width, height
		
		# creates a 2d array filled with floor tiles
		self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")

		# adding a few walls just for testing
		self.tiles[30:33, 22] = tile_types.wall
		
	def in_bounds(self, x: int, y: int) -> bool:
		"""Return True if x and y are inside of the bounds of this map."""
		return 0 <= x < self.width and 0 <= y < self.height

	# renders the entire map using tiles_rgb, much faster than the print we use in instances
	def render(self, console: Console) -> None:
		console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]