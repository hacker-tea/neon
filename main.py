def on_forever():
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.pause(500)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    basic.pause(500)
basic.forever(on_forever)
