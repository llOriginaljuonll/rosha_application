/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit', // เปิดใช้งานโหมด JIT
  darkMode: 'selector',
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js',
    './src/**/*.{js,jsx,ts,tsx}', // เพิ่มเส้นทางไฟล์สำหรับโหมด JIT
    './public/index.html', // เพิ่มเส้นทางไฟล์สำหรับโหมด JIT
  ],
  theme: {
    extend: {
      padding: {
        '12': '3rem', // ตรวจสอบว่ามีการกำหนดค่า padding นี้
      },
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
    require('flowbite/plugin'),
    function ({ addUtilities }) {
      const newUtilities = {
        '.placeholder-bold::placeholder': {
          fontWeight: '300',
        },
      };
      addUtilities(newUtilities, ['responsive', 'hover', 'focus']);
    },
  ],
}
