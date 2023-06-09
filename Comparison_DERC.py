import csv

def find_missing_titles():
    # Read the DERC regulations CSV file
    derc_file = 'derc_regulations.csv'
    derc_titles = set()
    with open(derc_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            title = row['Title']
            derc_titles.add(title)

    # Read the CER docs details CSV file
    cer_file = 'cer_docs_details.csv'
    with open(cer_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        found_titles = set()
        for row in reader:
            title = row['title']
            found_titles.add(title)

    # Find missing titles
    missing_titles = derc_titles - found_titles

    # Print the missing titles
    for title in missing_titles:
        print(title)

# Run the function
find_missing_titles()
