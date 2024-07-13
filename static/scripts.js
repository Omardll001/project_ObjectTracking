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

    // Show processing animation
    document.getElementById('result').innerHTML = '<div class="loader"></div>';

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        
         // Hide processing animation and show the video
         document.getElementById('result').innerHTML = `
         <p>${result.message}</p>
         <div class="video-container">
             <video controls>
                 <source src="${result.video_path}" type="video/mp4">
                 Your browser does not support the video tag.
             </video>
         </div>
     `;
 } catch (error) {
     console.error('Error uploading video:', error);
     document.getElementById('result').innerText = 'Error uploading video.';
 }
});