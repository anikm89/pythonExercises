s =[1,1,2,2,3]

def solution(id_list):

    unique_id = 0
    # XOR fo revery id in id list
    for i in id_list:

        print "number in the list : ",i
        print "number unique id   : ",unique_id
        print 'XOR result         :',unique_id ^i


        a = unique_id


        unique_id =unique_id ^ i


    return unique_id



print solution(s)