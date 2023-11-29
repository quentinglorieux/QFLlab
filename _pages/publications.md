---
title: "Glorieux Lab - Publications"
layout: publications
excerpt: "Glorieux Lab -- Publications."
sitemap: false
permalink: /publications/
---

# Publications

**At the end of this page, you can find the [full list of publications](#full-list-of-publications). All papers are available on Open Access on [arXiv](https://arxiv.org/a/glorieux_q_1.html).**

## Group highlights

{% assign number_printed = 0 %}
{% for publi in site.data.pub_highlights %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}

<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well" style="min-height:400px">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/rubidium/highlights/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p>{% for author in publi.authors %} {{ author.name }}
  {% if author.orcid %}<sup><a href="{{ author.orcid }}" target="_blank"><i class="ai ai-orcid"></i></a></sup>{% endif %}{% unless forloop.last%}, {% endunless %} {% endfor %}</p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"> {{ publi.news1 }}</p>
  <p> {{ publi.news2 }}</p>
 </div>
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

<p> &nbsp; </p>

<!-- ## Patents
<em>Milan P Allan, S Gröblacher, RA Norte, M Leeuwenhoek</em><br />Novel atomic force microscopy probes with phononic crystals<br /> PCT/NL20-20/050797 (2020)

<em>Milan P Allan</em><br /> Methods of manufacturing superconductor and phononic elements <br /> <a href="https://patents.google.com/patent/US10439125B2/en?inventor=Milan+ALLAN&oq=inventor:(Milan+ALLAN)">US10439125B2 (2016)</a> -->

## Full List of publications
