document
  .getElementById("login-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let userType = document.querySelector(
      'input[name="user-type"]:checked'
    ).value;
    let userId = document.getElementById("login-id").value;
    let url = "";

    if (userType === "patient") {
      url = `/patient/${userId}/`;
    } else if (userType === "doctor") {
      url = `/doctor/${userId}/`;
    } else if (userType === "pharmacist") {
      url = `/pharmacist/${userId}/`;
    }

    if (url) {
      window.location.href = url;
    }
  });
