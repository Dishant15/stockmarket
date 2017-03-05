from channels.routing import route
from market.consumers import (
	ws_message,
	ws_add,
	ws_disconnect,
)

channel_routing = [
	route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]