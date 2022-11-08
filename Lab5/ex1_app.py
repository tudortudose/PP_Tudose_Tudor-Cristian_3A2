from ex1_utils import process_item


while True:
    input_str = input("Input a number:")
    if input_str == "q":
        print("Goodbye!")
        break
    input_int = int(input_str)
    print(f"Least prime greater than {input_int} is: ", process_item(input_int))
