// script.js
const canvas = document.getElementById("paintCanvas");
const ctx = canvas.getContext("2d");
const cursorPreview = document.getElementById("cursorPreview");

canvas.width = window.innerWidth * 0.8;
canvas.height = window.innerHeight * 0.8;

let painting = false;
let brushColor = "#000000";
let brushSize = 5;

// Show custom cursor preview when on canvas
canvas.addEventListener("mouseenter", () => {
    cursorPreview.style.display = "block";
});
canvas.addEventListener("mouseleave", () => {
    cursorPreview.style.display = "none";
});

// Update cursor preview position, size, and color
canvas.addEventListener("mousemove", (e) => {
    const x = e.clientX;
    const y = e.clientY;

    cursorPreview.style.left = `${x}px`;
    cursorPreview.style.top = `${y}px`;
    cursorPreview.style.width = `${brushSize}px`;
    cursorPreview.style.height = `${brushSize}px`;
    cursorPreview.style.backgroundColor = brushColor;
});

// Update brush settings from inputs
document.getElementById("colorPicker").addEventListener("input", (e) => {
    brushColor = e.target.value;
});
document.getElementById("brushSize").addEventListener("input", (e) => {
    brushSize = e.target.value;
});

// Event listeners for drawing actions
canvas.addEventListener("mousedown", startPainting);
canvas.addEventListener("mouseup", stopPainting);
canvas.addEventListener("mousemove", draw);

// Functions for drawing
function startPainting(e) {
    painting = true;
    draw(e); // Draw on initial click
}

function stopPainting() {
    painting = false;
    ctx.beginPath(); // Reset path
}

function draw(e) {
    if (!painting) return;

    ctx.lineWidth = brushSize;
    ctx.lineCap = "round";
    ctx.strokeStyle = brushColor;

    ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
}

// Clear canvas function
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}
