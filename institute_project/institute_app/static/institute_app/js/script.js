// script.js
document.addEventListener("DOMContentLoaded", function () {
    console.log("Institute Dashboard Ready");

    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        alert.addEventListener("click", () => {
            alert.classList.add("fade");
        });
    });
});
