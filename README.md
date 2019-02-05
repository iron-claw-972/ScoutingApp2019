[![Build Status](https://travis-ci.com/iron-claw-972/ScoutingApp2019.svg?branch=master)](https://travis-ci.com/iron-claw-972/ScoutingApp2019)

## Setup
1. install latest version of python 3 (process depends on your machine). Installing anaconda makes it easy.
2. install flask: `pip3 install flask`
3. ~~install sql library: `pip3 install mysql-connector`~~
4. ~~install sql~~
5. install flask-ci: `pip3 install flask-ci`
6. to start the server: `python app/app.py runserver`
7. to run tests: `python app/app.py ci`
8. to access the server, go to [localhost:5000](http://localhost:5000)
9. (optional) configure environment variable FLASK_ENV="development" to run in development mode and get rid of the warning and get some dev features

## Code Structure
- Pit
  - pitHandler.py: contains all `@app.route`s for the pit (there should only be one or two pages)
  - everything else: files that pithandler calls
- Scouting
  - scoutingHandler.py: contains all `@app.route`s for the pit (there should only be one or two pages)
  - everything else: files that pithandler calls
- Publicity Board
  - Since this should just be a few html files, the handlers can go in `publicityBoard.py`
  
## Scouting App Requirements

### Scouting App
- [ ] Match Scouting
- [ ] Match Data
- [ ] Robot-Picking Data
- [ ] Pit Scouting
- [ ] Specific Bot Data
- [ ] ToN oF bIG dAtA?

### Hardware
- [ ] Computer
- [ ] 25" Touch Screen
- [ ] Pit Monitor
- [ ] Internet x2
- [ ] Cellular Hotspots
- [ ] Battery Charger Sensors

### Publicity Board
- [ ] Sponsors
- [ ] Tech Binder
- [ ] "Business Plan"
- [ ] CAD (interactive)

### Pit Display
- [ ] Team Match Schedule
- [ ] SA data for match prep
- [ ] Livestream
- [ ] Battery Tracker

## TODO
### Misc.
- [ ] move configurations from app.py to config.py
- [ ] configure production WSGI server
