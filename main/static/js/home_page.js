document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('piggyCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let piggyEmojis = [];
    const piggyEmoji = '🐷';

    function createPiggy() {
        const size = Math.random() * 20 + 10; // Size of piggy emoji
        const x = Math.random() * canvas.width;
        const acceleration = Math.random() * 0.05 + 0.01; // Acceleration
        piggyEmojis.push({x, y: -20, size, speed: 0, acceleration});
    }

    function updateAndDrawPiggies() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        piggyEmojis.forEach(piggy => {
            piggy.speed += piggy.acceleration;
            piggy.y += piggy.speed;
            ctx.font = `${piggy.size}px serif`;
            ctx.fillText(piggyEmoji, piggy.x, piggy.y);

            // Reset piggy position if it falls off screen
            if (piggy.y > canvas.height + piggy.size) {
                piggy.y = -20;
                piggy.x = Math.random() * canvas.width;
                piggy.speed = 0;
            }
        });

        requestAnimationFrame(updateAndDrawPiggies);
    }

    // Create a number of piggies based on screen size
    for (let i = 0; i < canvas.width / 50; i++) {
        createPiggy();
    }

    updateAndDrawPiggies();
});



