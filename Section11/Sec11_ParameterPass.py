# Create a function that will read input from a file. Your function will
# take the name of the file as a parameter, to be passed by the caller.
# The function will put the device information into the global devices_list.

#---- Function to read device information from file -------------------
def read_device_info(devices_file):

    # Read in the devices from the file
    file = open(devices_file,'r')
    for line in file:

        device_info_list = line.strip().split(',') # Get device info into list
        devices_list.append(device_info_list)

    file.close() # Close the file since we are done with it

#---- Function to go through devices printing them to table -----------
def print_device_info(list_of_devices):

    print ''
    print 'Name     OS-type  IP address           Software         '
    print '------   -------  ------------------   ------------------'

    # Go through the list of devices, printing out values in nice format
    for device in list_of_devices:

        print '{0:8} {1:8} {2:20} {3:20}'.format(device[0],device[1],
                                                 device[2],device[3])

    print ''

#---- Main: read device info, then print ------------------------------

devices_list = [] # Create empty list of devices

print ''
devices_file = raw_input('Enter devices filename:')

read_device_info(devices_file)
print_device_info(devices_list)
