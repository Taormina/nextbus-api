#nextbus-api

An API for GT's NextBus Application.

##Dependicies

- Python 2.7
+ web.py
+ BeautifulSoup4

##Request Syntax
>GET /route/destination/stop

##Response Syntax
###If valid:
>{"predictions":["Arr.", 6, 12, 18]}

The array consists of "Arr." for Arriving, "Dep." for Departing, or a integer for a time estimation.

###If invalid:
>{"predictions":"error"}

###Live Site
>http://quiet-fjord-4717.herokuapp.com/route/direction/stop

>[http://quiet-fjord-4717.herokuapp.com/red/clockwise/fitten](http://quiet-fjord-4717.herokuapp.com/red/stuff/fitten)
