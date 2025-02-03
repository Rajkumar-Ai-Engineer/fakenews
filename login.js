function login() {
    let username = document.getElementById("loginUsername").value;
    let password = document.getElementById("loginPassword").value;
    let storedUsername = localStorage.getItem("username");
    let storedPassword = localStorage.getItem("password");

    if (username === storedUsername && btoa(password) === storedPassword) {
        alert("Login Successful!");
        localStorage.setItem("isLoggedIn", "true");
        window.location.href = "index.html"; // Redirect to Home
    } else {
        alert("Invalid username or password.");
    }
}

// 🚪 Logout Functionality
function logout() {
    localStorage.removeItem("isLoggedIn");
    alert("Logged out successfully!");
    window.location.href = "login.html";
}

