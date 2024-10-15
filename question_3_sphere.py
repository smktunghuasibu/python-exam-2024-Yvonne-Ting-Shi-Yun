# Fill in the blanks for the following code.
# Run the code at online-python.com or IDLE PYTHON before you commit the changes at github.com

# This program is used to calculate the volume of sphere.

from math import pi

# kira_sfera() is a function that return the volume of sphere
def volume_sphere(radius):
    volume = 4/3 * pi * radius ** 3
    return volume

def main():
    r = float(input("Input radius: ")) 
    Volume = volume_sphere (r) 
    print(f"Isipadu sfera = { Volume :.2f}") 

# Don't change the code below!
if __name__ == "__main__":
    main()
