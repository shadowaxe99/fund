```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class ResponseAnalytics:
    def __init__(self, responseData):
        self.responseData = responseData

    def get_sentiment_distribution(self):
        positive_count = sum(1 for resp in self.responseData if resp['sentiment'] == 'positive')
        negative_count = sum(1 for resp in self.responseData if resp['sentiment'] == 'negative')
        neutral_count = sum(1 for resp in self.responseData if resp['sentiment'] == 'neutral')
        return {'positive': positive_count, 'negative': negative_count, 'neutral': neutral_count}

    def get_topic_distribution(self):
        vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
        tf = vectorizer.fit_transform([resp['text'] for resp in self.responseData])
        lda = LatentDirichletAllocation(n_components=10, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)
        feature_names = vectorizer.get_feature_names_out()
        topics = dict()
        for topic_idx, topic in enumerate(lda.components_):
            topics[topic_idx] = [feature_names[i] for i in topic.argsort()[:-10 - 1:-1]]
        return topics

    def get_question_count(self):
        return sum(1 for resp in self.responseData if '?' in resp['text'])

    def get_response_load(self):
        response_load = dict()
        for resp in self.responseData:
            if resp['assigned_to'] in response_load:
                response_load[resp['assigned_to']] += 1
            else:
                response_load[resp['assigned_to']] = 1
        return response_load
```