#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    f=open(filename).read().split(",")
    l=[]
    for i in f:
        l.append(int(i))
    return l 
print(read_file("data.txt"))
#Print list from file

