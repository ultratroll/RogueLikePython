from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

#new class to handle input events that inherits from tcod.event.EventDispatch[Action]
class EventHandler(tcod.event.EventDispatch[Action]):
	
	#override when we press the x button in the window
	def ev_quit(self, event:tcod.event.Quit) -> Optional[Action]:
		raise SystemExit()
		
	#override to handle key inputs
	def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
		action: Optional[Action] = None
		
		#key that was pressed
		key= event.sym
		
		if key== tcod.event.K_UP:
			action = MovementAction(dx=0, dy=-1)
		elif key== tcod.event.K_DOWN:
			action = MovementAction(dx=0, dy=1)
		elif key== tcod.event.K_LEFT:
			action = MovementAction(dx=-1, dy=0)
		elif key== tcod.event.K_RIGHT:
			action = MovementAction(dx=1, dy=0)
			
		elif key== tcod.event.K_ESCAPE:
			action = EscapeAction()
			
		#No valid key was pressed
		return action