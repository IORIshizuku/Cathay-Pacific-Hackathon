
function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
}
  

window.addEventListener("scroll", function() {
    var backToTopButton = document.getElementById("backToTopButton");
    if (window.pageYOffset > 100) {
      backToTopButton.classList.add("show");
    } else {
      backToTopButton.classList.remove("show");
    }
});