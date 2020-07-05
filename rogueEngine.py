from typing import Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

# this class will act as engine for the roguelike, drawing everything and handlind input
class Engine:
	def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
		self.event_handler= event_handler
		self.game_map = game_map
		self.player= player
		self.update_fov()
		
	# Just input events, getting the appropiate action in each case
	def handle_events(self, events: Iterable[Any])-> None:
		for event in events:
			action = self.event_handler.dispatch(event)
			
			if action is None:
				continue
			
			# now for the resulting actiosn from input (movement, quitting etc), the action must perform its own logic!
			action.perform(self, self.player)
			
			self.update_fov() # update fov before player next action
			
	def update_fov(self) -> None:
		"""Recompute the visible area based on the players point of view."""
		self.game_map.visible[:] = compute_fov(
			self.game_map.tiles["transparent"],
			(self.player.x, self.player.y),
			radius=8,
		)
		# If a tile is "visible" it should be added to "explored".
		self.game_map.explored |= self.game_map.visible
				
	# Just to draw
	def render(self, console: Console, context: Context) -> None:
		#render the map first
		self.game_map.render(console)
			
		context.present(console)
		
		console.clear()