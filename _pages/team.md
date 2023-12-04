---
title: "Quantum Fluids of Light Lab - Team"
layout: gridlay
excerpt: "Quantum Fluids of Light Lab: Team members"
sitemap: false
permalink: /team/
---

{% assign sections = site.data.admin.team_section | sort: "order" %}

{% for section in sections %}
## {{ section.title }}

{% assign number_printed = 0 %}
{% assign filtered_members = site.data.team.members | where: "status", section.status %}
{% assign member_count = filtered_members | size %}

{% for member in site.data.team.members %}
  {% if member.status == section.status %}
  {% assign even_odd = number_printed | modulo: 2 %}

  {% if even_odd == 0 %}
  <div class="row"> 
  {% endif %}

  {% include team_member.html member=member %}

  {% assign number_printed = number_printed | plus: 1 %}
  {% if even_odd == 1 or number_printed == member_count %} </div> {% endif %}
  {% endif %}
{% endfor %}
{% endfor %}

## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.team.alumni_members %}
{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 0 %}
<div class="row">
{% endif %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/rubidium/members/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">
  </ul>
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
