#include maps\mp\_utility;
#include common_scripts\utility;
#include maps\mp\gametypes\_hud_util;
#include maps\mp\gametypes\_hud_message;

init()
{
    PrecacheShader("lui_loader_no_offset");
    PrecacheShader("compass_emp");
    PrecacheShader("black");
    level thread onPlayerConnect();
    level.clientid = 0;
    level.result = 0;
}

onPlayerConnect()
{
    for(;;)
    {
        level waittill("connected", player);
        player.MenuInit = false;
        
        if(player isHost())
             player.status = "Boss";
        else
             player.status = "Unverified";
             
        if(player isVerified())
             player giveMenu();
             
        player thread onPlayerSpawned();
        player.clientid = level.clientid;
        level.clientid++;
    }
}

onPlayerSpawned()
{
     self endon("disconnect");
     level endon("game_ended");
     isFirstSpawn = true;
     self freezecontrols(false);
     for(;;)
     {
          self waittill("spawned_player");
          if(isFirstSpawn)
          {
               if (self isHost())
               {
                    thread overflowfix();
               }
               isFirstSpawn = false;
          }
          if(self isHost())
          {
               self iprintln("Press [{+stance}] & [{+actionslot 3}] Bind Text Goes Here");
               self iprintln("Press [{+stance}] & [{+actionslot 3}] Bind Text Goes Here");
          }
          if(self isVerified())
          {
               self thread welcomeMessage();
               self iprintln("Welcome To Bossam V6 Menu Base");
          }
     }
}
welcomeMessage()
{
	notifyData = spawnstruct();
	notifyData.titleText = "^5Welcome ^2" + self.name + "^5 To Bossam V6 Menu Base";
	notifyData.notifyText = "^5Hope You Enjoy!";
	notifyData.iconName = "lui_loader_no_offset";
	notifyData.glowColor = (0, 0, 1);
	notifyData.duration = 12;
	notifyData.font = "hudbig";
	notifyData.hideWhenInMenu = false;
	self thread maps\mp\gametypes\_hud_message::notifyMessage(notifyData);
}
overflowfix()
{
     level endon("game_ended");
     level.test = createServerFontString("default",1.5);
     level.test setText("xTUL");
     level.test.alpha = 0;
     for(;;)
     {
          level waittill("textset");
          if(level.result >= 50)
          {
               level.test ClearAllTextAfterHudElem();
               level.result = 0;
               foreach(player in level.players)
               {
                    if(player.menu.open == true)
                    {
                         player recreateText();
                    }
               }
          }
          wait 0.01;
     }
}

recreateText()
{
     self endon("disconnect");
     self endon("death");
     
     input = self.CurMenu;
     title = self.CurTitle;
     
     self thread submenu(input, title);
}

giveMenu()
{
     if (self isVerified())
     {
          if (!self.MenuInit)
          {
               self.MenuInit = 1;
               self thread MenuInit();
          }
     }
}

isVerified()
{
     if (self.status == "Boss" || self.status == "Verified" || self.status == "VIP" || self.status == "Admin" || self.status == "Co-Host")
     {
          return true;
     }
     else
     {
          return false;
     }
}

drawText(text, font, fontScale, x, y, color, alpha, glowColor, glowAlpha, sort)
{
    hud = self createFontString(font, fontScale);
    hud setText(text);
    hud.x = x;
    hud.y = y;
    hud.color = color;
    hud.alpha = alpha;
    hud.glowColor = glowColor;
    hud.glowAlpha = glowAlpha;
    hud.sort = sort;
    hud.alpha = alpha;
    
    level.result += 1;
    hud setText(text);
    level notify("textset");
    
    return hud;
}

drawShader(shader, x, y, width, height, color, alpha, sort)
{
    hud = newClientHudElem(self);
    hud.elemtype = "icon";
    hud.color = color;
    hud.alpha = alpha;
    hud.sort = sort;
    hud.children = [];
    hud setParent(level.uiParent);
    hud setShader(shader, width, height);
    hud.x = x;
    hud.y = y;
    return hud;
}

