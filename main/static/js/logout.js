document.addEventListener("DOMContentLoaded", function () {
  const logoutBtn = document.getElementById("logoutBtn");

  logoutBtn.addEventListener("click", function () {
    const token = localStorage.getItem("token");

    if (!token) {
      alert("شما وارد نشده‌اید");
      return;
    }

    fetch("/api/profiles/logout/", {
      method: "POST",
      headers: {
        "Authorization": "Token " + token,
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response.ok) {
          localStorage.removeItem("token");
          alert("با موفقیت خارج شدید");
           window.location.href = "/";
        } else {
          alert("مشکلی در خروج پیش آمده");
        }
      })
      .catch((error) => {
        console.error("خطا:", error);
        alert("ارتباط با سرور ممکن نیست");
      });
  });
});
