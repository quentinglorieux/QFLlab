---
title: "Quantum Fluids of Light Lab - Team"
layout: gridlay
excerpt: "Quantum Fluids of Light Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

We are a group of **friendly and welcoming scientists** and we aim to create an **inclusive and supportive research environment**. We strongly believe in the value of diversity and inclusion in the field of quantum physics and we encourage women and/or individuals from underrepresented minority groups to apply.
**We are currently looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**


<!-- Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors). -->


{% assign PIlist = site.data.team_members | where:"status", "PI" %}
{% assign lsPI = PIlist | size %} 
{% assign postdoclist = site.data.team_members | where:"status", "postdoc" %}
{% assign lspd = postdoclist | size %} 
{% assign phdlist = site.data.team_members | where:"status", "phd" %}
{% assign lsphd = phdlist | size %} 


## Permanent Researchers
{% assign number_printed = 0 %}
{% assign even_odd = 0 %}
{% for member in PIlist %}
{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/rubidium/members/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
<h4>{{ member.name }}</h4>
{{ member.info }} <br> 
<{{ member.email }}>
<br> 
<i>{{member.tagline}} </i>
<ul style="overflow: hidden">

{% if member.number_educ == 1 %}

<li> {{ member.education1 }} </li>
{% endif %}

{% if member.number_educ == 2 %}
<li> {{ member.education1 | markdownify}} </li>
<li> {{ member.education2 | markdownify}} </li>
{% endif %}

{% if member.number_educ == 3 %}
<li> {{ member.education1 }} </li>
<li> {{ member.education2 }} </li>
<li> {{ member.education3 }} </li>
{% endif %}

{% if member.number_educ == 4 %}
<li> {{ member.education1 }} </li>
<li> {{ member.education2 }} </li>
<li> {{ member.education3 }} </li>
<li> {{ member.education4 }} </li>
{% endif %}

{% if member.number_educ == 5 %}
<li> {{ member.education1 }} </li>
<li> {{ member.education2 }} </li>
<li> {{ member.education3 }} </li>
<li> {{ member.education4 }} </li>
<li> {{ member.education5 }} </li>
{% endif %}

</ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 or number_printed ==  lsPI%}
</div>
{% endif %}





{% endfor %}





## Postdocs
{% assign number_printed = 0 %}
{% for member in postdoclist %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/rubidium/members/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}


  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 or number_printed ==  lspd%}
</div>
{% endif %}



{% endfor %}




## PhD students
{% assign number_printed = 0 %}
{% for member in phdlist %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/rubidium/members/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 | markdownify}} </li>
  <li> {{ member.education2 | markdownify}} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}


  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 or number_printed ==  lsphd%}
</div>
{% endif %}


{% endfor %}






## Master and Bachelor Students
{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!-- <br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

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


## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

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
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% for member in site.data.alumni_msc %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% for member in site.data.alumni_bsc %}
{{ member.name }}
{% endfor %}
</div>

</div>


## Administrative Support
<a href="mailto:">David Noel</a>  and <a href="mailto:">Laetitia Morel</a> are helping us (and other groups) with administration.
