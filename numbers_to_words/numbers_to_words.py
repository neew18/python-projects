def dict_of_numbers():
    dict = {}
    list = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    listother =['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    listother1 = [ '', '-one', '-two', '-three', '-four', '-five', '-six', '-seven', '-eight', '-nine']

    for i in listother:
        for j in listother1:
            sum = i + j
            list.append(sum)
    index = 0
    for key in range(0,100):
        if index < len(list):
            dict[key] = list[index]
            index+=1

    return dict

if __name__=="__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])