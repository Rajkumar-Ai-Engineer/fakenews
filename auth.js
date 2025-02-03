// 🔐 Sign Up Function
function signUp() {
    let username = document.getElementById("signupUsername").value;
    let password = document.getElementById("signupPassword").value;

    if (!username || !password) {
        alert("Please enter a username and password.");
        return;
    }

    // Hash the password (simple encoding, not secure for production)
    let hashedPassword = btoa(password); // Base64 Encoding

    // Store in Local Storage
    localStorage.setItem("username", username);
    localStorage.setItem("password", hashedPassword);
    
    alert("Signup Successful! Please login.");
    window.location.href = "login.html"; // Redirect to login page
}

// 🔑 Login Function
function login() {
    let username = document.getElementById("loginUsername").value;
    let password = document.getElementById("loginPassword").value;
    let storedUsername = localStorage.getItem("username");
    let storedPassword = localStorage.getItem("password");

    if (username === storedUsername && btoa(password) === storedPassword) {
        alert("Login Successful!");
        localStorage.setItem("isLoggedIn", "true"); // Session Handling
        window.location.href = "index.html"; // Redirect to Home
    } else {
        alert("Invalid username or password.");
    }
}

// 🚪 Logout Function
function logout() {
    localStorage.removeItem("isLoggedIn"); // Clear session
    alert("Logged out successfully!");
    window.location.href = "login.html"; // Redirect to login page
}

// ⛔ Prevent Unauthorized Access
document.addEventListener("DOMContentLoaded", () => {
    let isLoggedIn = localStorage.getItem("isLoggedIn");
    let currentPage = window.location.pathname.split("/").pop();

    // Protect pages (except login & signup)
    if (!isLoggedIn && currentPage !== "login.html" && currentPage !== "signup.html") {
        alert("You must be logged in to access this page.");
        window.location.href = "login.html";
    }
});
