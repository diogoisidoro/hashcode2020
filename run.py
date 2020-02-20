""" EXAMPLE
books = [5, 2, 3]
# L = [n_book, day_sign, n_ship, [books_id]]
list_l = [
    [2, 1, 1, [0, 1]], 
    [1, 2, 1, [2]]
    ]
d = 5
signed_l = [
    [0, [0, 1]],
    [1, [2]]
    ]
"""

def output(signed_l):
    print(len(signed_l))
    for l in signed_l:
        print("%d %d" % (l[0], len(l[1])))
        for b in l[1]:
            print("%d" %(b), end=" ")
        print("")

def read_input():
    world_input = input()
    # Nbooks, Nlib, Ndays
    world = [int(x) for x in world_input.split()]

    # Scores of books with index as ID
    books_input = input()
    books = [int(x) for x in books_input.split()]

    total_libraries = world[1] 
    for x in range(total_libraries):
        libraries_input = input()
        libraries = [int(x) for x in libraries_input.split()]

        books_ids_input = input()
        books_ids = [int(x) for x in books_ids_input.split()]
        

if __name__ == "__main__" :
    read_input()
