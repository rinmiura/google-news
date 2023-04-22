import pickle
from random import randint
from datetime import datetime

import selenium.webdriver
from multiprocessing import Pool

from requests_client import get_all_urls
from models import create_schema_and_fill, CookieProfile


urls = get_all_urls()


def session_handler(profile):
    url = urls[randint(0, len(urls)-1)]
    driver = selenium.webdriver.Firefox()
    if profile.cookies_value:
        cookies = pickle.loads(profile.cookies_value)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.get(url)
    random = str(randint(2000, 5000))
    driver.execute_script("window.scrollTo(0," + random + ");")
    session.query(CookieProfile).filter(CookieProfile.id==profile.id).update({
        'cookies_value': pickle.dumps(driver.get_cookies()),
        'last_start_on': datetime.now(),
        'number_of_starts': profile.number_of_starts+1
    })
    session.commit()
    print(profile)
    driver.close()


def run():
    with Pool(2) as pool:
        profiles = session.query(CookieProfile).all()
        pool.map(session_handler, profiles)


session = create_schema_and_fill()
if __name__ == '__main__':
    run()
