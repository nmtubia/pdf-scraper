# PDF Link Scraper

## Overview
This Python script extracts and validates PDF links from a given webpage. It fetches all `<a>` tags with `href` attributes, checks if they point to a valid PDF file, and retrieves metadata like content length and the final URI.

## Features
- Parses a given URL to find all anchor tags (`<a>`).
- Resolves relative URLs to their absolute paths.
- Validates if the link points to a PDF file by checking the `Content-Type` header
- Prints the URI, final resolved URI, and content length of valid PDFs
- Handles common HTTP, timeout, and connection errors
- Includes a fallback mechanism for unexpected errors

## Prerequisites
- Python
- `requests` library
- `BeautifulSoup` from `bs4`

Install the dependencies using:

```bash
pip install requests beautifulsoup4
```

## Usage
Run the script with the URL of the webpage as a command-line argument:
```bash
python3 pdfs.py <URL>
```

Example:
```bash
python3 pdfs.py https://example.com
```

## Error Handling
The script is designed to handle:

- **HTTP Errors**: Issues like 404 (Not Found), 403 (Forbidden), etc.
- **Timeout Errors**: Requests exceeding a 2-minute limit.
- **Connection Errors**: Problems connecting to the server.
- **Unexpected Errors**: Any other unforeseen errors are caught and logged for debugging.

## Example Output
When run, the script outputs details for each valid PDF link:

```bash
URI: https://example.com/sample.pdf
Final URI: https://cdn.example.com/sample.pdf
Content Length: 2048 bytes
```

If an error occurs:
```bash
HTTP Error: 404 for URL: https://example.com/broken-link.pdf
Timeout Error: The request for https://example.com/slow-link.pdf took longer than 2 minutes
Connection Error: Failed to connect to https://example.com/offline.pdf
An unexpected error occurred for https://example.com/unexpected: [Error Message]
```
