let currentAction = ''; // Variable to store the current action (low-rated, high-rated, recommendations)

async function fetchLowRatedBooks(nums) {
    const response = await fetch('http://127.0.0.1:8000/low-rated', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nums: nums })
    });
    const data = await response.json();
    return data;
}

async function fetchHighRatedBooks(nums) {
    const response = await fetch('http://127.0.0.1:8000/high-rated', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nums: nums })
    });
    const data = await response.json();
    return data;
}

async function fetchExistingUsers() {
    const response = await fetch('http://127.0.0.1:8000/existing-users');
    const data = await response.json();
    return data;
}

async function fetchRecommendations(userId, numRecommendations) {
    const response = await fetch('http://127.0.0.1:8000/recommend/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: userId, num_recommendations: numRecommendations })
    });

    if (!response.ok) {
        const error = await response.json();
        return { error: error.detail }; // Return the error message from the backend
    }

    const data = await response.json();
    return data;
}

function toggleInputFields(action) {
    const inputContainer = document.getElementById('input-container');
    const numBooksInput = document.getElementById('num-books');
    const userIdInput = document.getElementById('user-id');
    const userIdLabel = document.getElementById('user-id-label');

    if (action === 'low-rated' || action === 'high-rated') {
        inputContainer.style.display = 'flex';
        userIdInput.style.display = 'none';
        userIdLabel.style.display = 'none';
        numBooksInput.style.display = 'inline-block';
    } else if (action === 'recommendation') {
        inputContainer.style.display = 'flex';
        userIdInput.style.display = 'inline-block';
        userIdLabel.style.display = 'inline-block';
        numBooksInput.style.display = 'inline-block';
    } else if (action === 'existing-users') {
        inputContainer.style.display = 'none';
    }
}

// Handle low-rated books button click
function handleLowRatedClick() {
    currentAction = 'low-rated';
    toggleInputFields(currentAction);
}

// Handle high-rated books button click
function handleHighRatedClick() {
    currentAction = 'high-rated';
    toggleInputFields(currentAction);
}

// Handle existing users button click
function handleExistingUsersClick() {
    currentAction = 'existing-users';
    toggleInputFields(currentAction);
    // Fetch and display existing users
    fetchExistingUsers().then(users => displayUsers(users));
}

// Handle recommendation button click
function handleRecommendationClick() {
    currentAction = 'recommendation';
    toggleInputFields(currentAction);
}

// Fetch books based on current action
async function fetchBooksByType() {
    const numBooks = document.getElementById('num-books').value;
    const userId = document.getElementById('user-id').value;

    if (!numBooks || numBooks <= 0) {
        alert("Please enter a valid number of books.");
        return;
    }

    let books = [];
    if (currentAction === 'low-rated') {
        books = await fetchLowRatedBooks(numBooks);
    } else if (currentAction === 'high-rated') {
        books = await fetchHighRatedBooks(numBooks);
    } else if (currentAction === 'recommendation') {
        if (!userId) {
            alert("Please enter a valid user ID.");
            return;
        }
        const recommendations = await fetchRecommendations(userId, numBooks);
        if (recommendations.error) {
            displayError(recommendations.error);
            return;
        }
        displayBooks(recommendations);
        return;
    }

    displayBooks(books);
}

// Display books in a table format
function displayBooks(books) {
    const bookListContainer = document.getElementById('book-list-container');
    bookListContainer.innerHTML = '';

    if (books.message) {
        bookListContainer.innerHTML = `<p>${books.message}</p>`;
        return;
    }

    const table = document.createElement('table');
    const headerRow = document.createElement('tr');
    headerRow.innerHTML = `
        <th>Book Title</th>
        <th>Author</th>
        <th>Year</th>
        <th>Publisher</th>
        <th>Image</th>
    `;
    table.appendChild(headerRow);

    books.forEach(book => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${book['Book-Title']}</td>
            <td>${book['Book-Author']}</td>
            <td>${book['Year-Of-Publication']}</td>
            <td>${book['Publisher']}</td>
            <td><img src="${book['Image-URL-L']}" alt="${book['Book-Title']}"></td>
        `;
        table.appendChild(row);
    });

    bookListContainer.appendChild(table);
}

// Display users in a list format
function displayUsers(users) {
    const bookListContainer = document.getElementById('book-list-container');
    bookListContainer.innerHTML = '';

    const userList = document.createElement('ul');
    users.forEach(user => {
        const userItem = document.createElement('li');
        userItem.textContent = `User ID: ${user}`;
        userList.appendChild(userItem);
    });

    bookListContainer.appendChild(userList);
}

// Display error message on the page
function displayError(errorMessage) {
    const bookListContainer = document.getElementById('book-list-container');
    bookListContainer.innerHTML = `<p style="color: red;">Error: ${errorMessage}</p>`;
}
