import datetime

class Ohce:
  def __init__(self):
    self.name = ''
    self.running = False

  def ohce(self, input):
    args = input.split()
    if not self.running and len(args) >= 2:
      if args[0] == 'ohce':
        self.name = args[1]
        self.running = True
        now = datetime.datetime.now().time()
        if now >= datetime.time(6) and now < datetime.time(12):
          return "¡Buenos días " + self.name + "!"
        elif now >= datetime.time(12) and now < datetime.time(20):
          return "¡Buenas tardes " + self.name + "!"
        else:
          return "¡Buenas noches " + self.name + "!"

    elif self.running:
      reversed_input = self.reverse_input(input)

      if input != "" and reversed_input == input:
        return reversed_input + '\n' + "¡Bonita palabra!"
      
      if(input=="Stop!"):
        return "Adios " + self.name

      return reversed_input

  def reverse_input(self, input):
    reversed_input = input[::-1]
    return reversed_input