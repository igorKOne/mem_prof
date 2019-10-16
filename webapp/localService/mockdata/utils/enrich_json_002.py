import json
import sys
import functools, operator

file_name = 'Business.json'
new_file_name = 'new_' + file_name
folder = '../'

def main():

    # Process each object in the list 
    def convert(obj):
        #print(obj)
        # calculate total of "RSCS"
        obj["total"] = functools.reduce(lambda x,y: x + y["value"], obj["RSCS"], 0)
        # calculate "warm_potential_perc"
        obj["warm_potential_perc"] = obj["warm_potential"] / obj["total"]
        return obj

    # read from "results" attribute
    with open(folder + file_name,'r') as f:
        l = json.load(f)
        nl = list(map(convert,l["results"]))
    
    # save to "results" attribute    
    with open(folder + new_file_name,'x') as f:
        json.dump({'results':nl},f)


if __name__ == "__main__":
    
    #file_name = sys.argv[1]

    main()