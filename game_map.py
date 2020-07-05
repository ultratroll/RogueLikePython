import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
	def __init__(self, width: int, height: int):
		self.width, self.height = width, height
		
		# creates a 2d array filled with wall tiles, our algorithm will carve out rooms and tunnels
		self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")
		self.visible = np.full((width, height), fill_value= False, order= "F") # tiles the player can see
		self.explored = np.full((width, height), fill_value= False, order= "F") # tiles the player has explored
		
	def in_bounds(self, x: int, y: int) -> bool:
		"""Return True if x and y are inside of the bounds of this map."""
		return 0 <= x < self.width and 0 <= y < self.height

	# renders the entire map using tiles_rgb, much faster than the print we use in instances
	def render(self, console: Console) -> None:
		"""
		Renders the map.
 
		If a tile is in the "visible" array, then draw it with the "light" colors.
		If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
		Otherwise, the default is "SHROUD".
		"""
		console.tiles_rgb[0:self.width, 0:self.height] = np.select(
			condlist=[self.visible, self.explored],
			choicelist=[self.tiles["light"], self.tiles["dark"]],
			default=tile_types.SHROUD
		)