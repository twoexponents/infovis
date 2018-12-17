import json



def run(output):

    data = []
    with open(output, 'w') as fw:
        with open('wine_full.json') as fr:
            rr = json.load(fr)

            print "Input len: ", len(rr)
            for line in rr:
                line.pop("description", None)
                line.pop("taster_twitter_handle", None)
                #print line['country'], cc_list[line['country']]
                if line['winery'] == 'X':
                    continue
                data.append(line)

            json.dump(data, fw)
            print "Output len: ", len(data)


if __name__ == "__main__":
    run('wine_full_ver2.json')
