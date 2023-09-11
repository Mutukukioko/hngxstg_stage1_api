import json
import datetime
from django.http import JsonResponse

def api_endpoint(request, slack_name, track):
    # Get the current day of the week and current UTC time.
    current_day = datetime.datetime.now().strftime('%A')
     # Calculate the UTC time with a +/-2 minute window.
    current_utc_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
    current_utc_time_str = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')

    # Define the GitHub repo URL and file URL.
    github_repo_url = 'https://github.com/Mutukukioko/hngxstg_stage1_api'
    github_file_url = f'{github_repo_url}/blob/main/api_1/views.py'

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
