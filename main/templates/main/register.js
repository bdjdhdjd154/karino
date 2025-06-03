const loginForm = document.getElementById("loginForm");

function showMessage(message, isSuccess = true) {
  const msg = document.createElement("p");
  msg.className = isSuccess ? "success" : "error";
  msg.textContent = message;
  loginForm.appendChild(msg);
}

function sendRegisterData(url, data) {
  fetch("http://127.0.0.1:8000/api/register/", {
    method: "POST",
    headers: { 
          "Content-Type":"application/json", },
    body: JSON.stringify({
      username:"test1",
      password:"1234"

    })
  })
  .then(res => {
    if (!res.ok) throw new Error("ثبت‌نام ناموفق بود.");
    return res.json();
  })
  .then(data => {
    console.log("ثبت‌نام موفق:", data);
    showMessage("ثبت‌نام با موفقیت انجام شد.", true);
  })
  .catch(err => {
    console.error("خطا:", err.message);
    alert("خطا در ارتباط با سرور: " + err.message);
    showMessage(err.message, false);
  });
}

function showJobSeekerForm() {
  loginForm.innerHTML = `
    <div class="div-2"><input id="username" class="text-wrapper" placeholder="نام کاربری"><hr></div>
    <div class="div-3"><input id="password" type="password" class="text-wrapper-2" placeholder="رمز عبور"><hr></div>
    <div class="div-3"><input id="email" class="text-wrapper-2" placeholder="ایمیل"><hr></div>
    <div class="div-3"><input id="first_name" class="text-wrapper-2" placeholder="نام"><hr></div>
    <div class="div-3"><input id="last_name" class="text-wrapper-2" placeholder="نام خانوادگی"><hr></div>
    <div class="div-3"><input id="phone_number" class="text-wrapper-2" placeholder="شماره تماس"><hr></div>
    <div class="div-6"><button id="submit-btn"><div class="text-wrapper-5">ارسال</div></button></div>
  `;
  const submitBtn = document.getElementById("submit-btn");
  submitBtn.onclick = () => {
    const data = {
      username: document.getElementById("username").value,
      password: document.getElementById("password").value,
      email: document.getElementById("email").value,
      first_name: document.getElementById("first_name").value,
      last_name: document.getElementById("last_name").value,
      phone_number: document.getElementById("phone_number").value,
    };
    sendRegisterData("http://127.0.0.1:8000/api/register/", data);
  }
}

//function showEmployerForm() {
  //loginForm.innerHTML = `
   // <div class="div-2"><input id="username" class="text-wrapper" placeholder="نام کاربری"><hr></div>
  //  <div class="div-3"><input id="password" type="password" class="text-wrapper-2" placeholder="رمز عبور"><hr></div>
  //  <div class="div-3"><input id="email" class="text-wrapper-2" placeholder="ایمیل"><hr></div>
  //  <div class="div-3"><input id="website" class="text-wrapper-2" placeholder="وب‌سایت"><hr></div>
  //  <div class="div-3"><input id="phone_number" class="text-wrapper-2" placeholder="شماره تماس"><hr></div>
  //  <div class="div-3"><input id="company_name" class="text-wrapper-2" placeholder="نام شرکت"><hr></div>
  //  <div class="div-3"><input id="address" class="text-wrapper-2" placeholder="آدرس شرکت"><hr></div>
  //  <div class="div-6"><button id="submit-btn"><div class="text-wrapper-5">ارسال</div></button></div>
  //`;
 // const submitBtn = document.getElementById("submit-btn");
  //submitBtn.onclick = () => {
  //  const data = {
  //    username: document.getElementById("username").value,
   //   password: document.getElementById("password").value,
   //   email: document.getElementById("email").value,
     // website: document.getElementById("website").value,
   //   phone_number: document.getElementById("phone_number").value,
     // company_name: document.getElementById("company_name").value,
    //  address: document.getElementById("address").value,
  //  };
  //  sendRegisterData("http://127.0.0.1:8000/api/register/company", data);
  //};
//}

function showRoleSelector() {
  loginForm.innerHTML = `
    <div class="div-6">
      <button id="employers-btn"><div class="text-wrapper-5">ورود کارفرمایان</div></button>
      <button id="job-seekers-btn"><div class="text-wrapper-5">ورود کارجویان</div></button>
    </div>
  `;
//  document.getElementById("employers-btn").onclick = showEmployerForm;
  document.getElementById("job-seekers-btn").onclick = showJobSeekerForm;
}
function handleRegisterResponse(response) {
    const msgBox = document.getElementById('message') || document.createElement('div');
    msgBox.id = 'message';
    msgBox.innerHTML = ''; // پاک‌سازی پیام‌های قبلی
    msgBox.style.marginTop = '15px';

    if (response.success) {
        msgBox.style.color = 'green';
        msgBox.innerText = response.message;

        // ساختن دکمه رفتن به صفحه اصلی
        const homeBtn = document.createElement('button');
        homeBtn.innerText = 'رفتن به صفحه اصلی';
        homeBtn.style.marginRight = '10px';
        homeBtn.onclick = () => {
            window.location.href = '/';
        };

        msgBox.appendChild(document.createElement('br'));
        msgBox.appendChild(homeBtn);
    } else {
        msgBox.style.color = 'red';
        msgBox.innerText = response.error;
    }

    document.getElementById('loginForm').appendChild(msgBox);
}


window.onload = showRoleSelector;
