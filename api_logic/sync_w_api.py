import requests

root = "http://127.0.0.1:8000/"


def get_articles():
	response = requests.get(root+"api/articles")
	return response.json()

def post_article(title,url,summary,complete):
	article = {
		"title":title,
		"url":url,
		"summary":summary,
		"complete":complete,
	}

	r = requests.post(root+"api/articles/", article)
	print(r)
