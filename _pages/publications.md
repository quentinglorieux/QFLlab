---
title: "LKB QFL Lab - Publications"
layout: publications
excerpt: Publications.
sitemap: false
permalink: /publications/
---
<div id="top"> </div> 
# Publications

The <span> <a href="#full-list-of-publications"> <button  class='btn nav-button'> full list </button></a> </span>  is at the end of this page. <br>
All papers are available on Open access on **[arXiv](https://arxiv.org/a/glorieux_q_1.html)**.

## Group highlights


{% assign number_printed = 0 %}
{% for highlight in site.data.publications.highlights %}
{% assign publi = site.data.publications.full_list_openalex | where: "title", highlight.title | first %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<!-- Highlights -->
<div markdown="0">
{% include publication_highlights.html  %}
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}



## Full List of publications
<a href="#top"> <button  class='btn nav-button'> To Top </button></a>
<a href="#group-highlights"> <button  class='btn nav-button'> Highlights </button></a>
<div markdown="0">
{% include publications_list.html %}
</div>


