document.getElementById('authbutton').onclick = function(){
	// change this when there's a domain
	location.href = 'https://'+window.location.hostname+'/authorize'
}
