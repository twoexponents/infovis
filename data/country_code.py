import json
import csv


def extract():
    f = open('country_id.csv', 'r')
    rdr = csv.reader(f)
    
    cc_list = {}
    for line in rdr:
        cc_list[line[0]] = line[1]

    return cc_list

def run(output, cc_list):

    data = []
    with open(output, 'w') as fw:
        with open('wine_full.json') as fr:
            rr = json.load(fr)

            print "Input len: ", len(rr)
            for line in rr:
                line['ctr_code'] = cc_list[line['country']]
                data.append(line)
                #print line['country'], cc_list[line['country']]

            json.dump(data, fw)
            print "Output len: ", len(data)


if __name__ == "__main__":
    cc_list = extract()
    run('wine_full2.json', cc_list)
