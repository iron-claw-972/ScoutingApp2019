from flask import render_template
import time


def matchSchedule(scraper):
    # currentTime = time.time()
    currentTime = 1521331740
    scraper = scraper.DataScraper()
    url = scraper.getWebcastUrl(scraper.SFeventKey)
    print(url)
    results = scraper.getMatches(scraper.SFeventKey, currentTime)[0:2]

    a1 = results[0]
    a2 = results[1]
    AP1 = ', '.join([e for e in (a1['alliances']['red']['team_keys'] if 'frc972' in a1['alliances']
                                 ['red']['team_keys'] else a1['alliances']['blue']['team_keys']) if e != 'frc972'])

    OT1 = ', '.join([e for e in (a1['alliances']['red']['team_keys'] if 'frc972' not in a1['alliances'][
        'red']['team_keys'] else a1['alliances']['blue']['team_keys']) if e != 'frc972'])
    T1 = str(a1['time']-currentTime)

    AP2 = ', '.join([e for e in (a2['alliances']['red']['team_keys'] if 'frc972' in a2['alliances'][
        'red']['team_keys'] else a2['alliances']['blue']['team_keys']) if e != 'frc972'])
    OT2 = ', '.join([e for e in (a2['alliances']['red']['team_keys'] if 'frc972' not in a2['alliances'][
        'red']['team_keys'] else a2['alliances']['blue']['team_keys']) if e != 'frc972'])
    T2 = str(a2['time']-currentTime)
    return AP1, OT1, T1, AP2, OT2, T2, url
