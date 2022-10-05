# anilist-ml

Learning the basics of machine learning with Anilist data

## Summary

I originally set out to make a model trained on my Anilist data that was able
to predict the score (1-10) that I would probably give an anime.

At first I tried to make a regression, but soon realized that since I was only rating 1-10,
I would probably have more accuracy using a classifier.

The best I was able to pull off was a random forest classifier with accuracy ~0.38.
I think my data is kind of bad since I tend to give scores of 7 too much and I only had ~500 data points.

After messing around for a while I decided to switch to a binary classification; Would I recommend or don't recommend?
TODO: results

Someone knowledgeable in machine learning could probably point out what I was doing wrong immediately.
But, oh well this was my first project and I have a lot to learn. This wasn't exactly a win, but hopefully the next
ML project goes better.

### Notebooks

1. [fetch.ipynb](fetch.ipynb) - Fetches user and anime data using Anilist's GraphQL API.
2. [clean.ipynb](clean.ipynb) - Cleans fetched data to prepare for data visualization and model training.
3. [explore.ipynb](explore.ipynb) - Some data visualizations and general exploration of data.
4. [model-selection.ipynb](model-selection.ipynb) - Testing out different models and selecting what seems to perform the best.
5. [model-final.ipynb](model-final.ipynb) - Final model training, verification, and presenting.

## Data

- fetched
  - [data/anime-YYYYMMDD-raw.csv](data/anime-20220927-raw.csv) - raw Anilist anime data
  - [data/user-YYYYMMDD-raw.csv](data/user-20220927-raw.csv) - raw Anilist user data
- cleaned/enriched
  - [data/anime-YYYYMMDD-clean.csv](data/anime-20220927-clean.csv) - cleaned anime data; usesless columns dropped and missing data filled
  - [data/user-YYYYMMDD-clean.csv](data/user-20220927-clean.csv) - cleaned user data; useless columns dropped
  - [data/user-YYYYMMDD-enriched.csv](data/user-20220927-enriched.csv) - user data joined with anime data
- regression
  - [data/user-YYYYMMDD-reg-train.csv](data/user-20220927-reg-train.csv) - train data for regression models
  - [data/user-YYYYMMDD-reg-valid.csv](data/user-20220927-reg-valid.csv) - validation data for regression models
  - [data/user-YYYYMMDD-reg-test.csv](data/user-20220927-reg-test.csv) - test data for regression models
- classification
  - [data/user-YYYYMMDD-cls-train.csv](data/user-20220927-cls-train.csv) - train data for classifier models
  - [data/user-YYYYMMDD-cls-valid.csv](data/user-20220927-cls-valid.csv) - validation data for classifier models
  - [data/user-YYYYMMDD-cls-test.csv](data/user-20220927-cls-test.csv) - test data for classifier models

## References

- [Anilist Interactive GraphQL Tool](https://anilist.co/graphiql)
- [Anilist GraphQL Documentation Explorer](https://anilist.github.io/ApiV2-GraphQL-Docs/)
- [Coursera Machine Learning Specialization (Andrew Ng)](https://www.coursera.org/specializations/machine-learning-introduction)
- [Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow. Geron](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646)
