from pyalex import Works, Authors
import pyalex
import json
import pandas as pd
import re
import sys


pyalex.config.email = "quentin.glorieux@lkb.upmc.fr"


def get_openalex_id(input_identifier):
    authors = Authors()
    if "0-" in input_identifier:  # Assuming it's an ORCID number
       orcid_url = f"https://orcid.org/{input_identifier}"
       openalex_url = authors[orcid_url]['id']
    else:
        name_result = authors.search_filter(display_name=input_identifier).get()
        openalex_url = name_result[0]['id']
        
    pattern = re.compile(r'A(\d+)')
    match = pattern.search(openalex_url)
    if match:
        extracted_id = match.group(1)
        return 'A' + extracted_id
    else:
        return    

# orcid_result = get_openalex_id("0000-0002-4297-0502")
# name_result = get_openalex_id("Hanna Le Jeannic")

def df_creation(openalex_id):
    pager = (
        Works()
        .filter(author={"id": openalex_id})
        .filter(has_doi=True, primary_location={"source": {"has_issn": True}})
        .select(
            [
                "id",
                "doi",
                "title",
                "publication_year",
                "ids",
                "type",
                "type_crossref",
                "open_access",
                "primary_location",
                "authorships",
                "biblio",
                "concepts",
            ]
        )
        .sort(publication_year="desc")
        .paginate(per_page=100)
    )
    list = []
    for page in pager:
        list = list + page
    df = pd.DataFrame(list)
    return df


# Define a function to extract information
def extract_info(row):

    match = re.search(r'physrev(.+?)(\d+)', row["doi"])
    if match:
        if match.group(1)[0] not in ('l', 'r', 'x') : 
            journal_abbreviation = match.group(1)[0].capitalize()
        else: 
            journal_abbreviation = ""
    else:
        journal_abbreviation = ""

    return {
        "title": row["title"],
        "authors": [
            {"name": entry["author"]["display_name"], "orcid": entry["author"]["orcid"]}
            for entry in row["authorships"]
        ],
        "link": {
            "url": row["doi"],
            "display": row["primary_location"]["source"]["display_name"]
            + " "
            + str(row["biblio"]["volume"])
            + " "
            + str(row["biblio"]["issue"])
            + " ("
            + str(row["publication_year"])
            + ").",
        },
        # "orcid": [entry["author"]["orcid"] for entry in row["authorships"]],
        "doi": row["doi"],
        "is_oa": row["open_access"]["is_oa"],
        "oa_url": row["open_access"]["oa_url"],
        "publication_year": row["publication_year"],
        "journal": row["primary_location"]["source"]["display_name"],
        "journal_abbreviation": journal_abbreviation,
        "biblio": row["biblio"],
    }


# Export JSON file
def export_data(df):
    author_pub_list = df.apply(extract_info, axis=1).tolist()
    json_string = json.dumps(author_pub_list, indent=2)

    # Save the JSON string to a file
    with open("../_data/openalex_list.json", "w") as file:
        file.write(json_string)



def main():
    if len(sys.argv) != 2:
        print("Usage: python ExtractPubli.py <input_parameter>")
        sys.exit(1)

    input_parameter = sys.argv[1]
    print(f"Input Parameter: {input_parameter}")

    df = df_creation(get_openalex_id(input_parameter))
    print(get_openalex_id(input_parameter))
    print(f"Number of records: {len(df)}")

    export_data(df)

if __name__ == "__main__":
    main()


### RUN THE EXPORT ###
