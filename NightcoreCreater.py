try:
    import concurrent.futures
    import multiprocessing
    import mutagen.mp4
    import mutagen.mp3
    import os
    import platform
    import shutil
    import subprocess
    import sys
    import tarfile
    import urllib.request
    import zipfile
    from io import BytesIO

    from PySide6.QtCore import (QCoreApplication, QByteArray, QMetaObject, QRect,
                                QSize, Qt)
    from PySide6.QtGui import (QFont, QIcon,
                               QImage, QPixmap)
    from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QProgressBar,
                                   QPushButton, QSizePolicy, QFileIconProvider, QFileDialog)

    DragPath = ['']
    DragPath2 = ['']

    class nightcore(object):
        def __init__(self, filename, ffmpeg_check):
            self.filename = filename
            self.ffmpeg_check = ffmpeg_check

        def sample_rate_check(self):
            if self.filename.split('.')[-1].lower() == 'm4a':
                if 48001 <= mutagen.mp4.MP4(self.filename).info.sample_rate:
                    self.create2()
                else:
                    self.create()
            if self.filename.split('.')[-1].lower() == 'mp3':
                if 44101 <= mutagen.mp3.MP3(self.filename).info.sample_rate:
                    self.create2()
                else:
                    self.create()
            if not self.filename.split('.')[-1].lower() == 'mp3' or not self.filename.split('.')[-1].lower() == 'm4a':
                self.create()

        def create2(self):
            if not self.ffmpeg_check:
                if self.filename.split('.')[-1].lower() == 'm4a':
                    subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.m4a', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'mp3':
                    subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.mp3', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'flac':
                    subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.flac', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'wav':
                    subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.wav', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
            else:
                if self.filename.split('.')[-1].lower() == 'm4a':
                    subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(self.filename, self.filename.replace('.m4a', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'mp3':
                    subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(self.filename, self.filename.replace('.mp3', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'flac':
                    subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(self.filename, self.filename.replace('.flac', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'wav':
                    subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/52.5,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(self.filename, self.filename.replace('.wav', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass

        def create(self):
            if not self.ffmpeg_check:
                if self.filename.split('.')[-1].lower() == 'm4a':
                    subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.m4a', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'mp3':
                    subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.mp3', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'flac':
                    subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.flac', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'wav':
                    subprocess.run('{} -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), self.filename, self.filename.replace('.wav', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
            else:
                if self.filename.split('.')[-1].lower() == 'm4a':
                    subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(self.filename, self.filename.replace('.m4a', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'mp3':
                    subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(self.filename, self.filename.replace('.mp3', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'flac':
                    subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(self.filename, self.filename.replace('.flac', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
                if self.filename.split('.')[-1].lower() == 'wav':
                    subprocess.run('ffmpeg -i "{}" -map_metadata -1 -af asetrate=44100*120/100,atempo=1.0083 -vn -acodec aac "{} (nightcore).m4a" -y'.format(self.filename, self.filename.replace('.wav', '')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    try:
                        os.remove(self.filename)
                    except:
                        pass


    class dragQLineEdit(QLineEdit):
        def __init__(self, parent=None):
            super(dragQLineEdit, self).__init__(parent)
            self.setPlaceholderText('Input Folder')

        def dragMoveEvent(self, event):
            if event.mimeData().hasUrls():
                event.setDropAction(Qt.CopyAction)
                event.accept()
            else:
                event.ignore()

        def dragEnterEvent(self, event):
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()

        def dropEvent(self, event):
            if event.mimeData().hasUrls():
                event.accept()
                event.setAccepted(True)
                self.setText(str(event.mimeData().urls()[0].toLocalFile()))
                DragPath[0] = str(event.mimeData().urls()[0].toLocalFile())
            else:
                event.ignore()

    class dragQLineEdit2(QLineEdit):
        def __init__(self, parent=None):
            super(dragQLineEdit2, self).__init__(parent)
            self.setPlaceholderText('Output Folder')

        def dragMoveEvent(self, event):
            if event.mimeData().hasUrls():
                event.setDropAction(Qt.CopyAction)
                event.accept()
            else:
                event.ignore()

        def dragEnterEvent(self, event):
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()

        def dropEvent(self, event):
            if event.mimeData().hasUrls():
                event.accept()
                event.setAccepted(True)
                self.setText(str(event.mimeData().urls()[0].toLocalFile()))
                DragPath2[0] = str(event.mimeData().urls()[0].toLocalFile())
            else:
                event.ignore()

    class MainWindow(QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)
            self.setAcceptDrops(True)
            self.setWindowIcon(QIcon(QPixmap(QSize(512, 512)).fromImage(QImage.fromData(QByteArray.fromBase64(b'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')))))

    class Ui_NightcoreCreater(object):
        def setupUi(self, NightcoreCreater):
            if not NightcoreCreater.objectName():
                NightcoreCreater.setObjectName("NightcoreCreater")
            NightcoreCreater.resize(1102, 348)
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(NightcoreCreater.sizePolicy().hasHeightForWidth())
            NightcoreCreater.setSizePolicy(sizePolicy)
            font = QFont()
            font.setFamilies(["Arial"])
            font.setPointSize(20)
            NightcoreCreater.setFont(font)
            NightcoreCreater.setAcceptDrops(True)
            NightcoreCreater.setStyleSheet("QWidget{color: White;background: #131519}")
            self.FileCompleteProgressBar = QProgressBar(NightcoreCreater)
            self.FileCompleteProgressBar.setObjectName("FileCompleteProgressBar")
            self.FileCompleteProgressBar.setGeometry(QRect(10, 290, 1081, 51))
            font1 = QFont()
            font1.setFamilies(["Arial"])
            font1.setPointSize(10)
            self.FileCompleteProgressBar.setFont(font1)
            self.FileCompleteProgressBar.setStyleSheet("QProgressBar{color: White;background: #131519;}")
            self.FileCompleteProgressBar.setValue(0)
            self.FileCompleteProgressBar.setTextVisible(False)
            self.Input = dragQLineEdit(NightcoreCreater)
            self.Input.setObjectName("Input")
            self.Input.setGeometry(QRect(10, 220, 411, 41))
            sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
            self.Input.setSizePolicy(sizePolicy)
            self.Input.setFont(font)
            self.Input.setStyleSheet("QLineEdit{color: White;background: #131519;border: 2px solid red;}\n"
                                     "")
            self.Input.setFrame(False)
            self.Output = dragQLineEdit2(NightcoreCreater)
            self.Output.setObjectName("Output")
            self.Output.setGeometry(QRect(520, 220, 411, 41))
            sizePolicy.setHeightForWidth(self.Output.sizePolicy().hasHeightForWidth())
            self.Output.setSizePolicy(sizePolicy)
            self.Output.setFont(font)
            self.Output.setStyleSheet("QLineEdit{color: White;background: #131519;border: 2px solid red;}")
            self.Output.setFrame(False)
            self.OpenFolder = QPushButton(NightcoreCreater)
            self.OpenFolder.setObjectName("OpenFolder")
            self.OpenFolder.setIcon(QFileIconProvider().icon(QFileIconProvider.Folder).pixmap(QSize(32, 32)))
            self.OpenFolder.setGeometry(QRect(430, 220, 41, 41))
            sizePolicy.setHeightForWidth(self.OpenFolder.sizePolicy().hasHeightForWidth())
            self.OpenFolder.setSizePolicy(sizePolicy)
            font2 = QFont()
            font2.setFamilies(["Arial"])
            font2.setPointSize(30)
            self.OpenFolder.setFont(font2)
            self.OpenFolder.setStyleSheet("QPushButton{color: #131519;background: #3d3d3d;}")
            self.OpenFolder.setIconSize(QSize(128, 128))
            self.OpenFolder.clicked.connect(self.InputFolders)
            self.OutputFolder = QPushButton(NightcoreCreater)
            self.OutputFolder.setObjectName("OutputFolder")
            self.OutputFolder.setIcon(QFileIconProvider().icon(QFileIconProvider.Folder).pixmap(QSize(32, 32)))
            self.OutputFolder.setGeometry(QRect(941, 220, 41, 41))
            sizePolicy.setHeightForWidth(self.OutputFolder.sizePolicy().hasHeightForWidth())
            self.OutputFolder.setSizePolicy(sizePolicy)
            self.OutputFolder.setFont(font2)
            self.OutputFolder.setStyleSheet("QPushButton{color: #131519;background-color: #3d3d3d;}")
            self.OutputFolder.setIconSize(QSize(128, 128))
            self.OutputFolder.clicked.connect(self.OutputFolders)
            self.StartButton = QPushButton(NightcoreCreater)
            self.StartButton.setObjectName("StartButton")
            self.StartButton.setGeometry(QRect(640, 90, 381, 81))
            sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
            self.StartButton.setSizePolicy(sizePolicy)
            self.StartButton.clicked.connect(self.convertClicked)
            font3 = QFont()
            font3.setFamilies(["Arial"])
            font3.setPointSize(33)
            self.StartButton.setFont(font3)
            self.StartButton.setStyleSheet("QPushButton{color: #131519;background: White;}\n"
                                           "QPushButton:checked {background: #2b2b2b; color: White;}")
            self.StartButton.setCheckable(True)
            self.StartButton.setFlat(False)
            self.Title = QLabel(NightcoreCreater)
            self.Title.setObjectName("Title")
            self.Title.setGeometry(QRect(200, 60, 361, 101))
            self.Title.setFont(font2)
            self.Title.setStyleSheet("QLabel{color: Red;background: #131519}")
            self.Title.setAlignment(Qt.AlignCenter)
            self.Icon = QLabel(NightcoreCreater)
            self.Icon.setObjectName("Icon")
            self.Icon.setGeometry(QRect(60, 50, 125, 125))
            self.Icon.setStyleSheet("QLabel{border: 2px solid red;}")
            self.Icon.setPixmap(QPixmap(QSize(64, 64)).fromImage(QImage.fromData(QByteArray.fromBase64(b'/9j/4AAQSkZJRgABAQAASABIAAD/4QDKRXhpZgAATU0AKgAAAAgABgESAAMAAAABAAEAAAEaAAUAAAABAAAAVgEbAAUAAAABAAAAXgEoAAMAAAABAAIAAAExAAIAAAARAAAAZodpAAQAAAABAAAAeAAAAAAAAABIAAAAAQAAAEgAAAABUGl4ZWxtYXRvciAyLjcuMwAAAASQBAACAAAAFAAAAK6gAQADAAAAAQABAACgAgAEAAAAAQAAAHqgAwAEAAAAAQAAAHoAAAAAMjAyMjoxMjozMCAxMzoxMDo1OAD/4QnFaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMi0xMi0zMFQxMzoxMTozMSswOTowMCIgeG1wOkNyZWF0b3JUb29sPSJQaXhlbG1hdG9yIDIuNy4zIiB4bXA6Q3JlYXRlRGF0ZT0iMjAyMi0xMi0zMFQxMzoxMDo1OCswOTowMCIvPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg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'))))
            self.StartButton.setDefault(False)
            self.is_conv_ok = True
            self.InputFolderPath = ''
            self.OutputFolderPath = ''
            self.ffmpeg_check_ok = False
            self.retranslateUi(NightcoreCreater)

            self.StartButton.setDefault(False)

            QMetaObject.connectSlotsByName(NightcoreCreater)

        def findAudioFile(self, path):
            for root, dirs, file in os.walk(path):
                yield root
                for f in file:
                    yield os.path.join(root, f)

        def detect_totalfiles(self, path):
            TFiles = []
            for r, d, file in os.walk(path):
                for f in file:
                    TFiles.append(f)
            return len(TFiles)

        def InputFolders(self, c):
            self.InputFolderPath = QFileDialog.getExistingDirectory(parent=None, caption='Select Input Folder', dir='.')
            if self.InputFolderPath == '':
                self.InputFolderPath = os.path.expanduser('~').replace(os.sep, '/')
            self.Input.setText(self.InputFolderPath)

        def OutputFolders(self, c):
            self.OutputFolderPath = QFileDialog.getExistingDirectory(parent=None, caption='Select Output Folder', dir=os.path.expanduser('~'))
            if self.OutputFolderPath == '':
                self.OutputFolderPath = os.path.expanduser('~').replace(os.sep, '/')
            self.Output.setText(self.OutputFolderPath)

        def ConvertPause(self):
            self.is_conv_ok = False
            self.StartButton.setText('Start')

        def ConvertStart(self):
            self.StartButton.setText('Stop')
            check_ffmpeg = subprocess.Popen('ffmpeg -hide_banner -version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[1].decode(errors='ignore')
            if not check_ffmpeg == '':
                check_ffmpeg2 = subprocess.Popen('{} -hide_banner -version'.format(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[1].decode(errors='ignore')
                if not check_ffmpeg2 == '':
                    if platform.system() == 'Windows':
                        os.makedirs(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp'), exist_ok=True)
                        back_path = os.getcwd()
                        os.chdir(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp'))
                        win_ffmpeg = urllib.request.urlopen(urllib.request.Request('https://github.com/BtbN/FFmpeg-Builds/releases/latest/download/ffmpeg-master-latest-win64-gpl.zip', headers={'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.0; en-la; Nexus Build/JPG991) AppleWebKit/511.2 (KHTML, like Gecko) Version/5.0 Mobile/11S444 YJApp-ANDROID jp.co.yahoo.android.yjtop/4.01.1.5'})).read()
                        with zipfile.ZipFile(BytesIO(win_ffmpeg)) as ffmpegzip:
                            ffmpegzip.extractall(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp') + '/.')
                        shutil.move(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp', 'ffmpeg-master-latest-win64-gpl', 'bin'), os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin'))
                        os.chdir(back_path)
                        shutil.rmtree(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp'))
                    if platform.system() == 'Linux':
                        os.makedirs(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp'), exist_ok=True)
                        back_path = os.getcwd()
                        os.chdir(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp'))
                        linux_ffmpeg = urllib.request.urlopen(urllib.request.Request('https://github.com/BtbN/FFmpeg-Builds/releases/latest/download/ffmpeg-master-latest-linux64-gpl.tar.xz', headers={'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.0; en-la; Nexus Build/JPG991) AppleWebKit/511.2 (KHTML, like Gecko) Version/5.0 Mobile/11S444 YJApp-ANDROID jp.co.yahoo.android.yjtop/4.01.1.5'})).read()
                        with open('tmp.tar.xz', 'wb') as f:
                            f.write(linux_ffmpeg)
                        os.remove('tmp.tar.xz')
                        with tarfile.open('tmp.tar.xz', 'r:xz') as ffmpegzip:
                            ffmpegzip.extractall(path=os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp') + '/.')
                        shutil.move(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp', 'ffmpeg-master-latest-linux64-gpl', 'bin'), os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin'))
                        os.chdir(back_path)
                        shutil.rmtree(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'tmp'))
                        os.chmod(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), 0o755)
                    if platform.system() == 'Darwin':
                        if not platform.machine() == 'arm64':
                            os.makedirs(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin'), exist_ok=True)
                            darwin_ffmpeg = urllib.request.urlopen(urllib.request.Request('https://evermeet.cx/ffmpeg/ffmpeg-5.1.2.zip', headers={'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.0; en-la; Nexus Build/JPG991) AppleWebKit/511.2 (KHTML, like Gecko) Version/5.0 Mobile/11S444 YJApp-ANDROID jp.co.yahoo.android.yjtop/4.01.1.5'})).read()
                            with zipfile.ZipFile(BytesIO(darwin_ffmpeg)) as ffmpegzip:
                                ffmpegzip.extractall(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin') + '/.')
                            os.chmod(os.path.join(os.path.expanduser('~'), 'ffmpeg_bin', 'bin', 'ffmpeg'), 0o755)
                        else:
                            try:
                                check_darwin_ffmpeg = subprocess.Popen('brew install ffmpeg', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[1].decode(errors='ignore')
                            except:
                                check_darwin_ffmpeg = '1'
                            if not check_darwin_ffmpeg == '':
                                sys.exit(1)
                            self.ffmpeg_check_ok = True
            else:
                self.ffmpeg_check_ok = True
            concurrent.futures.ThreadPoolExecutor(os.cpu_count() * 50).submit(self.ffconvert_main)

        def ffconvert_main(self):
            self.FileCompleteProgressBar.setValue(0)
            if self.InputFolderPath == '':
                self.InputFolderPath = DragPath[0]
            if self.OutputFolderPath == '':
                self.OutputFolderPath = DragPath2[0]
            if not self.InputFolderPath == '':
                if not self.OutputFolderPath == '':
                    outputdir_name = '{} (nightcore)'.format(self.InputFolderPath.split('/')[-1])
                    try:
                        shutil.copytree(self.InputFolderPath, os.path.join(self.OutputFolderPath, outputdir_name))
                    except:
                        pass
                    back_path = os.getcwd()
                    os.chdir(os.path.join(self.OutputFolderPath, outputdir_name))
                    for f in os.listdir():
                        shutil.move(f, self.OutputFolderPath)
                    os.chdir(self.OutputFolderPath)
                    shutil.rmtree(os.path.join(self.OutputFolderPath, outputdir_name))
                    workpath = os.getcwd()
                    self.TotalFiles = self.detect_totalfiles(workpath)
                    NCProcessList = []
                    for file1 in self.findAudioFile(self.OutputFolderPath):
                        file1 = file1.replace(os.sep, '/')
                        if self.is_conv_ok:
                            if os.path.exists(os.path.dirname(file1)):
                                os.chdir(os.path.dirname(file1))
                            else:
                                os.chdir(os.path.dirname(os.path.abspath(file1)))
                            if not '(nightcore)' in file1.split('/')[-1:][0]:
                                NC = nightcore(file1.split('/')[-1], self.ffmpeg_check_ok)
                                NCProcess = multiprocessing.Process(target=NC.sample_rate_check, daemon=True)
                                NCProcess.start()
                                NCProcessList.append(NCProcess)
                            os.chdir(workpath)
                        else:
                            break
                    for c, p in enumerate(NCProcessList):
                        p.join()
                        p.terminate()
                        self.FileCompleteProgressBar.setValue(min((c / self.TotalFiles) * 100.0, 100.0))
                    os.chdir(back_path)
                    self.StartButton.setChecked(False)
                    self.StartButton.setText('Start')
                    self.FileCompleteProgressBar.setValue(0)

        def convertClicked(self, c):
            if self.StartButton.isChecked():
                self.ConvertStart()
            else:
                self.ConvertPause()

        def retranslateUi(self, NightcoreCreater):
            NightcoreCreater.setWindowTitle("Nightcore Creater")
            self.StartButton.setText("Start")
            self.Title.setText("Nightcore Creater")
            self.Icon.setText("")

    def main():
        app = QApplication(sys.argv)
        main_win = MainWindow()
        ui = Ui_NightcoreCreater()
        ui.setupUi(main_win)
        main_win.setFixedSize(main_win.size())
        # main_win.setWindowFlags(Qt.WindowStaysOnTopHint) # 多分要らない
        main_win.show()
        app.exec()

    if __name__ == '__main__':
        if platform.system() == 'Linux':
            multiprocessing.set_start_method('fork')
        else:
            multiprocessing.set_start_method('spawn')
        main()
except:
    import subprocess, os, shutil
    if os.sep in sys.argv[0]:
        File = sys.argv[0].split(os.sep)[-1]
    else:
        File = sys.argv[0]
    if sys.argv[0].lower().endswith('.py'):
        File = File.replace('.py', '')
    if '-' or ' ' in File:
        shutil.copyfile('{}.py'.format(File), 'nightcore_tmp.py')
        File = "artifacter_tmp"
    subprocess.run('{} -c "from PySide6.QtCore import *;from PySide6.QtWidgets import *;from PySide6.QtGui import *;import {};{}.main()"'.format(sys.executable, File, File), shell=True)
    try:
        os.remove('nightcore_tmp.py')
    except:
        pass