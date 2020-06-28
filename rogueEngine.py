from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

# this class will act as engine for the roguelike, drawing everything and handlind input
class Engine:
	def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
		self.entities= entities
		self.event_handler= event_handler
		self.game_map = game_map
		self.player= player
		
	# Just input events, getting the appropiate action in each case
	def handle_events(self, events: Iterable[Any])-> None:
		for event in events:
			action = self.event_handler.dispatch(event)
			
			if action is None:
				continue
			
			# now for the resulting actiosn from input (movement, quitting etc), the action must perform its own logic!
			action.perform(self, self.player)
				
	# Just to draw
	def render(self, console: Console, context: Context) -> None:
		#render the map first
		self.game_map.render(console)
		
		for entity in self.entities:
			console.print(entity.x, entity.y, entity.char, fg= entity.color)
			
		context.present(console)
		
		console.clear()