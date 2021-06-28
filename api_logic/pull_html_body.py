import nltk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from readability import Document
import requests

def pull_body(url):
	response = requests.get(url)
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