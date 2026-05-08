$license = "Licensed to SCARLETTAS LOUNGE"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ProgrammeName = "DeaRMaileR Lab"

if($IsLinux -eq "True"){
$OS = "Linux Unix";
}elseif($IsMacOS -eq "True"){
$OS = "MacOS";
}Else{
$OS = "Windows OS";
}

[string]$v = "V.3.0.0";

$global:greetings = "$ProgrammeName - $OS - $v : [ $license ] : "
$global:unlicense = "$ProgrammeName - $OS - $v : [ Unlicensed Version ] : "
$global:c = @{
                'secureserver.net'                      =      'GoDaddy';
                'mail.protection.outlook.com'           =      'Office';
                'barracudanetworks.com'                 =      'Office';
                'pphosted.com'                          =      'Office';
                'ppe-hosted.com'                        =      'Office';
                'mail.eo.outlook.com'                   =      'Office';
                'mail.outlook.com'                      =      'Office';
                'arsmtp.com'                            =      'Office';
                'parsons-peebles.com'                   =      'Office';
                'inbound-2.mimecast.com'                =      'Mimecast';
                'inbound-1.mimecast.com'                =      'Mimecast';
                'messagelabs.com'                       =      'Office';
                'itwconnect.com'                        =      'Office';
                'prod.hydra.sophos.com'                 =      'Office';
                'antispam.spg-llc.com'                  =      'Office';
                'mxthunder.co'                          =      'Office';
                'mailanyone.net'                        =      'Office';
                'emailsrvr.com'                         =      'Rackspace';
                'netease.com'                           =      'Netease';
                'sunrise.ch'                            =      'Sunrise';
                '@126.com'                               =      'FreeNetase';
                '@163.com'                               =      'FreeNetase';
                '@yeah.com'                              =      'FreeNetase';
                '@hotmail.'                              =      'Microsoft';
                '@live.'                                 =      'Microsoft';
                '@outlook.'                              =      'Microsoft';
                '@msn.'                                 =      'Microsoft';
                '@windowslive.'                         =      'Microsoft';
                
                '.googlemail.com'                       =      'Gsuite';
                'google.com'                            =      'Gsuite';
                '@gmail.com'                             =      'Google';
                'mx.aol.com'                            =      'Aol';
                '@aol.com'                               =      'Aol';
                'comcast.com'                           =      'Comcast';
                'yahoodns.net'                          =      'Yahoo';
                'yahoo.'                                =      'Yahoo';
                'rocketmail'                            =      'Yahoo';
                'one.com'                               =      'One';
                'netsolmail.net'                        =      'Netsolution';
                'netvigator.com'                        =      'NetVigator';
                'hkstar.com'                            =      'NetVigator';
                'worksmobile.com'                       =      'WorkMobile';
                'mxhichina.com'                         =      'AliMail';
                'aliyun'                                =      'Aliyun';
                '263xmail.com'                          =      '263Mail';
                '263.net'                               =      '263Net';
                'mxbiz1.qq.com'                         =      'BizQQ';
                'mxbiz2.qq.com'                         =      'BizQQ';
                'mx1.qq.com'                            =      'QQ';
                'mx2.qq.com'                            =      'QQ';
                'mx3.qq.com'                            =      'QQ';
                'naver.com'                             =      'Naver';
                'serverdata.net'                        =      'Owa';
                'intermedia.net'                        =       'Owa';
                'net.il'                                =       'NetIL';
                '013net.net'                            =       '013Net';
                '1and1.com'                             =       '1And1';
                '21cn.com'                              =       '21Cn';
                'a1.net'                                =       'A1Net';
                'securemail.pro'                        =       'SecureMailPro';
                'ovh.net'                               =       'OVH';
                'dondominio.com'                        =       'DonDom';
                'agfa.com'                              =       'Agfa';
                'ajcmail.net'                           =       'AJCMail';
                '.liteoffice.net'                       =       'LiteOffice';
                '.his.com'                              =       'HisCom';
                '.oxcs.net'                             =       'Oxcs';
                '.viettelidc.com.vn'                    =       'VietVn';
                '.prodigy.net'                          =       'ProDigy';
                '.bbbell.it'                            =       'BBBell';
                '.bigpond.com'                          =       'BigPond';
                '.bluewin.ch'                           =       'Sunrise';
                '.as9143.net'                           =       'AS9143';
                '.locaweb.com.br'                       =       'LocaWebBr';
                '.hostedemail.com'                      =       'HostedMail';
                '.ispgateway.de'                        =       'ISPGateway';
                '.chinaemail.cn'                        =       'ChinaEmail';
                '.smtproutes.com'                       =       'SMTPRoutes';
                '.mailhop.org'                          =       'MailHop';
                '.saunalahti.fi'                        =       'SauNal';
                '.carrierzone.com'                      =       'CarrierZone';
                'eaglesmail.net'                        =       'EagleMail';
                'earthlink.net'                         =       'Earthlink';
                '.spamwall.co.uk'                       =       'SpamWall';
                'provider.nl'                           =       'ProviderNL';
                'seznam.cz'                             =       'SezMan';
                'everyone.net'                          =       'EveryOne';
                '.ctinetworks.com'                      =       'CtiNetworks';
                '.hgcbizmail.com'                       =       'HgcbizMail';
                '.mailhostbox.com'                      =       'MailHostBox.com'
}

