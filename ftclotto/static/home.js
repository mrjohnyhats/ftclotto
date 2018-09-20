var curPoints, username;


$(document).ready(function(){
	username = $('#usernameVal').text();
	getUserData(username, activateBetButton);
});


function getUserData(username, cb){
	$.ajax({
		type: 'POST',
		url: 'https://'+window.location.hostname+'/userdata',
		data: JSON.stringify({'username': username}),
		success: cb,
		contentType: 'application/json'
	});
}

function activateBetButton(data){
	curPoints = data['points'];
	username = data['username'];
	$('#points').text('points: '+curPoints);

	var betFinished = function(){
		getUserData(username, function(data){
			curPoints = data['points'];
			$('#points').text('points: '+curPoints);
		});
	}

	$('#betbutton').click(function(){
		var betAmount = parseInt($('#betAmount').val());

		if(isNaN(betAmount)){
			betAmount = 0;
		} else if(betAmount > curPoints){
			betAmount = curPoints;
		}

		$('#betAmount').val(betAmount);

		$.ajax({
			type: 'POST',
			url: 'https://'+window.location.hostname+'/bet',
			data: JSON.stringify({'username': username, 'betAmount': betAmount}),
			success: betFinished,
			contentType: 'application/json'
		});
	});
}
