import argparse
import csv
from pathlib import Path
from tqdm import tqdm


def main():
    """Main function to parse CSV and extract queries."""
    parser = argparse.ArgumentParser(
        description="Parse a Flipside query export CSV and format the SQL queries into a text file."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input CSV file (e.g., 'download-my-queries.csv')."
    )
    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.is_file():
        print(f"Error: Input file not found at '{input_path}'")
        return

    output_path = input_path.with_suffix('.txt')

    try:
        # First, count rows for an accurate progress bar without loading the file into memory
        with open(input_path, "r", encoding="utf-8") as f:
            # Subtract 1 for the header row
            total_rows = sum(1 for _ in f) - 1

        # Process and write in a single pass to conserve memory
        with open(input_path, "r", encoding="utf-8") as infile, \
             open(output_path, "w", encoding="utf-8") as outfile:

            reader = csv.reader(infile)
            next(reader)  # Skip header row

            for index, row in enumerate(tqdm(reader, total=total_rows, desc="Processing queries"), start=1):
                if not row:  # Handle potential empty rows
                    continue

                query_id = row[0]
                query_title = row[1]

                # Collect all non-empty string values after the title as parts of the SQL
                sql_parts = [part for part in row[2:] if part]
                raw_query_string = ",".join(sql_parts)

                '''
                The below substring replacement operations will have to be fine-tuned as per User SQL writing style
                '''
                formatted_query = raw_query_string.replace("   ", "\n\t")
                formatted_query = formatted_query.replace(" \t", "\n\t")
                formatted_query = formatted_query.replace("UNION ALL", "\n\tUNION ALL\n")

                # Write the formatted query directly to the output file
                outfile.write("=======================================================================================\n")
                outfile.write("=======================================================================================\n")
                outfile.write(f"QUERY_NO: {index}\n")
                outfile.write(f"QUERY_ID: {query_id}\n")
                outfile.write(f"QUERY_TITLE: {query_title}\n\n")
                outfile.write("QUERY_STRING:\n\n")
                outfile.write(f"{formatted_query}\n\n\n\n")

    except FileNotFoundError:
        print(f"Error: Could not find the file at {input_path}")
        return
    except Exception as e:
        print(f"An error occurred while processing the CSV: {e}")
        return

    print(f"\nSuccessfully wrote formatted queries to {output_path}")

if __name__ == "__main__":
    main()
