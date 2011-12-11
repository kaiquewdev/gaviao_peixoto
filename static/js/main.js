//Validadtion: verify email
function is_email(email, pattern) {
	email = email || '';
	pattern = /[a-z0-9]+@[a-z0-9]+(([\.][a-z]{2,3}){1,2})$/;

	if (typeof email !== 'undefinded') {
		if (email.match(pattern)) {
			return true;
		} else {
			return false;
		}
	}
}

//Validation: verify if the field was empty
function is_empty(field) {
	field = field || '';
	
	if (typeof field !== 'undefined') {
		if (field === '') {
			return true;			
		} else {
			return false;					
		}
	}	
}

//Initialize map
function CreateMap() {
	var args = arguments,
		myLatlng = new google.maps.LatLng(args[1], args[2]),
		myOptions = {
			  zoom: args[3],
			  center: myLatlng,
			  mapTypeId: google.maps.MapTypeId.ROADMAP
		},
		map = new google.maps.Map(document.getElementById(args[0]), myOptions);
		
		if (typeof args[0] !== 'undefinded' && 
			typeof args[1] !== 'undefinded' &&
			typeof args[2] !== 'undefinded' &&
			typeof args[3] !== 'undefinded') {
			
			return map;
		} else {
			return false;
		}
} 

//Main actions
$(function () {
	//Contact form
	var fields = [
			$('input#name')[0],
			$('input#email')[0],
			$('input#message')[0]
		];

	$('.contact').find('input, textarea').bind('keypress', function () {
		if (is_empty($(this).value) == false) {
			$(this).addClass('error');
		} else {
			$(this).removeClass('error');
		}
	})
	
	//Map in the contact
	var newMap = CreateMap('map-addrs', -23.404892, -46.7599589, 18);
});
