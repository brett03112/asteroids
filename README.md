# Asteroids Game

A Python implementation of the classic Asteroids arcade game using Pygame. This is a simple project from the course on boot.dev by Lane Wagner.

## Description

This project is a recreation of the classic Asteroids arcade game where players control a spaceship to navigate through space, avoid asteroids, and shoot them to break them into smaller pieces. The game features smooth controls, collision detection, and the classic Asteroids gameplay mechanics.

## Features

- Player-controlled spaceship with rotation and movement
- Asteroid generation with random spawning from screen edges
- Asteroid destruction and splitting mechanics
- Shooting system with cooldown
- Collision detection between player, asteroids, and shots
- Score tracking system
- Classic Asteroids-style graphics
- Smooth frame-rate independent movement
- Object-oriented design using Pygame sprites

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd asteroids
   ```

2. Install dependencies using pip:
   ```bash
   pip install pygame==2.6.1
   ```

   Or if using uv (recommended):
   ```bash
   uv sync
   ```

## Usage

Run the game with Python:

```bash
python main.py
```

Or with Python 3 specifically:

```bash
python3 main.py
```

Or with uv:

```bash
uv run main.py
```

## Controls

- **W** - Move forward
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right
- **SPACE** - Shoot

## Project Structure

- `main.py` - Main game loop and initialization
- `player.py` - Player spaceship class and controls
- `circleshape.py` - Base class for circular game objects
- `constants.py` - Game constants and configuration
- `pyproject.toml` - Project dependencies and metadata
- `shot.py` - Projectile class for shooting mechanics
- `asteroid.py` - Asteroid class with splitting behavior
- `asteroidfield.py` - Asteroid field management and spawning

## Game Mechanics

### Player Movement
The player's spaceship can rotate left and right using the A and D keys, and move forward/backward using W and S keys. Movement is frame-rate independent for smooth gameplay.

### Shooting
Players can fire projectiles by pressing the SPACE key. Each shot travels in the direction the spaceship is facing at a constant speed. There is a cooldown period between shots to prevent continuous firing.

### Scoring System
Players earn points for destroying asteroids:
- Large asteroids (radius 60): 1 point
- Medium asteroids (radius 40): 5 points
- Small asteroids (radius 20): 10 points

The score is displayed in the top-left corner of the screen.

### Asteroid Behavior
Asteroids spawn randomly from the edges of the screen and travel in straight lines. When an asteroid is hit by a shot:
- Large asteroids split into two smaller asteroids
- Medium asteroids split into two small asteroids
- Small asteroids are destroyed completely
- Each split creates asteroids with slightly increased speed

### Collision Detection
- Player vs Asteroid: Game ends immediately when the player collides with an asteroid
- Shot vs Asteroid: Shots destroy asteroids (with splitting behavior for larger asteroids)

### Object Management
The game uses Pygame sprite groups for efficient object management:
- **Updatable group**: Handles game object updates
- **Drawable group**: Handles game object rendering
- **Asteroids group**: Manages all asteroid objects for collision detection
- **Shots group**: Manages all projectile objects for collision detection

### Constants
Game parameters are configurable through `constants.py`:
- Screen dimensions (1280x720)
- Player movement and rotation speeds
- Asteroid properties and spawning rates
- Shot properties and cooldown timing

## Development

### Dependencies

- Pygame 2.6.1 - For game development and graphics

### Code Structure

The game follows object-oriented principles with a base `CircleShape` class that extends `pygame.sprite.Sprite`. This allows for easy management of game objects through sprite groups.

## Future Enhancements

- Particle effects for explosions
- Sound effects and music
- Multiple lives and game over screen
- Power-ups and special weapons
- Different asteroid types with varying behaviors
- High score tracking

## Contributing

This project is built using modern Python practices with:
- Dependency management via `pyproject.toml`
- Virtual environment support
- Type hints for better code maintainability

## License

This project is for educational purposes and follows the open-source principles of the Pygame community.

## Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Inspired by the classic Asteroids arcade game by Atari
