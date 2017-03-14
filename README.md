# stockmarket
Charting stock market data in real time with new Django websockets

## How to run

- start interface server : 
daphne stockmarket.asgi:channel_layer

- start channel layer ( redis ): ( start as a deamon for testing purpose )
redis-server

- start worker processes ( verbose ):
python manage.py runworker -v2