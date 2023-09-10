```python
import pandas as pd
from src.analytics.dashboard import analyticsData

class ROITracker:
    def __init__(self):
        self.campaign_roi = {}

    def calculate_roi(self, campaign_id):
        campaign_data = analyticsData[campaign_id]
        revenue = campaign_data['revenue']
        cost = campaign_data['cost']
        roi = (revenue - cost) / cost
        self.campaign_roi[campaign_id] = roi
        return roi

    def get_roi(self, campaign_id):
        if campaign_id not in self.campaign_roi:
            return self.calculate_roi(campaign_id)
        return self.campaign_roi[campaign_id]

    def get_all_roi(self):
        roi_df = pd.DataFrame(list(self.campaign_roi.items()), columns=['Campaign ID', 'ROI'])
        return roi_df
```