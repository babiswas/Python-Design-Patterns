def count_to(count):
   numbers_in_german=["eins","zwe1","dre1","vier","funf"]
   iterator=zip(range(count),numbers_in_german)
   for position,number in iterator:
        yield number


if __name__=="__main__":
  for num in count_to(3):
       print(f"{num}")

        