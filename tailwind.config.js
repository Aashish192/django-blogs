/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
  './templates/**/*.html',
  './**/templates/**/*.html',
  './static/**/*.js',
  './static/**/*.html',  // in case some html files are in static
],
  theme: {
    extend: {},
  },
  plugins: [],
}