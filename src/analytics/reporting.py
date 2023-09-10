```python
import pandas as pd
from src.response_handling.response_analyzer import ResponseAnalyzer

class Reporting:
    def __init__(self, analyticsData):
        self.analyticsData = analyticsData
        self.responseAnalyzer = ResponseAnalyzer()

    def team_member_workload(self):
        # Get the response data
        response_data = self.analyticsData['responseData']

        # Create a DataFrame from the response data
        df = pd.DataFrame(response_data)

        # Group by team member and count the number of responses
        workload_report = df.groupby('team_member')['response'].count()

        return workload_report

    def roi_tracking(self, campaignData, revenueData):
        # Get the campaign and revenue data
        campaign_data = campaignData
        revenue_data = revenueData

        # Create DataFrames from the campaign and revenue data
        df_campaign = pd.DataFrame(campaignData)
        df_revenue = pd.DataFrame(revenueData)

        # Merge the campaign and revenue data on campaign ID
        df_merged = pd.merge(df_campaign, df_revenue, on='campaign_id')

        # Calculate ROI by dividing revenue by cost for each campaign
        df_merged['roi'] = df_merged['revenue'] / df_merged['cost']

        return df_merged[['campaign_id', 'roi']]

    def response_analysis_report(self):
        # Get the response data
        response_data = self.analyticsData['responseData']

        # Analyze the responses
        analysis = self.responseAnalyzer.analyze_responses(response_data)

        return analysis
```