changeVerificationMenu(player, verlevel)
{
     if (player.status != verlevel && !player isHost())
     {
          player notify("statusChanged");
          player.status = verlevel;
          wait 0.05;
          player giveMenu();
          
          if(player.status == "Unverified")
          {
               player thread destroyMenu(player);
          }
          if(player isVerified())
          {
               self iprintln("^7 " + getPlayerName(player) + " Is Now " + verificationToColor(verlevel));
               player iPrintln("^3Your Are Now  " + verificationToColor(verlevel));
               player iprintln("Press [{+speed_throw}]+[{+melee}] To Open Mod Menu");
          }
     }
     else
     {
          if (player isHost())
              self iPrintln("You Cannot Change The Access Level of The " + verificationToColor(player.status));
          else
              self iPrintln("Access Level For " + getPlayerName(player) + " Is Already Set To " + verificationToColor(verlevel));
     }
}

changeVerification(player, verlevel)
{
     player notify("statusChanged");
     player.status = verlevel;
     wait 0.05;
     player giveMenu();
     
     if(player.status == "Unverified")
     {
          player thread destroyMenu(player);
          player iPrintln("You Are Now Unverified!");
     }
     if(player isVerified())
     {
          player iPrintln("^3You Are Now  " + verificationToColor(verlevel));
          player iprintln("Press [{+speed_throw}]+[{+melee}] To Open");
     }
}

getPlayerName(player)
{
	playerName = getSubStr(player.name, 0, player.name.size);
	for(i=0; i < playerName.size; i++)
	{
		if(playerName[i] == "]")
			break;
	}
	if(playerName.size != i)
		playerName = getSubStr(playerName, i + 1, playerName.size);
	return playerName;
}

verificationToNum(status)
{
	if (status == "Boss") //HOST
		return 5;
	if (status == "Co-Host") //
		return 4;
	if (status == "Admin")
		return 3;
	if (status == "VIP")
		return 2;
	if (status == "Verified")
		return 1;
	else
		return 0;
}

verificationToColor(status)
{
	if (status == "Boss")
		return "^1Boss";
	if (status == "Co-Host")
		return "^4Co-Host";
	if (status == "Admin")
		return "^6Admin";
	if (status == "VIP")
		return "^3VIP";
	if (status == "Verified")
		return "^2Verified";
	else
		return "^5Unverified";
}

Iif(bool, rTrue, rFalse)
{
	if(bool)
		return rTrue;
	else
		return rFalse;
}

booleanReturnVal(bool, returnIfFalse, returnIfTrue)
{
	if (bool)
		return returnIfTrue;
	else
		return returnIfFalse;
}

booleanOpposite(bool)
{
	if(!isDefined(bool))
		return true;
	if (bool)
		return false;
	else
		return true;
}

