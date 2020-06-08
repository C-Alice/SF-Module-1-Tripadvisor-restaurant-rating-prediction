## Goal

The main aim of this competition was to show how to work with datasets and prepare them for model training. 

Participants were expected to focus on data preprocessing and feature engineering to understand how much the model depend on good and correctly prepared data. For the same reason the model itself was fixed, and no parameters altering allowed.

## Data

Initially data contained the following features:

* ```City``` - the city, where a restaurant is located;
* ```Cuisine Style``` - cuisine styles a restaurant offers;
* ```Ranking``` - rank of a restauran in the city;
* ```Price Range``` - range of prices in a restaurant;
* ```Number of Reviews``` - number of reviews for each restaurant;
* ```Reviews``` - last two reviews and their dates;
* ```URL_TA``` - page of a restaurant on 'www.tripadvisor.ru';
* ```ID_TA``` - restaurant ID on Tripadvisor;
* ```Rating``` - restaurant rating (target).

More features were added in the process. Also, some research was made to find out what this rating really depends on. It appered that the majority of effect came from individual visitors rates. So, extra features (rates) were scrapped straight from Tripadvisor web-site, resulting in 13% improvment of model performance.

One more trick for this particular case, connected with the target, was that the ratings were discrete (numbers from 1 to 5 with the step 0.5). At the same time our model was for regression and returned continuous predictions. Rounding the predictions gave it another 19% of improvement!

## For more details

- First, check the corresponding notebook: [Predict Tripadvisor restaurant rating .ipynb](https://github.com/C-Alice/SF-Module-1-Tripadvisor-restaurant-rating-prediction/blob/master/Predict%20Tripadvisor%20restaurant%20rating%20.ipynb)
- You can also take a look at the Kaggle competition [here](https://www.kaggle.com/c/kaggle-sf-dst-through-1/overview)
