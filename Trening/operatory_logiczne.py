is_automatic_mode = True
is_80_percent_light = True
is_dircet_light = False
is_rainy = False


turn_lights_on = is_automatic_mode and (not is_80_percent_light or is_dircet_light or is_rainy)

print("Automatic mode: ", is_automatic_mode)
print("Is the light good: ", is_80_percent_light)
print("Is the sun low: ", is_dircet_light)
print("Is it rainy: ", is_rainy)
print("TURN LIGHTS ON: ", turn_lights_on)
