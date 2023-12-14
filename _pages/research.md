---
title: "LKB QFL - Research"
layout: research_list
excerpt: "Research"
sitemap: false
permalink: /research/
---

# Research
<!-- {% assign research_themes = site.posts | where_exp:"item", "item.categories contains 'research'"  %} -->

<section class="articles">
{% for post in site.research %}
  <div markdown="0">
    {% include card.html %}
  </div>
{% endfor %}
</section>
