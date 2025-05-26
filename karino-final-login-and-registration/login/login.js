document.addEventListener("DOMContentLoaded", () => {
  const doc = document;
  const login_btn = doc.getElementById('login-btn');
  const loginForm = doc.getElementById('login-form');
  const rgister = doc.getElementById('rgister');

  login_btn.addEventListener("click", () => {
    loginForm.innerHTML = `<div class="sucsses">
      <h1>ورود با موفقیت انجام شد.</h1>
      <h2>در حال انتقال به محتوای صفحه اصلی</h2>
      <img src="image/wait.svg" alt="">
    </div>`;
  });

  rgister.addEventListener('click', (event) => {
    event.preventDefault();
    loginForm.innerHTML = `
      <div class="div-6">
        <button id="employers-btn"><div class="text-wrapper-5">ورود کارفرمایان</div></button>
        <button id="job-seekers-btn"><div class="text-wrapper-5">ورود کارجویان</div></button>
      </div>
    `;

    const employers = document.getElementById('employers-btn');
    const jobseekers = document.getElementById('job-seekers-btn');

    employers.addEventListener('click', () => {
      loginForm.innerHTML = `
        <div class="div-2">
          <input class="text-wrapper" placeholder="نام کاربری:">
          <hr>
        </div>
        <div class="div-3">
          <input class="text-wrapper-2" placeholder="رمز عبور:">
          <hr>
        </div>
        <div class="div-3">
          <input class="text-wrapper-2" placeholder="آدرس ایمیل:">
          <hr>
        </div>
        <div class="div-3">
          <input class="text-wrapper-2" placeholder="آدرس شرکت:">
          <hr>
          <div class="div-6">
            <button id="login-btn"><div class="text-wrapper-5">ارسال</div></button>
          </div>
        </div>
      `;

      // ✨ بعد از اضافه شدن فرم، دکمه ارسال رو انتخاب کن و براش رویداد تعریف کن
      const submitBtn = document.getElementById('login-btn');
      submitBtn.addEventListener('click', () => {
        loginForm.innerHTML = `<div class="sucsses">
          <h1>ورود با موفقیت انجام شد.</h1>
          <h2>در حال انتقال به محتوای صفحه اصلی</h2>
          <img src="image/wait.svg" alt="">
        </div>`;
      });
    });

    jobseekers.addEventListener('click', () => {
      loginForm.innerHTML = `
      
        <div class="div-2">
          <input class="text-wrapper" placeholder="شماره تلفن:">
          <hr>
        </div>
        <div class="div-3">
          <input class="text-wrapper-2" placeholder="رمز عبور:">
          <hr>
        </div>
          <div class="div-6">
            <button id="login-btn"><div class="text-wrapper-5">ارسال</div></button>
          </div>
        </div>
      `;
    
    
      // ✨ بعد از اضافه شدن فرم، دکمه ارسال رو انتخاب کن و براش رویداد تعریف کن
      const submitBtn = document.getElementById('login-btn');
      submitBtn.addEventListener('click', () => {
        loginForm.innerHTML = `<div class="sucsses">
          <h1>ورود با موفقیت انجام شد.</h1>
          <h2>در حال انتقال به محتوای صفحه اصلی</h2>
          <img src="image/wait.svg" alt="">
        </div>`;
      });

  });
  });
});
