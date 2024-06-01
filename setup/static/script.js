const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('.menu-list');

menuToggle.addEventListener('click', () => {
  navMenu.classList.toggle('active');
});