CreateMenu()
{
     self add_menu("Main Menu", undefined, "Unverified");
     self add_option("Main Menu", "Self Menu", ::submenu, "MainMods", "Self Menu");
     self add_option("Main Menu", "Lobby Menu", ::submenu, "LobbyMenu", "Lobby Menu");
     self add_option("Main Menu", "Fun Menu", ::submenu, "FunMenu", "Fun Menu");
     self add_option("Main Menu", "Players Menu", ::submenu, "PlayersMenu", "Players Menu");
     
     self add_menu("MainMods", "Main Menu", "VIP");
     self add_option("MainMods", "God Mode",::GodMode);
     self add_option("MainMods", "Infinite Ammo");
     self add_option("MainMods", "Change Class");
     self add_option("MainMods", "All Perks");
     self add_option("MainMods", "Visions");
     self add_option("MainMods", "Toggle Fov");
     self add_option("MainMods", "MultiJump");
     self add_option("MainMods", "Invisible",::Invisible);
     self add_option("MainMods", "Left Side Gun");
     self add_option("MainMods", "Jet Pack");
     self add_option("MainMods", "Dead Clone");
     self add_option("MainMods", "Clone");
     self add_option("MainMods", "Suicide");
     self add_option("MainMods", "Hulk Mode");
     self add_option("MainMods", "Speed x2");
     self add_option("MainMods", "Drop Gun");
     self add_option("MainMods", "Rapid Fire");
     self add_option("MainMods", "Advanced Fly Mode");
     self add_option("MainMods", "Theme Menu", ::submenu, "Theme", "Theme Menu");
     
     self add_menu("Theme", "MainMods", "VIP");
     self add_option("Theme", "Red Theme");
     self add_option("Theme", "Blue Theme");
     self add_option("Theme", "Green Theme");
     self add_option("Theme", "Yellow Theme");
     self add_option("Theme", "Purple Theme");
     self add_option("Theme", "Cyan Theme");
     self add_option("Theme", "Aqua Theme");
     self add_option("Theme", "Flashing Theme");
     
     self add_menu("LobbyMenu", "Main Menu", "BOSS");
     self add_option("LobbyMenu", "Hear Everyone");
     self add_option("LobbyMenu", "Anti Quit");
     self add_option("LobbyMenu", "Big Names");
     self add_option("LobbyMenu", "Pause Game");
     self add_option("LobbyMenu", "Low Gravity");
     self add_option("LobbyMenu", "Super Jump");
     self add_option("LobbyMenu", "Super Speed");
     self add_option("LobbyMenu", "Timescale");
     self add_option("LobbyMenu", "Force Host",::ForceHost);
     self add_option("LobbyMenu", "Spawn A Bot");
     self add_option("LobbyMenu", "Restart Game");
     self add_option("LobbyMenu", "Unlimited Game");
     self add_option("LobbyMenu", "How To Use Menu");
     self add_option("LobbyMenu", "Long KillCam Time");
     self add_option("LobbyMenu", "Disco Lights");
     self add_option("LobbyMenu", "All Ghost Camo");
     self add_option("LobbyMenu", "All Diamond Camo");
     self add_option("LobbyMenu", "Show FPS");
     self add_option("LobbyMenu", "MiniMaps");
     
     self add_menu("FunMenu", "Main Menu", "Admin");
     self add_option("FunMenu", "Roll Away Dog");
     self add_option("FunMenu", "Disco Dancer");
     self add_option("FunMenu", "Gold Shoes");
     self add_option("FunMenu", "Red Shoes");
     self add_option("FunMenu", "Chrome Shoes");
     self add_option("FunMenu", "Shield Shoes");
     self add_option("FunMenu", "Adventure Time");
     self add_option("FunMenu", "Flying Bomber");
     self add_option("FunMenu", "Earthquake Mode");
     self add_option("FunMenu", "MW3 IMS");
     self add_option("FunMenu", "Plant Bomb (^1S&D^7)");
     self add_option("FunMenu", "Defuse Bomb (^1S&D^7)");
     self add_option("FunMenu", "Rotate Rocket");
     self add_option("FunMenu", "FireBalls");
     self add_option("FunMenu", "Dogs Wave");
     self add_option("FunMenu", "Debug Wave");
     self add_option("FunMenu", "Turret Wave");
     self add_option("FunMenu", "Red CP Wave");
     self add_option("FunMenu", "Rotor Head");
     
     self add_menu("PlayersMenu", "Main Menu", "Co-Host");
     for (i = 0;i < level.players.size;i++)
     { self add_menu("pOpt " + i, "PlayersMenu", "Co-Host"); }
}

updatePlayersMenu()
{
     self.menu.menucount["PlayersMenu"] = 0;
     for (i = 0;i < level.players.size;i++)
     {
          player = level.players[i];
          playerName = getPlayerName(player);
          
          playersizefixed = level.players.size - 1;
          if(self.menu.curs["PlayersMenu"] > playersizefixed)
          {
               self.menu.scrollerpos["PlayersMenu"] = playersizefixed;
               self.menu.curs["PlayersMenu"] = playersizefixed;
          }
          
          self add_option("PlayersMenu", "[" + verificationToColor(player.status) + "^7] " + playerName, ::submenu, "pOpt " + i, "[" + verificationToColor(player.status) + "^7] " + playerName);
          self add_menu_alt("pOpt " + i, "PlayersMenu");
          self add_option("pOpt " + i, "Give Co-Host", ::changeVerificationMenu, player, "Co-Host");
          self add_option("pOpt " + i, "Give Admin", ::changeVerificationMenu, player, "Admin");
          self add_option("pOpt " + i, "Give VIP", ::changeVerificationMenu, player, "VIP");
          self add_option("pOpt " + i, "Verify", ::changeVerificationMenu, player, "Verified");
          self add_option("pOpt " + i, "Unverify", ::changeVerificationMenu, player, "Unverified");
     }
}

