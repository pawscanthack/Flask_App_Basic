
console.log("Hello World");

			$(function() {
			  $('a#process_input').bind('click', function() {
				$.getJSON('/background_process', {
				  test_input: $('input[name="test_input"]').val(),
				}, function(data) {
				  $("#result").text(data.result);
				  if (data.result === "COOKIE COOKIE!!") {
					$("#cookie-image").show();
				  }
				});
				return false;
			  });
			});
