document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("themeToggle");
    const newsBox = document.getElementById("newsBox");

    // 🌑 Apply saved dark mode setting
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
    }

    // 🎛 Dark Mode Toggle
    themeToggle?.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
        localStorage.setItem("darkMode", document.body.classList.contains("dark-mode") ? "enabled" : "disabled");
    });
    document.addEventListener("DOMContentLoaded", () => {
        if (localStorage.getItem("darkMode") === "enabled") {
            document.body.classList.add("dark-mode");
        }
    });
    
    document.getElementById('darkModeToggle').addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem("darkMode", document.body.classList.contains("dark-mode") ? "enabled" : "disabled");
    });
    
    // 🚪 Prevent Unauthorized Access
    if (!localStorage.getItem("isLoggedIn") && !["/login.html", "/signup.html"].includes(window.location.pathname)) {
        alert("⚠️ You must be logged in to access this page.");
        window.location.href = "login.html";
    }

    // 📰 News Filter (With Loading Effect)
    window.filterNews = (category) => {
        newsBox.innerHTML = `<p>Loading ${category === "all" ? "all" : category} news...</p>`;
        setTimeout(() => {
            newsBox.innerHTML = `
                <h3>${category === "all" ? "All News" : category + " News"}</h3>
                <p>Displaying ${category === "all" ? "all" : category} news.</p>
            `;
        }, 500);
    };

    // 👤 Profile View (Simulation)
    window.viewProfile = () => {
        alert("👤 Profile settings will be available here.");
    };

    // 📝 Manage Articles (Simulation)
    window.manageArticles = () => {
        alert("✏️ Manage your articles here.");
    };

    // 🚪 Logout Functionality
    window.logout = () => {
        if (confirm("Are you sure you want to log out?")) {
            localStorage.removeItem("isLoggedIn"); // Clear session
            window.location.href = "login.html";
        }
    };
});