function isTrue{
 	param(
 	[string]
 	$domain,
 	[string]
 	$mx
 	)
    $valid = $false
    if($mx){
	    foreach($g in $c.Keys){
	        if($mx -imatch $g){
	            $valid = $true;
	        }
	    }
    }
    if($domain){
	    foreach($g in $c.Keys){
	        if($domain -match $g){
	            $valid = $true;
	        }
	    }
    }
    return $valid
 }

function FindMXText{
    param(
    [string]
    $domain,
    [string]
    $mx
    )

    if($mx){
        foreach($g in $c.Keys){
            if($mx -match $g){
                [string]$textname = $c[$g];
                write-host "$textname " -f Green -nonewline;
                return $true
            }
        }
    }

    if($domain){
        foreach($g in $c.Keys){
            if($domain -match $g){
                [string]$textname = $c[$g];
                write-host "$textname " -f Green -nonewline;
                return $true
            }
        }
    }


 }


 Function IsValidEmail   { 
    Param ([string] $In) 
    [system.Text.RegularExpressions.Regex]::IsMatch($In, "^[a-zA-Z0-9][-a-zA-Z0-9._]+@([-a-zA-Z0-9]+[.])+[a-zA-Z]{2,}$");  
}

function Check-Email {
    param(
    [string]
    $email
    )

    write-host -NoNewLine "Verifying... "

    if(IsValidEmail($email)){
        try{   
        $notexists = "true"
        $domain = $email.Split("@")[1]
        $ndomain = "@$domain"
        $test = $false
        $mx = (Resolve-DnsName -Type MX –Name $domain -ea 0)
            if($mx -ne $null){            
                if((FindMXText -domain $ndomain) -eq $true){
                    return $true
                }
                else{
                    if((FindMXText -mx $mx.nameexchange) -eq $true){
                        return $true
                    }else{
                        write-host "Other Domain " -f yellow -nonewline;
                    }
                }
            }
            elseif($mx -eq $null){
                    write-host "Not Exist! " -f Red -nonewline;
                    return $false
            }
        }
        catch [system.exception] {
                    Write-Host "$_.Exception.ToString() " - red -nonewline;
                    return $false
        }
    }
    else{
        write-host "Invalid Email " -f red -nonewline;
        return $false;
    }
}

