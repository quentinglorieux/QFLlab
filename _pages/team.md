---
title: "Quantum Fluids of Light Lab - Team"
excerpt: "Quantum Fluids of Light Lab: Team members"

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

<div class="row">

<div class="col-sm-4 clearfix">
<h4>Visitors</h4>
{% assign visitor_list = site.data.team.alumni_students | where:"status","visitor" %}

{% for member in visitor_list %}
{{ member.name }}
{% endfor %}

</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% assign master_list = site.data.team.alumni_students | where:"status","master" %}
{% for member in master_list %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% assign bsc_list = site.data.team.alumni_students | where:"status","bsc" %}
{% for member in bsc_list %}
{{ member.name }}
{% endfor %}
</div>

</div>

## Administrative Support

<a href="mailto:">David Noel</a> and <a href="mailto:">Laetitia Morel</a> are helping us (and other groups) with administration.
