---
title: "Theses of the group"
layout: default
sitemap: false
permalink: /theses
---


## PhD theses

#### Theses available on HAL
- Theses directed by **Quentin Glorieux** on : [HAL](https://theses.hal.science/search/index/?qa%5Bdirector_t%5D%5B%5D=quentin+glorieux&rows=30&sort=publicationDate_tdate+desc)
- Theses directed by **Alberto Bramati** on : [HAL](https://theses.hal.science/search/index/?qa%5Bdirector_t%5D%5B%5D=bramati&rows=30&sort=publicationDate_tdate+desc)
- Theses directed by **Elisabeth Giacobino** on : [HAL](https://theses.hal.science/search/index/?qa%5Bdirector_t%5D%5B%5D=giacobino&rows=30&sort=publicationDate_tdate+desc)

#### Full list of theses of the group

<ul>
  {% for thesis in site.data.theses.PhD_theses %}
  <li><strong>{{ thesis.name }}</strong> ({{ thesis.year }}) : {{ thesis.title }} 
    {% if thesis.link %}
    <a href="{{ thesis.link }}">[PDF]</a>
    {% endif %}
  </li>
  {% endfor %}
</ul>

## Master theses

{% for year_group in site.data.theses.internships %}
#### {{ year_group.year }}

<ul>
  {% for thesis in year_group.theses %}
  <li><strong>{{ thesis.name }}</strong> : {{ thesis.title }} 
    {% if thesis.link %}
    <a href="{{ thesis.link }}">[PDF]</a>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% endfor %}
<p class="pb-10">  </p>

<style>
  .pb-10 {
    padding-bottom: 1.5em;
  }
  </style>