function Sortanswer([string]$email, [string]$textinput, [string]$foldername){
                    [string]$textname = $textinput;
                    $mytemp = [environment]::getfolderpath(“Desktop”)
                    [string]$filePath = "$mytemp\SORTRESULT"; # Declared as string, to allow the use of texts without plings and still not fail.
                    [string]$timefolder = $foldername
                    [string]$sessionfolder = "$filepath\$timefolder"
                    [string]$ConsoleFileName = "$sessionfolder\$textname.txt"
                    [string]$fileContents = $email; # Statements can now be written on individual lines, instead of semicolon separated.
                    If (!(test-path $filePath))
                    {
                        New-Item -ItemType directory -Path $filePath | out-null;
                    }
                    if(!(Test-Path $sessionfolder)) {
                       New-Item -ItemType directory -Path $sessionfolder | Out-Null; # Ignore output of creating directory
                       Add-Content $ConsoleFileName "$fileContents"
                    }
                    else {
                      Add-Content $ConsoleFileName "$fileContents"
                    }
 }

function GetMXme{

    param(
    [string]
    $domain,
    [string]
    $mx
    )

    if($mx){
        foreach($g in $c.Keys){
            if($mx.tolower() -match $g){
                [string]$textname = $c[$g];
                $newtext = $textname
            }
        }
    }

    if($domain){
        foreach($g in $c.Keys){
            if($domain.tolower() -match $g){
                [string]$textname = $c[$g];
                $newtext = $textname
            }
        }
    }
    
    return $newtext
 }


function Get-Percent{
    param(
    [int]
    $num,
    [int]
    $total
    )
    $x = $total
    $y = $num
    $result = [math]::Round($y * 100 / $x)
    $last = "{0:N2}%" -f $result
    return "$last" 

}

function browse-file{
    Add-Type -AssemblyName System.Windows.Forms
    $FileBrowser = New-Object System.Windows.Forms.OpenFileDialog -Property @{ 
        InitialDirectory = "./"
        Filter = 'Text File (*.txt)|*.txt|CSV (*.csv)|*.csv'
        Title = 'BROWSE FILE CONTAINING EMAILS:'
    }
    #$FileBrowser.Size = '360, 100'
    $OKButton = New-Object System.Windows.Forms.Button
    $OKButton.Location = New-Object System.Drawing.Size(75, 20)
    $OKButton.Size = '75, 23'
    $OKButton.Text = 'OK'
    $OKButton.DialogResult = 'Ok'
    #$FileBrowser.Controls.Add($OKButton)
    $CancelButton = New-Object System.Windows.Forms.Button
    $CancelButton.Location = '160, 20'
    $CancelButton.Size = '75, 23'
    $CancelButton.Text = 'Cancel'
    $CancelButton.DialogResult = 'Cancel'
    #$FileBrowser.Controls.Add($CancelButton)
    #$FileBrowser.Topmost = $True
    #$FileBrowser.Add_Shown({ $FileBrowser.Activate() })
    if('Ok' -eq $FileBrowser.ShowDialog()){
        $computerFile = $FileBrowser.FileName
        return $computerFile
    }else{
        Read-Host "OPeration Cancelled: Press ENTER TO START OVER";
        browse-file 
    }
}

function findfile([string]$filename){
    $filetofind = "$filename"
    if(!(Test-Path $filetofind -PathType leaf) ){
        ##Write-Host "[!]" -f red -nonewline;write-host "$filename " -nonewline; write-host "doesn't exist !." -f red
        $status = "N"
    }else{
        ##Write-Host "[*]" -f green -nonewline;write-host "$filename " -nonewline; write-host "exist !." -f green
        $status = "Y"
    }
 return $status;
}

function isTrueComma([string]$text,[string]$comma){
    foreach($key in $comma.split(",")){
        if($key -eq $text){
        return $key
        }
    }
}




