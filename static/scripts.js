document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const videoInput = document.getElementById('videoInput');
    const file = videoInput.files[0];
    if (!file) {
        alert("Please select a video file.");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    // Show processing animation
    document.body.innerHTML = `
        <h1>Processing...</h1>
        <div class="loader"></div>
    `;

    fetch('/upload', {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        } else {
            alert('Error processing video.');
        }
    }).catch(error => {
        console.error('Error uploading video:', error);
        alert('Error uploading video.');
    });
});
