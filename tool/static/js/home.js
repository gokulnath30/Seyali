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
    for (var i = 0; i < res['api'].length; i++) {
        var ele = ''
        ele += ` <div class="col-8 mt-4 ">
        <div class="cards p-4 bg_gradient_own min_h_100" style="height:190px;">
          <div class="d-flex">
            <div>
              <img src="static/images/download.png" alt="" height="100px" width="100px"
                style="border-radius:10px">
            </div>
            <div>
              <div class="d-flex  pb-4">
                <div class="col">
                  <h4 class="font-weight-bold text-dark text-center pr-5"><span class=""></span> <a href = "annotate+page" style="text-decoration:none"> ${res['api'][i][1]}</a></h4>
                </div>

                <div class="col" id="container">
                  <div id="menu-wrap">
                    <input type="checkbox" class="toggler" />
                    <div class="dots">
                      <div></div>
                    </div>
                    <div class="menu">
                      <div>
                        <ul>
                          <li><a href="#" class="link font-weight-bold">Manage project</a></li>
                          <li><a href="#" class="link font-weight-bold">Rename Project</a></li>
                          <li><a href="#" class="link font-weight-bold text-danger">Delete Project</a></li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="row">
                <div class="col-12">
                  <div class="row text-center">
                    <div class="col-4">
                      <h5 class="bolder text-dark">Classes</h5>
                      <h5 class="bolder text-dark" id="classes_count">${res['api'][i][6]}</h5>
                    </div>

                    <div class="col-4 border-left">
                      <h5 class="bolder text-dark">Images Count</h5>
                      <h5 class="bolder text-dark" id="images_count"><i class="fa-solid fa-image" style="color:#36b9cc"></i> &nbsp; ${res['api'][i][2]}</h5>
                    </div>
                  </div>

                </div>
              </div>
            </div>
          </div>

        </div>
      </div>`
        $('#project_details').html(ele)

    }


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