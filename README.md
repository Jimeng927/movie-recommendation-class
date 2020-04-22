Building recommendation systems for movies

Instantiate - fit - predict rating 

Run the recommendation class from terminal:

1. `ipython`
2. `from recommender import Recommender`
3. `rec = Recommender()` # Initiate data
4. `rec.fit('train_data.csv','movies_clean.csv')` # fit data
5. `rec.make_recommendations()` # predict, input:  _id, _id_type, eg. rec.make_recommendations(37287, _id_type = 'user')
