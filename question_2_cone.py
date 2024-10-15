# Fill in the blanks for the following code.
# Run the code at online-python.com or IDLE PYTHON before you commit the changes at github.com

# This program is used to calculate the volume of cone.

from math import pi

def volume_cone(radius, height):
    volume = (1 / 3) * pi * radius ** 2 * height
    return volume

def main():
    a = float(input("Input radius: ")) 
    b = float(input("Input height: ")) 
    volume = volume_cone(a, b) 
    print(f"Volume of cone = { volume :.2f}") 

# Don't change the code below!
if __name__ == "__main__":
    main()
