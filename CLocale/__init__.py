import locale
LOCALE = locale.getdefaultlocale()[0]

if LOCALE == 'de_DE':
    import de_DE as CStrings
else:
    import en_US as CStrings