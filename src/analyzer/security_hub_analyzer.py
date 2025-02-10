# src/analyzer/security_hub_analyzer.py
import boto3
from datetime import datetime, timedelta

class SecurityHubAnalyzer:
    def __init__(self, region_name='us-east-1'):
        self.security_hub = boto3.client('securityhub', region_name=region_name)
        
    def get_critical_findings(self, days=7):
        start_time = datetime.now() - timedelta(days=days)
        
        response = self.security_hub.get_findings(
            Filters={
                'SeverityLabel': [{'Value': 'CRITICAL', 'Comparison': 'EQUALS'}],
                'UpdatedAt': [
                    {
                        'Start': start_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                        'End': datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
                    }
                ]
            }
        )
        return response['Findings']
