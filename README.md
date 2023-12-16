# Quantum Fluids of Light Lab Website

This is the website of our academic research group at Sorbonne University.
This website is powered by Jekyll and some Bootstrap, Bootwatch. 

## Install

[Clone](https://github.com/quentinglorieux/) this repository.

Install Jekyll (see [here](https://jekyllrb.com/docs/installation/)).
Go to your folder and run `bundle exec jekyll serve`
Your demo site is available at [http://localhost:4000](http://localhost:4000)

### Local dev
To run it locally : `bundle exec jekyll serve`

## Set-up the content

### Create your publication list
There is a Python function to generate automatically your publication list from your name or your ORCID identifier.

#### Example use:
Type ` cd python `, then 

```python ExtractPubli.py "Quentin Glorieux"``` , or 

```python ExtractPubli.py "https://orcid.org/0000-0003-0903-0233"```

It will create a file based on your publications in the _datas/publications folder.

### Load your assets
Load your images in the `images` folder. 
- in the `home_carousel` folder, put the files for the carousel on the homepage.
- in the `logo` folder, put the logo for the homepage.
- in the `members` folder, put your members.
- in the `members/placeholders` folder, put the images for missing members.
- in the `news` folder, put your news.
- in the `research` folder, put your research.

## Edit your datas (members list and publications)
Open the `_data` folder and edit the yaml files.

### Fundings
Open the `fundings.yml` file, then edit your fundings following yml syntax:
```yaml
- name: Agence Nationale de la Recherche
  projectID: XR204957
  acronym: GDSOU
  link: https://anr.fr/ 
  link_text: (ANR)
```

### Publications
Open the `publications` folder then the `full_list_openalex.json` is supposed to be populated with your publication data (see Create your Publication list above).
Then the file `highlights.json` contains the highlighted publications (with a picture). 
The picture must be saved in `images/highlights/`
The format is 
```yaml
- title: High-Resolution Coherent Probe Spectroscopy of a Polariton Quantum Fluid
  image: bragg_polariton1.png
  description: 
    A promising spectroscopy technique to measure the dispersion relation of a Polariton Quantum Fluid
    even at very low momenta, and with access to the ghost (negative energy) modes.
```

### Team members
Open the `team` folder.
#### Current members 
For current members edit the `members.yml` file with the following yml syntax:
```yaml
- name: Hanna Le Jeannic
  tagline: Quantum Hanna
  photo: Hanna.png
  info: CNRS Researcher
  status: PI
  email: 
  education1: Postdoc at NBI (Peter Lodhal group)
  education2: PhD at LKB (Laurat group)
  education3: MSc at ESPCI
  ```
  You can add up to 5 `eduactions`. It can includes *html* or *md* formating.
  Photos are stored in the `images/members/` folder

#### Alumni members 
For alumni members (when a PhD or a postdoc leaves) edit the `alumni_members.yml` file with the following yml syntax:
```yaml
- name: Quentin Fontaine
  tagline: Experimental theoritician
  photo: QuentinF.png
  duration: PhD from 2017 to 2020
  thesis: Titre
  email: 
  now_at: C2N
  ```
Copy paste from the members.yml but remove the `education` and `status` fields and add `duration`, `thesis` and `now_at` fields.
Photos are stored in the `images/members/` folder

#### Alumni visitors 
For alumni visitors (when a visitor, bachelor or master students leaves) edit the `alumni_visitors.yml` file with the following yml syntax:
```yaml
- name: BSc (X), Spring 2017
  status: bsc
  pdf:
  ```

## Edit the Pages
### Homepage
Open the `_pages` folder then `home.md`
This file contains the markup for the homepage.
Some HTML codes are included using e.g. `{% include carousel.html %}`.
Do not edit this part (except if you want to remove it from the template).
This file content can be modified using *markdown* syntax.

### Job page 
Open the `_pages` folder then `openings.md`
This file contains the markup for the job page.

## Edit the collections
There are 4 collections:
- members: for detailled pages of each member
- news: for the news of the homepage
- research: to list the research topics
- projects: to present recent research projects

### Member collection

### News collection

### Research collection
Edit the md files with this frontmatter:
```yaml
---
title: Superfluidity
slug: superfluidity
abstract : Superfluidity is one of the most striking manifestation of quantum many-body physics. Initially observed in liquid Helium, the realization of atomic Bose-Einstein condensates (BEC) has allowed detailed investigations of this macroscopic quantum phenomenon exploiting the precise control over the system parameters. 
image: bottle.png
team: 
    - Quentin Glorieux
    - Tangui Aladjidi
    - Chengjie Ding
    - Clara Piekarski
publications: 
    - https://doi.org/10.1103/physrevlett.129.100602
    - https://doi.org/10.1051/epjconf/202226608004
    - https://doi.org/10.1103/physrevlett.127.023401
---
```

### Project collection