// Get the canvas element
const canvas = document.getElementById('myCanvas');

// Get the 2D context of the canvas
const ctx = canvas.getContext('2d');

// Create a new image element and set its source
const img = new Image();
img.src = 'static/images/sample.png';

// Define variables to keep track of the mouse position and rectangle coordinates
let mouseX, mouseY;
let rectX, rectY, rectWidth, rectHeight;
let isDragging = false;

// When the image has loaded, draw it on the canvas
img.onload = function() {
  // Draw the image on the canvas
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

  // Add event listeners to the canvas
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
  // console.log(rectangles)
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
    
    console.log(rectX, rectY, parseInt(rectX+rectWidth), parseInt(rectY+rectHeight),':::::::::::')
    ctx.strokeRect(rectX, rectY, rectWidth, rectHeight);
  }
}

// Define an array to store all rectangles
const rectangles = [];