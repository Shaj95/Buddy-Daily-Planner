#the below function is defined to get complaint types based on keywords from eliza300_5_runtime_data

def get_complaint_type(a_user_complaint):

    
    #importing the complaint_type and key_words lists from eliza300_5_runtime_data 
    from Buddy_runtime_data import complaint_type, key_words
    
    target = set()

#Post2: using the key_words to determine the complaint_type 
    
    for counter in range (len(complaint_type)):

        for keyword in key_words[counter]:
        
#Post3
            if keyword.lower() in a_user_complaint.lower():
                target.add(counter)
            
          
    return target
