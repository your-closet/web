function previewFile() {
    // Where you will display your image
    var preview = document.getElementById('clothing-view');
    // The button where the user chooses the local image to display
    var file = document.getElementById('image').files[0];
    // FileReader instance
    var reader = new FileReader();
    console.log(reader);

    // When the image is loaded we will set it as source of
    // our img tag
    reader.onloadend = function () {
        preview.style.backgroundColor = "transparent";
        preview.style.backgroundImage = "url(" + reader.result + ")";
    }

    if (file) {
        // Load image as a base64 encoded URI
        reader.readAsDataURL(file);
    } else {
        preview.style.backgroundImage = "";
    }
}

