```python
import redis
from src.shared_dependencies import campaignData, emailData, responseData, analyticsData

class RedisCache:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def cache_campaign_data(self, campaign_id):
        self.redis.set(f'campaign:{campaign_id}', campaignData)

    def cache_email_data(self, email_id):
        self.redis.set(f'email:{email_id}', emailData)

    def cache_response_data(self, response_id):
        self.redis.set(f'response:{response_id}', responseData)

    def cache_analytics_data(self, analytics_id):
        self.redis.set(f'analytics:{analytics_id}', analyticsData)

    def get_campaign_data(self, campaign_id):
        return self.redis.get(f'campaign:{campaign_id}')

    def get_email_data(self, email_id):
        return self.redis.get(f'email:{email_id}')

    def get_response_data(self, response_id):
        return self.redis.get(f'response:{response_id}')

    def get_analytics_data(self, analytics_id):
        return self.redis.get(f'analytics:{analytics_id}')
```