Download `all.json` from http://www.yelp.com/dataset_challenge.

Business Objects
================

Business objects contain basic information about local businesses. The
`business_id` field can be used with the Yelp API to fetch even more
information for visualizations, but note that you'll still need to comply with
the API TOS. The fields are as follows:

```
{
  'type': 'business',
  'business_id': (a unique identifier for this business),
  'name': (the full business name),
  'neighborhoods': (a list of neighborhood names, might be empty),
  'full_address': (localized address),
  'city': (city),
  'state': (state),
  'latitude': (latitude),
  'longitude': (longitude),
  'stars': (star rating, rounded to half-stars),
  'review_count': (review count),
  'categories': [(localized category names)]
  'open': (is the business still open for business?),
}
```

Review Objects
==============

Review objects contain the review text, the star rating, and information on
votes Yelp users have cast on the review. Use `user_id` to associate this
review with others by the same user. Use `business_id` to associate this review
with others of the same business.

```
{
  'type': 'review',
  'business_id': (the identifier of the reviewed business),
  'user_id': (the identifier of the authoring user),
  'stars': (star rating, integer 1-5),
  'text': (review text),
  'date': (date, formatted like '2011-04-19'),
  'votes': {
    'useful': (count of useful votes),
    'funny': (count of funny votes),
    'cool': (count of cool votes)
  }
}
```

User Objects
============

User objects contain aggregate information about a single user across all of
Yelp (including businesses and reviews not in this dataset).

```
{
  'type': 'user',
  'user_id': (unique user identifier),
  'name': (first name, last initial, like 'Matt J.'),
  'review_count': (review count),
  'average_stars': (floating point average, like 4.31),
  'votes': {
    'useful': (count of useful votes across all reviews),
    'funny': (count of funny votes across all reviews),
    'cool': (count of cool votes across all reviews)
  }
}
```

Checkin Objects
===============

```
{
	'type': 'checkin',
	'business_id': (encrypted business id),
	'checkin_info': {
		'0-0': (number of checkins from 00:00 to 01:00 on all Sundays),
		'1-0': (number of checkins from 01:00 to 02:00 on all Sundays),
		...
		'14-4': (number of checkins from 14:00 to 15:00 on all Thursdays),
		...
		'23-6': (number of checkins from 23:00 to 00:00 on all Saturdays)
	} # if there was no checkin for a hour-day block it will not be in the dict
}
```
