# URL Extractor

A simple Python script to extract all URLs (both relative and absolute) from a given webpage and save them to a text file.

## Features

- Fetches HTML content from a specified URL.
- Parses all `<a>` tags to extract `href` attributes.
- Converts relative URLs to absolute URLs using the base URL.
- Outputs both the original href and the full URL for each link.
- Saves the extracted URLs to a specified text file.

## Requirements

- Python 3.6 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone or download the repository.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Edit the `page_url` variable in `extract.py` to the desired webpage URL.
2. Optionally, change the `file_name` for the output file.
3. Run the script:
   ```
   python extract.py
   ```
4. The extracted URLs will be written to the specified file (e.g., `url11.txt`).

## Example Output

The output file will contain lines like:
```
/f/somepath
https://example.com/f/somepath
https://example.com/anotherlink
```

## Troubleshooting

- Ensure the target URL is accessible and returns HTML.
- If you encounter import errors, verify that dependencies are installed.
- For large pages, the script may take time to process.

## License

This project is for educational purposes. Use responsibly and respect website terms of service.