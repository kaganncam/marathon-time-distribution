# Running Statistics

This Python script scrapes data from the "https://event.spor.istanbul/eventresults.aspx" website, specifically the Istanbul Marathon results, and generates a histogram visualization of the runner finish times.

## Installation

1. Install the required dependencies:
   - `beautifulsoup4`
   - `matplotlib`
   - `selenium`
   - `webdriver-manager` (for automatic Firefox driver installation)

   You can install these dependencies using pip:

   ```
   pip install beautifulsoup4 matplotlib selenium webdriver-manager
   ```

2. Ensure you have the Firefox web browser installed on your system.

## Usage

1. Run the `running_statistic.py` script:

   ```
   python running_statistic.py
   ```

2. The script will automatically scrape the data from the website, save the results to a file named `spor-ist-sonuclar.text`, and display a histogram of the runner finish times.

## API

The script uses the following APIs and libraries:

- `BeautifulSoup` (from `bs4`) for parsing the HTML content of the website.
- `matplotlib` for generating the histogram visualization.
- `selenium` and `webdriver-manager` for automating the web browser interaction and scraping the data.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

The script has been tested on Windows 10 with Python 3.9 and the specified dependencies installed. However, it's recommended to test the script in your own environment to ensure compatibility.
