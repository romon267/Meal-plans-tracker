// Navbar
const burgerIcon = document.querySelector('#burger');
const navbarMenu = document.querySelector('#nav-links');

burgerIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active');
    burgerIcon.classList.toggle('is-active');
});

const notificationDelete = document.querySelector('#delete-notification');
const notification = document.querySelector('#notification');

notificationDelete.addEventListener('click', () => {
    notification.parentNode.removeChild(notification);
});