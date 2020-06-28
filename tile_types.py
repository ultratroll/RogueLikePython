from typing import Tuple

import numpy as np  # type: ignore

#dtypes are similar to structs

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
	[
		("ch", np.int32),  #CHARACTER: Unicode codepoint.
		("fg", "3B"),  #FOREGROUND COLOR(3B means 3 unsinged bytes, used for RGB) 3 unsigned bytes, for RGB colors.
		("bg", "3B"),  #BACKGROUND COLOR(3B means 3 unsinged bytes, used for RGB)
	]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
	[
		("walkable", np.bool),  # True if this tile can be walked over.
		("transparent", np.bool),  # True if this tile doesn't block FOV.
		("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
	]
)

# Construction of a tile type
def new_tile(
	*,  # Enforce the use of keywords, so that parameter order doesn't matter.
	walkable: int,
	transparent: int,
	dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
	"""Helper function for defining individual tile types """
	return np.array((walkable, transparent, dark), dtype=tile_dt)
	
floor = new_tile(
	walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
	walkable=False, transparent=False, dark=(ord("#"), (255, 255, 255), (0, 0, 100)),
)