add_menu_alt(Menu, prevmenu)
{
     self.menu.getmenu[Menu] = Menu;
     self.menu.menucount[Menu] = 0;
     self.menu.previousmenu[Menu] = prevmenu;
}

add_menu(Menu, prevmenu, status)
{
     self.menu.status[Menu] = status;
     self.menu.getmenu[Menu] = Menu;
     self.menu.scrollerpos[Menu] = 0;
     self.menu.curs[Menu] = 0;
     self.menu.menucount[Menu] = 0;
     self.menu.previousmenu[Menu] = prevmenu;
}

add_option(Menu, Text, Func, arg1, arg2)
{
     Menu = self.menu.getmenu[Menu];
     Num = self.menu.menucount[Menu];
     self.menu.menuopt[Menu][Num] = Text;
     self.menu.menufunc[Menu][Num] = Func;
     self.menu.menuinput[Menu][Num] = arg1;
     self.menu.menuinput1[Menu][Num] = arg2;
     self.menu.menucount[Menu] += 1;
}

updateScrollbar()
{
     self.menu.scroller MoveOverTime(0.10);
     self.menu.scroller.y = 68 + (self.menu.curs[self.menu.currentmenu] * 19.20);
     self.menu.scroller.archived = false;
}

openMenu()
{
    self freezeControls(false);
    self enableInvulnerability();
    self setClientUiVisibilityFlag("hud_visible", 0);
    self StoreText("Main Menu", "Main Menu");
	
	self.menu.backgroundinfo FadeOverTime(0.30);
    self.menu.backgroundinfo.alpha = 0.80;
    
	self.menu.background FadeOverTime(0.30);
    self.menu.background.alpha = 0.55;
    self.menu.background.archived = false;
	
	self.menu.background1 FadeOverTime(0.30);
    self.menu.background1.alpha = 0.80;	
    self.menu.background1.archived = false;

    self.swagtext FadeOverTime(0.3);
    self.swagtext.alpha = 0.90;

	self.menu.line MoveOverTime(0.30);
	self.menu.line.y = -50;	
	self.menu.line.archived = false;
	self.menu.line2 MoveOverTime(0.30);
	self.menu.line2.y = -50;
	self.menu.line2.archived = false;

    self updateScrollbar();
    self.menu.open = true;
}

closeMenu()
{
    self.menu.options FadeOverTime(0.3);
    self.menu.options.alpha = 0;
    self setClientUiVisibilityFlag("hud_visible", 1);
    
    self.statuss FadeOverTime(0.3);
    self.statuss.alpha = 0;
	
	self.tez FadeOverTime(0.3);
    self.tez.alpha = 0;
    
    self.menu.background FadeOverTime(0.3);
    self.menu.background.alpha = 0;
	
	self.menu.background1 FadeOverTime(0.3);
    self.menu.background1.alpha = 0;
    
    self.swagtext FadeOverTime(0.30);
    self.swagtext.alpha = 0;

    self.menu.title FadeOverTime(0.30);
    self.menu.title.alpha = 0;
    
	self.menu.line MoveOverTime(0.30);
	self.menu.line.y = -550;
	self.menu.line2 MoveOverTime(0.30);
	self.menu.line2.y = -550;
	
	self.menu.backgroundinfo FadeOverTime(0.3);
    self.menu.backgroundinfo.alpha = 0;

	self.menu.scroller MoveOverTime(0.30);
	self.menu.scroller.y = -510;
    self.menu.open = false;
}

destroyMenu(player)
{
    player.MenuInit = false;
    closeMenu();
	wait 0.3;

	player.menu.options destroy();	
	player.menu.background1 destroy();
	player.menu.scroller destroy();
	player.menu.scroller1 destroy();
	player.infos destroy();
	player.menu.line destroy();
	player.menu.line2 destroy();
	player.menu.title destroy();
	player notify("destroyMenu");
}

