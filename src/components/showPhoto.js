const photoFileInput = document.getElementById('photoFile');
const selectedPhotoContainer = document.getElementById('selectedPhotoContainer');
const selectedPhoto = document.getElementById('selectedPhoto');

photoFileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        selectedPhoto.src = e.target.result;
        selectedPhotoContainer.style.display = 'block';
    };

    reader.readAsDataURL(file);
});