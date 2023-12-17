// highlight.js
$(document).ready(function(){
    $("body:contains('Quentin Glorieux')").html(function(_, html) {
        return html.replace(/(Quentin Glorieux)/g, '<span class="highlight">$1</span>');
    });
});