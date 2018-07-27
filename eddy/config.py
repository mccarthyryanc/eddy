"""
Config file with variety of presets
"""


# The format on the presets is:
#    name: (delay-time, display-iterable)
presets = {
    'classic':(0.1,
        '|/-\\'),
    'circle':(0.1,
        '◵◴◷◶',),
    'square':(0.1,
        '◱◰◳◲',),
    'arc':(0.1,
        '◟◜◝◞',),
    'cross':(0.1,
        '┌┐┘└',),
    'blink':(0.1,
        '▚▞',),
    'pulse-plus':(0.1,
        '🞡🞢🞣🞤🞥🞦🞧🞦🞥🞤🞣🞢🞡',),
    'pulse-circle':(0.1,
        '🞅🞆🞇🞈🞉🞈🞇🞆🞅',),
    'pulse-box':(0.1,
        '🞎🞏🞐🞑🞒🞓🞒🞑🞐🞏🞎',),
    'dice':(0.1,
        '⚀⚁⚂⚃⚄⚅⚄⚃⚂⚁⚀',),
    'earth':(0.1,
        '🌎🌎🌍🌍🌏🌏',),
    'clock':(0.1,
        '🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚',),
    'flip':(0.25,
        ['(╮◜⬞◝)╮┳━┳   ',
         '(╯°□°)╯︵ ┻━┻']),
    'deal':(0.5,
        ['(•_•)      ',
         '( •_•)>⌐■-■',
         '(⌐■_■)     ',
         'YYEEAAHH!  ']),
    'shrug':(0.5,
        ['   (ツ)   ',
         '  _(ツ)_  ',
         '¯\_(ツ)_/¯',
         '  _(ツ)_  ',]),
}