#!/usr/bin/python3

import mutagen.mp4
import mutagen.mp3
import os, subprocess, shutil, sys

class nightcore(object):
    def __init__(self, filename):
        self.filename = filename
        self.ffmpeg_check = True

    def sample_rate_check(self):
        if self.filename.split('.')[-1].lower() == 'm4a':
            if mutagen.mp4.MP4(self.filename).info.sample_rate == 48000:
                self.create()
            else:
                self.create2()
        if self.filename.split('.')[-1].lower() == 'mp3':
            if mutagen.mp3.MP3(self.filename).info.sample_rate == 44100:
                self.create()
            else:
                self.create2()
        if not self.filename.split('.')[-1].lower() == 'mp3' or not self.filename.split('.')[-1].lower() == 'm4a':
            self.create()

    def create2(self):
        if not self.ffmpeg_check:
            if self.filename.split('.')[-1].lower() == 'm4a':
                subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.m4a', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'mp3':
                subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.mp3', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'flac':
                subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.flac', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'wav':
                subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.wav', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
        else:
            if self.filename.split('.')[-1].lower() == 'm4a':
                subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(self.filename, self.filename.replace('.m4a', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'mp3':
                subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(self.filename, self.filename.replace('.mp3', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'flac':
                subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(self.filename, self.filename.replace('.flac', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'wav':
                subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(self.filename, self.filename.replace('.wav', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass

    def create(self):
        if not self.ffmpeg_check:
            if self.filename.split('.')[-1].lower() == 'm4a':
                subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.m4a', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'mp3':
                subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.mp3', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'flac':
                subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.flac', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'wav':
                subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.wav', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
        else:
            if self.filename.split('.')[-1].lower() == 'm4a':
                subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(self.filename, self.filename.replace('.m4a', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'mp3':
                subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(self.filename, self.filename.replace('.mp3', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'flac':
                subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(self.filename, self.filename.replace('.flac', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass
            if self.filename.split('.')[-1].lower() == 'wav':
                subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a"'.format(self.filename, self.filename.replace('.wav', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    os.remove(self.filename)
                except:
                    pass



class LoadMusicFile(object):
    def __init__(self, target_folder):
        self.rootpath = os.getcwd()
        if os.path.exists(os.path.join(os.getcwd(), '_tmp')):
            shutil.rmtree(os.path.join(os.getcwd(), '_tmp'))
        os.makedirs('_tmp', exist_ok=True)
        for file in self.find_target_file(target_folder):
            try:
                shutil.copyfile(file, os.path.join(os.getcwd(), '_tmp', file.split(os.sep)[-1]))
            except:
                pass

    def find_target_file(self, target_folder):
        for root, dirs, files in os.walk(target_folder):
            for file in files:
                if file.split('.')[-1].lower() == 'm4a':
                    yield os.path.join(root, file)
                if file.split('.')[-1].lower() == 'mp3':
                    yield os.path.join(root, file)
                if file.split('.')[-1].lower() == 'flac':
                    yield os.path.join(root, file)
                if file.split('.')[-1].lower() == 'wav':
                    yield os.path.join(root, file)

    def find_nightcored_file(self, target_folder):
        for root, dirs, files in os.walk(target_folder):
            for file in files:
                if file.split('.')[-1].lower() == 'm4a':
                    if ' (nightcore)' in file:
                        yield os.path.join(root, file)

    def __enter__(self):
        return self.find_target_file(os.path.join(os.getcwd(), '_tmp'))

    def __exit__(self, _, __, ___):
        os.makedirs('nightcore_output', exist_ok=True)
        for file in self.find_nightcored_file(os.path.join(os.getcwd(), '_tmp')):
            try:
                shutil.copyfile(file, os.path.join(os.getcwd(), 'nightcore_output', file.split(os.sep)[-1]))
            except:
                pass
        try:
            shutil.rmtree(os.path.join(os.getcwd(), '_tmp'))
        except:
            pass

def main():
    if len(sys.argv) != 1:
        if sys.argv[1] != '-h':
            if sys.argv[1] != '--help':
                with LoadMusicFile(sys.argv[1]) as Load:
                    for file in Load:
                        nightcore(file).create()
            else:
                print('{} [Target Folder]'.format(sys.argv[0]))
                sys.exit(0)
        else:
            print('{} [Target Folder]'.format(sys.argv[0]))
            sys.exit(0)
    else:
        print('{} [Target Folder]'.format(sys.argv[0]))
        sys.exit(0)

if __name__ == '__main__':
    main()
