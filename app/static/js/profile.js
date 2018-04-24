// Scripts to run on profile.html

// Change User Email
// Click button -> display form
let emailForm = document.getElementById('email-form');
let emailButton = document.getElementById('change-email-button');

emailForm.style.display = 'none';

emailButton.addEventListener('click', function() {
    emailForm.style.display = 'inline';
})