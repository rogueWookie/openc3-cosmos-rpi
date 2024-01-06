# Script Runner test script
cmd("RPI EXAMPLE")
wait_check("RPI STATUS BOOL == 'FALSE'", 5)
