$("#register").on("submit", function (event) {
  event.preventDefault();
  $.post('newuser', $(this).serialize(), function (res) {
    if (res['res'] == 'success') {
      alert('User registered successfully')
      window.location.href = '/';
    }
  })

});