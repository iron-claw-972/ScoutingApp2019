[![Build Status](https://travis-ci.com/iron-claw-972/ScoutingApp2019.svg?branch=master)](https://travis-ci.com/iron-claw-972/ScoutingApp2019)

## Setup
1. install latest version of python 3 (process depends on your machine). Installing anaconda makes it easy.
2. install flask: `pip3 install flask`
3. install sql library: `pip install mysql-connector`
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
  - scoutingHandler.py: contains all `@app.route`s for the pit
  - everything else: files that pithandler calls
- Publicity Board
  - publicityHandler.py: contains all `@app.route`s for publicity (there should only be one or two pages)
  - everything else: files that pithandler calls
- templates
  - all html files for :
    - pit
    - scouting
    - publicity
- static
  - all resources for front end access
    - css
    - js
    - images
    - ...
  
## Scouting App Requirements

### Scouting App
- [x] Match Scouting
- [x] Match Data
- [ ] Robot-Picking Data
- [x] Pit Scouting
- [x] Specific Bot Data
- [ ] ToN oF bIG dAtA?

### Hardware
- [x] 25" Touch Screen for publicity board
- [x] Pit Monitor for pit display

### Publicity Board
- [x] Sponsors
- [ ] Tech Binder
- [ ] Business Plan
- [x] interactive CAD

### Pit Display
- [x] Team Match Schedule
- [x] SA data for match prep
- [x] Livestream
- [ ] Battery Tracker

## TODO
- [x] UI for match input
- [X] UI for pit input
- [x] Database utility
- [x] Data output for matches
- [x] Data output for pits
- [x] Reformat database to match new design (Pranav)
- [x] Make pit scouting work (Alan)
- [x] Team page ui to encorporate more data (Holden)
- [x] Publicity board outline (more details) (Alexis and Dawson)
- [x] add more to todo (Holden)
- [x] get robot cad in step (Ethan)
- [x] fix travis building (Holden)

### Misc.
- [ ] move configurations from app.py to config.py
- [ ] configure production WSGI server
- [x] configure proper unit testing and travis integration
