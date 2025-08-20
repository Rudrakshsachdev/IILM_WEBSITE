function togglePassword() {
  var x = document.querySelectorAll('input[type="password"]');
  x.forEach(input => {
    input.type = input.type === "password" ? "text" : "password";
  });
}

