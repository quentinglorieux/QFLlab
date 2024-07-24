# Python publication import
## AddPublication.py

### Overview

`AddPublication.py` is a Python script designed to add a new publication to an existing YAML file containing a list of publications. The script fetches publication details using the DOI (Digital Object Identifier) from the OpenAlex API and appends this data to the YAML file.


### Script Usage

#### Command
```bash
python AddPublication.py <DOI>
```

#### Arguments
- `<DOI>`: The DOI of the publication you want to add (e.g., `https://doi.org/10.7717/peerj.4375`).

### Script Details

#### Configuration
The script requires setting an email for the `pyalex` API configuration:
```python
pyalex.config.email = "quentin.glorieux@lkb.upmc.fr"
```

### Functions

#### `extract_single_info(paper)`
Extracts detailed information from the publication data.
- **Parameters:** `paper` (dict) - The publication data retrieved from OpenAlex.
- **Returns:** Dictionary with publication details.

#### `get_single_paper(doi)`
Fetches the publication data from OpenAlex using the DOI and appends it to the existing YAML file.
- **Parameters:** `doi` (str) - The DOI of the publication.

### Main Function
The `main` function handles the following:
1. Checks for the correct number of arguments.
2. Fetches the publication data using the provided DOI.
3. Appends the publication data to the YAML file.

### Example Execution
```bash
python AddPublication.py "https://doi.org/10.7717/peerj.4375"
```

This documentation should help you understand and use the `AddPublication.py` script effectively. If you have any questions or need further assistance, feel free to ask.



## MyPubli.py
### Overview

`MyPubli.py` is a Python script designed to retrieve and export an author's publication data from the OpenAlex API based on either an ORCID or the author's name. The retrieved data is exported into a YAML file.

### Script Usage

#### Command
```bash
python MyPubli.py <input_parameter> <your_name>
```

#### Arguments
- `<input_parameter>`: This can be either the ORCID or the full name of the author (e.g., "0000-0001-2345-6789" or "John Doe").
- `<your_name>`: Your name, used for naming the output YAML file.

### Script Details

#### Configuration
The script requires setting an email for the `pyalex` API configuration:
```python
pyalex.config.email = "quentin.glorieux@lkb.upmc.fr"
```

### Functions

#### `get_openalex_id(input_identifier)`
This function retrieves the OpenAlex ID of an author based on the given ORCID or name.
- **Parameters:** `input_identifier` (str) - ORCID or full name.
- **Returns:** OpenAlex author ID (str).

#### `df_creation(openalex_id)`
This function creates a DataFrame of the author's works from OpenAlex.
- **Parameters:** `openalex_id` (str) - OpenAlex author ID.
- **Returns:** DataFrame containing publication data.

#### `extract_info(row)`
Extracts detailed information from each row of the DataFrame.
- **Parameters:** `row` (DataFrame row) - A single row of the DataFrame.
- **Returns:** Dictionary with publication details.

#### `export_data(df)`
Exports the DataFrame data to a YAML file.
- **Parameters:** `df` (DataFrame) - DataFrame containing publication data.

### Main Function
The `main` function coordinates the retrieval and export of the author's publication data:
1. Checks for the correct number of arguments.
2. Retrieves the OpenAlex ID.
3. Creates the DataFrame of works.
4. Exports the data to a YAML file.

### Example Execution
```bash
python MyPubli.py "0000-0001-2345-6789" "john_doe"
```
