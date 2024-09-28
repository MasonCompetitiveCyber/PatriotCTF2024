Give me four words, Vasily

Description:
We have been tracking a highly suspicious submarine believed to be harboring and hiding many enemy skiddies. Unfortunately, this satellite image is rather out of date. Your mission is to locate the submarines there, and tell us what class they are with their NATO reporting name - a letter from the NATO phonetic alphabet, spelled out.

We want to know precisely where the aft end of northernmost submarine attached to the pier is. Communicate its location in three words. Include the NATO reporting name of the class of submarine in your answer.

Submission format: PCTF{three.position.words.class_name}
Example submission: PCTF{employing.broken.imports.sierra}


Difficulty:
4/10

Flag:
PCTF{bagels.light.vivid.kilo}

Hints
what3words.com - Use the image of the submarines on this site.
The submarines are known to be of an old design, diesel-electric, and slightly under 200 ft in length.


Author:
James Crowley {@zephyrone3956}

Tester


Writeup
1. Use reverse image search to identify the location as the Shkval Naval Shipyard, in, Polyyarny, Murmansk Oblast, Russia.
2. Find the exact pier on the map on what3words.com. The image provided is from 2018 on Bing Maps, which uses DigitalGlobe. what3words uses a different site.
3. See the detailed images attached for the exact placement, per the instructions. The northernmost submarine is outboard of the other one, on the east side of the eastern pier. The aft end is the pointy bit,
4. To identify the submarines as a Kilo-class, the easiest entry point is their length.
    a. The Kilos are significantly shorter than other submarines, these particular examples being under 200 ft. Newer models of the class are slightly longer with an added hull section. See the Russian submarines in the DO_NOT_DIST folder: Apart from the little auxilliary ones at the bottom, and the Lada-class (no NATO phonetic alphabet reporting name), the Kilos are the only answer.
    b. https://www.space.com/russian-submarine-missile-loading-satellite-photo This link shows a Kilo-class submarine being loaded in Sevastopol.
    c. https://www.reddit.com/r/submarines/comments/rqnvk6/i_cant_identify_some_of_these_all_spotted_around/ This reddit post has the Kilo identified...the exact picture on what3words (rotated) in the third slide.
