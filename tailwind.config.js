/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/",
    "./**\*.py",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      screens: {
        'sm': '300px',
        'md': '640px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
