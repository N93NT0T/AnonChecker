import string
import random
import time
import sys
from threading import Thread

import requests
from fake_useragent import UserAgent
from colorama import init, Fore



class SessionBuilder:
    headers = {
        'Host': 'anonfiles.com',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": UserAgent().random,
        "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        'Connection': 'keep-alive'
    }

    @staticmethod
    def build():
        session = requests.Session()
        session.headers.update(SessionBuilder.headers)
        return session







workers = []
running = True


def worker_thread():
    
    while running:
        try:
            url = "https://anonfiles.com/" + "".join(
                random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.digits) for _ in
                range(10))
            session = SessionBuilder.build()

            data = session.get(url).status_code
            #print(f"{Fore.RED}{data} {Fore.YELLOW}{url}")
            if data == 200:
                print(f"{Fore.GREEN}{data} {Fore.WHITE}{url}")
                
            else:
                pass

        except:
            pass

        time.sleep(1 / 100)


if __name__ == "__main__":
    init(True)
    for x in range(int(sys.argv[1])):
        worker = Thread(target=worker_thread)
        workers.append(worker)
    for w in workers:
        w.start()
    print(f"{Fore.WHITE}Anon{Fore.RED}Checker{Fore.GREEN} Started 💲 <3")
    