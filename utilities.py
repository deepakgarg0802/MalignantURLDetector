import csv
import Feature_extraction as urlfeature
import trainer as tr
import pandas

#---------function to write the attrivutes to csv file--------------#
def resultwriter(feature,output_dest):
    flag=True
    with open(output_dest,'wb') as f:
        for item in feature:
            w = csv.DictWriter(f, item[1].keys())
            if flag:
                w.writeheader()
                flag=False
            w.writerow(item[1])

#----------extract feature to dictionary and write in csv----------
def features_to_csv(url,output_dest):
    feature=[]
    url=url.strip()
    if url!='':
        print 'working on: '+url           #showoff 
        ret_dict=urlfeature.feature_extract(url)
        feature.append([url,ret_dict]);
    resultwriter(feature,output_dest)

#---------function to append the result to csv file--------------#
def check_cache(input_url,output_dest):
    flag=-1
    data = pandas.DataFrame.from_csv(output_dest, index_col=None)
    if any(data.URL==input_url):
        flag=data[data.URL==input_url].malicious.values[0]
        
    return flag

#---------function to append the result to csv file--------------#
def append_result(outcome,output_dest):
    with open(output_dest,'a') as f:
        fieldnames = ['URL', 'malicious']
        w = csv.DictWriter(f,fieldnames=fieldnames)
        #w.writeheader()
        w.writerow({'URL' :outcome[0], 'malicious':outcome[1]})
