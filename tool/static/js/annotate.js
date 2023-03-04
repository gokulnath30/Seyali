$('#user_form').on('submit', function (e) {
    e.preventDefault();
    var form_data = $(this).serialize();
    // form_data['project_name'] = window.location.href.split('/')[4]

    $.post('/assign_user', form_data+'&project_name='+window.location.href.split('/')[4], function (res) {
        if (res['res'] === 'success') {
            alert("user assigned successfully")
        } else {
            alert("user rejected")
        }

    })
})