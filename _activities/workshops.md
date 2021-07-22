---
layout: page
title: Workshops
---


{% assign workyears = site.workshops | map: "event_year" | uniq | reverse %}

{% for year in workyears %}

  <div class="row">
    <div class="col-lg-12">

      <h2 data-toggle="collapse" data-target="#{{ year }}">
        {{ year }}
        <img class="icon_rotation" src="{{ site.url }}/assets/0-expand_on.png" style="float:right;width:50px;height:50px" data-toggle="collapse" data-target="#{{ year }}" />
      </h2>
      <hr>

      <div id="{{ year }}" class="collapse in">
        {% assign workshop_list = site.workshops | sort: 'event_date' | reverse %}
        {% for workshop in workshop_list %}
          {% if workshop.event_year == year %}
            <div class="row">
              <div class="col-lg-12">
                <h2>{{ workshop.title }}</h2>
                <h4 class="event">

                  {% if workshop.venue %}
                    {{ workshop.venue }}
                  {% endif %}
                  ,
                  {% if workshop.location %}
                    {{ workshop.location }}
                  {% endif %}
                  ,
                  {{ workshop.event_date | date: "%B %d, %Y" }}

                </h4>

                {{ workshop.content }}

              </div>
            </div>
          {% endif %}

        {% endfor %}

      </div>
    </div>
  </div>
{% endfor %}

<script>
$(document).ready(function(){
  $('.icon_rotation').on({
    'click': function () {
      var origsrc = $(this).attr('src');
      var src = '';
      if (origsrc == '{{ site.url }}/assets/0-expand_off.png') src = '{{ site.url }}/assets/0-expand_on.png';
      if (origsrc == '{{ site.url }}/assets/0-expand_on.png') src = '{{ site.url }}/assets/0-expand_off.png';
      $(this).attr('src', src);
    }
  });
});
</script>
