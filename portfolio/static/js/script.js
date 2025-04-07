// Contact form submission
document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/contact', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('formMessage').innerText = result.message;
    this.reset(); // Reset the contact form
});

// Lead generation pop-up
const popup = document.getElementById('leadGenPopup');
const closeBtn = document.getElementsByClassName('close')[0];

// Show pop-up after 5 seconds
setTimeout(() => {
    popup.style.display = 'block';
}, 5000);

// Close pop-up when clicking the 'x'
closeBtn.onclick = function() {
    popup.style.display = 'none';
};

// Handle lead gen form submission
document.getElementById('leadGenForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/lead-gen', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('leadGenMessage').innerText = result.message;
    this.reset(); // Reset the lead gen form
    setTimeout(() => {
        popup.style.display = 'none';
    }, 2000); // Hide pop-up after 2 seconds
});