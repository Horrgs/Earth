document.addEventListener("DOMContentLoaded", function () {
    var subNavButtons = document.querySelectorAll(".sub-nav-button");
    var sections = document.querySelectorAll(".core-content section");

    subNavButtons.forEach((button) => {
        button.addEventListener("click", () => {
            var target = button.getAttribute("data-target");

            sections.forEach((section) => {
                section.classList.remove("active");
            });

            document.getElementById(target).classList.add("active");
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const sidebarToggle = document.getElementById("sidebar-toggle");
    const sidebar = document.getElementById("sidebar");
    const closeSidebarButton = document.getElementById("close-sidebar");

    sidebarToggle.addEventListener("click", function () {
        sidebar.classList.add("active");
    });

    closeSidebarButton.addEventListener("click", function () {
        sidebar.classList.remove("active");
    });
});

