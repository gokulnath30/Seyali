$('#data_upload').on('submit', function(event){
    event.preventDefault();
    var formData = new FormData($('#images')[0])
    formData.append('pname',$('#pname').val())
    console.log(formData,':::::::')
    
    $.ajax({
        url: 'create_project',
        type: 'post',
        data: formData,
        contentType: false,
        processData: false,
        success: function(response){
            if(response != 0){
                $("#img").attr("src",response); 
                $(".preview img").show(); // Display image element
            }else{
                alert('file not uploaded');
            }
        },
    });


    return false;
    
})

var fileInput = document.getElementById('file-input');
var fileList = [];

fileInput.addEventListener('change', function (evnt) { 

     fileList = [];
    for (var i = 0; i < fileInput.files.length; i++) {
        fileList.push(fileInput.files[i]);
    }
  }

);

