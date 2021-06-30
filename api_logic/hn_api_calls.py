import requests

import time

from operator import itemgetter

from pull_html_body import pull_body
from pysummarizer_test import sum_text

from sync_w_api import get_articles, post_article, update_article

from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


def get_top_stories(depth=10):
	url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
	r = requests.get(url)

	print({"Status Code": r.status_code})
	
	article_ids = r.json()
	articles_dicts = []

	for article_id in article_ids[:depth]:
		url = 'https://hacker-news.firebaseio.com/v0/item/' + str(article_id) + '.json'
		article_r = requests.get(url)

		print(article_r.status_code)

		one_article = article_r.json()
		if "url" in one_article.keys():
			article_dict = {
				"title": one_article["title"],
				"url": one_article["url"]
			}

			articles_dicts.append(article_dict)

	return articles_dicts




if __name__ == '__main__':
	while True:
		print("Making database population run")
		articles = get_top_stories(100)
		existing_articles = get_articles()
		existing_titles = []

		hn_articles_dict = {}
		count = 0 
		for art in articles:
			art["rank"] = count
			hn_articles_dict[art["title"]] = art
			count+=1

		db_articles_dict = {}
		for art in existing_articles:
			db_articles_dict[art["title"]] = art

		for art in existing_articles:
			existing_titles.append(art["title"])

		for title, art in db_articles_dict.items():
			if title in hn_articles_dict.keys():
				print("Article exists, updating")
				art["hn_rank"] = hn_articles_dict[title]["rank"]
			else:
				print("Article is not in top 100")
				art["hn_rank"] = -1

			update_article(art, art["id"])



		for article in articles:
			if article["title"] not in existing_titles:

				print("\n"+article["title"])
				print("-------------------------------------")
				text = pull_body(article["url"])
				if text != "FAILED REQUEST":
					summary = sum_text(text)
			
					post_article(
						article["title"],
						article["url"],
						summary,
						text
					)
				else:
					print("Failed summary")

		print("Sleeping before rechecking")	
		time.sleep(60)


