document.getElementById('uploadForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const videoInput = document.getElementById('videoInput');
    const file = videoInput.files[0];
    if (!file) {
        alert("Please select a video file.");
        return;
    }

    const formData = new FormData();
    formData.append('video', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById('result').innerText = result.message;
    } catch (error) {
        console.error('Error uploading video:', error);
        document.getElementById('result').innerText = 'Error uploading video.';
    }
});
