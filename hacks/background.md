---
layout: base
title: Background with Object
description: Use JavaScript to have an in motion background.
sprite: images/platformer/sprites/flying-ufo.png
background: images/platformer/backgrounds/stars.jpeg
permalink: /background
---

<canvas id="world"></canvas>

<script>
  // Get the canvas element and its 2D rendering context
  const canvas = document.getElementById("world");
  const ctx = canvas.getContext('2d');

  // Create Image objects for the background and the player sprite
  const backgroundImg = new Image();
  const spriteImg = new Image();

  // Set the image sources using Jekyll/Liquid page variables
  backgroundImg.src = '{{page.background}}';
  spriteImg.src = '{{page.sprite}}';

  // Counter to check when both images have finished loading
  let imagesLoaded = 0;

  // When background image is loaded, increment counter and try starting the game
  backgroundImg.onload = function() {
    imagesLoaded++;
    startGameWorld();
  };

  // When sprite image is loaded, increment counter and try starting the game
  spriteImg.onload = function() {
    imagesLoaded++;
    startGameWorld();
  };

  // Start the game only if both images are loaded
  function startGameWorld() {
    if (imagesLoaded < 2) return;

    // Base class for all game objects
    class GameObject {
      constructor(image, width, height, x = 0, y = 0, speedRatio = 0) {
        this.image = image;       // Image of the object
        this.width = width;       // Width to draw
        this.height = height;     // Height to draw
        this.x = x;               // X position
        this.y = y;               // Y position
        this.speedRatio = speedRatio; // Speed multiplier for moving objects
        this.speed = GameWorld.gameSpeed * this.speedRatio; // Actual speed
      }

      // Default update method, can be overridden
      update() {}

      // Draw the object on the canvas
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
      }
    }

    // Background class inherits from GameObject
    class Background extends GameObject {
      constructor(image, gameWorld) {
        // Fill entire canvas with background
        super(image, gameWorld.width, gameWorld.height, 0, 0, 0.1);
      }

      // Update the background position for scrolling effect
      update() {
        this.x = (this.x - this.speed) % this.width;
      }

      // Draw the background twice to create seamless looping
      draw(ctx) {
        ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
        ctx.drawImage(this.image, this.x + this.width, this.y, this.width, this.height);
      }
    }

    // Player class inherits from GameObject
    class Player extends GameObject {
      constructor(image, gameWorld) {
        // Set player size to half of original image
        const width = image.naturalWidth / 2;
        const height = image.naturalHeight / 2;
        // Center player on screen
        const x = (gameWorld.width - width) / 2;
        const y = (gameWorld.height - height) / 2;
        super(image, width, height, x, y);

        this.baseY = y;  // Base Y position for floating effect
        this.frame = 0;  // Animation frame counter
      }

      // Make the player float up and down using a sine wave
      update() {
        this.y = this.baseY + Math.sin(this.frame * 0.05) * 20;
        this.frame++;
      }
    }

    // Main GameWorld class to manage game loop and objects
    class GameWorld {
      static gameSpeed = 5; // Base speed for moving objects

      constructor(backgroundImg, spriteImg) {
        this.canvas = document.getElementById("world");
        this.ctx = this.canvas.getContext('2d');

        // Set canvas size to match the window
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.canvas.width = this.width;
        this.canvas.height = this.height;

        // Set CSS styles for canvas positioning
        this.canvas.style.width = `${this.width}px`;
        this.canvas.style.height = `${this.height}px`;
        this.canvas.style.position = 'absolute';
        this.canvas.style.left = `0px`;
        this.canvas.style.top = `${(window.innerHeight - this.height) / 2}px`;

        // Create game objects: background and player
        this.gameObjects = [
          new Background(backgroundImg, this),
          new Player(spriteImg, this)
        ];
      }

      // Main game loop
      gameLoop() {
        // Clear the canvas each frame
        this.ctx.clearRect(0, 0, this.width, this.height);

        // Update and draw all game objects
        for (const obj of this.gameObjects) {
          obj.update();
          obj.draw(this.ctx);
        }

        // Request next animation frame
        requestAnimationFrame(this.gameLoop.bind(this));
      }

      // Start the game loop
      start() {
        this.gameLoop();
      }
    }

    // Instantiate the GameWorld and start it
    const world = new GameWorld(backgroundImg, spriteImg);
    world.start();
  }
</script>
