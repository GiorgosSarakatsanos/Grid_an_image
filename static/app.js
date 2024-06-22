if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/static/service-worker.js').then(function(registration) {
            console.log('Service Worker registered with scope:', registration.scope);

            registration.addEventListener('updatefound', () => {
                const installingWorker = registration.installing;
                installingWorker.addEventListener('statechange', () => {
                    if (installingWorker.state === 'installed') {
                        if (navigator.serviceWorker.controller) {
                            // New update available
                            const statusElement = document.getElementById('status');
                            statusElement.textContent = 'Update Available. Please refresh the page.';
                        }
                    }
                });
            });
        }).catch(function(error) {
            console.error('Service Worker registration failed:', error);
        });
    });
}
