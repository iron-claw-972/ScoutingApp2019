from flask import render_template
import time


def matchSchedule(scraper):
    currentTime = time.time()
    results = scraper.getMatches(scraper.SFeventKey, currentTime)
