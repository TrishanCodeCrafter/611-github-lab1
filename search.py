import json

def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    
    # Converts the search string to lowercase to make the search case-insensitive.
    search_string = search_string.lower()  
    
    # Loops through each item (which is likely a dictionary) in the `json_data`
    for entry in json_data:
        if (search_string in str(entry.values()).lower()):
            # If a match is found, the current `entry` is added to the `results` list and we break the loop.
            results.append(entry)
            break

    # Returns the list of matching items.
    return results  
    



    