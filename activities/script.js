document.addEventListener('DOMContentLoaded', function() {
    // Function to load and display JSON content
    function loadJSON() {
        let xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let jsonData = JSON.parse(xhr.responseText);
                displayContent(jsonData);
            }
        };

        xhr.open('GET', 'content.json', true);
        xhr.send();
    }

    // Function to display JSON content in the HTML
    function displayContent(data) {
        let container = document.getElementById('json-content');
        let html = '';
        let years = Object.keys(data).reverse();
        for (let key of years) {
            if (data.hasOwnProperty(key)) {
                let year = key;
                html += `<h2 data-toggle="collapse" data-target="#${year}"><img class="icon_rotation" src="../../assets/0-expand_on.png" style="float:right;width:50px;height:50px" data-toggle="collapse" data-target="#${year}">${year}</h2><hr /><div id="${year}" class="collapse in"><ul>`
                for (entry of data[key]) {
                    html += `<li><p>${entry}</p></li>`;
                }
                html += `</ul></div><p><br /></p>`;
            }
        }
        container.innerHTML = html;

        $(document).ready(function(){
            $('.icon_rotation').on({
              'click': function () {
                console.log('click');
                var origsrc = $(this).attr('src');
                var src = '';
                if (origsrc == '../../assets/0-expand_off.png') src = '../../assets/0-expand_on.png';
                if (origsrc == '../../assets/0-expand_on.png') src = '../../assets/0-expand_off.png';
                $(this).attr('src', src);
              }
            });
          });
    }

    // Load JSON content on page load
    loadJSON();
});