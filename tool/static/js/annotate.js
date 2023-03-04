$.get('add_users', function (res) {
    all = ''

    for (var i = 0; i < res['api'].length; i++) {
        var user = res['api'][i][0].split(',')
        var user_name = user[0]
        console.log(user_name, "...........")

    }
    all += `<option value=${user_name}>${user_name}</option>`
    all += user_name
    $(`#annotaters`).html(all)

})