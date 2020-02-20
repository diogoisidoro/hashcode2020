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

def output():
    print(len(signed_l))
    for l in signed_l:
        print("%d %d" % (l[0], len(l[1])))
        for b in l[1]:
            print("%d" %(b), end=" ")
        print("")

def run():
    books_input = input()
    books = [int(x) for x in books_input.split()]
    print ("books array: ", books)

    scores_input = input()
    scores = [int(x) for x in scores_input.split()]
    print ("scores array: ", scores)

    total_libraries = books[1] 
    for x in range(0,total_libraries):
        print("\n")
        libraries_input = input()
        libraries = [int(x) for x in libraries_input.split()]
        print ("libraries array: ", libraries)

        books_ids_input = input()
        books_ids = [int(x) for x in books_ids_input.split()]
        print ("books ids array: ", books_ids)
        
if __name__ == "__main__" :
    run()
