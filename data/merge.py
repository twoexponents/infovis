import json


def run(output):

    data = []
    with open(output, 'w') as fw:
        with open('test1.json') as fr:
            rr = json.load(fr)

            print "Input1 len: ", len(rr)
            for line in rr:
                data.append(line)

        with open('test2.json') as fr:
            rr = json.load(fr)
            
            print "Input2 len: ", len(rr)
            for line in rr:
                data.append(line)
        
        with open('test3.json') as fr:
            rr = json.load(fr)
            
            print "Input3 len: ", len(rr)
            for line in rr:
                data.append(line)

        with open('test4.json') as fr:
            rr = json.load(fr)
            
            print "Input4 len: ", len(rr)
            for line in rr:
                data.append(line)

        with open('test5.json') as fr:
            rr = json.load(fr)
            
            print "Input5 len: ", len(rr)
            for line in rr:
                data.append(line)

        with open('test6.json') as fr:
            rr = json.load(fr)
            
            print "Input6 len: ", len(rr)
            for line in rr:
                data.append(line)


        json.dump(data, fw)
        print "Output len: ", len(data)


if __name__ == "__main__":
    run('wine_full_ver2.json')
