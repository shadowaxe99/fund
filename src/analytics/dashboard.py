```python
import matplotlib.pyplot as plt
from src.analytics.response_analytics import ResponseAnalytics
from src.analytics.list_hygiene import ListHygiene
from src.analytics.reporting import Reporting
from src.analytics.roi_tracker import ROITracker

class Dashboard:
    def __init__(self, analyticsData):
        self.analyticsData = analyticsData
        self.responseAnalytics = ResponseAnalytics(analyticsData)
        self.listHygiene = ListHygiene(analyticsData)
        self.reporting = Reporting(analyticsData)
        self.roiTracker = ROITracker(analyticsData)

    def display_dashboard(self):
        self.display_campaign_metrics()
        self.display_response_metrics()
        self.display_list_hygiene_metrics()
        self.display_reporting_metrics()
        self.display_roi_metrics()

    def display_campaign_metrics(self):
        opens, clicks, unsubscribes, bounces = self.responseAnalytics.get_campaign_metrics()
        labels = ['Opens', 'Clicks', 'Unsubscribes', 'Bounces']
        sizes = [opens, clicks, unsubscribes, bounces]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Campaign Metrics')
        plt.show()

    def display_response_metrics(self):
        positive, negative, neutral = self.responseAnalytics.get_sentiment_metrics()
        labels = ['Positive', 'Negative', 'Neutral']
        sizes = [positive, negative, neutral]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Response Sentiment Metrics')
        plt.show()

    def display_list_hygiene_metrics(self):
        unsubscribes, bounces = self.listHygiene.get_list_hygiene_metrics()
        labels = ['Unsubscribes', 'Bounces']
        sizes = [unsubscribes, bounces]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('List Hygiene Metrics')
        plt.show()

    def display_reporting_metrics(self):
        workload = self.reporting.get_workload_metrics()
        plt.bar(range(len(workload)), list(workload.values()), align='center')
        plt.xticks(range(len(workload)), list(workload.keys()))
        plt.title('Team Member Workload')
        plt.show()

    def display_roi_metrics(self):
        roi = self.roiTracker.get_roi_metrics()
        plt.bar(range(len(roi)), list(roi.values()), align='center')
        plt.xticks(range(len(roi)), list(roi.keys()))
        plt.title('Campaign ROI')
        plt.show()
```