import os

# App info
APP_TITLE = "CMDevCenter"
APP_TITLE_LONG = "CyanogenMod Dev Center"
APP_VERSION = "v0.1"
APP_AUTHOR = "Jeremie Long"

# Local Stuff
FINAL_HOME = (os.environ['HOME'])
FINAL_HOME_BIN = "%s/bin" % (FINAL_HOME)
FINAL_CONFIG_DIR = ('%s/.config/cmdevcenter') % (FINAL_HOME)
FINAL_APP_DATA = ('/usr/share/cmdevcenter/')
FINAL_CONFIG = ('%s/cmdevcenter.conf') % (FINAL_CONFIG_DIR)
FINAL_REPO_DIR = ('%s/build') % (FINAL_CONFIG_DIR)
FINAL_PATCH_DIR = ('%s/cm-gerrit') % (FINAL_CONFIG_DIR)
