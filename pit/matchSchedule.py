from flask import render_template
import time
from flask import Markup
import datetime

def sec2time(sec, n_msec=0):
    ''' Convert seconds to 'D days, HH:MM:SS.FFF' '''
    if hasattr(sec,'__len__'):
        return [sec2time(s) for s in sec]
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if n_msec > 0:
        pattern = '%%02d:%%02d:%%0%d.%df' % (n_msec+3, n_msec)
    else:
        pattern = r'%02d:%02d:%02d'
    if d == 0:
        return pattern % (h, m, s)
    return ('%d days, ' + pattern) % (d, h, m, s)

def matchSchedule(scraper):
    # currentTime = time.time()
    currentTime = time.time()
    scraper = scraper.DataScraper()
    url = scraper.getWebcastUrl(scraper.eventKey)
    print(url)
    results = scraper.getMatches(scraper.eventKey, currentTime)[0:2]

    a1 = results[0]
    a2 = results[1]
    AP1 = Markup(', '.join(['<a href="/scouting/teamPage/%s"><p style="display:inline">%s</p></a>' %
                            (e[3:], e[3:]) for e in a1['alliances']['red']['team_keys']]))
    OT1 = Markup(', '.join(['<a href="/scouting/teamPage/%s"><p style="display:inline">%s</p></a>' %
                            (e[3:], e[3:]) for e in a1['alliances']['blue']['team_keys']]))

    T1 = str(sec2time(a1['time']-currentTime,0))
    C1 = ('lightblue' if '972' in str(OT1) else '#ff4141')

    AP2 = Markup(', '.join(['<a href="/scouting/teamPage/%s"><p style="display:inline">%s</p></a>' %
                            (e[3:], e[3:]) for e in a2['alliances']['red']['team_keys']]))
    OT2 = Markup(', '.join(['<a href="/scouting/teamPage/%s"><p style="display:inline">%s</p></a>' %
                            (e[3:], e[3:]) for e in a2['alliances']['blue']['team_keys']]))

    C2 = ('lightblue' if '972' in str(OT2) else '#ff4141')

    T2 = str(sec2time(a2['time']-currentTime,0))
    return AP1, OT1, T1, AP2, OT2, T2, url, C1, C2
