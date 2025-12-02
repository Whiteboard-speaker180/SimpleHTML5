// Get reference to the theme toggle button element by its ID
const toggle = document.getElementById('theme-toggle');

// Get reference to the root HTML element to set the data-theme attribute
const html = document.documentElement;

// Function to get the current theme from the data-theme attribute or system preference
function getTheme() {
    // Check if data-theme is already set on the html element; otherwise fall back to system preference
    return html.getAttribute('data-theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
}

// Function to set the theme on the html element and save it to localStorage
function setTheme(theme) {
    // Apply the theme by setting the data-theme attribute on the root html element
    html.setAttribute('data-theme', theme);
    // Persist the user's theme choice in browser storage
    localStorage.setItem('theme', theme);
    // Update the toggle button text to reflect the opposite theme
    updateToggleText(theme);
}

// Function to update the toggle button text and aria-label for accessibility
function updateToggleText(theme) {
    // Query the .toggle-text element inside the toggle button to update its display text
    const text = toggle.querySelector('.toggle-text');
    // Set button text to show what theme will be switched to (opposite of current)
    text.textContent = theme === 'dark' ? 'Light' : 'Dark';
    // Update aria-label for screen readers
    toggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
}

// Initialize theme on page load
// Check if user has previously saved a theme preference in localStorage
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    // Use the saved theme preference
    setTheme(savedTheme);
} else {
    // Use the detected current theme (system preference or default)
    setTheme(getTheme());
}

// Handle toggle button click to switch between themes
toggle.addEventListener('click', () => {
    // Get the current theme and toggle to the opposite
    const currentTheme = getTheme();
    setTheme(currentTheme === 'dark' ? 'light' : 'dark');
});

// Listen for changes to the system color scheme preference and update theme accordingly
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (event) => {
    // Update theme when system preference changes (only if no user preference is saved)
    setTheme(event.matches ? 'dark' : 'light');
});
