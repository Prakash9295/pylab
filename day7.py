def count_data_types(*args):
    int_count = 0
    float_count = 0
    string_count = 0
    others = 0

    for item in args:
        if isinstance(item, int):
            int_count += 1
        elif isinstance(item, float):
            float_count += 1
        elif isinstance(item, str):
            string_count += 1
        else:
            others += 1

    print("Integers:", int_count)
    print("Floats:", float_count)
    print("Strings:", string_count)
    print("Others:", others)

count_data_types(10, 3.14, "hello", 25, "world", 7.5, 42, 23, "Sagar", 1.255, [1,2,3])


    

