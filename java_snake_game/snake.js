const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const boxSize = 20; // Size of each square in the grid
let direction = "RIGHT";
let snake = [{ x: 9 * boxSize, y: 9 * boxSize}];
let food = generateFood();
let score = 0;

// Control the snake
document.addEventListener("keydown", changeDirection);

function changeDirection(event) {
    if (event.key === "ArrowUp" && direction !== "DOWN") {
        direction = 
    }
}