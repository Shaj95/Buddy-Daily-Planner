complaint_type, key_words = [], []

# defining the function read_complaint_data that populates the lists: \
# complaint_type and key_words

def read_complaint_data():

    #the global function is required to populate the lists as they are outside the function

    global complaint_type, key_words

    #attempt to read the elizadata.txt text file and factored in the response if it does not open

    try:
        data_source = open("Buddy_data.txt", 'r')
    
    except:
        print ('Could not open Buddy_data.text')
        exit()

#print(data_source.read())

    # initializing the line_read function for the elizadata text file    

    line_read = '\n'

    # while loop iniitiated so that the program continuously reads the text file\
    # until it reaches a line that does not end with a return (or '\n')
    
    while line_read.endswith ('\n'):
        
        # the variable line_read is set to read the current line of the text file
        line_read = data_source.readline()
        
        # the variable complaint_type_with_backslash_n filters out the complaint_type from unimportant words
        complaint_type_with_backslash_n = line_read[14:]

        # appending the complaint_type word from the text file to the complaint_type list in python
        complaint_type.append(complaint_type_with_backslash_n[:-1])

        line_read = data_source.readline()

        #the split function is used to only account for the keywords and not spaces
        key_words_for_this_complaint_type = line_read.split(' ')

        # the pop function picks out the last word in the line of the keywords
        last_word = key_words_for_this_complaint_type.pop()

        #in order to only utilize the last word and not the backslash n after it:
        if last_word.endswith('\n'):
            last_word = last_word[:-1]
            
        # appending the keywords word from the text file to the key_words list in python
        key_words_for_this_complaint_type.append(last_word)
        key_words.append(key_words_for_this_complaint_type)

        #continuing the loop until it reaches a line with no backslash n at the end
        if line_read.endswith('\n'):
            line_read = data_source.readline()

#the function that has been defined above is now being initialized below for its utilization
read_complaint_data() # this is followed by the print functions
                        #in order to test if the text file has populated the lists correctly

#print("printing complaint_type and key_words from runtime data...")
#print(complaint_type)
#print(key_words)

