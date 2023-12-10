let hamb = document.querySelector(".btn_burger");
let subMenu = document.querySelector(".sub_menu");

hamb.addEventListener("click", menu);

function menu() {
    hamb.classList.toggle("active");
    subMenu.classList.toggle("active");
}

