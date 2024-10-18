document.addEventListener('DOMContentLoaded', function () {
    // Sélectionner tous les liens du sidenav
    const navLinks = document.querySelectorAll('.nav-link');
    const contentDiv = document.getElementById('content');
    const loadingSpinner = document.getElementById('loading-spinner');

    navLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault(); // Empêcher le comportement par défaut (rechargement de la page)
            const url = this.getAttribute('href');

            // Afficher le spinner de chargement
            loadingSpinner.classList.remove('hidden');

            // Requête Fetch pour charger dynamiquement le contenu
            fetch(url)
                .then(response => response.text())
                .then(data => {
                    // Remplacer le contenu de la div #content avec le nouveau contenu
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(data, 'text/html');
                    const newContent = doc.querySelector('#content').innerHTML;
                    contentDiv.innerHTML = newContent;

                    // Cacher le spinner de chargement
                    loadingSpinner.classList.add('hidden');
                })
                .catch(error => {
                    console.error('Erreur de chargement:', error);
                    // Cacher le spinner même en cas d'erreur
                    loadingSpinner.classList.add('hidden');
                });
        });
    });
});