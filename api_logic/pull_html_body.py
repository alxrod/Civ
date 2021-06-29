import nltk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from readability import Document
import requests
import signal
import threading
import sys
from wrapt_timeout_decorator import *


@timeout(3)
def send_request(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}
	try:
		return requests.get(url, headers=headers)
	except requests.exceptions.Timeout as err:
		print(err)


def pull_body(url):
	response = None
	try:
		response = send_request(url)
	except:
		print("request timed out")
	if response == None:
		return "FAILED REQUEST"
	doc = Document(response.text)

	text = doc.summary()
	soup = BeautifulSoup(text, "html.parser")

	cleaned_soup = soup.get_text()

	split_text = cleaned_soup.split("\n")
	exclude_empties = []
	for txt in split_text:
		if txt != "":
			exclude_empties.append(txt)

	return " ".join(exclude_empties)