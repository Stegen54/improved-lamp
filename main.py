import random
import time

# Game introduction
def intro():
    print("Welcome to the Treasure Hunt Game!")
    time.sleep(1)
    print("Your mission is to find the hidden treasure.")
    time.sleep(1)
    print("Be careful, though! There are traps along the way.\n")
    time.sleep(1)

# Create the maze
def create_maze():
    maze = [
        ["Start", "Path", "Trap", "Treasure"],
        ["Trap", "Path", "Path", "Trap"],
        ["Path", "Trap", "Path", "Path"],
        ["Trap", "Trap", "Path", "Treasure"]
    ]
    return maze

# Display maze status
def display_status(position):
    print(f"You are now at position {position}.")
    print("Choose your direction: (N)orth, (S)outh, (E)ast, (W)est")

# Move in the maze
def move(maze, position, direction):
    row, col = position
    if direction == "N":
        row = max(0, row - 1)
    elif direction == "S":
        row = min(len(maze) - 1, row + 1)
    elif direction == "E":
        col = min(len(maze[0]) - 1, col + 1)
    elif direction == "W":
        col = max(0, col - 1)
    return row, col

# Main game logic
def play_game():
    maze = create_maze()
    position = (0, 0)
    intro()
    
    while True:
        display_status(position)
        move_choice = input("Your move: ").strip().upper()
        if move_choice not in ["N", "S", "E", "W"]:
            print("Invalid move. Try again.")
            continue
        
        new_position = move(maze, position, move_choice)
        if new_position == position:
            print("You can't move in that direction. Try again.")
            continue

        position = new_position
        cell = maze[position[0]][position[1]]

        if cell == "Trap":
            print("Oh no! You stepped on a trap. Game over!")
            break
        elif cell == "Treasure":
            print("Congratulations! You found the treasure!")
            break
        else:
            print("Safe for now... Keep going.\n")

# Start the game
if __name__ == "__main__":
    play_game()
