---
title: "LKB QFL Team"
excerpt: "Team members"
layout: gridlay
sitemap: false
permalink: /team/
---

{% assign sections = site.data.admin.team_section | sort: "order" %}

{% for sec in sections %}

## {{ sec.title }}
{% include team_member.html s=sec %}

{% endfor %}


## Alumni
{% include team_alumni.html%}


## Former visitors, BSc/ MSc students
{% include team_visitors.html%}


## Administrative Support
<a href="mailto:">David Noel</a> and <a href="mailto:">Laetitia Morel</a> are helping us (and other groups) with administration.


