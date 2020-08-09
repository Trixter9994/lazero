var killer=/\[(?:unified\-canadian\-aboriginal\-syllabics|(?:international\-phonetic\-alphab|tai\-vi)et|linear\-b\-Syllabary|(?:caucasian\-alba|ukrai)nian|(?:japanese\-(?:katak|hirag)an|s(?:aurashtr|inhal)|t(?:agbanw|irhut)|phags\-p|o(?:sman|ri)y|sharad|kannad|granth|thaan|lepch)a|c(?:y(?:priot\-syllabary|rillic)|optic|ha(?:kma|m))|(?:old\-(?:south\-arab|north\-arab|pers)|phoenic|b(?:elarus|ulgar)|mongol|hungar|georg|shav|ital|russ|ly[cd]|car)ian|(?:imperial\-arama|old\-(?:turk|perm)|old\-ital|ethiop|manda|goth|run)ic|(?:meroitic\-cursiv|new\-tai\-lu|palmyren|cheroke|tai\-l)e|(?:m(?:ende\-kikaku|ahajan|od)|varang\-kshit|(?:syloti\-nag|tak)r|k(?:harosh|ai)th|devanagar|kh(?:udawad|ojk)|ol\-chik|gu(?:rmukh|jarat)|pahlav)i|yi\-syllables|(?:sora\-sompe|reja)ng|pahawh\-hmong|(?:meetei\-may|gre)ek|(?:pau\-cin\-ha|telug)u|(?:glagol|ugar)itic|(?:(?:manich|nabat)ae|(?:samari|tibe)t|elbas|germ)an|(?:esperant|hanuno|nk|mr)o|(?:malayal|(?:tai\-t|sidd|og)h)am|(?:(?:sund|jav)a|chi)nese|b(?:a(?:s(?:sa\-vah|hkir)|linese|tak|mum)|opomofo|uginese|engali|rahmi|uhid)|kayah\-li|(?:tifinag|(?:turk|span)is|englis|kazak|polis|frenc|czec)h|a(?:r(?:menian|ab)|vestan)|tagalog|deseret|pollard|(?:(?:myanm|tat)a|khme)r|h(?:ebrew|angul)|syriac|l(?:i(?:mb|s)u|ao)|tamil|latin|thai|vai)\]/

var noman="[arab] iraq [arab]"
// what does this mean?
// i hate regex.
var norman=killer.exec(noman)
//var northman=killer.split(noman)
console.log(norman)
console.log("--fuck--")
//console.log(northman)
