def main():
    data = [
        {'name' : 'Redmi', 'price' : 12000, 'color' : 'silver'},
        {'name' : 'Apple', 'price' : 82000, 'color' : 'black'},
        {'name' : 'Samsung', 'price' : 52000, 'color' : 'white'},
        {'name' : 'Nokia', 'price' : 17000, 'color' : 'black'},
        {'name' : 'Apple', 'price' : 35000, 'color' : 'white'},
        {'name' : 'Apple', 'price' : 52000, 'color' : 'silver'},
        {'name' : 'Redmi', 'price' : 15000, 'color' : 'white'},
        {'name' : 'Samsung', 'price' : 32000, 'color' : 'silver'},
        {'name' : 'Vivo', 'price' : 20000, 'color' : 'black'}
        ]

##    sorted_data = sorted(data, key=lambda x : x['name'])
##
##    for d in sorted_data:
##        print(d)

    filtered_data = list(filter(lambda x : x['name'] == 'Apple', data))
    for d in filtered_data:
        print(d)
    

main()
