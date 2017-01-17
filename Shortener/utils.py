import string,random

def urlGenerator(size=6,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def shortcodeGenerator(instance,size=6):
    newcode = urlGenerator(size)
    KirrURL = instance.__class__
    notUniqueCode = KirrURL.objects.filter(shortenurl=newcode).exists()
    if notUniqueCode :
        return shortcodeGenerator(instance)
    return newcode