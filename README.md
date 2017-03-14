# stockmarket
Charting stock market data in real time with new Django websockets

![indexsnap](https://cloud.githubusercontent.com/assets/3438538/23888603/d8822670-08ae-11e7-9fde-7d7f07e8e330.png)

See [Live Demo](https://stockmarket15.herokuapp.com)

## How to run

- start interface server : 
daphne stockmarket.asgi:channel_layer

- start channel layer ( redis, start as a deamon for testing purpose ) : 
redis-server

- start worker processes ( verbose ) : 
python manage.py runworker -v2


## Technology Stack

- Django ( backend )
- django-channels ( websockets with http )
- redis ( channel layer )
- react ( dynamic frontend )
- webpack 2 ( compile react es6 code with babel )

## To Do

- Change frontend charting library, current library can not chart more than 5 stock's data
- Session management, show stocks choosen by logged user and that user group only