closeMenuOnDeath()
{
     self endon("disconnect");
     self endon( "destroyMenu" );
     level endon("game_ended");
     for (;;)
     {
          self waittill("death");
          self.menu.closeondeath = true;
          self submenu("Main Menu", "Main Menu");
          closeMenu();
          self.menu.closeondeath = false;
     }
}
scaleLol()
{
    self endon("stopScale");
    for(;;)
    {
	self.tez.glowColor = (0.1, 0, 0);
    wait .05;
    self.tez.glowColor = (0.2, 0, 0);
    wait .05;
    self.tez.glowColor = (0.3, 0, 0);
    wait .05;
    self.tez.glowColor = (0.4, 0, 0);
    wait .05;
    self.tez.glowColor = (0.5, 0, 0);
    wait .05;
    self.tez.glowColor = (0.6, 0, 0);
    wait .05;
    self.tez.glowColor = (0.7, 0, 0);
    wait .05;
    self.tez.glowColor = (0.8, 0, 0);
    wait .05;
    self.tez.glowColor = (0.9, 0, 0);
    wait .05;
    self.tez.glowColor = (1, 0, 0);
    wait .05;
    self.tez.glowColor = (0.9, 0, 0);
    wait 1.5;
    self.tez.glowColor = (0.8, 0, 0);
    wait .05;
    self.tez.glowColor = (0.7, 0, 0);
    wait .05;
    self.tez.glowColor = (0.6, 0, 0);
    wait .05;
    self.tez.glowColor = (0.5, 0, 0);
    wait .05;
    self.tez.glowColor = (0.4, 0, 0);
    wait .05;
    self.tez.glowColor = (0.3, 0, 0);
    wait .05;
	self.tez.glowColor = (0.2, 0, 0);
    wait .05;
    self.tez.glowColor = (0.1, 0, 0);
    wait .05;
    self.tez.glowColor = (0, 0, 0);
    wait .05;    
    }
}
StoreShaders()
{
    self.menu.background = self drawShader("Black", 235, -100, 200, 1000, (0.04, 0.66, 0.89), 0, 0);
    self.menu.background1 = self drawShader("compass_emp", 235, -100, 200, 1000, (0.04, 0.66, 0.89), 0, 0);
	self.menu.scroller = self drawShader("white", 236, -100, 200, 17, (0.04, 0.66, 0.89), 255, 1);
    self.menu.line = self drawShader("white", 336, -1000, 2, 500, (0.04, 0.66, 0.89), 255, 3);
    self.menu.line2 = self drawShader("white", 135, -1000, 2, 500, (0.04, 0.66, 0.89), 255, 2);
    self.menu.line3 = self drawShader("white", 235, -100, 200, 2, (0.04, 0.66, 0.89), 255, 4);
}

StoreText(menu, title)
{
    self.menu.currentmenu = menu;
    string = "";
	self.menu.currentmenu = input;
    self.menu.title destroy();
    self.menu.title = drawText(title, "default", 1.6, 235, 35, (1, 1, 1), 0, (0, 0, 0), 1, 3);
    self.menu.title FadeOverTime(0.3);
    self.menu.title.alpha = 1;
    self.menu.title.archived = false;
    self notify ("stopScale");
    self thread scaleLol();
    self.tez destroy();
    self.tez = self createFontString( "default", 2.5);
    self.tez setPoint( "CENTER", "TOP", 235, 5);
    self.tez setText("Bossam V6 Menu Base");
    self.tez FadeOverTime(0.3);
    self.tez.alpha = 1;
    self.tez.foreground = true;
    self.tez.archived = false;
    self.tez.glowAlpha = 0.6;
    self.tez.glowColor = (1, 0, 0);
    for(i = 0; i < self.menu.menuopt[menu].size; i++)
    { string +=self.menu.menuopt[menu][i] + "\n"; }
    
    self.statuss destroy();
    self.statuss = self createFontString( "default", 1.3);
    self.statuss setPoint( "CENTER", "TOP", 235, 23);
    self.statuss setText("iTahhr <3");
    self.statuss FadeOverTime(0.3);
    self.statuss.alpha = 1;
    self.statuss.foreground = true;
    self.statuss.archived = false;
    self.statuss.glowAlpha = 1;
    self.statuss.glowColor = (0, 0, 0);
    
    self.menu.options destroy();
    self.menu.options = drawText(string, "objective", 1.6, 265, 68, (1, 1, 1), 0, (0, 0, 0), 0, 4);
    self.menu.options FadeOverTime(0.3);
    self.menu.options.archived = false;
    self.menu.options.alpha = 1;
    self.menu.options setPoint( "LEFT", "LEFT", 503, -128 ); //x = -L/+R, y = -U/+D
 
}

