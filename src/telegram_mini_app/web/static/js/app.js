// Initialize the Telegram WebApp
const webApp = window.Telegram.WebApp;

// Expand the app to full height
webApp.expand();

// Get user data
const user = webApp.initDataUnsafe.user;

// Update the UI with user information
document.getElementById('username').textContent = user?.first_name || 'there';

// Handle profile picture
const avatarElement = document.getElementById('user-avatar');
const requestButton = document.getElementById('request-photo');
const userDataElement = document.getElementById('user-data');

async function saveUserData() {
    try {
        const response = await fetch('/api/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: user.id,
                first_name: user.first_name,
                last_name: user.last_name,
                username: user.username,
                photo_url: user.photo_url
            })
        });
        const data = await response.json();
        console.log('User data saved:', data);
    } catch (error) {
        console.error('Error saving user data:', error);
    }
}

async function loadUserData() {
    try {
        const response = await fetch(`/api/users?telegramId=${user.id}`);
        const data = await response.json();
        if (data.last_seen) {
            userDataElement.innerHTML = `Last seen: ${new Date(data.last_seen).toLocaleString()}`;
        }
    } catch (error) {
        console.error('Error loading user data:', error);
    }
}

function updateAvatar() {
    if (user?.photo_url) {
        avatarElement.src = user.photo_url;
        requestButton.style.display = 'none';
    } else {
        avatarElement.style.display = 'none';
        requestButton.style.display = 'block';
    }
}

// Initial check
updateAvatar();
saveUserData();
loadUserData();

// Handle photo request button click
requestButton.addEventListener('click', () => {
    webApp.requestWriteAccess().then(() => {
        // After getting write access, the photo_url should be available
        const updatedUser = webApp.initDataUnsafe.user;
        if (updatedUser?.photo_url) {
            avatarElement.style.display = 'block';
            avatarElement.src = updatedUser.photo_url;
            requestButton.style.display = 'none';
            saveUserData(); // Save updated user data
        }
    }).catch(() => {
        // Handle the case when user denies access
        alert('Please grant access to show your profile picture');
    });
}); 