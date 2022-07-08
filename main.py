from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random
import string
import colorama
import pyautogui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import threading, requests, ctypes, os, time, random, string
from datetime import datetime
from colorama import Fore, Style

PATH = "C:\Stuff\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#EXCET#4508

count = 0
while (count < 999999):
  driver.get("Ytlink")
  time.sleep(30)

  