function newRead-Host{
    
        Param(
                [String]
                $cmdname
            ,
                [string]
                $cmdtext
            ,
                [string]
                $cmdvalues
            ,
                [int]
                $required
            ,
                [string]
                $cmdtype
            )


        Do {
            $invalid = $True;
            try{
                if($cmdtype -eq "[int]"){
                    [int]$info = Read-Host -Prompt "$cmdtext"
                }
                if($cmdtype -eq "[string]"){
                    [string]$info = Read-Host -Prompt "$cmdtext"
                }
                if($cmdtype -eq "[array]"){
                    [array]$info = Read-Host -Prompt "$cmdtext"
                }
                

                if($required -eq 1){
                        if($info -eq "" -or $info -eq $null){
                            write-host "[!] " -nonewline; write-host "$cmdname CNT BE EMPTY" -f red -nonewline;write-host " Try again"
                        }else{
                            if($cmdvalues){
                                $key = isTrueComma -text "$info" -comma "$cmdvalues"
                                if($key){
                                        $invalid = $False
                                        return $key
                                }
                                else{

                                    $vvalue = ""
                                    foreach($cmdvalue in $cmdvalues.split(",")){
                                        $vvalue += "[$cmdvalue] "
                                    }
                                    write-host "[!] " -nonewline; write-host "Input is WRONG" -f red -nonewline;write-host " Use Either $vvalue"




                                }
                            }
                            else{
                                $invalid = $False
                                return $info
                            }
                        }
                }
                elseif($required -eq 0){
                    if($cmdvalues){
                        $key = isTrueComma -text "$info" -comma "$cmdvalues"
                                if($key){
                                        $invalid = $False
                                        return $key
                                }
                                else{

                                    $vvalue = ""
                                    foreach($cmdvalue in $cmdvalues.split(",")){
                                        $vvalue += "[$cmdvalue] "
                                    }
                                    write-host "[!] " -nonewline; write-host "Input is WRONG" -f red -nonewline;write-host " Use Either $vvalue"




                                }
                    }
                    else{
                                $invalid = $False
                                return $info
                        }
                }

            }
            catch [System.Management.Automation.ArgumentTransformationMetadataException]{
                        $vvalue = ""
                        foreach($cmdvalue in $cmdvalues.split(",")){
                            $vvalue += "[$cmdvalue] "
                        }
                        write-host "[!] " -nonewline; write-host "ANS IN WRONG FORMAT" -f red -nonewline;write-host " Use Either $vvalue"
            }
            catch{
                $write = "Something Wrong"
                if($cmdvalues){
                    $vvalue = ""
                    foreach($cmdvalue in $cmdvalues.split(",")){
                        $vvalue += "[$cmdvalue] "
                    }
                    $write = "Something Wrong please use $vvalue"
                }
                
                write-host "[!] " -nonewline;write-warning $write

            }


        } While ($invalid)

            
}

function createfile([string]$file,[string]$text){
        Add-Content "$file " "$text"
}

function mainmunnuechoice{
    write-host "[+] Go Back to Main Menue ?"
    write-host "   - Y : To go back to Main Menue " -nonewline;write-host "<<--" -f red -nonewline;write-host " `r`n   - N : To continue " -nonewline;write-host "-->>" -f green;
    $opt = newRead-Host -cmdname "MAIN MENUE OPTIONN" -cmdtext "`r`n  [Y/N] " -cmdvalues "Y,N" -required 1 -cmdtype "[string]"

    switch($opt){
        Y{&$index}
        N{$ans = 'true'}
    }
}

function loadsettingsfile{
    $opt = newRead-Host -cmdname "SETTINGS OPTIONN" -cmdtext "[+] LOAD Settings From File [Y/N] " -cmdvalues "Y,N" -required 1 -cmdtype "[string]"
    switch($opt){
        Y{return "Y"}
        N{return "N"}
    }
}

function mainmunnuechoice{
    write-host "[+] Go Back to Main Menue ?"
    write-host "   - Y : To go back to Main Menue " -nonewline;write-host "<<--" -f red -nonewline;write-host " `r`n   - N : To continue " -nonewline;write-host "-->>" -f green;
    $opt = newRead-Host -cmdname "MAIN MENUE OPTIONN" -cmdtext "`r`n  [Y/N] " -cmdvalues "Y,N" -required 1 -cmdtype "[string]"

    switch($opt){
        Y{$ans = 'true'}
        N{$ans = 'true'}
    }
}

