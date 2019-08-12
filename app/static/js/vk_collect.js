function vkvk() {
	let tok = '2ae1b3d3aae47b6f27b06dc7e2efc2c8f2004b971ed4a398cee255ad5c11a69b1bab496cd0e56cfd8205c';
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