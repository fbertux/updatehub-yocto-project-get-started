def __set_defaults_updatehub():
    set_default('MACHINE', 'raspberrypi3')

def __after_init_updatehub():
    set_var('UPDATEHUB_POLLING_INTERVAL', '1m')
    set_var('ENABLE_UART', '1')

run_set_defaults(__set_defaults_updatehub)
run_after_init(__after_init_updatehub)
