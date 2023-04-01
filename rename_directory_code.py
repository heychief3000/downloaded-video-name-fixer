#Jonathan Westlake
#1/30/21
#JW
import os
import re
import traceback
#import MediaInfo
#import magic
import mimetypes
import shutil
from e_enums import *

class ProcessData:
    def __init__(self):

        # Old
        # self.paths = [r"X:\torrents\movies",
        #               r"X:\torrents\shows",
        #               r"Y:\torrents\shows",
        #               r"Z:\torrents\shows"]


        # 1/16/23
        self.root_paths = [r"O:\VMs\X\torrents\movies",
                      r"O:\VMs\X\torrents\shows",
                           #r"Y:\torrents\shows",
                      r"O:\VMs\Z\torrents\shows"]

        #self.root_paths = [r"O:\VMs\Z\torrents\01_SampleData"] #Debug


        # self.paths = [
        #               r"Z:\torrents\shows"]

        self.string_list = ["1080p", "DVDRip", "720p", "2160p", "WEB-DL"]

    def findStringsTypeIndex(self, f):

        x=-1
        for str in self.string_list:
            x = f.find(str)
            if x != -1:
                break
        return x

    def RenameDirs(self, f):
        # print(f)
        x = self.findStringsTypeIndex(f)
        # print(x)
        if x > 0:
            sub_str = f[0:x - 1]
            # print(sub_str)
            split_array = sub_str.split(".")
            # print(split_array)
            new_string = " ".join(split_array)
            print(f"Rename {f} into:\t\t\t {new_string}")
            os.rename(f, new_string)
        else:
            dir2 = os.getcwd()
            print(f"Can't Process {f}, dir {dir2}")

    def moveFilesIntoFolder(self, source_folder, dest_folder):

        files = os.listdir(source_folder)

        for file in files:
            bIsVideo = False
            file_path = os.path.join(source_folder, file)
            if os.path.isfile(file_path):

                mimeType = mimetypes.guess_type(file_path)[0]
                if mimeType:
                    if mimeType.startswith("video"):
                        bIsVideo = True

                print(f"\t{file_path}: Video: {mimeType}")
                if bIsVideo:
                    print(f"Moving:({file_path}) to:({dest_folder})")
                    shutil.move(file_path, dest_folder)
                    x=0



    def CreateShowFolders(self, path, dir):

        if 'shows' in path and os.path.isdir(dir):
            self.reg1ExCaseSeasonEpisode(path, dir)
            self.reg2ExCaseSeason(path, dir)

    def reg1ExCaseSeasonEpisode(self, path, dir):
        regex = "s[0-9][0-9]e[0-9][0-9]"
        result = re.search(regex, dir.lower())
        if not result:
            print(f"Reg1 - Show Match Not Found: '{dir}'")
            return

        str_s, str_e = result.regs[0]
        season_str = dir[str_s + 1: str_e].lower()  # Add 1 to remove the 's'
        folder_str = dir[0:str_s - 1]
        season_num = season_str.split("e")[0]
        season_folder = f"Season {season_num}"

        print(f"Reg1 - Show Match Found: ({folder_str}) :::::: ({season_str}) :::: ({season_folder})")

        new_path = os.path.join(path, "_PLEX_READY_", folder_str, season_folder)
        if not os.path.exists(new_path):
            print(f"Reg1 - Making dir {new_path}")
            os.makedirs(new_path)

        old_path = os.path.join(path, dir)

        bMoveSuccessful = False
        try:

            # os.replace(old_path, new_path)
            # os.system(f"move {old_path} {new_path}")
            self.moveFilesIntoFolder(old_path, new_path)
            bMoveSuccessful = True
        except:
            error_traceback = traceback.format_exc()
            print_color(error_traceback, ConsoleColor.RED)

        try:
            if bMoveSuccessful:
                print_color(f"Reg1 - Trying to Delete: '{old_path}'")
                shutil.rmtree(old_path)
                print_color(f"Reg1 -Delete successful to Delete: '{old_path}'", ConsoleColor.OKGREEN)
                pass
            else:
                print_color(f"Reg1 -Not Trying to to Delete because no MOVE happened successfully: '{old_path}'",
                            ConsoleColor.OKGREEN)
        except:
            print_color(f"Reg1 - [ERROR] Failed  to Delete: '{old_path}'", ConsoleColor.RED)
            error_traceback = traceback.format_exc()
            print(error_traceback)

        x = 0
        # lstr = dir.split(" ")
        # for str in lstr:

    def reg2ExCaseSeason(self, path, dir):
        #Note: $ forces nothing after it.
        regex = "s[0-9][0-9]$"
        result = re.search(regex, dir.lower())
        if not result:
            print(f"Reg2 - Show Match Not Found: '{dir}'")
            return

        str_s, str_e = result.regs[0]
        season_str = dir[str_s + 1: str_e].lower()  # Add 1 to remove the 's'
        folder_str = dir[0:str_s - 1]
        season_num = season_str.split("e")[0]
        season_folder = f"Season {season_num}"

        print(f"Reg2 - Show Match Found: ({folder_str}) :::::: ({season_str}) :::: ({season_folder})")

        new_path = os.path.join(path, "_PLEX_READY_", folder_str, season_folder)

        if not os.path.exists(new_path):
            print(f"Reg2 - Making dir {new_path}")
            os.makedirs(new_path)

        old_path = os.path.join(path, dir)

        bMoveSuccessful = False

        try:

            # os.replace(old_path, new_path)
            # os.system(f"move {old_path} {new_path}")
            self.moveFilesIntoFolder(old_path, new_path)
            bMoveSuccessful = True
        except:
            error_traceback = traceback.format_exc()
            print_color(error_traceback, ConsoleColor.RED)

        try:
            if bMoveSuccessful:
                print_color(f"Reg2 - Trying to Delete: '{old_path}'")
                shutil.rmtree(old_path)
                print_color(f"Reg2 - Delete successful to Delete: '{old_path}'", ConsoleColor.OKGREEN)
                pass
            else:
                print_color(f"Reg2 - Not Trying to to Delete because no MOVE happened successfully: '{old_path}'",
                            ConsoleColor.OKGREEN)
        except:
            print_color(f"Reg2 - [ERROR] Failed  to Delete: '{old_path}'", ConsoleColor.RED)
            error_traceback = traceback.format_exc()
            print(error_traceback)

        x = 0


        x=0

    def checkDirectoryDownloadingFiles(self, path, sub_folder):

        bContainsOnePartial = False
        new_path = os.path.join(path, sub_folder)
        os.chdir(new_path)
        files = [f for f in os.listdir('.')]
        for f in files:
            if ".!qB" in f:
                bContainsOnePartial = True

        os.chdir(path) #Return back to normal
        return bContainsOnePartial



    def execute(self):

        for root_path in self.root_paths:
            print(f"Processing: {root_path}")
            print("======================="
                  ""
                  "=========")
            if os.path.exists(root_path):
                os.chdir(root_path)
                dir2 = os.getcwd()
                print(f"Changed Directory {dir2}")

                files = [f for f in os.listdir('.')]
                for f in files:
                    #if self.checkDirectoryDownloadingFiles(path, f):
                    #    print(f"Skipping .!qB: '{f}'")
                    #    continue
                    #else:
                    self.RenameDirs(f)

                #Get updated file list since we renamed the folders above.
                files = [f for f in os.listdir('.')]
                for f in files:
                    #if self.checkDirectoryDownloadingFiles(path, f):
                    #    continue
                    #else:
                    self.CreateShowFolders(path=root_path, dir=f)

            else:
                print("===============================================================")
                print(f"ERROR: Path does not exist: {root_path}")
                print(f"ERROR: Path does not exist: {root_path}")
                print(f"ERROR: Path does not exist: {root_path}")
                print(f"ERROR: Path does not exist: {root_path}")
                print("===============================================================")


def main():
    oPD = ProcessData()
    oPD.execute()

if __name__ == '__main__':
    #main_Downloader_Test()
    main()

#>>> s = 'foo123bar'
#>>> re.search('1.3', s)
#<_sre.SRE_Match object; span=(3, 6), match='123'>
#.	Matches any single character except newline
#^	∙ Anchors a match at the start of a string
#∙ Complements a character class
#$	Anchors a match at the end of a string
#*	Matches zero or more repetitions
#+	Matches one or more repetitions
