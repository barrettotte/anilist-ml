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

- [data/anime-YYYYMMDD-raw.csv](data/anime-20220927-raw.csv)
- [data/user-YYYYMMDD-raw.csv](data/user-20220927-raw.csv)
- [data/anime-YYYYMMDD-clean.csv](data/anime-20220927-clean.csv)
- [data/user-YYYYMMDD-clean.csv](data/user-20220927-clean.csv)
- [data/user-YYYYMMDD-enriched.csv](data/user-20220927-enriched.csv)
- [data/anime-YYYYMMDD-encoded.csv](data/user-20220927-encoded.csv)

## References

- [Anilist Interactive GraphQL Tool](https://anilist.co/graphiql)
- [Anilist GraphQL Documentation Explorer](https://anilist.github.io/ApiV2-GraphQL-Docs/)
