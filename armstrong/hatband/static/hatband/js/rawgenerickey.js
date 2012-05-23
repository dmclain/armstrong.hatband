var jQuery = jQuery || django.jQuery;
var armstrong = armstrong || {};
armstrong.widgets = armstrong.widgets || {};

armstrong.widgets.raw_generic_key = function(type_input, id_input, picker_anchor) {
	var $ = jQuery;
	type_input.change(function(){
		var ct = armstrong.widgets.raw_generic_key.content_types[type_input.val()];
		picker_anchor.attr('href', '/admin/' + ct.app_label + '/' + ct.model);
	});
};