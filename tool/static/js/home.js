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
        $('#exampleModal').modal('toggle');


        get_project();
      } else {
        alert('Project not created')
      }
    },
  });

  return false;

})
const get_project = ()=>{
  
$.get('project_details', function (res) {
  var ele = ''
  for (var i = 0; i < res['api'].length; i++) {
   
    ele += ` <div class="col-xl-4 col-md-6 mb-4">
              <div class="card border-left-primary shadow h-100 py-2">
              <div class="card-body">
              <a href = "annotate_page/${res['api'][i]['project']}" style="text-decoration:none"><div class="row no-gutters align-items-center">
                <div class="col mr-2">
                  
                  <div class="h2 mt-1 mb-0 font-weight-bold text-gray-800 text-uppercase">${res['api'][i]['project']}</div>
                  <div class="h6 font-weight-bold text-primary mt-2">
                    ${res['api'][i]['count']} Images</div>
                </div>
                <div class="col-auto">
                  <img src="${res['api'][i]['sample']}" class="mt-2" height="80px" width="80px" style="border-radius:10px">
                </div>
              </div></a>
            </div>
          </div>
        </div>`

  }

  $('#project_details').html(ele)

})
}

get_project()