# Query CSV Handler

## Purpose
This script parses a CSV file exported from Flipside Crypto containing multiple SQL queries. It extracts each query, formats it for better readability, and saves the result as a single, well-structured `.txt` file.

## Setup
1. Ensure you have Python 3.8+ installed.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Executing the Script
Run the script from your terminal, providing the path to the input CSV file as an argument.

```bash
python parser.py path/to/your/downloaded-queries.csv
```

### Example
If your file is named `download-my-queries.csv` and is in the same directory, run:
```bash
python parser.py download-my-queries.csv
```

This will produce an output file named `download-my-queries.txt` in the same directory.
