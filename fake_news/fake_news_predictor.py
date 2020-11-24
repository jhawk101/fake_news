import pickle

RED_BOUND = 0.6
GREEN_BOUND = 0.4

class FakeNews:
    def __init__(self, title, body):
        self.text = title + " " + body
    
    @property
    def _tfidf_transform(self):
        with open("fake_news/models/tfidf.pk", "rb") as f:
            vec = pickle.load(f)

        return vec.transform([self.text])
    
    @property
    def score(self):
        with open("fake_news/models/logreg.pk", "rb") as f:
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

