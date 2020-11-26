import pickle

RED_BOUND = 0.6
GREEN_BOUND = 0.4

class FakeNews:
    def __init__(self, title, body:str=""):
        self.title_model = len(body) == 0
        self.text = title + " " + body
    
    @property
    def _tfidf_transform(self):
        if self.title_model:
            tfidf_path = "fake_news/models/tfidf_titles.pk"
        else:
            tfidf_path = "fake_news/models/tfidf.pk"

        with open(tfidf_path, "rb") as f:
            vec = pickle.load(f)

        return vec.transform([self.text])
    
    @property
    def score(self):
        if self.title_model:
            model_path = "fake_news/models/logreg_titles.pk"
        else:
            model_path = "fake_news/models/logreg.pk"

        with open(model_path, "rb") as f:
            clf = pickle.load(f)

        return clf.predict_proba(self._tfidf_transform)[0, 1]

    @property
    def RAG(self):
        if self.score >= RED_BOUND:
            return "Red"
        elif self.score >= GREEN_BOUND:
            return "Amber"
        else:
            return "Green" 

