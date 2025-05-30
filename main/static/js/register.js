function showJobSeekerForm() {
  loginForm.innerHTML = `
    <div class="div-2">
      <input id="username" class="text-wrapper" placeholder="نام کاربری"><hr>
    </div>
    <div class="div-3">
      <input type="password" id="password" class="text-wrapper-2" placeholder="رمز عبور"><hr>
    </div>
    <div class="div-6">
      <button id="submit-btn"><div class="text-wrapper-5">ارسال</div></button>
    </div>
  `;

  document.getElementById("submit-btn").addEventListener("click", async () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const payload = {
      role: "jobseeker",
      username,
      password
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/api/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        showSuccessMessage("ثبت‌نام کارجو با موفقیت انجام شد.");
      } else {
        const error = await response.json();
        showSuccessMessage("❌ خطا: " + error.message);
      }
    } catch (err) {
      showSuccessMessage("❌ خطا در اتصال به سرور");
    }
  });
}

function showEmployerForm() {
  loginForm.innerHTML = `
    <div class="div-2">
      <input id="username" class="text-wrapper" placeholder="نام کاربری"><hr>
    </div>
    <div class="div-3">
      <input type="password" id="password" class="text-wrapper-2" placeholder="رمز عبور"><hr>
    </div>
    <div class="div-3">
      <input id="email" class="text-wrapper-2" placeholder="آدرس ایمیل"><hr>
    </div>
    <div class="div-3">
      <input id="company" class="text-wrapper-2" placeholder="آدرس شرکت"><hr>
    </div>
    <div class="div-6">
      <button id="submit-btn"><div class="text-wrapper-5">ارسال</div></button>
    </div>
  `;

  document.getElementById("submit-btn").addEventListener("click", async () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const email = document.getElementById("email").value;
    const company = document.getElementById("company").value;

    const payload = {
      role: "employer",
      username,
      password,
      email,
      company
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/api/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        showSuccessMessage("ثبت‌نام کارفرما با موفقیت انجام شد.");
      } else {
        const error = await response.json();
        showSuccessMessage("❌ خطا: " + error.message);
      }
    } catch (err) {
      showSuccessMessage("❌ خطا در اتصال به سرور");
    }
  });
}
