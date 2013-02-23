import os
import ConfigParser
from gi.repository import Gtk

import CLocale
Str = CLocale.CStrings

class Log():
    def start(self):
        Parser().write("verbose", True)
        self.send("Starting", "Starting verbose mode", \
                    "You have started the verbose option, expect verbosity!")
     
    def stop(self):
        self.send("Stopping", "Stopping verbose mode", \
                    "You have stopped the verbose option")
        Parser().write("verbose", False)

    def send(self, ty, title, message):
        if Parser().read("verbose"):
            print "/*** %s ***/\nTitle: %s\nMessage: %s\n" \
                    % (ty, title, message)
                    
class Dialogs():

    def CDial(self, num, title, message):
        Dtype = (Gtk.MessageType.INFO, Gtk.MessageType.WARNING, Gtk.MessageType.ERROR)
        dialog = Gtk.MessageDialog(None, Gtk.DialogFlags.MODAL, message_type=Dtype[num], buttons=Gtk.ButtonsType.OK)
        dialog.set_title(title)
        dialog.set_markup(message)
        dialog.run()
        dialog.destroy()
        return True

    def QDial(self, title, message):
        dialog = Gtk.MessageDialog(None, Gtk.DialogFlags.MODAL, message_type=Gtk.MessageType.QUESTION, buttons=Gtk.ButtonsType.YES_NO)
        dialog.set_markup(title)
        dialog.format_secondary_markup(message)
        response = dialog.run()
        dialog.destroy()

        if response == Gtk.ResponseType.YES:
            return True
        else:
            return False

class Parser():                
    def read(self, arg):
        try:
            config = ConfigParser.RawConfigParser()
            config.read(Str.FINAL_CONFIG)
            c = config.get(Str.APP_TITLE, arg)
        except ConfigParser.NoSectionError:
            c = "%s" % ("Default")

        if c == "True": c = True
        if c == "False": c = False
        if c == "None": c = None

        return c

    def write(self, arg, value):
        for paths in Str.FINAL_CONFIG_DIR, Str.FINAL_REPO_DIR:
            if not os.path.exists(paths):
                os.makedirs(paths)
        try:
            config = ConfigParser.RawConfigParser()
            config.read(Str.FINAL_CONFIG)
            getVerbose = config.get(Str.APP_TITLE, 'verbose')
            getRepoPath = config.get(Str.APP_TITLE, 'repo_path')
            getBranch = config.get(Str.APP_TITLE, 'branch')
            getDevice = config.get(Str.APP_TITLE, 'device')
        except:
            getVerbose = None
            getRepoPath = None
            getBranch = None
            getDevice = None

        config = ConfigParser.RawConfigParser()
        config.add_section(Str.APP_TITLE)

        if arg == 'verbose':
            config.set(Str.APP_TITLE, 'verbose', value)
        elif getVerbose:
            config.set(Str.APP_TITLE, 'verbose', getVerbose)
        else:
            config.set(Str.APP_TITLE, 'verbose', False)
            
        if arg == 'repo_path':
            config.set(Str.APP_TITLE, 'repo_path', value)
        elif getRepoPath:
            config.set(Str.APP_TITLE, 'repo_path', getRepoPath)
        else:
            config.set(Str.APP_TITLE, 'repo_path', Str.FINAL_REPO_DIR)
            
        if arg == 'branch':
            config.set(Str.APP_TITLE, 'branch', value)
        elif getBranch:
            config.set(Str.APP_TITLE, 'branch', getBranch)
        else:
            config.set(Str.APP_TITLE, 'branch', "(None)")
            
        if arg == 'device':
            config.set(Str.APP_TITLE, 'device', value)
        elif getDevice:
            config.set(Str.APP_TITLE, 'device', getDevice)
        else:
            config.set(Str.APP_TITLE, 'device', "(None)")

        with open(Str.FINAL_CONFIG, 'wb') as configfile:
                config.write(configfile)
                
class Util():
    
    def which(self, program):
        def is_exe(fpath):
            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

        return None
                
