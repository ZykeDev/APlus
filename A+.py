# A+ (plus) Pathfinding

# Node class
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.pos = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos


def aplus(maze, start, end):
    # Initialize both open and closed list
    openList = []
    closedList = []

    # Add the start node
    startNode = Node(None, start)
    startNode.g = 0
    startNode.h = 0
    startNode.f = 0

    openList.append(startNode)

    # Init the end node
    endNode = Node(None, end)
    endNode.g = 0
    endNode.h = 0
    endNode.f = 0



    while len(openList) > 0:
        currentNode = openList[0] # Default node is start
        currentIndex = 0

        # Find the open node with min f
        for index, node in enumerate(openList):
            if node.f < currentNode.f:
                currentNode = node
                currentIndex = index

        # Move it from open list -> closed list
        openList.pop(currentIndex) 
        closedList.append(currentNode)
        
        # Goal found
        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1] # Return reversed path



        # Generate children of the new node
        children = []

        for newPos in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            # Get node position
            nodePos = (currentNode.pos[0] + newPos[0], currentNode.pos[1] + newPos[1])


            # Skip if out of range
            if nodePos[0] > (len(maze) - 1) or nodePos[0] < 0 or nodePos[1] > (len(maze[len(maze)-1]) -1) or nodePos[1] < 0:
                continue

            # Skip if it's untraversable
            if maze[nodePos[0]][nodePos[1]] != 0: 
                continue

 
            # Create new child node and append it 
            newNode = Node(currentNode, nodePos)
            children.append(newNode)


        # Loop every child
        for child in children:

            # Skip if the child is closed
            for closedChild in closedList:
                if child == closedChild:
                    continue


            child.g = currentNode.g + 1
            child.h = ((child.pos[0] - endNode.pos[0]) ** 2) + ((child.pos[1] - endNode.pos[1]) ** 2)
            child.f = child.g + child.h

            for openNode in openList:
                if openNode == child and child.g > openNode.g:
                    continue


            # Append the surviving child to the open list
            openList.append(child)




def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (0, 9) # TODO doesn't lookup upove?

    print("Finding path: " + str(start) + " -> " + str(end) + "\n")
    path = aplus(maze, start, end)

    print(path)

    print("\nSteps: " + str(len(path)-1))


if __name__ == '__main__':
    main()