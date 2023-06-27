var baseUrl = window.location.protocol + "//" + window.location.host;
var endpoint = '/process_image'
console.log(baseUrl);
// Define a function to show the loading animation
function showLoadingAnimation() {
  $('.loading-ring').show();
}

// Define a function to hide the loading animation
function hideLoadingAnimation() {
  $('.loading-ring').hide();
}

$(document).ready(function() {
      $('#upload-form').submit(function(e) {
        e.preventDefault();
        showLoadingAnimation();
        $('#result-container').text('');
        var formData = new FormData(this);

        // Make AJAX request to Flask route
        $.ajax({
          url: baseUrl + endpoint,
          type: 'POST',
          data: formData,
          processData: false,
          contentType: false,
          success: function(response) {
            hideLoadingAnimation();
            // Handle the response from Flask
            $('#result-container').text(response);
          },
          error: function(xhr, status, error) {
            hideLoadingAnimation();
            $('#result-container').text(error);
          }
        });
      });
    });