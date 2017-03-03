from channels.routing import route
channel_routing = [
    route("http.request", "market.consumers.http_consumer"),
]