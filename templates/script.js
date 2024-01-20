// JavaScript to handle image selection and AJAX request
document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    // Display the selected image
    var image = document.getElementById('image-input').files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('selected-image').src = e.target.result;
        document.getElementById('selected-image').style.display = 'block';
    }
    reader.readAsDataURL(image);

    // AJAX request to Flask server
    var formData = new FormData();
    formData.append('file', image);
    fetch('/predict', {
        method: 'POST',
        body: formData
    }).then(response => response.json()).then(data => {
        console.log(data); // This will log the response data to the console
        document.getElementById('prediction').textContent = 'Predicted Label: ' + data.predicted_class;
    }).catch(error => {
console.error('Error:', error);
});
reader.onload = function(e) {
var imgElement = document.getElementById('selected-image');
imgElement.src = e.target.result;
imgElement.style.display = 'block';
imgElement.width = 32;   // Set width to 32 pixels
imgElement.height = 32;  // Set height to 32 pixels
}
});

