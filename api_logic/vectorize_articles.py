from sync_w_api import get_articles
import pickle 
import pandas as pd
import numpy
import re
import os
import numpy as np
import gensim
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from gensim.models import Doc2Vec

def preprocess(df):
	LabeledSentence1 = gensim.models.doc2vec.TaggedDocument
	all_content_train = []
	j=0

	for em in df["complete"].values:
		all_content_train.append(LabeledSentence1(em,[j]))
		j+=1
	print("Processed " + str(j) + " texts")
	return all_content_train

def define_doc2vec(all_content_train):
	d2v_model = Doc2Vec(all_content_train, vector_size=100, window=10, min_count=500, workers=7, dm=1, alpha=0.025, min_alpha=0.001)

	d2v_model.train(all_content_train, total_examples=d2v_model.corpus_count, epochs=10, start_alpha=0.002, end_alpha=-0.016)
	return d2v_model

def kmean_cluster(d2v_model):
	kmeans_model = KMeans(n_clusters=4, init="k-means++",max_iter=100)
	X = kmeans_model.fit(d2v_model.dv.get_normed_vectors())
	labels = kmeans_model.labels_.tolist()
	
	l = kmeans_model.fit_predict(d2v_model.dv.get_normed_vectors())
	return (labels,l)



articles = get_articles()
article_df = pd.DataFrame(articles)
all_content_train = preprocess(article_df)
d2v_model = define_doc2vec(all_content_train)
labels, l = kmean_cluster(d2v_model)
print(labels)
print(l)

