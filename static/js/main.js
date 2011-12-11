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
	
});
