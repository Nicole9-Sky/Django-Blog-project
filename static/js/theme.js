// Theme toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);

    // Theme toggle button
    const themeToggle = document.getElementById('theme-toggle');

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            // Get current theme
            let currentTheme = document.documentElement.getAttribute('data-theme');

            // Toggle between light and dark
            let newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            // Update theme
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);

            // Optional: Add smooth transition
            document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
        });
    }

    // Handle system theme preference changes
    if (window.matchMedia) {
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

        // Check if user hasn't manually selected a theme
        if (!localStorage.getItem('theme')) {
            // Set initial theme based on system preference
            if (mediaQuery.matches) {
                document.documentElement.setAttribute('data-theme', 'dark');
            }

            // Listen for system theme changes
            mediaQuery.addEventListener('change', function(e) {
                if (!localStorage.getItem('theme')) {
                    const newTheme = e.matches ? 'dark' : 'light';
                    document.documentElement.setAttribute('data-theme', newTheme);
                }
            });
        }
    }
});