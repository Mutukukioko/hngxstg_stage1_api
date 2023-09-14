# hngxstg_stage1_api

```markdown
# API Endpoint Documentation

This repository contains a Django-based API endpoint that provides specific information in JSON format based on the provided query parameters.

## 🚀 Getting Started

To use this API, you can make GET requests to the following endpoint:

```
http://example.com/api/?slack_name=<slack_name>&track=<track>
```

Replace `<slack_name>` and `<track>` with the values you want to query.

## 🔍 Query Parameters

- `slack_name`: The name you want to query (e.g., "example_name").
- `track`: The track you want to query (e.g., "backend").

Both `slack_name` and `track` parameters are required. If either of them is missing, the API will return a 400 Bad Request response.

## 📋 Response Format

The API response is in JSON format and includes the following fields:

- `slack_name`: The slack_name parameter from the request.
- `current_day`: The current day of the week (e.g., "Monday," "Tuesday").
- `current_utc_time`: The current UTC time.
- `track`: The track parameter from the request, mapped to a letter.
- `github_repo_url`: The link to the main page of the GitHub repository.
- `github_file_url`: The link to the specific file in the GitHub repository.
- `status_code`: The HTTP status code (200 for success).

## Examples

### 📡 Request

```
GET http://example.com/api/?slack_name=example_name&track=backend
```

### 📢 Response

```json
{
    "slack_name": "example_name",
    "current_day": "Monday",
    "current_utc_time": "2023-09-08 12:00:00",
    "track": "B",
    "github_repo_url": "https://github.com/your_username/your_repo",
    "github_file_url": "https://github.com/your_username/your_repo/blob/master/path/to/your/file.py",
    "status_code": 200
}
```

## 🛠️ Development

To run this API locally for development purposes, follow these steps:

1. Clone this repository.
2. Create a virtual environment and install the required dependencies.
3. Configure your Django settings (database, security settings, etc.).
4. Run the Django development server.
5. Access the API endpoint locally at `http://localhost:8000/api/`.

## 🌐 Deployment

To deploy this API in a production environment, consider using web hosting services, cloud platforms, or containerization technologies. Ensure you configure your Django settings for production, secure your server, and manage your application's dependencies.

## 🤝 Contributing

Feel free to contribute to this project by submitting pull requests, reporting issues, or suggesting improvements. We welcome your input!

## 📄 License

This project is licensed under the [MIT License](LICENSE).
```