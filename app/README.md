This project uses play by play NBA data to predict future games, specifically the spread between 2 teams (as defined by a set of players).  

The data can be downloaded directly from Kaggle here (https://www.kaggle.com/schmadam97/nba-playbyplay-data-20182019)

Run get_data.py, then data_wrangling.py to create our dataset.  You'll also need postgres installed to properly use the databaseClass file.  

Once you have generated the dataset, the modeling.ipynb notebook goes through our modeling process.  Our data representation contains high dimensions, which are also sparse.  This is because we use each player and each game dimension (e.g, points, rebounds, shots, etc) as features.  This high dimensional representation is a perfect case for PCA.  We model off of our reduced dataset.  

Finally, in order to serve the model, you can run app.py, and in order to get predctions, you can run requests.py