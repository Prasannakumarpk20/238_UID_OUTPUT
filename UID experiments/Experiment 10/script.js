document
  .getElementById("registrationForm")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    let isValid = true;

    // Get form fields
    const fullname = document.getElementById("fullname");
    const rollnumber = document.getElementById("rollnumber");
    const phone = document.getElementById("phone");
    const email = document.getElementById("email");
    const address = document.getElementById("address");

    // Get error fields
    const fullnameError = document.getElementById("fullnameError");
    const rollnumberError = document.getElementById("rollnumberError");
    const phoneError = document.getElementById("phoneError");
    const emailError = document.getElementById("emailError");
    const addressError = document.getElementById("addressError");

    // Reset error messages
    fullnameError.textContent = "";
    rollnumberError.textContent = "";
    phoneError.textContent = "";
    emailError.textContent = "";
    addressError.textContent = "";

    // Full Name validation
    if (fullname.value.trim() === "") {
      fullnameError.textContent = "Full Name is required.";
      isValid = false;
    }

    // Roll Number validation (should be alphanumeric)
    if (!/^[a-zA-Z0-9]+$/.test(rollnumber.value.trim())) {
      rollnumberError.textContent = "Roll Number must be alphanumeric.";
      isValid = false;
    }

    // Phone validation (should be exactly 10 digits)
    if (!/^\d{10}$/.test(phone.value.trim())) {
      phoneError.textContent = "Phone number must be exactly 10 digits.";
      isValid = false;
    }

    // Email validation (basic pattern)
    if (!/^\S+@\S+\.\S+$/.test(email.value.trim())) {
      emailError.textContent = "Enter a valid email address.";
      isValid = false;
    }

    // Address validation
    if (address.value.trim() === "") {
      addressError.textContent = "Address is required.";
      isValid = false;
    }

    if (isValid) {
      alert("Form submitted successfully!");
      document.getElementById("registrationForm").reset();
    }
  });
