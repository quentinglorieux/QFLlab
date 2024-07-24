---
title: "News"
excerpt: "QFL Lab at Sorbonne University."
layout: textlay
sitemap: false
permalink: /allnews
---

# All News

{% assign sorted_articles = site.news | sort: 'date' | reverse %}
<ul class="no-bullet">
{% for article in sorted_articles%}
    <li style="margin-bottom: 10px; padding-bottom: 2px; border-bottom: 1px solid #ccc;">
        <span style="font-weight: 500; font-size: 1.5rem;">{{ article.date | date: "%B %d, %Y" }}</span>
        <div style="display: flex;">
            <img src="assets/images/news/{{ article.image }}" alt="{{ article.image }}" style="width: 100px; height: auto;  margin-right: 10px;">
            <div> 
            <div style="font-weight: 500; font-size: 1.45rem; padding-top: 15px;">{{ article.title}}</div>
            <div>
                {{ article.content | strip_html | truncatewords: 40 }}
            </div>

            <a href="{{ article.url }}">
                <div class="btn-home" style="margin-top: 2px; margin-bottom: 15px; font-size: 1.4rem;">
                    <span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span>
                    Read more
                </div>
            </a>
            </div>
        </div>
    </li>
{% endfor %}
</ul>

    
{% for article in site.data.news %}
{{ article.date }} - {{ article.headline }}
{% endfor %}
