$('#data_upload').on('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(this); // Create FormData object with the form data
    const fileInput = $('#imag_path'); // Get the file input element
    // const file = fileInput.files; // Get the selected file

    $.ajax({
        url: 'create_project',
        type: 'post',
        data: formData,
        contentType: false,
        processData: false,
        success: function (res) {
            if (res['res'] == 'success') {
                alert('Project created')
                $('#exampleModal').modal('toggle')
            } else {
                alert('Project not created')
            }
        },
    });

    return false;

})

$.get('project_details', function (res) {
  var ele = '';

  for (var i = 0; i < res['api'].length; i++) {

    ele += ` <div class="col-xl-3 col-md-6 mb-4">
          <div class="card border-left-primary shadow h-100 py-2">
            <div class="card-body">
              <div class="row no-gutters align-items-center">
                <div class="col mr-2">
                  <div class="h6 font-weight-bold text-primary text-uppercase mb-1">
                    ${res['api'][i][1]}</div>
                  <div class="h2 mt-1 mb-0 font-weight-bold text-gray-800">${res['api'][i][6]}</div>
                </div>
                <div class="col-auto">
                  <i class="fas fa-calendar fa-2x text-gray-300"></i>
                </div>
              </div>
            </div>
          </div>
        </div>`

  }

  $('#project_details').html(ele)



})
// var fileInput = document.getElementById('file-input');
// var fileList = [];

// fileInput.addEventListener('change', function (evnt) {

//         fileList = [];
//         for (var i = 0; i < fileInput.files.length; i++) {
//             fileList.push(fileInput.files[i]);
//         }
//     }

// );