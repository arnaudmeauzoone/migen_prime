set_device -name GW2A-18C GW2A-LV18PG256C8/I7
#add_file prime.cst
add_file prime.v
set_option -use_mspi_as_gpio 1
set_option -use_sspi_as_gpio 1
set_option -use_ready_as_gpio 1
set_option -use_done_as_gpio 1
set_option -rw_check_on_ram 1
set_option -top_module top

run all
