#!/usr/bin/env python3

import sys

def fix_ner(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()
                if line:
                    # Split the line into word and tag
                    word, tag = line.split('\t')

                    # Check if the word is punctuation
                    if word.strip() in ['.', ',', '!', '?', ';', ':', '...', '``', "''", '(', ')', '[', ']', '{', '}']:
                        tag = '/O'

                    # Write the fixed line to the output file
                    outfile.write(f"{word}\t{tag}\n")
                else:
                    # Empty line, write it as is
                    outfile.write('\n')

        print(f"Tags in {input_file} have been fixed and saved to {output_file}")
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fix-ner.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    fix_ner(input_file, output_file)
