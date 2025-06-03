document.addEventListener("DOMContentLoaded", function () {
  const loginBtn = document.getElementById("login-btn");

  loginBtn.addEventListener("click", async function () {
    const username = document.querySelector(".text-wrapper").value.trim();
    const password = document.querySelector(".text-wrapper-2").value.trim();

    if (!username || !password) {
      alert("نام کاربری و رمز عبور را وارد کنید.");
      return;
    }

    fetch("http://127.0.0.1:8000/api/login/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ username:"test1", password:"1234" })
})
  .then(res => res.json().then(data => {
    if (res.ok) {
      console.log("توکن:", data.token);
      localStorage.setItem("token", data.token);
      alert("ورود موفق!");
    } else {
      throw new Error(data.detail || "مشکلی پیش آمد");
    }
  }))
  .catch(err => {
    alert("خطا: " + err.message);
  })})})