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

def output():
    print(len(signed_l))
    for l in signed_l:
        print("%d %d" % (l[0], len(l[1])))
        for b in l[1]:
            print("%d" %(b), end=" ")
        print("")

def run():
    output()

if __name__ == "__main__" :
    run()
