// Scroll to top function
function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
}
  
// Show/hide back to top button based on scroll position
window.addEventListener("scroll", function() {
    var backToTopButton = document.getElementById("backToTopButton");
    if (window.pageYOffset > 100) {
      backToTopButton.classList.add("show");
    } else {
      backToTopButton.classList.remove("show");
    }
});