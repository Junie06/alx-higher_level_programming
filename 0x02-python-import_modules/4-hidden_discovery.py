#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_names = dir(hidden_4)
    for name in list_names:
        if list_names[:2] != "__":
            print("{}".format(name))