function Sort-Email{
    param(
    [string]
    $email,
    [string]
    $timefolder
    )

    write-host -NoNewLine "Verifying ... "

    if(IsValidEmail($email)){
        try{   
        $notexists = "true"
        $domain = $email.Split("@")[1].tolower()
        $ndomain = "@$domain"
        $test = $false
        $mx = (Resolve-DnsName -Type MX –Name $domain -ea 0)
            if($mx -ne $null){            
                if((FindMXText -domain $ndomain) -eq $true){
                    write-host ""
                    $insert = GetMXme -domain $ndomain
                    Sortanswer -email $email -textinput $insert -foldername $timefolder;
                }
                else{
                    if((FindMXText -mx $mx.nameexchange) -eq $true){
                        write-host ""
                        $insert = GetMXme -mx $mx.nameexchange
                        Sortanswer -email $email -textinput $insert -foldername $timefolder;
                    }else{
                        write-host "Others " -f yellow;
                        Sortanswer -email $email -textinput "Others" -foldername $timefolder;
                    }
                }
            }
            elseif($mx -eq $null){
                    write-host "Not Exist! " -f Red;
            }
        }
        catch [system.exception] {
                    Write-Host "$_.Exception.ToString() " - red;
        }
    }
    else{
        write-host "Invalid Email " -f red;
    }
}


function salut{
param(
    [string]$color,
    [string]$back
)
if(!($back)){
    $back = "white"
}
cls;
write-host "    █ ▄▀█  █▀▄ █     " -f $color
write-host "   ▐▌          ▐▌    " -f $color
write-host "   █▌▀▄  ▄▄  ▄▀▐█    " -f $color
write-host "  ▐██  ▀▀  ▀▀  ██▌   " -f $color
write-host " ▄████▄  ▐▌  ▄████▄  " -f $color
write-host " -DeaRMaileR XXL->> " -f $back -b $color
Write-Host "  $v (c) 2020  " -f $back -b $color; 
write-host "                                ";
}

$Sorter = {
    $host.UI.RawUI.WindowTitle = "$greetings | DeaRMaileR PRO Sorter";
    $DeaRSorter = { 
        salut -color Yellow -back "black"
        [string]$timefolder = Get-Date -Format "MM.dd.yyyy.HH.mm"
        $computerFile = browse-file
        $TotalfileLine = Get-Content $computerFile
        $i = 0
        $f = 0
        $s = 0
        $numbersLineS = $TotalfileLine.count
        $readfile = [System.IO.File]::ReadLines($computerFile);
        foreach($line in $readfile){
            $i++
            $perc = Get-Percent -num "$i" -total "$numbersLineS"
            write-host "[@] $perc $i/$numbersLineS : " -nonewline; write-host $line.ToLower()" "  -f Yellow -NoNewline; Sort-Email -email $line -timefolder $timefolder;
        }
        Read-Host "Press ENTER";
        mainmunnuechoice
        &$SendMEE
    }
    $SendMEE = { 
        &$DeaRSorter
    }
    $host.UI.RawUI.WindowTitle = "$greetings | DeaRMaileR PRO Sorter";
    salut -color Yellow -back "black"
    Read-Host "Welcome! Press ENTER TO SORT"
    &$SendMEE 
}

$SystemName = $env:computername

if ($env:computername -eq $SystemName){
    &$Sorter
    ##catch{write-host "[!] Something is wrong: " -nonewline;write-host "Unknownn Error!!" -f red;}
} else {
    salut -color red
    $host.UI.RawUI.WindowTitle = "$unlicense";
    write-host "[!] This app is not yet registered: " -nonewline;write-host "Invalid License!!" -f red; 
} 