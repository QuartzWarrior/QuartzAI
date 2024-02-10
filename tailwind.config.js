/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html", "./templates/*.html", "./*.{html,css,js}", "./templates/gui.html"],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/forms'),
  ],
}

