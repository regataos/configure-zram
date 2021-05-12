#!/bin/bash
#
# This script helps to decide the "vm.swappiness" value,
# according to the size of the RAM memory available in the hardware,
# so that the zRAM can have at least one block device compressed in the 1GB RAM.

# Set Swap File priority
/sbin/swapoff /swap/swapfile
/sbin/swapon -p 10 /swap/swapfile

# Set the value of the "vm.swappiness" option and configure zram rules
ram_size=$(free -g | grep Mem | awk '{print $2}')
if [ $ram_size -le 1 ]; then
    sysctl vm.swappiness=60
    /sbin/mkswap /dev/zram0 524288
    /sbin/swapon -p 100 /dev/zram0

elif [ $ram_size -le 2 ]; then
    sysctl vm.swappiness=35
    /sbin/mkswap /dev/zram0 1048572
    /sbin/swapon -p 100 /dev/zram0

elif [ $ram_size -le 5 ]; then
    sysctl vm.swappiness=25
    /sbin/mkswap /dev/zram0 1048572
    /sbin/swapon -p 100 /dev/zram0

elif [ $ram_size -le 7 ]; then
    sysctl vm.swappiness=20
    /sbin/mkswap /dev/zram0 1048572
    /sbin/swapon -p 100 /dev/zram0

elif [ $ram_size -le 14 ]; then
    sysctl vm.swappiness=10
    /sbin/mkswap /dev/zram0 2097148
    /sbin/swapon -p 100 /dev/zram0

elif [ $ram_size -le 15 ]; then
    sysctl vm.swappiness=10
    /sbin/mkswap /dev/zram0 2097148
    /sbin/swapon -p 100 /dev/zram0

else
    sysctl vm.swappiness=10
    /sbin/mkswap /dev/zram0 2097148
    /sbin/swapon -p 100 /dev/zram0
fi
