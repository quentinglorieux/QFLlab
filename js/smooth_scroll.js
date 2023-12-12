document.querySelectorAll('a[href^="#"]').forEach(anchor => {
anchor.addEventListener('click', function (e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute('href'));
    const offset = 20; // Adjust this value to set your desired offset

    if (target) {
    window.scrollTo({
        top: target.offsetTop - offset,
        behavior: 'smooth'
    });
    }
});
});
