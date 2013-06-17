all: data/yelp/reviews_100.json

data/yelp/reviews_100.json:
	head -n 100 data/yelp/yelp_academic_dataset_review.json > data/yelp/reviews_100.json
