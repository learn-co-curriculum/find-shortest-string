import time

def find_shortest_string(list):

    # THE LONGER WAY OF DOING THE SAME THING AS LINE 15

    '''
    shortest = list[0]

    for item in list:
        if len(item) < len(shortest):
            shortest = item

    return shortest
    '''
    
    return min(list, key = len)

if __name__ == '__main__':


    print("Expecting: 'a'")
    print(find_shortest_string(['aaa', 'a', 'bb', 'ccc']))

    print("")

    print("Expecting: 'hi'")
    print(find_shortest_string(['cat', 'hi', 'dog', 'an']))

    print("")

    print("Expecting: 'lily'")
    print(find_shortest_string(['flower', 'juniper', 'lily', 'dandelion']))

    print("")

    print("Expecting: 'cat'")
    print(find_shortest_string(['cat']))

    # BENCHMARK HERE

    start_time = time.time()

    for i in range(1000):
        find_shortest_string(['flower', 'juniper', 'lily', 'dandelion'])

    avg_time = ( time.time() - start_time ) / 1000

    print(avg_time)