import random

def main():
  #print("Keep it logically awesome.")
  last = 13
  rnd = random.randint(0, last)
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  main()
