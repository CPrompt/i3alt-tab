#!/usr/bin/python3


import subprocess
import json

output_workspace = subprocess.Popen(
        ['i3-msg','-t','get_workspaces'],
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

output,err = output_workspace.communicate()

# make the output readable json
str_response = output.decode('utf-8')
readable_json = json.loads(str_response)

# loop through all indicies of "num"
# This will tell us how many workspaces are active
# as well as which one has focus
#
# The num cooresponding to the focused workpsace is our
# starting point.
#
# Then we add 1 to that number each time the key combo is pressed
#
# If the focused workspace is equal to the number of workspaces
# the next keypress starts at 1

max_value = []
for i in readable_json:
    num_values = i["num"]
    max_value.append(num_values)
    greatest_workspace = max(max_value)
    focused_value = i["focused"]

    if focused_value == True:
        starting_workspace = num_values
        #print("Focused workspace is:" + str(num_values))
        #print("We will start on workspace : " + str(num_values))
        next_workspace = num_values + 1
        #print("Our next workspace will be : "+ str(next_workspace))

if next_workspace > greatest_workspace:
    print("We are going back to 1")
    subprocess.call(["i3-msg","workspace","1"])
else:
    subprocess.call(["i3-msg","workspace",next_workspace])
    print(next_workspace)
    print("We are going to " + str(next_workspace))

#print(str(num_values) + ":" + str(focused_value))
#print("There are " + str(greatest_workspace) + " workspaces")

