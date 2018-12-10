import json


def add_province(country_province, country, province, tag, value):

    for list in country_province:
        if list['country'] == country:
            for pr_list in list['provinces']:
                if pr_list['province'] == province:
                    pr_list[tag] = pr_list[tag] + value
                    pr_list['num'] = pr_list['num'] + 1
                    list[tag] = list[tag] + value
                    list['total_num'] = list['total_num'] + 1
                    return country_province
            list['provinces'].append({'province': province, tag: value, 'num': 1})
            list[tag] = list[tag] + value
            list['total_num'] = list['total_num'] + 1
            return country_province
    country_province.append({'country': country, tag: value, 'total_num': 1, 'provinces': [{'province': province, tag: value, 'num': 1}]})

    return country_province


def calc_stat(country_province, tag):

    country_total = []
    province_total = []

    for list in country_province:
        list[tag] = round( (list[tag] / list['total_num']) , 3)
        country_total.append(list[tag])
        
        tmp_list = []
        for pr_list in list['provinces']:
            pr_list[tag] = round( (pr_list[tag] / pr_list['num']), 3)
            tmp_list.append(pr_list[tag])

        tmp_list = sorted(tmp_list)
        province_total.append({list['country']: tmp_list})


    return country_province, country_total, province_total


def run(tag):
    country_list = []
    province_list = []
    country_province = []

    with open('parsed_wine.json') as fr:
        rr = json.load(fr)

        count = 0
        for line in rr:
            #print line['country'],', ', line['province']
            
            country = line['country']
            province = line['province']
            value = float(line[tag])

            if country not in country_list:
                country_list.append(country)
            if province not in province_list:
                province_list.append(province)

            country_province = add_province(country_province, country, province, tag, value)

    stat_result, country_result, province_result = calc_stat(country_province, tag) 

    for data in stat_result:
        print "\n----------------", data['country'], "------------------"
        print "Average", tag, ":", data[tag]
        print "Number of records :", data['total_num']
        print "Number of provinces :", len(data['provinces'])
        print data['provinces']

    print "\nCountry results: "
    print sorted(country_result)

    print "\nProvince results: "
    for prov in province_result:
        print "-", prov

if __name__ == "__main__":
    run('points')
    #run('price')
