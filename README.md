# Fake News classifier

## Dependencies

### Prerequisites

Ensure you have on your system:

* `pip` v3
* `python` v3.6
* `poetry`

### Install dependencies

``` bash
# Install dependencies via poetry
poetry install

# Spawn new shell within virtualenv.
poetry shell
```

## Model

Read [this notebook](Model%20explanation.ipynb) to see how the model was derived.

To explore the model code, download the train data from [kaggle](https://www.kaggle.com/c/fake-news/data) and add to `fake_news/data` . Then run:

``` bash
jupyter notebook
```

To change the bands for RAGing the scores, see the globals in `fake_news/fake_news_predictor.py`

### Title only model

If a `FakeNews` class is instantiated with a single string, it's assumed to be the title of an article and will return a score based on a model build with just titles, see [headline model](headline%20model.ipynb) for code to build.

## Testing

This will run the model tests, the test shows how to instantiate a `FakeNews` class and obtain a prediction.

``` bash
poetry run pytest
```
