from multiprocessing import Pool

def cube(number):
    return number*number*number
if __name__ == '__main__':
    pool = Pool()

    #map, apply, join, close

    numbers = range(10)

    result = pool.map(cube, numbers)
    # result = pool.apply(cube, (numbers[3],))

    pool.close()
    pool.join()
    print(result)