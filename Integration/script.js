const API_URL = "http://127.0.0.1:8000"; 

function login() {
    let username = document.getElementById("login-username").value;
    let password = document.getElementById("login-password").value;

    fetch(`${API_URL}/articles/api/custom-token/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.access) {
            localStorage.setItem("access_token", data.access);
            window.location.href = "articles.html"; // Redirect to articles page
        } else {
            alert("Invalid credentials");
        }
    })
    .catch(error => console.error("Login Error:", error));
}

function signup() {
    let username = document.getElementById("signup-username").value;
    let email = document.getElementById("signup-email").value;
    let password = document.getElementById("signup-password").value;

    fetch(`${API_URL}/articles/register/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email, password })
    })
    .then(response => response.json())
    .then(data => {
        alert("User registered! Please login.");
        window.location.href = "login.html"; // Redirect to login page
    })
    .catch(error => console.error("Signup Error:", error));
}

function logout() {
    localStorage.removeItem("access_token");
    window.location.href = "login.html"; // Redirect to login after logout
}

function checkAuth() {
    let accessToken = localStorage.getItem("access_token");

    if (!accessToken) {
        window.location.href = "login.html"; // Redirect if not logged in
    } else {
        try {
            let decoded = JSON.parse(atob(accessToken.split('.')[1])); // Decode JWT
            document.getElementById("user-name").innerText = decoded.username || "User";
            document.getElementById("user-email").innerText = decoded.email || "No Email";
            fetchArticles();
        } catch (error) {
            console.error("Error decoding token:", error);
        }
    }
}

function fetchArticles() {
    let accessToken = localStorage.getItem("access_token");

    fetch(`${API_URL}/articles/`, {
        method: "GET",
        // headers: { "Authorization": `Bearer ${accessToken}` }
    })
    .then(response => response.json())
    .then(data => {
        let articlesDiv = document.getElementById("articles-list");
        articlesDiv.innerHTML = "";
        data.forEach(article => {
            articlesDiv.innerHTML += `<div>
                <h3>${article.title}</h3>
                <p>${article.content}</p>
                <button onclick="deleteArticle(${article.id})">Delete</button>
            </div>`;
        });
    });
}

function createArticle() {
    let title = document.getElementById("article-title").value;
    let content = document.getElementById("article-content").value;
    let accessToken = localStorage.getItem("access_token");

    fetch(`${API_URL}/articles/`, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Authorization": `` },
        body: JSON.stringify({ title, content, author: 1 })
    })
    .then(response => response.json())
    .then(() => fetchArticles());
}

function deleteArticle(id) {
    let accessToken = localStorage.getItem("access_token");

    fetch(`${API_URL}/api/articles/${id}/`, {
        method: "DELETE",
        headers: { "Authorization": `Bearer ${accessToken}` }
    })
    .then(() => fetchArticles());
}
