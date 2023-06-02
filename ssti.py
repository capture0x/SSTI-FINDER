import random
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re
import sys


class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

color_random = [
    colors.CBLUE, colors.CVIOLET, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,
    colors.CRED, colors.CBEIGE
]
random.shuffle(color_random)

def entryy():
    x = color_random[0] + """
       ⣿⣿⣿⣿⣿⣿⣿⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣿⣿⡏⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣍⡙⢿⣿⣦⡙⠻⣿⣿⣿⡿⠁⣾⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⠛⠓⠢⡈⢿⡿⠁⣸⣿⡿⠿⢋⣴⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣯⣍⣙⡋⠠⠄⠄⠄⠄⠁⠘⠁⠄⠴⠚⠻⢿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⡿⠿⢏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣧⡴⠖⠒⠄⠁⠄⢀⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⠿⠟⣩⣴⣶⣿⣿⣶⡞⠉⣠⣇⠄⣿⣶⣦⣄⡀⠲⢿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⡿⢠⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣶⣌⠻⠿⣿⣿⣿⣿ <<   SSTI FINDER TOOL   >>
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿ <<  CODED BY TMRSWRR    >>
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ <<  INSTAGRAM==>tmrswrr >>
\n"""
    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    oo = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in oo:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    tt = " " * 6 + "░⣿" + " " * 18 + "WELCOME TO SSTI FINDER TOOL" + " " * 12 + "░⣿" + "\n\n"
    for c in tt:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    xx = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in xx:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
        


def get_parameter_from_url(url):
    pattern = r"\?([^=]+)="
    match = re.search(pattern, url)
    if match:
        parameter = match.group(1)
        return parameter
    return None
entryy()
target_url = input(colors.CVIOLET +"ex:https://xss-game.appspot.com/level1/frame?query=\nEnter the target URL: ")
parameter = get_parameter_from_url(target_url)

def check_ssti_vulnerability(url):
    print(colors.CBLUE + "Trying payloads list, please wait...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    count = 0
    vulnerable_urls = []
    with open("ssti.txt", "r", encoding="UTF-8") as file:
        payloads = file.readlines()
        try:
            while count < len(payloads):
                target_url = url + payloads[count]
                browser.get(target_url)
                print(colors.CGREEN + "Testing: " + payloads[count])
                time.sleep(random.randint(1, 3))
                count += 1
                input_element = browser.find_element(By.NAME, parameter)
                input_value = input_element.get_attribute('value')
                if "49" in input_value:
                    vulnerable_urls.append(target_url)
                    print(colors.CRED + "SSTI Vuln Url: " + target_url)
                if count == len(payloads):
                    browser.close()
        except NoSuchElementException:
            pass

    browser.quit()
    return vulnerable_urls


vulnerable_urls = check_ssti_vulnerability(target_url)

if vulnerable_urls:
    print("SSTI Vulnerability Found!")
    print("Vulnerable URLs:")
    for url in vulnerable_urls:
        print(url)
else:
    print("No SSTI Vulnerability Found.")
