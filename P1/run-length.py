bytes_series = '11000' # we define a possible byte series

def run_length(bytes_series):
    final_list = []
    count = 1
    char = bytes_series[0] # the first element of the byte series is stored in char
    for i in range(1, len(bytes_series)):
        if bytes_series[i] == char:
            count = count + 1 # if the char does not change, we count the contiguous number of '0' or '1'
        else:
            final_list.append([char, count]) # if it changes, we store the previous number of '0' or '1'
            char = bytes_series[i] # the char changes to the other one
            count = 1 # we initialize again the counter
    final_list.append([char, count])
    return final_list


bytes_series_rl = run_length(bytes_series) # call the function
print(bytes_series_rl) # print the result