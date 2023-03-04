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
  var ele = ''

  for (var i = 0; i < res['api'].length; i++) {
    var image_length = res['api'][i][2].split(',')
    var ImageCount = image_length.length
    ele += ` <div class="col-xl-4 col-md-6 mb-4">
              <div class="card border-left-primary shadow h-100 py-2">
              <div class="card-body">
              <a href = "annotate_page/${res['api'][i][1]}" style="text-decoration:none"><div class="row no-gutters align-items-center">
                <div class="col mr-2">
                  
                  <div class="h2 mt-1 mb-0 font-weight-bold text-gray-800 text-uppercase">${res['api'][i][1]}</div>
                  <div class="h6 font-weight-bold text-primary mt-2">
                    ${ImageCount} Images</div>
                </div>
                <div class="col-auto">
                  <img src="static/images/download.png" class="mt-2" height="80px" width="80px" style="border-radius:10px">
                </div>
              </div></a>
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