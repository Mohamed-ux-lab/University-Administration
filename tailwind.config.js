/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
   './templates/**/*.html',  // Prend en compte tous les fichiers HTML dans le dossier templates
   './classes/templates/**/*.html',
   './etudiant/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

