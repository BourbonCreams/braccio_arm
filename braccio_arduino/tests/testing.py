import moving_braccio_pc
import time

#my_list0 = ['__ignored__', '0', '15', '180', '170', '90', '73']
my_list0 = ['__ignored__', '0', '90', '90', '120', '90', '73']
my_list = ['__ignored__', '90', '90', '90', '90', '90', '73']
my_list2 = ['__ignored__', '113.31737217956655', '31.196046390035818', '106.08270991063819', '44.023738844039364', '24.849715641384', '73']

my_list3 = ['__ignored__', '90', '90', '90', '90', '90', '73']

'''
Test if the gripper moves from 10 degrees to 73 degrees (open to closed)
increasing the angle one degree at a time. Change False to True in the 
following if statement if you want to run this test.
'''
if False:
    for a in range(11,73,1):
        if len(my_list) == 6:
            my_list = ['__ignored__'] + my_list
        my_list[6] = str(a)
        print "\n", my_list
        moving_braccio_pc.main(my_list)
        #time.sleep(3)

    my_list = ['__ignored__'] + my_list
    my_list[6] = '73'


difference = ['4', '0', '-5', '6', '-4']

for i in range(1,6):
    my_list[i] = int(float(my_list[i])) + int(float(difference[i-1]))
print my_list

moving_braccio_pc.main(my_list)
