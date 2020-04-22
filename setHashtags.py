import json

hashtags = [
    # 'junkjournal','illustratorsoninstagram','more_illustrations',
    # 'cuteillustrations','kidlitillustration',
    # 'artistsoninstagram','illustration_best','illustration_of_the_day',
    # 'floralillustration','theartofslowliving','beigeaesthetic',
    # 'flatlay_art','hobonichi','fashionillustration','fashionsketch','illustrator',
    # 'brwnpaperbag','cuteart','instaart','procreate','flatlayua',
    # 'myhyggehome','slowandsimpledays',
    # 'illustracion','socialdistancingart','picturebookart','neutralpalette',
    # 'lavieparisienne','nordicmood','aquarellepainting','watercolordaily',
    # 'watercolorillustrations','gouacheillustration',
    # 'sketchbookpainting'
    'procreateart', 'procreate5', 'procreatepainting', 'illustrator',
    'illustrationoftheday', 'paintingoftheday', 'floralpainting', 
    'aquarelle', 'watercolorart', 'watercolorpainting', 'gouacheillustration',
    'floralillustration', 'cutepainting', 'illustratorsofinstagram', 
    'neutralpalette', 'fashionillustration',
    'fashionsketch', 'flatlay', 'beigeaesthetic', 'kidlitart', 'myhyggehome', 
    'theartofslowliving', 'junkjournal', 'characterart', 'characterdesign',
    'graphicdesign', 'picturebookart', 'illustration', 'drawingoftheday', 'sketchbook',
    'artist', 'artjournal','watercolorillustrations','hobonichi',
    ]


with open("hashtags.json","w") as f:
    json.dump(hashtags, f)