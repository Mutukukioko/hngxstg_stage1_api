import json
import datetime
from django.http import JsonResponse

def api_endpoint(request, slack_name, track):
    # Get the current day of the week and current UTC time.
    current_day = datetime.datetime.now().strftime('%A')
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    # Define the GitHub repo URL and file URL.
    github_repo_url = 'https://github.com/your_username/your_repo'
    github_file_url = f'{github_repo_url}/blob/master/path/to/your/file.py'

    # Create the JSON response.
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_utc_time,
        'track': track,
        'github_repo_url': github_repo_url,
        'github_file_url': github_file_url,
        'status_code': 200
    }

    return JsonResponse(response_data)
