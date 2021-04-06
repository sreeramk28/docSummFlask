$(document).ready(function() { 
  // fetch('https://api.github.com/repos/javascript-tutorial/en.javascript.info/commits')
  // .then(response => response.json())
  // .then(commits => 	
  // 			document.getElementById("summary").innerHTML = commits[1].author.login);
	//$('form').on('submit', function(event) {
	$("#paperInput").on("change", uploadHandler);
	
});
function uploadHandler(event) {
	let fileInputControl = event.target;
	let files = fileInputControl.files;
	let firstFile = files[0];
	let fileReader = new FileReader();
	
	fileReader.onload = function(event) {
		let fileContents = event.target.result;
		//alert(fileContents);
		go(fileContents);
	}
	fileReader.readAsText(firstFile);
}
function go(fileContents) {
	$.ajax({
		data : {
			paper : fileContents,
		},
		type : 'POST',
		url : '/summary'
	})
	.done(function(data) {
		//console.log(data);
		document.getElementById("summary").innerHTML = data.summary;
	});

	//event.preventDefault();

}