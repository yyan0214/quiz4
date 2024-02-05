import argparse

def demo() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help = "say something", dest = "input_string",type = str)
    parser.add_argument(help = "Enter a integer number", dest = "input_num", type = int)
    parser.add_argument(help = "Enter a float number", dest = "input_float", type = float)

    args = parser.parse_args()

    str_sth = args.input_string
    int_num = args.input_num
    float_num = args.input_float


    print("What are you say: ",str_sth)
    print("The int number is: ",int_num)
    print("The float number is: ",float_num)

if __name__ == '__main__':
    demo()