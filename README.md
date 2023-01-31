# google_apis

## YouTube Analytics Examples

**Example #1**

```python
import os
import pandas as pd
from google_apis.gdrive import GDrive
from google_apis.ytube_analytics import YouTubeAnalytics

client_file = 'client-secret.json'

yt_analytics = YouTubeAnalytics(client_file)
yt_analytics.init_service()

report = yt_analytics.run_report(
    '2009-11-01',
    '2022-11-30',
    ['views', 'estimatedMinutesWatched', 'estimatedRevenue', 'likes', 'dislikes', 
     'comments', 'subscribersGained', 'subscribersLost'],
     'day'
)
df = pd.DataFrame(data=report['rows'], columns=report['columns'])
```
