# URL Shortener with Analytics

This is a simple URL Shortener web application built using Flask, MySQL, and Python. The application allows users to shorten URLs and track the number of clicks on each shortened URL. It provides a clean user interface where users can input a URL to shorten it and see the resulting shortened URL instantly.

## Features
- Shorten any URL using a user-friendly web interface.
- Redirect users to the original URL when the short URL is visited.
- Track analytics: number of clicks for each shortened URL.

## Tech Stack
- **Frontend**: HTML (form for URL input)
- **Backend**: Flask (Python Web Framework)
- **Database**: MySQL (stores original URLs, short URLs, and click counts)
- **Libraries**:
  - `Flask`
  - `SQLAlchemy`
  - `shortuuid`
  - `python-dotenv`

## Getting Started

### Prerequisites
- Python 3.x
- MySQL Server running locally
- Git (for version control)
- Virtual Environment (optional but recommended)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/varun97979/URL-Shortener.git
