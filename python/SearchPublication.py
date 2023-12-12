from pyalex import Works
import pyalex
import sys
import re
import yaml


pyalex.config.email = "quentin.glorieux@lkb.upmc.fr"

def find_paper(key):
    papers = Works().search_filter(title=key).get()
    if (papers[0]):
        paper = papers[0]
        print(f"Paper found. \n DOI: {paper['doi']}.\n First author: {paper['authorships'][0]['author']['display_name']}.\n Year: {paper['publication_year']}")

    else : print("Not Found.")
    return paper


def extract_single_info(paper):

    match = re.search(r'physrev(.+?)(\d+)', paper["doi"])
    if match:
        if match.group(1)[0] not in ('l', 'r', 'x') : 
            if paper["primary_location"]["source"]["display_name"][-1] != match.group(1)[0].capitalize():
                journal_abbreviation = match.group(1)[0].capitalize()
            else : journal_abbreviation = ""
        else: journal_abbreviation = ""
    else: journal_abbreviation = ""

    return {
        'title': paper['title'],
        "authors": [
                {"name": entry["author"]["display_name"], "orcid": entry["author"]["orcid"]}
                for entry in paper["authorships"]
            ],
        'link': {
            'url' : paper['doi'],
            'display' :paper["primary_location"]["source"]["display_name"]
                + " "
                + str(paper["biblio"]["volume"])
                + " "
                + str(paper["biblio"]["issue"])
                + " ("
                + str(paper["publication_year"])
                + ").",
            },
        "doi": paper["doi"],
        "is_oa": paper["open_access"]["is_oa"],
        "oa_url": paper["open_access"]["oa_url"],
        "publication_year": paper["publication_year"],
        "journal": paper["primary_location"]["source"]["display_name"],
        "journal_abbreviation": journal_abbreviation,
        "biblio": paper["biblio"],
    }
    

# Export YAML file
def get_single_paper(paper):
    data = [extract_single_info(paper)]

    with open("../_data/publications/full_list_openalex.yaml", 'r') as file:
        current_data = yaml.safe_load(file)
        new_data = data + current_data
    with open('../_data/publications/full_list_openalex.yaml', 'w+') as f:
        for yaml_obj in new_data:
            f.write(yaml.dump([yaml_obj], default_flow_style=False , sort_keys=False))
            f.write("\n")


def main():
    if len(sys.argv) != 2:
        print("Missing Title argument. Usage: python SearchPublication.py <title>")
        sys.exit(1)

    input_key = sys.argv[1]

    paper = find_paper(input_key)

    user_input = input("Did we find it right? Save it now? (Y/n): ").lower()
    if user_input == 'n':
        print("Nothing added to your list.")  
    else:
        get_single_paper(paper)
    

if __name__ == "__main__":
    main()
