import turtle

# Part A
 """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
def seq3np1(n):
  count = 0
  while(n != 1):
    count += 1
    if(n % 2) == 0:
      n = n // 2
    else:
      n = n * 3 + 1
  return count

#Part B
def graph (upper_bound):
  turtleA = turtle.Turtle()
  window = turtle.Screen()
  turtleB = turtle.Turtle()
  turtle.setworldcoordinates(0, 0, 10, 10)
  max_so_far = 0
  previous_x = 0
  previous_y = 0
  for i in range (upper_bound):
    result = seq3np1(i+1)
    if result > max_so_far:
      max_so_far = result
      turtle.setworldcoordinates(0, 0, i+10, max_so_far+10)
      turtleA.up()
      turtleA.goto(0,0)
      turtleA.down()
      turtleA.goto(i+10,0)
      turtleA.goto(0,0)
      turtleA.goto(0,max_so_far+10)
      turtleA.up()
      turtleA.goto(previous_x, previous_y)
      if previous_x != 0 and previous_y != 0:
        turtleA.down()
      turtleA.goto(i,max_so_far)
      previous_x=i
      previous_y=max_so_far
      turtleA.dot(3)
      turtleB.clear()
      turtleB.up()
      turtleB.goto(0, max_so_far)
      turtleB.write("Maximum so far: " + str(i) + ", " + str(max_so_far))
  window.exitonclick()

def main():
    user_num = int(input("Please enter a number:"))
    if user_num > 0:
        for start in range (user_num):
            print(start+1, seq3np1(start+1))
        graph(user_num)
    exit()

main()