import json
import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET  # Ensure the view only accepts GET requests
def api_endpoint(request):
    # Get the query parameters slack_name and track from the request's GET parameters.
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', '')

    # Check if both slack_name and track parameters are provided.
    if not slack_name or not track:
        return JsonResponse({'error': 'Both slack_name and track parameters are required.'}, status=400)

    # Get the current day of the week and current UTC time.
    current_day = datetime.datetime.now().strftime('%A')
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

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