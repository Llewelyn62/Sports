#parse_FC_doc_list.py
import re
import sys
filename = '/Users/Llewelyn_home/Downloads/McIntosh Rogers List of docs.txt'
#This works provided that there are two or more spaces between the end of title
#and date. 
def main(filename=filename):
    try:
        #^(?:\d{1,}.\s)(.*?)(?:\s{1,})(?:Dated|Filed\s+)(\d{2}[\/]\d{2}[\/]\d{4})
        #This works
        date_reg_exp = re.compile(r'\d{2}[/]\d{2}[/]\d{4}')
        multi_spaces = re.compile(r'^(?:\d{1,}.\s+)(.*?)(?:\s{2,})')
        blank_line = re.compile(r'^\s*$')
        edited_file = []
        with open (filename, 'rt') as in_file:
            for line in in_file: # Store each line in a string variable "line"
                if blank_line.findall(line) != True:
                    matches_list=date_reg_exp.findall(line)
                    text_list = multi_spaces.findall(line)
                    if (len(text_list) and len(matches_list))>0:
                        edited_file.insert(-1,text_list[0]+','+matches_list[0])
        with open("edited_file.txt", "w") as output:
            output.write('\n'.join(str(line) for line in edited_file))
    
    except IndexError:
        print('IndexError has occurred, probably sub-list continas null values')
    except TypeError:
        print("TypeError has occurred: something is of the wrong type")
    except:
        print( "Unexpected error:", sys.exc_info()[0])
        raise
if __name__=='__main__':
    main()
    print("Done!")