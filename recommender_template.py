import numpy as np
import pandas as pd
import sys # can use sys to take command line arguments

class Recommender():
    '''
    What is this class all about - write a really good doc string here
    '''
    def __init__(self, ):
        '''
        what do we need to start out our recommender system
        '''



    def fit(self, ):
        '''
        fit the recommender to your dataset and also have this save the results
        to pull from when you need to make predictions
        '''

    def predict_rating(self, ):
        '''
        makes predictions of a rating for a user on a movie-user combo
        '''

    def make_recs(self,):
        '''
        INPUT:
        _id - either a user or movie id (int)
        _id_type - "movie" or "user" (str)
        train_data - dataframe of data as user-movie matrix
        train_df - dataframe of training data reviews
        movies - movies df
        rec_num - number of recommendations to return (int)
        user_mat - the U matrix of matrix factorization
        movie_mat - the V matrix of matrix factorization
        
        OUTPUT:
        recs - (array) a list or numpy array of recommended movies like the 
                       given movie, or recs for a user_id given
        '''
        val_users = train_data_df.index
        rec_ids = create_ranked_df(movies, train_df)
        
        if _id_type == 'user':
            if _id in train_data.index:
                # Get the index of which row the user is in for use in U matrix
                idx = np.where(val_users == _id)[0][0]
                
                # take the dot product of that row and the V matrix
                preds = np.dot(user_mat[idx,:],movie_mat)
                
                # pull the top movies according to the prediction
                indices = preds.argsort()[-rec_num:][::-1] #indices
                rec_ids = train_data_df.columns[indices]
                rec_names = get_movie_names(rec_ids)
                
            else:
                # if we don't have this user, give just top ratings back
                rec_names = popular_recommendations(_id, rec_num, ranked_movies)
                
        # Find similar movies if it is a movie that is passed
        else:
            rec_ids = find_similar_movies(_id)
            rec_names = get_movie_names(rec_ids)
    
        return rec_ids, rec_names

if __name__ == '__main__':
    # test different parts to make sure it works
