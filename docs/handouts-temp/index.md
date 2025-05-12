---
layout: default
title: All Handouts
permalink: /Math-497-Final-Project/handouts/
---

# All Handouts

<ul>
{% for i in (1..6) %}
  <li>
    <a href="{{ '/handouts/handout' | append: i | relative_url }}">
      Handout {{ i }}
    </a>
  </li>
{% endfor %}
</ul>