jQuery(document).ready(function ($) {
    $('input').on('keypress', function () {
        $('.has-error').hide();
    });
});

var loginLink = document.getElementById('id_login');
if (loginLink) {
  loginLink.onclick = function() { navigator.id.request(); };
}

