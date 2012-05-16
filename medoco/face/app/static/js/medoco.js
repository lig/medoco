$(function() {
	$.address.change(function(e) {
		var url = medoco_base_url;
		if (e.value === '/') {
			url += medoco_default_url;
		} else {
			url += e.value;
		}
		$('#medoco-content').load(url, function() {
			$('a.medoco-ajax').mousedown(function(e) {
				if (e.which == 1) {
					$.address.value($(this).attr('href'));
					return false;
				}
			});
		});
	});
});
