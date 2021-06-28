import requests

from operator import itemgetter

from pull_html_body import pull_body
from pysummarizer_test import sum_text

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
				"Title": one_article["title"],
				"url": one_article["url"]
			}

			articles_dicts.append(article_dict)

	return articles_dicts




if __name__ == '__main__':
	articles = get_top_stories(5)
	text = pull_body(articles[1]["url"])
	sum_text(text)