// script.js

document
  .getElementById("login-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form from submitting immediately

    // Get input values
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;

    // Reset previous error messages
    resetErrors();

    // Validation flags
    let isValid = true;

    // Email Validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      document.getElementById("email-error").style.display = "block";
      isValid = false;
    }

    // Phone Number Validation (10 digits)
    const phoneRegex = /^\d{10}$/;
    if (!phoneRegex.test(phone)) {
      document.getElementById("phone-error").style.display = "block";
      isValid = false;
    }

    // If everything is valid, display success message
    if (isValid) {
      document.getElementById("success-message").style.display = "block";
    }
  });

// Function to reset error messages
function resetErrors() {
  document.getElementById("email-error").style.display = "none";
  document.getElementById("phone-error").style.display = "none";
  document.getElementById("success-message").style.display = "none";
}
