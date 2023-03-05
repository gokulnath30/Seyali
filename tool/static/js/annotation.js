const canvas = document.getElementById('myCanvas');
const annotations = {}
const ctx = canvas.getContext('2d');

const height = 650;
const width = 650;

canvas.height = height;
canvas.width = width;

const rectangles = []
let mouseX, mouseY;
let rectX, rectY, rectWidth, rectHeight;
let isDragging = false;
const img = new Image();

img.onload = function () {
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
  canvas.addEventListener('mousedown', handleMouseDown);
  canvas.addEventListener('mousemove', handleMouseMove);
  canvas.addEventListener('mouseup', handleMouseUp);
};

function handleMouseDown(e) {
  // Get the mouse position relative to the canvas
  const rect = canvas.getBoundingClientRect();
  mouseX = e.clientX - rect.left;
  mouseY = e.clientY - rect.top;

  // Start drawing the rectangle
  rectX = mouseX;
  rectY = mouseY;
  rectWidth = 0;
  rectHeight = 0;
  isDragging = true;
}

function handleMouseMove(e) {
  if (isDragging) {
    // Get the mouse position relative to the canvas
    const rect = canvas.getBoundingClientRect();
    const mouseX2 = e.clientX - rect.left;
    const mouseY2 = e.clientY - rect.top;

    // Calculate the rectangle coordinates and dimensions
    rectX = Math.min(mouseX, mouseX2);
    rectY = Math.min(mouseY, mouseY2);
    rectWidth = Math.abs(mouseX - mouseX2);
    rectHeight = Math.abs(mouseY - mouseY2);

    // Redraw the image and all rectangles
    draw();
  }
}

function handleMouseUp(e) {
  if (isDragging) {
    // Stop drawing the rectangle
    isDragging = false;

    // Add the rectangle to the array of rectangles
    rectangles.push({
      x: rectX,
      y: rectY,
      width: rectWidth,
      height: rectHeight
    });

    // Redraw the image and all rectangles
    draw();
  }
  var iname = $("#img_names").html();
  annotations[iname].push({'cls': [parseInt(rectX), parseInt(rectY), parseInt(rectX + rectWidth), parseInt(rectY + rectHeight)]  })

}

function draw() {
  // Clear the canvas
  ctx.strokeRect(0, 0, canvas.width, canvas.height);

  // Draw the image on the canvas
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

  // Draw all rectangles
  ctx.fillStyle = 'blue';
  for (let i = 0; i < rectangles.length; i++) {
    ctx.strokeRect(rectangles[i].x, rectangles[i].y, rectangles[i].width, rectangles[i].height);
  }

  // Draw the current rectangle
  if (isDragging) {
    ctx.strokeRect(rectX, rectY, rectWidth, rectHeight);
    ctx.strokeStyle = "#FF0000";

  }
}


$.get('get_images', function (res) {
  // annotations['project'] = res['pname'];
  // annotations['ann'] = {}
  $("#pro_names").html(res['pname']);

  for (let i = 0; i < res['images'].length; i++) {
    let ilist = res['images'][i].split('/')
    var iname = ilist[ilist.length - 1]


    if (i == 0) {
      $("#img_names").html(iname);
      img.src = res['images'][i]
    }
    $("#showImg").append(`<img style="cursor: pointer;" onclick="show_img('${iname}','${res['images'][i]}')" src="${res['images'][i]}" class="img-fluid pt-1" alt="placeholder">`)

    annotations[iname] = []

  }

  console.log(annotations)
})

const show_img = (iname, ipath) => {
  img.src = ipath
  console.log(iname)
}

const start_magic = () => {
  $.post('start_magic',{'req':JSON.stringify(annotations)},function(res){
    console.log(res,'====')
})
}