import csv
import Feature_extraction as urlfeature
import trainer as tr

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