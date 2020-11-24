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

Read `Model explanation.html` to see how the model was derived.

To explore the model code, download the train data from [kaggle](https://www.kaggle.com/c/fake-news/data) and add to `fake_news/data` . Then run:

``` bash
jupyter notebook
```

To change the bands for RAGing the scores, see the globals in `fake_news/fake_news_predictor.py`

## Testing

This will run the model tests, the test shows how to instantiate a `FakeNews` class and obtain a prediction.

``` bash
poetry run pytest
```
