const canvas = document.getElementById("myCanvas");
const context = canvas.getContext("2d");

const annotations = {'checker':{}}

const height = 650;
const width = 650;

// resize canvas (CSS does scale it up or down)
canvas.height = height;
canvas.width = width;

context.strokeStyle = "red";
context.fillStyle = "red";


// implement drawing
let drawing = false;


function startDrawing(e) {
    drawing = true;
    context.beginPath();
    draw(e);
}

function endDrawing(e) {
  drawing = false;
}

// window.addEventListener("mouseup", endDrawing);

function getMousePos(canvas, evt) {
  var rect = canvas.getBoundingClientRect(),
    scaleX = canvas.width / rect.width,
    scaleY = canvas.height / rect.height;

  return {
    x: (evt.clientX - rect.left) * scaleX,
    y: (evt.clientY - rect.top) * scaleY,
  };
}

function draw(e) {
  if (!drawing) return;

  let { x, y } = getMousePos(canvas, e);
  context.lineTo(x, y);
  context.stroke();
}

// window.addEventListener("mousemove", draw);

context.lineWidth = 3;
context.lineCap = "round";

// implement drawing rectangle
let start = {}

function startRect(e) {
    start = getMousePos(canvas, e);
}

window.addEventListener("mousedown", startRect);

function endRect(e) {
    let { x, y } = getMousePos(canvas, e);
    let x1 = Math.round(start.x);
    let x2 = Math.round(start.y)
    let y1 = Math.round(x - start.x);
    let y2 = Math.round(y - start.y);
    context.strokeRect(x1,x2,y1,y2);
    if(y1 != 0 && y2 != 0){
        console.log(x1,x2,y1,y2,'::::::::')
        annotations['checker'][$("#imag_name").html()].push({'class1':[x1,x2,y1,y2]})

    }



}


window.addEventListener("mouseup", endRect);

var totalImages = 0;
var currentImage = 0;
var imgList = undefined;


const startMagic = () =>{
    console.log(annotations,'::::::>>>')
    $.post('start_magic',{'req':JSON.stringify(annotations)},function(res){
        console.log(res,'====')
    })
}

const showImg = ()=>{
    $.get('get_images',{'inx':currentImage},function(res){
        totalImages = res['img_len']
        var imname = res['img_name']
        $("#showImg").attr("src",res['img_path']);
        $("#imag_name").html(imname);
        
        annotations[res['pname']][imname] = []
    })

    console.log(annotations,'....')

}

const moveForward = ()=>{
    if(currentImage < totalImages)
        currentImage += 1
    else
        currentImage = totalImages

        showImg()
}

const moveBackward = ()=>{
    if (currentImage >= 1)
        currentImage -= 1
    else
        currentImage = 0

        showImg()
    
}

showImg()