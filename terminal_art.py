from ascii_magic import AsciiArt
import time
import os

def clear_terminal():
    # Clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_ascii_image(image_path, min_columns=60, max_columns=100, delay=0.05, steps=10):
    """
    Creates a pulsing effect by resizing the ASCII art.
    :param image_path: Path to the image file
    :param min_columns: Minimum width (in columns) for ASCII art
    :param max_columns: Maximum width (in columns) for ASCII art
    :param delay: Time delay between frames
    :param steps: Number of steps in one cycle of the animation
    """
    # Generate frames by resizing ASCII art between min and max columns
    for i in range(steps * 2):  # Go up and down to create a pulsing effect
        columns = min_columns + abs((i % (2 * steps)) - steps) * (max_columns - min_columns) // steps
        clear_terminal()  # Clear the terminal for smooth animation
        my_art = AsciiArt.from_image(image_path)
        my_art.to_terminal()  # Display ASCII art in the terminal
        time.sleep(delay)  # Pause before showing the next frame

print("Welcome to Our Coding Flower Shop")
user = input("Enter: 1. Cherry Blossom \n 2. Roses \n 3. Blue Flower \n 4. KUWIC \n Your Input: ")

# Choose the image based on user input and animate it
if user == "Roses":
    animate_ascii_image('flower.jpeg')
elif user == "Cherry Blossom":
    animate_ascii_image('cherry_blossom.webp')
elif user == "Blue Flower":
    animate_ascii_image('blue_flower.webp')
elif user == "KUWIC":
    animate_ascii_image('KU_WIC.png')
