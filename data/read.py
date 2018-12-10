import json


def write1(output):

    data = []
    with open(output, 'w') as fw:
        with open('winemag-data-130k-v2.json') as fr:
            rr = json.load(fr)

            count = 0
            for line in rr:
                if count == 10000:
                    break

                if line["title"] == None:
                    continue
                if line["points"] == None:
                    continue
                if line["description"] == None:
                    continue
                if line["price"] == None:
                    continue
                if line["designation"] == None:
                    continue
                if line["variety"] == None:
                    continue
                if line["province"] == None:
                    continue
                if line["province"] == "Other":
                    continue
                if line["country"] == None:
                    continue
                if line["winery"] == None:
                    continue

                count = count + 1

                data.append(line)

            print "Data len: ", len(data)
            json.dump(data, fw)


if __name__ == "__main__":
    write1('parsed_wine_10000.json')
