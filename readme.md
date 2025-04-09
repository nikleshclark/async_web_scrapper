# 🌐 Async Web Scraper

An **asynchronous web scraper** built with Python's `aiohttp` and `asyncio` libraries. This scraper efficiently fetches content from multiple URLs concurrently, with built-in retry logic, error handling, and rate limiting.

---

## 🚀 Features

- **Asynchronous Requests**: Fetch multiple URLs concurrently using `asyncio` and `aiohttp`.
- **Retry Logic**: Automatically retries failed requests with exponential backoff.
- **Rate Limiting**: Limits the number of concurrent requests to avoid overwhelming servers.
- **Timeout Handling**: Ensures requests don't hang indefinitely.
- **Customizable**: Easily extendable for additional functionality.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/async-web-scraper.git
   cd async-web-scraper
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install aiohttp
   ```

---

## 📝 Usage

1. Add the URLs you want to scrape in the `urls` list in `scrapper.py`:
   ```python
   urls = [
       "https://en.wikipedia.org/wiki/Python_(programming_language)", 
       "https://en.wikipedia.org/wiki/Vimy_Ridge_Day",
       "https://en.wikipedia.org/wiki/Food_safety",
       "https://en.wikipedia.org/wiki/Health"
   ]
   ```

2. Run the scraper:
   ```bash
   python scrapper.py
   ```

3. Output:
   - The scraper will fetch the content of each URL and print the first 100 characters of each result.
   - Example:
     ```
     Fetched 4 URLs in 3.45 seconds
     <!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" conten...
     <!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" conten...
     <!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" conten...
     <!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" conten...
     ```

---

## ⚙️ Configuration

- **Concurrency Limit**: Adjust the number of concurrent requests by modifying the semaphore in `fetch_all`:
  ```python
  semaphore = asyncio.Semaphore(5)  # Change 5 to your desired limit
  ```

- **Timeout**: Set the timeout for requests in `aiohttp.ClientTimeout`:
  ```python
  timeout = aiohttp.ClientTimeout(total=30)  # Change 30 to your desired timeout in seconds
  ```

- **Retries**: Configure the number of retries in the `fetch` method:
  ```python
  retries = 3  # Change 3 to your desired number of retries
  ```

---

## 📂 Project Structure

```
async_web_scrapper/
│
├── scrapper.py          # Main script for the async web scraper
├── README.md            # Project documentation
└── requirements.txt     # Dependencies (optional)
```

---

## 🛡️ Error Handling

- **Client Errors**: Handles HTTP errors like 404 or 500 gracefully.
- **Timeouts**: Retries requests if a timeout occurs.
- **Unexpected Errors**: Logs unexpected errors without crashing the program.

---

## 🛠️ Future Improvements

- Add support for scraping specific elements (e.g., titles, links) using `BeautifulSoup`.
- Save results to a file (e.g., JSON or CSV).
- Add unit tests for better reliability.
- Implement proxy support for bypassing rate limits.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- [aiohttp Documentation](https://docs.aiohttp.org/)
- [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)