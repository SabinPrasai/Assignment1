import spacy
import os

# Load the English NER model
nlp = spacy.load("en_core_web_sm")

# List of input and output file paths
input_files = ["wikipedia.txt", "fanwiki.txt", "sample.txt"]
output_files = ["ner-list-wikipedia.txt","ner-list-fanwiki.txt", "ner-list-sample.txt"]
for i in range(len(input_files)):
    input_file = input_files[i]
    output_file = output_files[i]

    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        # Read the content of the input file
        text = infile.read()

        # Process the text with spaCy
        doc = nlp(text)

        # Extract NERs and write them to the output file
        for ent in doc.ents:
            outfile.write(ent.text + "\n")

    print(f"NERs extracted from {input_file} and saved to {output_file}")
