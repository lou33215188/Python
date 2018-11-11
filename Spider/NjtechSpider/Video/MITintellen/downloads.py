import os


def loadVideoLinks(videoLinksText):
    with open(videoLinksText, 'r') as videoLinksFile:
        videoLinks = videoLinksFile.readlines()
        return videoLinks


def loadReDownLoadFile(videoLinkForDownloaded_NAME='downloaded.txt'):  # 缓存已经下载过的文件目录
    os.chdir("C:\\Users\\22306\\Documents\\Python\\Spider\\NjtechSpider\\Video\\MITintellen")
    #  此目录为代码存放目录
    fileLists = os.listdir()
    if videoLinkForDownloaded_NAME not in fileLists:
        with open(videoLinkForDownloaded_NAME, 'w') as videoLinkForDownloaded_File:
            os.chdir('Videos')
            downloadedVedios = os.listdir()
            for downloadedVedio in downloadedVedios:
                downloadedVedio = downloadedVedio + '\n'
                videoLinkForDownloaded_File.write(downloadedVedio)
    with open(videoLinkForDownloaded_NAME, 'r') as videoLinkForDownloaded_FileFORREAD:
        videoLinkForDownloaded = videoLinkForDownloaded_FileFORREAD.readlines()
    return videoLinkForDownloaded


def reDownLoadFileAppend(newdownloadlink, videoLinkForDownloaded_NAME='downloaded.txt'):
    os.chdir("C:\\Users\\22306\\Documents\\Python\\Spider\\NjtechSpider\\Video\\MITintellen")
    #  此目录为代码存放目录
    with open(videoLinkForDownloaded_NAME, 'a') as addfile:
        newdownloadlink = newdownloadlink+'\n'
        addfile.write(newdownloadlink)


def downloadVideo(videoLinkForDownload):
    videoLinkForDownloaded = loadReDownLoadFile()
    videoLinkForDownload = videoLinkForDownload + '\n'
    if videoLinkForDownload not in videoLinkForDownloaded:

        reDownLoadFileAppend(videoLinkForDownload)
        shell_commandFORdownload = "you-get " + videoLinkForDownload
        os.chdir('C:\\Users\\22306\\Documents\\Python\\Spider\\NjtechSpider\\Video\\MITintellen\\Videos')
        # 此目录为视频存放目录
        os.system(shell_commandFORdownload)
        os.chdir('C:\\Users\\22306\\Documents\\Python\\Spider\\NjtechSpider\\Video\\MITintellen')
        # 此目录为代码存放目录

        print(videoLinkForDownloaded)
        print(videoLinkForDownload)
        print("我要开始下载啦！")


if __name__ == "__main__":
    videoLinks = loadVideoLinks("C:\\Users\\22306\\Documents\\Python\\Spider\\NjtechSpider\\Video\\MITintellen\\videoLink.txt")
    # 此目录为代码存放目录
    videoLinkForDownloaded = loadReDownLoadFile()     # To forbid redownload
    for eachVideoLink in videoLinks:
        videoLinkForDownload = eachVideoLink[:-1]
        downloadVideo(videoLinkForDownload)
