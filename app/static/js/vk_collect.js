function vkvk() {
	let tok = '';
	let user = '110606704';
	var req="https://api.vk.com/method/users.get?user_ids="+user+"&v=5.59&access_token="+tok;
	$.ajax({
	url: req,
	type: 'post',
	dataType: 'jsonp',
	success: function (msg) {
		console.log(msg.response[0]);
	},
	complete: function () {
		// Schedule the next request when the current one has been completed
		
	}
	});
	
}
