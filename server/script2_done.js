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

function toggleInputVisibility() {
    const numBooksInput = document.getElementById('num-books');
    const userIdInput = document.getElementById('user-id');
    const submitButton = document.querySelector('.input-container button');

    if (currentAction === 'recommendation') {
        userIdInput.style.display = 'inline-block'; // Show User ID input
    } else {
        userIdInput.style.display = 'none'; // Hide User ID input for other actions
    }

    document.getElementById('input-container').style.display = 'flex'; // Show input form
}

// Handle low-rated books button click
async function handleLowRatedClick() {
    currentAction = 'low-rated'; // Set the current action to low-rated
    toggleInputVisibility(); // Show input form
}

// Handle high-rated books button click
async function handleHighRatedClick() {
    currentAction = 'high-rated'; // Set the current action to high-rated
    toggleInputVisibility(); // Show input form
}

// Handle existing users button click
async function handleExistingUsersClick() {
    const users = await fetchExistingUsers();
    displayUsers(users);
}

// Handle recommendation button click
async function handleRecommendationClick() {
    currentAction = 'recommendation'; // Set the current action to recommendation
    toggleInputVisibility(); // Show input form
}

// Fetch books based on current action
async function fetchBooksByType() {
    const numBooks = document.getElementById('num-books').value;
    if (!numBooks || numBooks <= 0) {
        alert("Please enter a valid number of books.");
        return;
    }

    let books = [];
    const userId = document.getElementById('user-id').value;

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
            displayError(recommendations.error); // Display the error message
            return; // Exit early if there's an error
        }
        displayBooks(recommendations);
        return; // Return early to prevent the default behavior
    }

    displayBooks(books); // Display the books after fetching
    document.getElementById('input-container').style.display = 'none'; // Hide input form after submission
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

    if (users.message) {
        bookListContainer.innerHTML = `<p>${users.message}</p>`;
        return;
    }

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
