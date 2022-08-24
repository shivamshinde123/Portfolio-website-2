
//this is used to make the navbar responsive
const toggleButton = document.getElementsByClassName('toggle-btn')[0]
const navbarLinks = document.getElementsByClassName('nav')[0]

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})
