
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  // const overlaproup = document.getElementById("overlap-group");
  const loginBtn = document.getElementById("login-btn");
  const registerBtn = document.getElementById("rgister");
  const resetPasswordBtn = document.getElementById("reset-password");

  // تابع نمایش پیام موفقیت
  function showSuccessMessage(message) {
    loginForm.innerHTML = `
      <div class="sucsses">
        <h1 style="font-size:4rem;">${message} </h1>
        <img src="./image/smile.svg" class='smile'>
        
        <h2>در حال انتقال به محتوای صفحه اصلی</h2>
        <img src="image/wait.svg" alt="" class="wait">
      </div>
    `;
  }

  // تابع ساخت فرم ورود اولیه
  function showLoginForm() {
    showSuccessMessage("ورود با موفقیت انجام شد.");
  }

  // فرم ثبت‌نام کارفرما
  function showEmployerForm() {
    loginForm.innerHTML = `
      <div class="div-2">
        <input class="text-wrapper" placeholder="نام کاربری"><hr>
      </div>
      <div class="div-3">
        <input class="text-wrapper-2" placeholder="رمز عبور"><hr>
      </div>
      <div class="div-3">
        <input class="text-wrapper-2" placeholder="آدرس ایمیل"><hr>
      </div>
      <div class="div-3">
        <input class="text-wrapper-2" placeholder="آدرس شرکت"><hr>
      </div>
      <div class="div-6">
        <button id="submit-btn"><div class="text-wrapper-5">ارسال</div></button>
      </div>
    `;
    document.getElementById("submit-btn").addEventListener("click", () => {
      showSuccessMessage("ورود با موفقیت انجام شد.");
    });
  }

  // فرم ثبت‌نام کارجو
  function showJobSeekerForm() {
    loginForm.innerHTML = `
      <div class="div-2">
        <input class="text-wrapper" placeholder="نام کاربری"><hr>
      </div>
      <div class="div-3">
        <input class="text-wrapper-2" placeholder="رمز عبور"><hr>
      </div>
      <div class="div-6">
        <button id="submit-btn"><div class="text-wrapper-5">ارسال</div></button>
      </div>
    `;
    document.getElementById("submit-btn").addEventListener("click", () => {
      showSuccessMessage("ورود با موفقیت انجام شد.");
    });
  }

  // فرم انتخاب نقش (کارجو/کارفرما)
  function showRoleSelector() {
    loginForm.innerHTML = `
      <div class="div-6">
        <button id="employers-btn"><div class="text-wrapper-5">ورود کارفرمایان</div></button>
        <button id="job-seekers-btn"><div class="text-wrapper-5">ورود کارجویان</div></button>
      </div>
    `;

    document.getElementById("employers-btn").addEventListener("click", showEmployerForm);
    document.getElementById("job-seekers-btn").addEventListener("click", showJobSeekerForm);
  }

  // فرم بازیابی رمز عبور
  function showResetPasswordForm() {
    loginForm.innerHTML = `
      <div class="div-2">
        <input class="text-wrapper" placeholder="شماره تلفن"><hr>
      </div>
      <div class="div-3">
        <input class="text-wrapper-2" placeholder="رمز عبور"><hr>
      </div>
      <div class="div-3">
        <input class="text-wrapper-2" placeholder="تکرار رمز عبور"><hr>
      </div>
      <div class="div-6">
        <button id="submit-btn"><div class="text-wrapper-5">ارسال</div></button>
      </div>
    `;
    document.getElementById("submit-btn").addEventListener("click", () => {
      showSuccessMessage("رمز عبور با موفقیت تغییر کرد.");
    });
  }

  // رویدادها
  loginBtn.addEventListener("click", showLoginForm);
  registerBtn.addEventListener("click", (e) => {
    e.preventDefault();
    showRoleSelector();
  });
  resetPasswordBtn.addEventListener("click", (e) => {
    e.preventDefault();
    showResetPasswordForm();
  });
});

