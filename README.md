# anilist-ml

Practicing machine learning with Anilist data

## Summary

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
  - [data/user-YYYYMMDD-train-reg.csv](data/user-20220927-reg-train.csv) - train data for regression models
  - [data/user-YYYYMMDD-valid-reg.csv](data/user-20220927-reg-valid.csv) - validation data for regression models
  - [data/user-YYYYMMDD-test-reg.csv](data/user-20220927-reg-test.csv) - test data for regression models

## References

- [Anilist Interactive GraphQL Tool](https://anilist.co/graphiql)
- [Anilist GraphQL Documentation Explorer](https://anilist.github.io/ApiV2-GraphQL-Docs/)
- [Coursera Machine Learning Specialization (Andrew Ng)](https://www.coursera.org/specializations/machine-learning-introduction)
- [Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow. Geron](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646)