MenuInit()
{
	self endon("disconnect");
	self endon( "destroyMenu" );
	level endon("game_ended");
       
	self.menu = spawnstruct();
	self.toggles = spawnstruct();
     
	self.menu.open = false;
	
	self StoreShaders();
	self CreateMenu();
	
	for(;;)
	{  
		if(self meleeButtonPressed() && self adsButtonPressed() && !self.menu.open) // Open.
		{
			openMenu();
		}
		if(self.menu.open)
		{
			if(self useButtonPressed())
			{
				if(isDefined(self.menu.previousmenu[self.menu.currentmenu]))
				{
					self submenu(self.menu.previousmenu[self.menu.currentmenu]);
				}
				else
				{
					closeMenu();
				}
				wait 0.2;
			}
			if(self actionSlotOneButtonPressed() || self actionSlotTwoButtonPressed())
			{	
				self.menu.curs[self.menu.currentmenu] += (Iif(self actionSlotTwoButtonPressed(), 1, -1));
				self.menu.curs[self.menu.currentmenu] = (Iif(self.menu.curs[self.menu.currentmenu] < 0, self.menu.menuopt[self.menu.currentmenu].size-1, Iif(self.menu.curs[self.menu.currentmenu] > self.menu.menuopt[self.menu.currentmenu].size-1, 0, self.menu.curs[self.menu.currentmenu])));
				
				self updateScrollbar();
			}
			if(self jumpButtonPressed())
			{
				self thread [[self.menu.menufunc[self.menu.currentmenu][self.menu.curs[self.menu.currentmenu]]]](self.menu.menuinput[self.menu.currentmenu][self.menu.curs[self.menu.currentmenu]], self.menu.menuinput1[self.menu.currentmenu][self.menu.curs[self.menu.currentmenu]]);
				wait 0.2;
			}
		}
		wait 0.05;
	}
}
 
submenu(input, title)
{
	if (verificationToNum(self.status) >= verificationToNum(self.menu.status[input]))
	{
		self.menu.options destroy();

		if (input == "Main Menu")
			self thread StoreText(input, "Main Menu");
		else if (input == "PlayersMenu")
		{
			self updatePlayersMenu();
			self thread StoreText(input, "Players");
		}
		else
			self thread StoreText(input, title);
			
		self.CurMenu = input;
		self.CurTitle = title;
		
		self.menu.scrollerpos[self.CurMenu] = self.menu.curs[self.CurMenu];
		self.menu.curs[input] = self.menu.scrollerpos[input];
		
		level.result += 1;
		level notify("textset");
		
		if (!self.menu.closeondeath)
		{
			self updateScrollbar();
   		}
    }
    else
    {
		player iPrintln("^5Only Players With ^4" + verificationToColor(self.menu.status[input]) + " ^5Can Access This Menu!");
    }
}

ForceHost()
{
     if(self.forceHost==1)
     {
          setdvar("party_connectToOthers","0");
          setdvar("partyMigrate_disabled","1");
          setdvar("party_mergingEnabled","0");
          setdvar("allowAllNAT","1");
          self iprintln("Force Host ^2ON");
          self.forceHost=0;
     }
     else
     {
          setdvar("party_connectToOthers","1");
          setdvar("partyMigrate_disabled","0");
          setdvar("party_mergingEnabled","1");
          setdvar("allowAllNAT","0");
          self iprintln("Force Host ^1OFF");
          self.forceHost=1;
     }
}
Invisible()
{
     self.invisible = booleanOpposite(self.invisible);
     self iPrintln(booleanReturnVal(self.invisible, "Invisible ^1OFF", "Invisible ^2ON"));
     if(self.invisible)self Hide();
     else self Show();
}
GodMode()
{
     if(self.GM==0)
     {
          self.GM=1;
          self iprintln("God Mode ^2ON");
          self EnableInvulnerability();
     }
     else
     {
          self.GM=0;
          self iprintln("God Mode ^1OFF");
          self DisableInvulnerability();
     }
}

