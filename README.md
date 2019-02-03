## Setup
1. install latest version of python 3 (process depends on your machine). Installing anaconda makes it easy.
2. install flask: `pip3 install flask`
3. ~install sql library: `pip3 install mysql-connector` ~
4. ~install sql~
5. install flask-ci: `pip3 install flask-ci`
6. to start the server: `python app/app.py runserver`
7. to run tests: `python app/app.py ci`
8. to access the server, go to [localhost:5000](localhost:5000)
7. all the files where you write your code (not app.py), must start with:
```python
from app import app
from flask import Flask, request
import sys
sys.path.append("..")
```
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
