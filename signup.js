function signUp() {
    let username = document.getElementById("signupUsername").value;
    let password = document.getElementById("signupPassword").value;

    if (!username || !password) {
        alert("Please enter a username and password.");
        return;
    }

    // Hash the password (Base64 Encoding)
    let hashedPassword = btoa(password);

    // Store in Local Storage
    localStorage.setItem("username", username);
    localStorage.setItem("password", hashedPassword);
    
    alert("Signup Successful! Please login.");
    window.location.href = "login.html";
}
