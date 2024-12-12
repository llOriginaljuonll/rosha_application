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
    colors: {
      green: {
        "50": "#F3FAF7",
        "100": "#DEF7EC",
        "200": "#BCF0DA",
        "300": "#84E1BC",
        "400": "#31C48D",
        "500": "#0E9F6E",
        "600": "#057A55",
        "700": "#046C4E",
        "800": "#03543F",
        "900": "#014737",
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
