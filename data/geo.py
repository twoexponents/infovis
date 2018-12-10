import geocoder
import json
import logging
import inspect

def makeAddr (json):
    sep = ', '
    addr = json['province'] + sep + json['country']

    if json['region_1'] != None:
        addr = json['region_1'] + sep + addr

    if json['region_2'] != None:
        addr = json['region_2'] + sep + addr
    return addr


def run(output):

    logging.basicConfig()
    #g = geocoder.mapquest('Salta, None, Argentian',  key='SmpPVNYKcPvAJeT0VefAvJf8p8VvSqcJ')


    #key = 'SmpPVNYKcPvAJeT0VefAvJf8p8VvSqcJ'
    key = 'tyzAkVeIdsJdOaAR5MDzUYPUFl1fUtTv'

    data = []
    with open(output, 'w') as fw:
        with open('parsed_wine_10000.json') as fr:
            rr = json.load(fr)

            print "Input len: ", len(rr)

            sep = ', '
            count = 0
            addrs = []
            list_10 = []
            eof = len(rr) - 1

            for idx, line in enumerate(rr):
                count = count + 1
                addr = makeAddr(line)
                addrs.append(addr)
                list_10.append(line)

                if count == 10 or idx == eof:
                    g = geocoder.mapquest(addrs, method='batch', key=key)
                    # append to original data
                    for idx, val in enumerate(g):
                        list_10[idx]['lat'] = val.raw['latLng']['lat']
                        list_10[idx]['lng'] = val.raw['latLng']['lng']
                        data.append(list_10[idx])
                    addrs = []
                    count = 0
                    list_10 = []

            print "Output len: ", len(data)
            json.dump(data, fw)
    
    #for result in g:
    #    print(result.raw['latLng']['lat'])
    #print(g.raw['latLng'])



if __name__ == "__main__":
    run('parsed_wine_latlng_10000.json')
