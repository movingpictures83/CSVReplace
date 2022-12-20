# CSVReplace
# Language: Python
# Input: TXT
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin to take a CSV file and replace a value with another value.
Multiple values can be replaced.

The plugin accepts as input a TXT file, with tab-delimited keyword value pairs:
csvfile: Input CSV
values: Values to replace, pairwise, tab-delimited, one pair per row.

The output CSV file will be the input CSV file but with the appropriate values replaced.
