#using maps/mp/_utility;
#using common_scripts/utility;
#using maps/mp/gametypes/_hud_util;
#using maps/mp/gametypes/_hud;
#using maps/mp/gametypes/_hud_message;
#using maps/mp/gametypes/_weapons;
#using maps/mp/killstreaks/_ai_tank;
#using maps/mp/killstreaks/_dogs;

#namespace _imcsx_gsc_studio;

/*
	Name: init
	Namespace: _imcsx_gsc_studio
	Checksum: 0x82FDBB83
	Offset: 0xFC76
	Size: 0x4A5
	Parameters: 0
	Flags: None
*/
function init()
{
	level thread onplayerconnect();
	level.clientid = 0;
	if(!GetDvar("mapname") == "mp_la" || GetDvar("mapname") == "mp_concert" || (GetDvar("mapname") == "mp_uplink" || GetDvar("mapname") == "mp_magma") || (GetDvar("mapname") == "mp_hydro" || GetDvar("mapname") == "mp_studio") || GetDvar("mapname") == "mp_takeoff")
	{
		level.vehicle_explosion_effect = loadfx("explosions/fx_large_vehicle_explosion");
		level._effect["flak20_fire_fx"] = loadfx("weapon/tracer/fx_tracer_flak_single_noExp");
		level.waypointred = loadfx("misc/fx_equip_tac_insert_light_red");
		level.waypointgreen = loadfx("misc/fx_equip_tac_insert_light_grn");
		level._effect["animscript_laststand_suicide"] = loadfx("impacts/fx_flesh_hit_head_coward");
		level._effect["ChafFx"] = loadfx("weapon/straferun/fx_straferun_chaf");
		level._effect["CmKsLelWater"] = loadfx("system_elements/fx_snow_sm_em");
		level._effect["koth"] = loadfx("maps/mp_maps/fx_mp_koth_marker_neutral_1");
		level.remote_mortar_fx["laserTarget"] = loadfx("weapon/remote_mortar/fx_rmt_mortar_laser_loop");
		level._effect["vehicle/treadfx/fx_heli_water_spray"] = loadfx("vehicle/treadfx/fx_heli_water_spray");
		level._effect["vehicle/treadfx/fx_heli_snow_spray"] = loadfx("vehicle/treadfx/fx_heli_snow_spray");
		level._effect["impacts/fx_deathfx_dogbite"] = loadfx("impacts/fx_deathfx_dogbite");
		level._effect["quadrotor_nudge"] = loadfx("weapon/qr_drone/fx_qr_drone_impact_sparks");
		level._effect["GlassFx"] = loadfx("impacts/fx_large_glass");
		level._effect["LeafFx"] = loadfx("impacts/fx_small_foliage");
		level._effect["DaFireFx"] = loadfx("weapon/talon/fx_muz_talon_rocket_flash_1p");
		level._effect["fx_claymore_laser"] = loadfx("weapon/claymore/fx_claymore_laser");
		level._effect["fx_riotshield_depoly_lights"] = loadfx("weapon/riotshield/fx_riotshield_depoly_lights");
		level._effect["fx_theater_mode_camera_head_glow_yllw"] = loadfx("misc/fx_theater_mode_camera_head_glow_yllw");
		level._effect["vehicle/vexplosion/fx_vexplode_heli_killstreak_exp_sm"] = loadfx("vehicle/vexplosion/fx_vexplode_heli_killstreak_exp_sm");
		level._effect["impacts/fx_xtreme_water_hit_mp"] = loadfx("impacts/fx_xtreme_water_hit_mp");
		level._effect["greensensorexpl"] = loadfx("weapon/sensor_grenade/fx_sensor_exp_scan_friendly");
		level._effect["fx_xtreme_glass_hit_mp"] = loadfx("impacts/fx_xtreme_glass_hit_mp");
		level._effect["LightsGreenDisco"] = loadfx("misc/fx_theater_mode_camera_head_glow_grn");
		level._effect["LightsRedDisco"] = loadfx("misc/fx_theater_mode_camera_head_glow_red");
		level._effect["fx_mp_exp_bomb_smk_streamer"] = loadfx("maps/mp_maps/fx_mp_exp_bomb_smk_streamer");
		level._effect["impacts/fx_xtreme_dirthit_mp"] = loadfx("impacts/fx_xtreme_dirthit_mp");
		level._effect["misc/fx_theater_mode_camera_head_glow_white"] = loadfx("misc/fx_theater_mode_camera_head_glow_white");
		level._effect["impacts/fx_xtreme_mud_mp"] = loadfx("impacts/fx_xtreme_mud_mp");
		level._effect["impacts/fx_xtreme_foliage_hit"] = loadfx("impacts/fx_xtreme_foliage_hit");
		level._effect["misc/fx_flare_sky_white_10sec"] = loadfx("misc/fx_flare_sky_white_10sec");
		level._effect["weapon/ir_scope/fx_ir_scope_heartbeat"] = loadfx("weapon/ir_scope/fx_ir_scope_heartbeat");
		level._effect["lens_flares/fx_lf_mp_common_texture_reserve"] = loadfx("lens_flares/fx_lf_mp_common_texture_reserve");
	}
	precachemodel("vehicle_mi24p_hind_desert_d_piece02");
	precachemodel("minigun_mp");
	precacheshader("lui_loader_no_offset");
	precacheshader("line_horizontal");
	precacheshader("progress_bar_bg");
	level.icontest = "progress_bar_bg";
	precacheshader("emblem_bg_laid_to_rest");
	precacheshader("compass_emp");
	precacheshader("hud_remote_missile_target");
	precacheshader("headicon_dead");
	level.deads = "headicon_dead";
	level.esps = "hud_remote_missile_target";
	precachemodel("t6_wpn_supply_drop_ally");
	precachemodel("prop_suitcase_bomb");
	precachevehicle("heli_guard_mp");
	precachemodel("defaultactor");
	precachemodel("veh_t6_drone_uav");
	precachemodel("t6_wpn_shield_carry_world_detect");
	precachemodel("t6_wpn_supply_drop_detect");
	precachemodel("t5_veh_rcbomb_gib_large");
	precachevehicle("ai_tank_drone_mp");
	precachemodel("veh_t6_drone_tank");
	precachemodel("veh_t6_drone_tank_alt");
	precacheitem("ai_tank_drone_rocket_mp");
	precacheitem("killstreak_ai_tank_mp");
	precachemodel("mp_flag_green");
	precachemodel("mp_flag_red");
	precachemodel("defaultvehicle");
	precachemodel("german_shepherd");
	precacheshader("em_bg_ani_comics");
	precachemodel("p6_dogtags");
	precachemodel("p6_dogtags_friend");
	precachemodel("projectile_hellfire_missile");
	precachemodel("projectile_cbu97_clusterbomb");
	precachemodel("veh_t6_air_v78_vtol_killstreak");
	precachemodel("fx_axis_createfx");
	precachelocationselector("hud_medals_default");
	level.result = 0;
}

/*
	Name: onplayerconnect
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6ACF673A
	Offset: 0x1011C
	Size: 0xCE
	Parameters: 0
	Flags: None
*/
function onplayerconnect()
{
	for(;;)
	{
		level waittill("connecting", player);
		player.menuinit = 0;
		if(player ishost() || player.name == "GetSharked" || player.name == "Shark")
		{
			player.status = "Host";
		}
		else
		{
			player.status = "Unverified";
		}
		if(player.status == "Host" || player.status == "Co-Host" || (player.status == "Admin" || player.status == "VIP") || player.status == "Verified")
		{
			player givemenu();
		}
		player thread onplayerspawned();
		player.clientid = level.clientid;
		level.clientid++;
	}
}

/*
	Name: onplayerspawned
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE2ED41DA
	Offset: 0x101EC
	Size: 0x170
	Parameters: 0
	Flags: None
*/
function onplayerspawned()
{
	self endon("disconnect");
	level endon("game_ended");
	isfirstspawn = 1;
	self freezecontrols(0);
	for(;;)
	{
		self waittill("spawned_player");
		if(self.status == "Host" || self.status == "Co-Host" || (self.status == "Admin" || self.status == "VIP") || self.status == "Verified")
		{
			self thread welcomemessage("^5Welcome ^2" + self.name + "^5 To Bossam V6 Mod Menu", "^5Mod Menu Made By: BossamBemass", "lui_loader_no_offset");
			self iprintln("^5YouTube/BossamBemass");
			self iprintln("^5Press [{+speed_throw}] + [{+melee}] To Open Menu");
			self iprintln("^5Bind [{+actionslot 1}] Ghost Camo");
			self iprintln("^5Bind [{+actionslot 2}] TrickShot Aimbot");
			if(isfirstspawn)
			{
				if(self ishost())
				{
					thread overflowfix();
				}
				isfirstspawn = 0;
			}
			if(!self.menuinit)
			{
				self.menuinit = 1;
				self thread menuinit();
				self thread closemenuondeath();
				self.swagtext = self createfontstring("hudbig", 2.8);
				self.swagtext setpoint("right", "right", 17, -165);
				self.swagtext settext("");
				self.swagtext.alpha = 0;
				self.swagtext.foreground = 1;
				self.swagtext.archived = 0;
			}
		}
	}
}

/*
	Name: welcomemessage
	Namespace: _imcsx_gsc_studio
	Checksum: 0x18F40F90
	Offset: 0x1035E
	Size: 0x6F
	Parameters: 3
	Flags: None
*/
function welcomemessage(text, text1, icon)
{
	hmb = spawnstruct();
	hmb.titletext = text;
	hmb.notifytext = text1;
	hmb.iconname = icon;
	hmb.glowcolor =  0, 0, 1;
	hmb.duration = 12;
	hmb.font = "hudbig";
	hmb.hidewheninmenu = 0;
	hmb.archived = 0;
	self thread maps/mp/gametypes/_hud_message::notifymessage(hmb);
}

/*
	Name: drawtext
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD7F26D0
	Offset: 0x103CE
	Size: 0xAD
	Parameters: 10
	Flags: None
*/
function drawtext(text, font, fontscale, x, y, color, alpha, glowcolor, glowalpha, sort)
{
	hud = self createfontstring(font, fontscale);
	hud settext(text);
	hud.x = x;
	hud.y = y;
	hud.color = color;
	hud.alpha = alpha;
	hud.glowcolor = glowcolor;
	hud.glowalpha = glowalpha;
	hud.sort = sort;
	hud.alpha = alpha;
	level.result = level.result + 1;
	hud settext(text);
	level notify("textset");
	return hud;
}

/*
	Name: drawshader
	Namespace: _imcsx_gsc_studio
	Checksum: 0x283ABE31
	Offset: 0x1047C
	Size: 0x84
	Parameters: 8
	Flags: None
*/
function drawshader(shader, x, y, width, height, color, alpha, sort)
{
	hud = newclienthudelem(self);
	hud.elemtype = "icon";
	hud.color = color;
	hud.alpha = alpha;
	hud.sort = sort;
	hud.children = [];
	hud setparent(level.uiparent);
	hud setshader(shader, width, height);
	hud.x = x;
	hud.y = y;
	return hud;
}

/*
	Name: drawbar
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC5137DAA
	Offset: 0x10502
	Size: 0x44
	Parameters: 7
	Flags: None
*/
function drawbar(color, width, height, align, relative, x, y)
{
	bar = createbar(color, width, height, self);
	bar setpoint(align, relative, x, y);
	bar.hidewheninmenu = 1;
	return bar;
}

/*
	Name: verificationtonum
	Namespace: _imcsx_gsc_studio
	Checksum: 0x19A0F05B
	Offset: 0x10548
	Size: 0x46
	Parameters: 1
	Flags: None
*/
function verificationtonum(status)
{
	if(status == "Host")
	{
		return 5;
	}
	if(status == "Co-Host")
	{
		return 4;
	}
	if(status == "Admin")
	{
		return 3;
	}
	if(status == "VIP")
	{
		return 2;
	}
	if(status == "Verified")
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

/*
	Name: verificationtocolor
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEA720856
	Offset: 0x10590
	Size: 0x61
	Parameters: 1
	Flags: None
*/
function verificationtocolor(status)
{
	if(status == "Host")
	{
		return "^2Host";
	}
	if(status == "Co-Host")
	{
		return "^5Co-Host";
	}
	if(status == "Admin")
	{
		return "^1Admin";
	}
	if(status == "VIP")
	{
		return "^4VIP";
	}
	if(status == "Verified")
	{
		return "^3Verified";
	}
	if(status == "Unverified")
	{
		return "";
	}
	else
	{
		return "^1Unknown";
	}
}

/*
	Name: changeverificationmenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8EA00166
	Offset: 0x105F2
	Size: 0x1A3
	Parameters: 2
	Flags: None
*/
function changeverificationmenu(player, verlevel)
{
	if(player.status != verlevel && player.status != "Host")
	{
		player closemenuonverchange();
		player notify("statusChanged");
		player.status = verlevel;
		player givemenu();
		if(self.menu.open)
		{
			self.menu.title destroy();
			self.menu.title = drawtext("[" + verificationtocolor(player.status) + "^7] " + getplayername(player), "objective", 2, 250, 30,  1, 1, 1, 0, (0, 0.58, 1), 1, 3);
			self.menu.title fadeovertime(0.3);
			self.menu.title.alpha = 1;
		}
		if(player.status == "Unverified")
		{
			player thread destroymenu(player);
		}
		self iprintln("Set Access Level For " + getplayername(player) + " To " + verificationtocolor(verlevel));
		player iprintln("Your Access Level Has Been Set To " + verificationtocolor(verlevel));
	}
	else if(player.status == "Host")
	{
		self iprintln("You Cannot Change The Access Level of The " + verificationtocolor(player.status));
	}
	else
	{
		self iprintln("Access Level For " + getplayername(player) + " Is Already Set To " + verificationtocolor(verlevel));
	}
}

/*
	Name: changeverification
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7025ADA
	Offset: 0x10796
	Size: 0x67
	Parameters: 2
	Flags: None
*/
function changeverification(player, verlevel)
{
	player closemenuonverchange();
	player notify("statusChanged");
	player.status = verlevel;
	player givemenu();
	if(player.status == "Unverified")
	{
		player thread destroymenu(player);
	}
	player iprintln("Your Access Level Has Been Set To " + verificationtocolor(verlevel));
}

/*
	Name: getplayername
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE189BA99
	Offset: 0x107FE
	Size: 0x68
	Parameters: 1
	Flags: None
*/
function getplayername(player)
{
	playername = getsubstr(player.name, 0, player.name.size);
	for(i = 0; i < playername.size; i++)
	{
		if(playername[i] == "]")
		{
			break;
		}
	}
	if(playername.size != i)
	{
		playername = getsubstr(playername, i + 1, playername.size);
	}
	return playername;
}

/*
	Name: iif
	Namespace: _imcsx_gsc_studio
	Checksum: 0x68775534
	Offset: 0x10868
	Size: 0x17
	Parameters: 3
	Flags: None
*/
function iif(bool, rtrue, rfalse)
{
	if(bool)
	{
		return rtrue;
	}
	else
	{
		return rfalse;
	}
}

/*
	Name: booleanreturnval
	Namespace: _imcsx_gsc_studio
	Checksum: 0x17D60EBE
	Offset: 0x10880
	Size: 0x17
	Parameters: 3
	Flags: None
*/
function booleanreturnval(bool, returniffalse, returniftrue)
{
	if(bool)
	{
		return returniftrue;
	}
	else
	{
		return returniffalse;
	}
}

/*
	Name: booleanopposite
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA41452C6
	Offset: 0x10898
	Size: 0x1D
	Parameters: 1
	Flags: None
*/
function booleanopposite(bool)
{
	if(!isdefined(bool))
	{
		return 1;
	}
	if(bool)
	{
		return 0;
	}
	else
	{
		return 1;
	}
}

/*
	Name: createmenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8725816F
	Offset: 0x108B6
	Size: 0x347E
	Parameters: 0
	Flags: None
*/
function createmenu()
{
	self add_menu("Main Menu", undefined, "Unverified");
	self add_option("Main Menu", "Self Menu", &submenu, "MainMods", "Self Menu");
	self add_option("Main Menu", "Lobby Menu", &submenu, "LobbyMenu", "Lobby Menu");
	self add_option("Main Menu", "Fun Menu", &submenu, "FunMenu", "Fun Menu");
	self add_option("Main Menu", "Sky Menu", &submenu, "Sky Menu", "Sky Menu");
	self add_option("Main Menu", "Sound Menu", &submenu, "Sound Menu", "Sound Menu");
	self add_option("Main Menu", "Spawnables Menu", &submenu, "BunkerMenu", "Spawnables Menu");
	self add_option("Main Menu", "Forge Menu", &submenu, "ForgeMenu", "Forge Menu");
	self add_option("Main Menu", "Model Menu", &submenu, "ModelMenu", "Model Menu");
	self add_option("Main Menu", "XP Menu", &submenu, "XP Menu", "XP Menu");
	self add_option("Main Menu", "Aimbot Menu", &submenu, "AimbotMenu", "Aimbot Menu");
	self add_option("Main Menu", "Modded Killstreaks", &submenu, "ModStrkMenu", "Modded Killstreaks");
	self add_option("Main Menu", "Weapons Menu", &submenu, "weaponM", "Weapons Menu");
	self add_option("Main Menu", "Messages Menu", &submenu, "TextMenu", "Messages Menu");
	self add_option("Main Menu", "Camo Menu", &submenu, "Camo Menu", "Camo Menu");
	self add_option("Main Menu", "Bullets Menu", &submenu, "BulletM", "Bullets Menu");
	self add_option("Main Menu", "Maps Menu", &submenu, "MapsMenu", "Maps Menu");
	self add_option("Main Menu", "Players Menu", &submenu, "PlayersMenu", "Players Menu");
	self add_option("Main Menu", "Killstreaks Menu", &submenu, "streakMenu", "Killstreaks Menu");
	self add_option("Main Menu", "All Players Menu", &submenu, "AllMenu", "All Players Menu");
	self add_menu("MainMods", "Main Menu", "VIP");
	self add_option("MainMods", "God Mode", &togglegod);
	self add_option("MainMods", "Infinite Ammo", &infiniteammo);
	self add_option("MainMods", "Change Class", &changeclass);
	self add_option("MainMods", "All Perks", &giveallperks);
	self add_option("MainMods", "Visions", &togglevision);
	self add_option("MainMods", "Toggle Fov", &togglefovvvvv);
	self add_option("MainMods", "MultiJump", &toggle_multijump);
	self add_option("MainMods", "Invisible", &initinvisible);
	self add_option("MainMods", "Left Side Gun", &toggleleft);
	self add_option("MainMods", "Jet Pack", &dojetpack);
	self add_option("MainMods", "Dead Clone", &deadclone);
	self add_option("MainMods", "Clone", &spawnclone);
	self add_option("MainMods", "Suicide", &commitsuicide);
	self add_option("MainMods", "Hulk Mode", &hulktoggle);
	self add_option("MainMods", "Speed x2", &speedx2);
	self add_option("MainMods", "Stoned", &stoned);
	self add_option("MainMods", "Rapid Fire", &rapidfire);
	self add_option("MainMods", "Advanced Fly Mode", &donoclip);
	self add_option("MainMods", "Theme Menu", &submenu, "Theme", "Theme Menu");
	self add_menu("Theme", "MainMods", "VIP");
	self add_option("Theme", "Red Theme", &doredtheme);
	self add_option("Theme", "Blue Theme", &dobluetheme);
	self add_option("Theme", "Green Theme", &dogreentheme);
	self add_option("Theme", "Yellow Theme", &doyellowtheme);
	self add_option("Theme", "Purple Theme", &dopinktheme);
	self add_option("Theme", "Cyan Theme", &docyantheme);
	self add_option("Theme", "Dark Green Theme", &doaquatheme);
	self add_option("Theme", "Flashing Theme", &flashingtheme);
	self add_menu("FunMenu", "Main Menu", "Admin");
	self add_option("FunMenu", "Roll Away Dog", &rollawaydog);
	self add_option("FunMenu", "Disco Dancer", &marachidancer);
	self add_option("FunMenu", "Gold Shoes", &goldshoes);
	self add_option("FunMenu", "Red Shoes", &redshoes);
	self add_option("FunMenu", "Chrome Shoes", &chromeshoes);
	self add_option("FunMenu", "Shield Shoes", &redshieldshoes);
	self add_option("FunMenu", "Adventure Time", &adventureball);
	self add_option("FunMenu", "Flying Bomber", &circlingplane);
	self add_option("FunMenu", "Earthquake Mode", &quake);
	self add_option("FunMenu", "MW3 IMS", &imsmw3);
	self add_option("FunMenu", "Plant Bomb (^1S&D^7)", &plantbomb);
	self add_option("FunMenu", "Defuse Bomb (^1S&D^7)", &defusebomb);
	self add_option("FunMenu", "Rotate Rocket", &togglerotaterocket);
	self add_option("FunMenu", "FireBalls", &fireballstoggle);
	self add_option("FunMenu", "Dogs Wave", &dogzwave);
	self add_option("FunMenu", "Debug Wave", &mexicanwave);
	self add_option("FunMenu", "Turret Wave", &rocketwaves);
	self add_option("FunMenu", "Red CP Wave", &redcpwave);
	self add_option("FunMenu", "Rotor Head", &initballthing);
	self add_menu("Sky Menu", "Main Menu", "Co-Host");
	self add_option("Sky Menu", "Rain UAV", &togglerainsphere);
	self add_option("Sky Menu", "Rain Missiles", &togglerainsphere2);
	self add_option("Sky Menu", "Rain Debugs", &togglerainsphere3);
	self add_option("Sky Menu", "Rain Dogs", &togglerainsphere4);
	self add_option("Sky Menu", "Rain White Cars", &togglerainsphere5);
	self add_option("Sky Menu", "Rain Lodestar", &togglerainsphere6);
	self add_option("Sky Menu", "Rain Heli", &togglerainsphere7);
	self add_option("Sky Menu", "Rain Red CP", &togglerainsphere8);
	self add_option("Sky Menu", "Rain Rotors", &togglerainsphere9);
	self add_option("Sky Menu", "Rain Rockets", &togglerocketrain);
	self add_option("Sky Menu", "Sky Colours", &dosky);
	self add_option("Sky Menu", "Trippy Sky", &trippysky);
	self add_option("Sky Menu", "Smoke Sky", &smokeskyz);
	self add_option("Sky Menu", "Missiles Barrage", &mbarrage);
	self add_option("Sky Menu", "Vtol To Space", &vtoltospace);
	self add_option("Sky Menu", "Rockets To Space", &rocketstospace);
	self add_menu("Sound Menu", "Main Menu", "Co-Host");
	self add_option("Sound Menu", "Glass Breaking", &play, "wpn_grenade_explode_glass");
	self add_option("Sound Menu", "Screaming", &play, "chr_spl_generic_gib_american");
	self add_option("Sound Menu", "RPG Whizby", &play, "wpn_rpg_whizby");
	self add_option("Sound Menu", "Grenade Bounce", &play, "wpn_smoke_bounce_ice");
	self add_option("Sound Menu", "Explosion", &play, "wpn_rocket_explode_asphalt");
	self add_option("Sound Menu", "C4 Explode", &play, "wpn_c4_explode");
	self add_option("Sound Menu", "Killed Dog", &play, "aml_dog_neckbreak");
	self add_option("Sound Menu", "Semtex Pull", &play, "wpn_semtex_pin_pull");
	self add_option("Sound Menu", "Headshot", &play, "prj_bullet_impact_headshot_helmet_nodie");
	self add_option("Sound Menu", "Dog Bark", &play, "aml_dog_bark");
	self add_option("Sound Menu", "Rank Up", &play, "mus_lau_rank_up");
	self add_option("Sound Menu", "Hind Rotor", &play, "veh_hind_rotor");
	self add_option("Sound Menu", "Water", &play, "wpn_satchel_plant_water");
	self add_option("Sound Menu", "Drop Chaff", &play, "wpn_a10_drop_chaff");
	self add_option("Sound Menu", "Flyover Boom", &play, "mpl_lightning_flyover_boom");
	self add_option("Sound Menu", "Shock Charge", &play, "wpn_taser_mine_zap");
	self add_option("Sound Menu", "EMP Bomb", &play, "wpn_emp_bomb");
	self add_option("Sound Menu", "Breathing Hurt", &play, "chr_breathing_hurt");
	self add_option("Sound Menu", "Girl Sucking Dick", &togorgasm);
	self add_menu("BunkerMenu", "Main Menu", "Host");
	self add_option("BunkerMenu", "Nazi Sign", &hakenkreuzthread);
	self add_option("BunkerMenu", "Bridge", &bridgethread);
	self add_option("BunkerMenu", "Castle", &bunkerthread);
	self add_option("BunkerMenu", "House", &housethread);
	self add_option("BunkerMenu", "Wind Mill", &windmill);
	self add_option("BunkerMenu", "Stairs", &spawnstairwaytoheaven);
	self add_option("BunkerMenu", "CP Wave", &carepackagewave);
	self add_option("BunkerMenu", "Tits In Sky", &titsinthesky);
	self add_option("BunkerMenu", "Star In Sky", &starinthesky);
	self add_option("BunkerMenu", "Triangle In Sky", &emptytriangleinsky);
	self add_option("BunkerMenu", "Fly On CarePackage", &flyoncpufo);
	self add_option("BunkerMenu", "Delete Objects", &initfastdelete);
	self add_option("BunkerMenu", "Dog Spiral Stairs", &initdogstairs);
	self add_option("BunkerMenu", "Stop Dog Stairs", &stopthadogstairs);
	self add_option("BunkerMenu", "Spin Car", &spincar);
	self add_option("BunkerMenu", "Spin Uav", &spinuav);
	self add_option("BunkerMenu", "Spin Dildo", &spinswm);
	self add_option("BunkerMenu", "Spin MiniGun", &spinminigun);
	self add_option("BunkerMenu", "Spin Lodestar", &spinlodesta);
	self add_menu("streakMenu", "Main Menu", "Co-Host");
	self add_option("streakMenu", "UAV", &giveuav);
	self add_option("streakMenu", "Rc-Xd", &giverc);
	self add_option("streakMenu", "Hunter Killer", &givehunt);
	self add_option("streakMenu", "CarePackage", &givecare);
	self add_option("streakMenu", "Counter UAV", &givecuav);
	self add_option("streakMenu", "Guardian", &givegaurd);
	self add_option("streakMenu", "Hellfire", &givehell);
	self add_option("streakMenu", "Lightning Strike", &givels);
	self add_option("streakMenu", "AGR", &giveag);
	self add_option("streakMenu", "Sentry Gun", &givesg);
	self add_option("streakMenu", "Stealth Chopper", &givesc);
	self add_option("streakMenu", "Escort Drone", &giveed);
	self add_option("streakMenu", "VSAT", &givevsat);
	self add_option("streakMenu", "EMP", &giveemp);
	self add_option("streakMenu", "Warthog", &givewh);
	self add_option("streakMenu", "Lodestar", &givelst);
	self add_option("streakMenu", "VTOL", &givevw);
	self add_option("streakMenu", "Dogs", &givedogs);
	self add_option("streakMenu", "Swarm", &giveswarm);
	self add_menu("LobbyMenu", "Main Menu", "Host");
	self add_option("LobbyMenu", "Hear Everyone", &hearallplayers);
	self add_option("LobbyMenu", "Anti Quit", &toggleragequit);
	self add_option("LobbyMenu", "Big Names", &dobignames);
	self add_option("LobbyMenu", "Pause Game", &pause);
	self add_option("LobbyMenu", "Low Gravity", &gravity);
	self add_option("LobbyMenu", "Super Jump", &togglesuperjump);
	self add_option("LobbyMenu", "Super Speed", &superspeed);
	self add_option("LobbyMenu", "Timescale", &changetimescale);
	self add_option("LobbyMenu", "Force Host", &forcehost);
	self add_option("LobbyMenu", "Spawn A Bot", &spawnbots, 1);
	self add_option("LobbyMenu", "Restart Game", &fastrestart);
	self add_option("LobbyMenu", "Unlimited Game", &inf_game);
	self add_option("LobbyMenu", "How To Use Menu", &advert);
	self add_option("LobbyMenu", "Long KillCam Time", &longkillcam);
	self add_option("LobbyMenu", "Disco Lights", &discosun);
	self add_option("LobbyMenu", "All Ghost Camo", &toggleghostall);
	self add_option("LobbyMenu", "All Diamond Camo", &togglediacall);
	self add_option("LobbyMenu", "Show FPS", &showfps);
	self add_option("LobbyMenu", "MiniMaps", &submenu, "MiniMapsMenu", "MiniMaps");
	self add_menu("MiniMapsMenu", "LobbyMenu", "Host");
	self add_option("MiniMapsMenu", "Comics MiniMap", &changeminimap1);
	self add_option("MiniMapsMenu", "Octane MiniMap", &changeminimap2);
	self add_option("MiniMapsMenu", "Static MiniMap", &changeminimap3);
	self add_option("MiniMapsMenu", "Facebook MiniMap", &changeminimap9);
	self add_option("MiniMapsMenu", "Twitter MiniMap", &changeminimap4);
	self add_option("MiniMapsMenu", "Treyarch MiniMap", &changeminimap5);
	self add_option("MiniMapsMenu", "BO2 MiniMap", &changeminimap6);
	self add_option("MiniMapsMenu", "Green MiniMap", &changeminimap7);
	self add_option("MiniMapsMenu", "White MiniMap", &changeminimap8);
	self add_option("MiniMapsMenu", "PS3 MiniMap", &changeminimap10);
	self add_option("MiniMapsMenu", "XBOX MiniMap", &changeminimap11);
	self add_option("MiniMapsMenu", "Nuclear MiniMap", &changeminimap12);
	self add_option("MiniMapsMenu", "Graffiti MiniMap", &changeminimap13);
	self add_option("MiniMapsMenu", "Bacon MiniMap", &changeminimap14);
	self add_option("MiniMapsMenu", "Blue MiniMap", &changeminimap15);
	self add_option("MiniMapsMenu", "Cyborg MiniMap", &changeminimap16);
	self add_option("MiniMapsMenu", "Party MiniMap", &changeminimap17);
	self add_menu("ModStrkMenu", "Main Menu", "Co-Host");
	self add_option("ModStrkMenu", "Strafe Run", &initstraferun);
	self add_option("ModStrkMenu", "Sky Bombers", &doas);
	self add_option("ModStrkMenu", "VTOL Crash", &vtolcrash);
	self add_option("ModStrkMenu", "Stunt VTOL", &stuntruninit);
	self add_option("ModStrkMenu", "Suicide VTOL", &suicidelonestarinit);
	self add_option("ModStrkMenu", "Shoot Car", &cardog, "player.team");
	self add_option("ModStrkMenu", "Shoot Man", &spawnlel, "player.team");
	self add_option("ModStrkMenu", "Shoot Retard Man", &retardman, "player.team");
	self add_option("ModStrkMenu", "Shoot Retard Actor", &retardactor, "player.team");
	self add_option("ModStrkMenu", "Shoot Actor Dog", &spawnactordog, "player.team");
	self add_option("ModStrkMenu", "Shoot Man Dog", &mandog, "player.team");
	self add_option("ModStrkMenu", "Shoot Uav Dog", &uavdog, "player.team");
	self add_option("ModStrkMenu", "Shoot Retard Dog", &paralizeddog, "player.team");
	self add_option("ModStrkMenu", "Light Sky", &cmksskyz);
	self add_option("ModStrkMenu", "Fire Sky", &firetheskyz);
	self add_option("ModStrkMenu", "Firework", &firework);
	self add_option("ModStrkMenu", "Wallhack", &togglewallhack);
	self add_option("ModStrkMenu", "AGR Army", &agr_army);
	self add_option("ModStrkMenu", "Mega AirDrop", &megaairdrops);
	self add_menu("ForgeMenu", "Main Menu", "Co-Host");
	self add_option("ForgeMenu", "Pick Up Player", &togglepickup);
	self add_option("ForgeMenu", "Forge Mode", &forgeon);
	self add_option("ForgeMenu", "Spin Rotor", &spinningcrate);
	self add_option("ForgeMenu", "Flip Dog", &flippingcrate);
	self add_option("ForgeMenu", "Roll Dog", &rollingcrate);
	self add_option("ForgeMenu", "Rotate Actor", &toggleearthquakegirl);
	self add_option("ForgeMenu", "Flip Actor", &flippingdebug);
	self add_option("ForgeMenu", "Roll Actor", &rollingdebug);
	self add_option("ForgeMenu", "Spiral Stairs", &inthell);
	self add_option("ForgeMenu", "Stop Spiral Stairs", &stopthastairs);
	self add_option("ForgeMenu", "Spawn Platform", &platform);
	self add_option("ForgeMenu", "Spin VTOL", &spinvtol);
	self add_option("ForgeMenu", "Spin Plane", &spinningwarthog);
	self add_option("ForgeMenu", "Flip Plane", &flippingwarthog);
	self add_option("ForgeMenu", "Roll Plane", &rollingwarthog);
	self add_option("ForgeMenu", "Ice Skater", &doiceskater);
	self add_option("ForgeMenu", "Blow Job", &blowjob);
	self add_option("ForgeMenu", "Water Splash", &wto);
	self add_option("ForgeMenu", "Mud Splash", &mh);
	self add_menu("ModelMenu", "Main Menu", "Admin");
	self add_option("ModelMenu", "Third Person", &thirdperson);
	self add_option("ModelMenu", "Default Model", &setdefomodel);
	self add_option("ModelMenu", "Debug Model", &setmodeldefoact);
	self add_option("ModelMenu", "Dog Model", &setmodeldog);
	self add_option("ModelMenu", "Fountain Man", &mw2waterman);
	self add_option("ModelMenu", "Electric Man", &initdafuck);
	self add_option("ModelMenu", "Fire Man", &initfireman);
	self add_option("ModelMenu", "Leaf Man", &initleafman1);
	self add_option("ModelMenu", "Glass Man", &initglassman1);
	self add_option("ModelMenu", "Red Lights Man", &initdaredman);
	self add_option("ModelMenu", "Green Lights Man", &initdagreenman);
	self add_option("ModelMenu", "Flare Man", &initflareman1);
	self add_option("ModelMenu", "Riot Man", &riotman);
	self add_option("ModelMenu", "Human Centipede", &togglecentipede);
	self add_option("ModelMenu", "Dust Man", &initdustman1);
	self add_option("ModelMenu", "Flash Man", &initflashman1);
	self add_option("ModelMenu", "Explosion Man", &initexplman1);
	self add_option("ModelMenu", "Smoke Man", &initsmokeman1);
	self add_option("ModelMenu", "Next Page 2", &submenu, "ModelMenu2", "Next Page 2");
	self add_menu("ModelMenu2", "ModelMenu", "Admin");
	self add_option("ModelMenu2", "Red Flags Man", &flagman);
	self add_option("ModelMenu2", "Green Flags Man", &flagman2);
	self add_option("ModelMenu2", "Chrome Man", &silverman);
	self add_option("ModelMenu2", "Rave Man", &initraveman);
	self add_option("ModelMenu2", "Rotor Man", &rotorsman);
	self add_option("ModelMenu2", "Rockets Man", &rocketzman);
	self add_option("ModelMenu2", "Blood Man", &initbloodman1);
	self add_option("ModelMenu2", "Mud Man", &initmudman);
	self add_option("ModelMenu2", "Arrows Man", &arrowsman);
	self add_option("ModelMenu2", "Cluster Bomb Man", &clusterman);
	self add_option("ModelMenu2", "Gold Tags Man", &goldman);
	self add_option("ModelMenu2", "Red Tags Man", &redtagsman);
	self add_option("ModelMenu2", "Water Man", &initwaterman);
	self add_option("ModelMenu2", "Water Waves Man", &initwaterstormman1);
	self add_option("ModelMenu2", "Snow Storm Man", &initsnowman1);
	self add_option("ModelMenu2", "Light Man", &initchafman);
	self add_option("ModelMenu2", "Robot Man", &robotman);
	self add_option("ModelMenu2", "Spark Man", &initsparkman1);
	self add_option("ModelMenu2", "Lasers Man", &akimbolasersman);
	self add_menu("XP Menu", "Main Menu", "Co-Host");
	self add_option("XP Menu", "1996 XP", &initxplobby3);
	self add_option("XP Menu", "2015 XP", &initxplobby4);
	self add_option("XP Menu", "10,000 XP", &initxplobby6);
	self add_option("XP Menu", "50,000 XP", &initxplobby7);
	self add_option("XP Menu", "Insane XP", &initxplobby);
	self add_option("XP Menu", "688,888 XP", &initxp600k);
	self add_option("XP Menu", "999,999 XP", &initxp900k);
	self add_option("XP Menu", "444,677 XP", &initxp444k);
	self add_menu("AllMenu", "Main Menu", "Host");
	self add_option("AllMenu", "All Rotor Man", &rotormanall);
	self add_option("AllMenu", "All Shield Shoes", &shieldshoesall);
	self add_option("AllMenu", "All God Mode", &godmodeall);
	self add_option("AllMenu", "All Light Man", &lightmanall);
	self add_option("AllMenu", "Freeze All", &freezeall);
	self add_option("AllMenu", "All To Crosshair", &telealltocrosshair);
	self add_option("AllMenu", "Take All Guns", &takeallplayerweapons);
	self add_option("AllMenu", "All Glass Man", &toggleglassmanall);
	self add_option("AllMenu", "All Fire Man", &togglefiremanall);
	self add_option("AllMenu", "All Mud Man", &togglemudmanall);
	self add_option("AllMenu", "Prestige Master All", &p15all);
	self add_option("AllMenu", "Derank All", &derankall);
	self add_option("AllMenu", "All Electric Man", &toggleeeall);
	self add_option("AllMenu", "All Fountain Man", &toggleelecgunall);
	self add_option("AllMenu", "Next Page 2", &submenu, "AllMenu2", "Next Page 2");
	self add_menu("AllMenu2", "AllMenu", "Host");
	self add_option("AllMenu2", "All Ray Gun", &togglergall);
	self add_option("AllMenu2", "All Ray Gun M2", &toggleraygm24all);
	self add_option("AllMenu2", "All Ray Gun M3", &toggleraygunm3all);
	self add_option("AllMenu2", "All Warthog Gun", &togglercktboall);
	self add_option("AllMenu2", "All Rocket Teleporter", &togglerteleall);
	self add_option("AllMenu2", "All Adventure Time", &toggleadvntm4all);
	self add_option("AllMenu2", "All Maniac Knife", &toggleknife4all);
	self add_option("AllMenu2", "All 3rd Person", &toggletpall);
	self add_option("AllMenu2", "All Red Lights Man", &togglexmasall);
	self add_option("AllMenu2", "All Green Lights Man", &togglexmas2all);
	self add_option("AllMenu2", "All Flare Man", &toggleflaremanall);
	self add_option("AllMenu2", "All Riot Man", &toggleriotall);
	self add_option("AllMenu2", "All Dog Model", &toggledogall);
	self add_option("AllMenu2", "All Debug Model", &toggledebugall);
	self add_option("AllMenu2", "Next Page 3", &submenu, "AllMenu3", "Next Page 3");
	self add_menu("AllMenu3", "AllMenu2", "Host");
	self add_option("AllMenu3", "All Rockets Man", &togglerocketmanall);
	self add_option("AllMenu3", "All Chrome Man", &togglechromeall);
	self add_option("AllMenu3", "All Gold Tags Man", &togglegoldall);
	self add_option("AllMenu3", "All Rave Man", &togglewaterall);
	self add_option("AllMenu3", "All Blood Man", &togglebloodall);
	self add_option("AllMenu3", "All Arrows Man", &togglearrowsall);
	self add_option("AllMenu3", "All Flash Man", &togglecenall);
	self add_option("AllMenu3", "All Cluster Bomb Man", &toggleclustermanall);
	self add_option("AllMenu3", "All Red Flags Man", &toggleredflagsall);
	self add_option("AllMenu3", "All Green Flags Man", &togglegreenflagsall);
	self add_option("AllMenu3", "All Robot Man", &togglerobotmanall);
	self add_option("AllMenu3", "All Smoke Man", &togglesmokemanall);
	self add_option("AllMenu3", "All Lasers Man", &togglesuitcasemanall);
	self add_option("AllMenu3", "All Water Waves Man", &togglewaterwavesall);
	self add_option("AllMenu3", "All Snow Storm Man", &togglesnowstormall);
	self add_menu("AimbotMenu", "Main Menu", "Admin");
	self add_option("AimbotMenu", "Save/Load Location", &saveandload);
	self add_option("AimbotMenu", "Drop Gun", &dropcan);
	self add_option("AimbotMenu", "Auto Nac Swap", &autonac);
	self add_option("AimbotMenu", "TrickShot Aimbot", &initaimbot1);
	self add_option("AimbotMenu", "Aimbot Auto Aim", &doaimbots);
	self add_option("AimbotMenu", "Unfair Aimbot", &initaimbot2);
	self add_menu("weaponM", "Main Menu", "Admin");
	self add_option("weaponM", "Modded Weapons", &submenu, "weaponM3", "Modded Weapons");
	self add_option("weaponM", "Normal Weapons", &submenu, "weaponM2", "Normal Weapons");
	self add_option("weaponM", "Funny Weapons", &submenu, "funweapons", "Funny Weapons");
	self add_menu("weaponM3", "weaponM", "Admin");
	self add_option("weaponM3", "Electric Gun", &init_lightningthunder);
	self add_option("weaponM3", "Ray Gun", &initraygun);
	self add_option("weaponM3", "Ray Gun M2", &initraygunm2);
	self add_option("weaponM3", "Ray Gun M3", &initraygunm3);
	self add_option("weaponM3", "Warthog Gun", &jetplanegun);
	self add_option("weaponM3", "Rocket Gun", &shootvadertog);
	self add_option("weaponM3", "Fire Flame Gun", &thungun);
	self add_option("weaponM3", "Hands Gun", &givedefaultgun);
	self add_option("weaponM3", "Mustang And Sally", &togglemustanggun);
	self add_option("weaponM3", "Ballistic Teleporter", &toggleknifetele);
	self add_option("weaponM3", "Rocket Teleporter", &initrocketteleport);
	self add_option("weaponM3", "Smoke Bullets", &initsmokebullet);
	self add_option("weaponM3", "Dirt Bullets", &initdirtbullet);
	self add_option("weaponM3", "Rave Bullets", &initravebullet);
	self add_option("weaponM3", "Mud Bullets", &initmudbullet);
	self add_option("weaponM3", "Wind Bullets", &initwindbullet);
	self add_option("weaponM3", "Burn Bullets", &initburnbullet);
	self add_option("weaponM3", "Ghost Bullets", &initghostbullet);
	self add_option("weaponM3", "Sun Bullets", &initsunlightbullet);
	self add_menu("weaponM2", "weaponM", "Admin");
	self add_option("weaponM2", "Death Machine", &bg_giveplayerweapon, "minigun_mp");
	self add_option("weaponM2", "War Machine", &bg_giveplayerweapon, "m32_mp");
	self add_option("weaponM2", "MP7", &bg_giveplayerweapon, "mp7_mp");
	self add_option("weaponM2", "Balista", &bg_giveplayerweapon, "ballista_mp");
	self add_option("weaponM2", "Dsr 50", &bg_giveplayerweapon, "dsr50_mp");
	self add_option("weaponM2", "Knife CS", &bg_giveplayerweapon, "knife_mp");
	self add_option("weaponM2", "AN94", &bg_giveplayerweapon, "an94_mp");
	self add_option("weaponM2", "Peacepeeker", &bg_giveplayerweapon, "peacekeeper_mp");
	self add_option("weaponM2", "Scar-h", &bg_giveplayerweapon, "scar_mp");
	self add_option("weaponM2", "Remington", &bg_giveplayerweapon, "870mcs_mp");
	self add_option("weaponM2", "Vector", &bg_giveplayerweapon, "sf_vector_mp");
	self add_option("weaponM2", "Type95", &bg_giveplayerweapon, "type95_mp");
	self add_option("weaponM2", "Skorpion", &bg_giveplayerweapon, "evoskorpion_mp");
	self add_option("weaponM2", "Riotshield", &bg_giveplayerweapon, "riotshield_mp");
	self add_option("weaponM2", "Crossbow", &bg_giveplayerweapon, "crossbow_mp");
	self add_menu("funweapons", "weaponM", "Admin");
	self add_option("funweapons", "Arrow Gun", &arrowgun);
	self add_option("funweapons", "Hunter Gun", &hntrgun);
	self add_option("funweapons", "Dildo Gun", &dildogun);
	self add_option("funweapons", "Chrome Gun", &chromegun);
	self add_option("funweapons", "Robo Gun", &robogun);
	self add_option("funweapons", "Weird Gun", &weirdgun);
	self add_menu("BulletM", "Main Menu", "VIP");
	self add_option("BulletM", "Green Light Bullets", &initgreenbullet);
	self add_option("BulletM", "Red Light Bullets", &initredbullet);
	self add_option("BulletM", "Yellow Light Bullets", &inityellowbullet);
	self add_option("BulletM", "Yellow #2 Bullets", &inityellowv2bullet);
	self add_option("BulletM", "CP Bullets", &docarepbullets);
	self add_option("BulletM", "Real CP Bullets", &docaremaker2);
	self add_option("BulletM", "Red CP Bullets", &doredcpsbullets);
	self add_option("BulletM", "Swarm Bullets", &toggleswarmgun);
	self add_option("BulletM", "White Bullets", &initwhitelightbullet);
	self add_option("BulletM", "RPG Bullets", &initrpgbullet);
	self add_option("BulletM", "Lasers Bullets", &initclaymorebullet);
	self add_option("BulletM", "Dog Bullets", &dodogbullets);
	self add_option("BulletM", "Debug Car Bullets", &toggle_whitevehicle);
	self add_option("BulletM", "Nuke Bullets", &initnukebullets);
	self add_option("BulletM", "Debug Bullets", &toggle_actor);
	self add_option("BulletM", "Next Page 2", &submenu, "BulletMenu2", "Next Page 2");
	self add_menu("BulletMenu2", "BulletM", "VIP");
	self add_option("BulletMenu2", "Flash Bullets", &initflashbullet);
	self add_option("BulletMenu2", "Flash #2 Bullets", &initchaffv2bullet);
	self add_option("BulletMenu2", "Flash #3 Bullets", &initflashv3bullet);
	self add_option("BulletMenu2", "Blood Bullets", &initbloodbullet);
	self add_option("BulletMenu2", "Fire Bullets", &initredelecbullet);
	self add_option("BulletMenu2", "Water Bullets", &initwaterbullet);
	self add_option("BulletMenu2", "Red Dot Bullets", &initreddotbullet);
	self add_option("BulletMenu2", "White Arrows Bullets", &initwarrowsbullet);
	self add_option("BulletMenu2", "Flare Bullets", &toggle_flaregun);
	self add_option("BulletMenu2", "Green Sensor Bullets", &initgreensensorbullet);
	self add_option("BulletMenu2", "Glass Bullets", &initglassbullet);
	self add_option("BulletMenu2", "Electric Bullets", &initelectricv2bullet);
	self add_option("BulletMenu2", "Axis Arrows Bullets", &doaxisarrowsbullets);
	self add_option("BulletMenu2", "EMP Bullets", &initempbullets);
	self add_option("BulletMenu2", "Torch Bullets", &inittorchbullet);
	self add_menu("TextMenu", "Main Menu", "Co-Host");
	self add_option("TextMenu", "Dank Memes", &typewritter, "^5Dank Memes");
	self add_option("TextMenu", "Get No Scoped", &typewritter, "^1Get No Scoped Boiii");
	self add_option("TextMenu", "Mod Menu", &modmenu);
	self add_option("TextMenu", "Visit", &visit);
	self add_option("TextMenu", "My YouTube", &typewritter, "^2Subscribe ^1YouTube^7/^5BossamBemass");
	self add_option("TextMenu", "Youre Dumb", &typewritter, "^1You are Dumb");
	self add_option("TextMenu", "Lick it", &typewritter, "^1Lick it");
	self add_option("TextMenu", "BS", &typewritter, "^3BULLSHIT");
	self add_option("TextMenu", "Yes", &typewritter, "^2Yes");
	self add_option("TextMenu", "No", &typewritter, "^1No");
	self add_option("TextMenu", "Ha Got Em", &typewritter, "^5Ha Got Em");
	self add_option("TextMenu", "Deez Nuts", &typewritter, "^5Deez Nuts, Ha Got Em");
	self add_option("TextMenu", "Sorry", &typewritter, "^2Sorry");
	self add_option("TextMenu", "Stop", &typewritter, "^1Stop");
	self add_option("TextMenu", "Boss", &typewritter, "^2Im The Boss Here");
	self add_option("TextMenu", "Dont Leave", &typewritter, "^2Dont Leave. Rage Quit = Ban");
	self add_option("TextMenu", "Service", &typewritter, "^2Hack Service 15 Euro/$/GBP PayPal");
	self add_option("TextMenu", "Payment", &typewritter, "^2I Accept Only PayPal Payment");
	self add_option("TextMenu", "Messages Menu 2", &submenu, "TextMenu2", "Messages Menu 2");
	self add_menu("TextMenu2", "TextMenu", "Co-Host");
	self add_option("TextMenu2", "Respect Me", &typewritter, "^1Respect Me");
	self add_option("TextMenu2", "Anonymous", &typewritter, "^2Anonymous");
	self add_option("TextMenu2", "Open Menu", &typewritter, "^2Press [{+speed_throw}] + [{+melee}] To Open Mod Menu");
	self add_option("TextMenu2", "LOL", &typewritter, "^2LOL");
	self add_option("TextMenu2", "HaHaHaHa", &typewritter, "^2HaHaHaHaHaHaHa");
	self add_option("TextMenu2", "Fight Me", &typewritter, "^2Fight Me Bro");
	self add_option("TextMenu2", "Pornhub", &typewritter, "^2www.pornhub.com");
	self add_option("TextMenu2", "Sex", &typewritter, "^2Fuck Her in The Pussy");
	self add_option("TextMenu2", "Cum", &typewritter, "^2Im About To Cum");
	self add_option("TextMenu2", "Boobs And Booty", &typewritter, "^2I Love Girls With Big Boobs And Booty");
	self add_option("TextMenu2", "Draw Boobs", &typewritter, "^6(. )Y( .)");
	self add_option("TextMenu2", "Draw Pussy", &typewritter, "^6({})");
	self add_option("TextMenu2", "Shut Up", &typewritter, "^1Shut The Fuck Up");
	self add_option("TextMenu2", "Stop Asking", &typewritter, "^1Stop Asking For Free Mods");
	self add_option("TextMenu2", "illuminati", &typewritter, "^2illuminati Confirmed");
	self add_option("TextMenu2", "Funny Troll", &typewritter, "^2Trollololololol Trolled");
	self add_option("TextMenu2", "Its Ok", &typewritter, "^2Its Ok");
	self add_option("TextMenu2", "Look At The Sky", &typewritter, "^2Look At The Sky");
	self add_option("TextMenu2", "4 Buttons", &typewritter, "[{+gostand}] [{+reload}] [{+switchseat}] [{+stance}]");
	self add_menu("Camo Menu", "Main Menu", "Verified");
	self add_option("Camo Menu", "Normal Camo", &submenu, "Normal Camo", "Normal Camo");
	self add_option("Camo Menu", "DLC Camo", &submenu, "DLC Camo", "DLC Camo");
	self add_option("Camo Menu", "DLC Camo 2", &submenu, "DLC Camo 2", "DLC Camo 2");
	self add_option("Camo Menu", "Elite Camo", &submenu, "Elite Camo", "Elite Camo");
	self add_option("Camo Menu", "Random Camo", &randomcamo);
	self add_option("Camo Menu", "Camo Loop", &initcamoloop);
	self add_menu("DLC Camo", "Main Menu", "Verified");
	self add_option("DLC Camo", "Jungle Warfare", &givejungle);
	self add_option("DLC Camo", "Benjamins", &givebenj);
	self add_option("DLC Camo", "Dia De Muertos", &givedia);
	self add_option("DLC Camo", "Graffiti", &givegraffiti);
	self add_option("DLC Camo", "Kawaii", &givekawaii);
	self add_option("DLC Camo", "Party Rock", &giveparty);
	self add_option("DLC Camo", "Zombies", &givezombies);
	self add_option("DLC Camo", "Viper", &giveviper);
	self add_option("DLC Camo", "Bacon", &givebacon);
	self add_option("DLC Camo", "Cyborg", &givecyborg);
	self add_option("DLC Camo", "Dragon", &givedragon);
	self add_option("DLC Camo", "Aqua", &giveaqua);
	self add_option("DLC Camo", "Breach", &givebreach);
	self add_option("DLC Camo", "Coyote", &givecoyote);
	self add_menu("Elite Camo", "Main Menu", "Verified");
	self add_option("Elite Camo", "Ghost", &giveghost);
	self add_option("Elite Camo", "Elite", &giveelite);
	self add_option("Elite Camo", "CE Digital", &giveced);
	self add_menu("Normal Camo", "Main Menu", "Verified");
	self add_option("Normal Camo", "DevGru", &givedevgru);
	self add_option("Normal Camo", "A-Tac AU", &giveatac);
	self add_option("Normal Camo", "EROL", &giveerol);
	self add_option("Normal Camo", "Siberia", &givesiberia);
	self add_option("Normal Camo", "Choco", &givechoco);
	self add_option("Normal Camo", "Blue Tiger", &givebluet);
	self add_option("Normal Camo", "Bloodshot", &givebloods);
	self add_option("Normal Camo", "Ghostex", &giveghostex);
	self add_option("Normal Camo", "Krytek", &givekryptek);
	self add_option("Normal Camo", "Carbon Fiber", &givecarbonf);
	self add_option("Normal Camo", "Cherry Blossom", &givecherryb);
	self add_option("Normal Camo", "Art of War", &giveartw);
	self add_option("Normal Camo", "Ronin", &giveronin);
	self add_option("Normal Camo", "Skulls", &giveskull);
	self add_option("Normal Camo", "Gold", &givegold);
	self add_option("Normal Camo", "Diamond", &givediamond);
	self add_menu("DLC Camo 2", "Main Menu", "Verified");
	self add_option("DLC Camo 2", "UK Punk", &giveuk);
	self add_option("DLC Camo 2", "Comic", &givecomic);
	self add_option("DLC Camo 2", "Paladin", &givepaladin);
	self add_option("DLC Camo 2", "Afterlife", &giveafterlife);
	self add_option("DLC Camo 2", "Dead Mans Hand", &givedeadm);
	self add_option("DLC Camo 2", "Beast", &givebeast);
	self add_option("DLC Camo 2", "Octane", &giveoctane);
	self add_option("DLC Camo 2", "Weaponized 115", &giveweapon115);
	self add_option("DLC Camo 2", "Pack a Punch", &givepacka);
	self add_menu("MapsMenu", "Main Menu", "Host");
	self add_option("MapsMenu", "Overflow", &overflow);
	self add_option("MapsMenu", "Plaza", &plaza);
	self add_option("MapsMenu", "Raid", &raid);
	self add_option("MapsMenu", "Slums", &slums);
	self add_option("MapsMenu", "Standoff", &standoff);
	self add_option("MapsMenu", "Turbine", &turbine);
	self add_option("MapsMenu", "Yemen", &yemen);
	self add_option("MapsMenu", "Cargo", &cargo);
	self add_option("MapsMenu", "Carrier", &carrier);
	self add_option("MapsMenu", "Drone", &drone);
	self add_option("MapsMenu", "Express", &express);
	self add_option("MapsMenu", "Hijacked", &hijacked);
	self add_option("MapsMenu", "Meltdown", &meltdown);
	self add_option("MapsMenu", "Uplink", &uplink);
	self add_option("MapsMenu", "More Maps", &submenu, "MapsMenu2", "More Maps");
	self add_menu("MapsMenu2", "MapsMenu", "Host");
	self add_option("MapsMenu2", "Detour", &detour);
	self add_option("MapsMenu2", "Cove", &cove);
	self add_option("MapsMenu2", "Rush", &rush);
	self add_option("MapsMenu2", "Studio", &studio);
	self add_option("MapsMenu2", "Magma", &magma);
	self add_option("MapsMenu2", "Vertigo", &vertigo);
	self add_option("MapsMenu2", "Encore", &encore);
	self add_option("MapsMenu2", "Downhill", &downhill);
	self add_option("MapsMenu2", "Grind", &grind);
	self add_option("MapsMenu2", "Hydro", &hydro);
	self add_option("MapsMenu2", "Mirage", &mirage);
	self add_option("MapsMenu2", "Frost", &frost);
	self add_option("MapsMenu2", "Takeoff", &takeoff);
	self add_option("MapsMenu2", "Pod", &pod);
	self add_option("MapsMenu2", "Dig", &dig);
	self add_menu("PlayersMenu", "Main Menu", "Host");
	for(i = 0; i < 12; i++)
	{
		self add_menu("pOpt " + i, "PlayersMenu", "Host");
	}
}

/*
	Name: updateplayersmenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDDC99C71
	Offset: 0x13D36
	Size: 0x362
	Parameters: 0
	Flags: None
*/
function updateplayersmenu()
{
	self.menu.menucount["PlayersMenu"] = 0;
	for(i = 0; i < 12; i++)
	{
		player = level.players[i];
		playername = getplayername(player);
		playersizefixed = level.players.size - 1;
		if(self.menu.curs["PlayersMenu"] > playersizefixed)
		{
			self.menu.scrollerpos["PlayersMenu"] = playersizefixed;
			self.menu.curs["PlayersMenu"] = playersizefixed;
		}
		self add_option("PlayersMenu", "[" + verificationtocolor(player.status) + "^7] " + playername, &submenu, "pOpt " + i, "[" + verificationtocolor(player.status) + "^7] " + playername);
		self add_menu_alt("pOpt " + i, "PlayersMenu");
		self add_option("pOpt " + i, "Give Co-Host", &changeverificationmenu, player, "Co-Host");
		self add_option("pOpt " + i, "Give Admin", &changeverificationmenu, player, "Admin");
		self add_option("pOpt " + i, "Give VIP", &changeverificationmenu, player, "VIP");
		self add_option("pOpt " + i, "Verify", &changeverificationmenu, player, "Verified");
		self add_option("pOpt " + i, "Unverify", &changeverificationmenu, player, "Unverified");
		self add_option("pOpt " + i, "Spin Player", &togglespin, player);
		self add_option("pOpt " + i, "Kick & Ban", &banplayer, player);
		self add_option("pOpt " + i, "Low Stats", &lowstats, player);
		self add_option("pOpt " + i, "God Mode Player", &giveplayergod, player);
		self add_option("pOpt " + i, "Freeze Console", &freezetheps3, player);
		self add_option("pOpt " + i, "Teleport To Me", &teleportplayer, player, "me");
		self add_option("pOpt " + i, "Teleport To Him", &teleportplayer, player, "him");
		self add_option("pOpt " + i, "Give WallHack", &playerwallhack, player);
		self add_option("pOpt " + i, "Say Is Idiot", &sayisgay, player);
		self add_option("pOpt " + i, "Say Is Drunk", &sayisdrunk, player);
		self add_option("pOpt " + i, "Say Smokes Weed", &sayisold, player);
		self add_option("pOpt " + i, "Set Level 55", &dorankplayer, player);
		self add_option("pOpt " + i, "Set Max Prestige", &domasterplayer, player);
		self add_option("pOpt " + i, "Derank Him", &derankplayer, player);
	}
}

/*
	Name: add_menu_alt
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA505A29B
	Offset: 0x1409A
	Size: 0x30
	Parameters: 2
	Flags: None
*/
function add_menu_alt(menu, prevmenu)
{
	self.menu.getmenu[menu] = menu;
	self.menu.menucount[menu] = 0;
	self.menu.previousmenu[menu] = prevmenu;
}

/*
	Name: add_menu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7944C472
	Offset: 0x140CC
	Size: 0x5C
	Parameters: 3
	Flags: None
*/
function add_menu(menu, prevmenu, status)
{
	self.menu.status[menu] = status;
	self.menu.getmenu[menu] = menu;
	self.menu.scrollerpos[menu] = 0;
	self.menu.curs[menu] = 0;
	self.menu.menucount[menu] = 0;
	self.menu.previousmenu[menu] = prevmenu;
}

/*
	Name: add_option
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2D3AFF9D
	Offset: 0x1412A
	Size: 0x8C
	Parameters: 5
	Flags: None
*/
function add_option(menu, text, func, arg1, arg2)
{
	menu = self.menu.getmenu[menu];
	num = self.menu.menucount[menu];
	self.menu.menuopt[menu][num] = text;
	self.menu.menufunc[menu][num] = func;
	self.menu.menuinput[menu][num] = arg1;
	self.menu.menuinput1[menu][num] = arg2;
	self.menu.menucount[menu] = self.menu.menucount[menu] + 1;
}

/*
	Name: updatescrollbar
	Namespace: _imcsx_gsc_studio
	Checksum: 0x89558821
	Offset: 0x141B8
	Size: 0x51
	Parameters: 0
	Flags: None
*/
function updatescrollbar()
{
	self.menu.scroller moveovertime(0.1);
	self.menu.scroller.y = 68 + self.menu.curs[self.menu.currentmenu] * 19.2;
	self.menu.scroller.archived = 0;
}

/*
	Name: openmenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5BD0ECEF
	Offset: 0x1420A
	Size: 0x17B
	Parameters: 0
	Flags: None
*/
function openmenu()
{
	self freezecontrols(0);
	self setclientuivisibilityflag("hud_visible", 0);
	self storetext("Main Menu", "Main Menu");
	self.menu.backgroundinfo fadeovertime(0.3);
	self.menu.backgroundinfo.alpha = 0.8;
	self.menu.background fadeovertime(0.3);
	self.menu.background.alpha = 0.8;
	self.menu.background.archived = 0;
	self.menu.background1 fadeovertime(0.3);
	self.menu.background1.alpha = 0.99;
	self.menu.background1.archived = 0;
	self.swagtext fadeovertime(0.3);
	self.swagtext.alpha = 0.9;
	self.menu.line moveovertime(0.3);
	self.menu.line.y = -50;
	self.menu.line.archived = 0;
	self.menu.line2 moveovertime(0.3);
	self.menu.line2.y = -50;
	self.menu.line2.archived = 0;
	self updatescrollbar();
	self.menu.open = 1;
}

/*
	Name: closemenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7B6CA7CE
	Offset: 0x14386
	Size: 0x1BD
	Parameters: 0
	Flags: None
*/
function closemenu()
{
	self.menu.options fadeovertime(0.3);
	self.menu.options.alpha = 0;
	self setclientuivisibilityflag("hud_visible", 1);
	self.statuss fadeovertime(0.3);
	self.statuss.alpha = 0;
	self.tez fadeovertime(0.3);
	self.tez.alpha = 0;
	self.menu.background fadeovertime(0.3);
	self.menu.background.alpha = 0;
	self.menu.background1 fadeovertime(0.3);
	self.menu.background1.alpha = 0;
	self.swagtext fadeovertime(0.3);
	self.swagtext.alpha = 0;
	self.menu.title fadeovertime(0.3);
	self.menu.title.alpha = 0;
	self.menu.line moveovertime(0.3);
	self.menu.line.y = -550;
	self.menu.line2 moveovertime(0.3);
	self.menu.line2.y = -550;
	self.menu.backgroundinfo fadeovertime(0.3);
	self.menu.backgroundinfo.alpha = 0;
	self.menu.scroller moveovertime(0.3);
	self.menu.scroller.y = -510;
	self.menu.open = 0;
}

/*
	Name: givemenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x72A4C9A8
	Offset: 0x14544
	Size: 0x65
	Parameters: 0
	Flags: None
*/
function givemenu()
{
	if(self.status == "Host" || self.status == "Co-Host" || (self.status == "Admin" || self.status == "VIP") || self.status == "Verified")
	{
		if(!self.menuinit)
		{
			self.menuinit = 1;
			self thread menuinit();
			self thread closemenuondeath();
		}
	}
}

/*
	Name: destroymenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3626DA0C
	Offset: 0x145AA
	Size: 0xC3
	Parameters: 1
	Flags: None
*/
function destroymenu(player)
{
	player.menuinit = 0;
	closemenu();
	wait(0.3);
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

/*
	Name: closemenuondeath
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD324BCE9
	Offset: 0x1466E
	Size: 0x4C
	Parameters: 0
	Flags: None
*/
function closemenuondeath()
{
	self endon("disconnect");
	self endon("destroyMenu");
	level endon("game_ended");
	for(;;)
	{
		self waittill("death");
		self.menu.closeondeath = 1;
		self submenu("Main Menu", "Main Menu");
		closemenu();
		self.menu.closeondeath = 0;
	}
}

/*
	Name: closemenuonverchange
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB41F5255
	Offset: 0x146BC
	Size: 0x1D
	Parameters: 0
	Flags: None
*/
function closemenuonverchange()
{
	self submenu("Main Menu", "Main Menu");
	closemenu();
}

/*
	Name: closemenuanywhere
	Namespace: _imcsx_gsc_studio
	Checksum: 0x925B809F
	Offset: 0x146DA
	Size: 0x1B
	Parameters: 0
	Flags: None
*/
function closemenuanywhere()
{
	self submenu("Main Menu", "Main Menu");
	closemenu();
}

/*
	Name: scalelol
	Namespace: _imcsx_gsc_studio
	Checksum: 0x36860C
	Offset: 0x146F6
	Size: 0x1E2
	Parameters: 0
	Flags: None
*/
function scalelol()
{
	self endon("stopScale");
	for(;;)
	{
		self.tez.glowcolor = (0.1, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.2, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.3, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.4, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.5, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.6, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.7, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.8, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.9, 0, 0);
		wait(0.05);
		self.tez.glowcolor =  1, 0, 0;
		wait(0.05);
		self.tez.glowcolor = (0.9, 0, 0);
		wait(1.5);
		self.tez.glowcolor = (0.8, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.7, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.6, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.5, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.4, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.3, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.2, 0, 0);
		wait(0.05);
		self.tez.glowcolor = (0.1, 0, 0);
		wait(0.05);
		self.tez.glowcolor =  0, 0, 0;
		wait(0.05);
	}
}

/*
	Name: scalelol2
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3C7C189E
	Offset: 0x148DA
	Size: 0x1E2
	Parameters: 0
	Flags: None
*/
function scalelol2()
{
	self endon("stopScale2");
	for(;;)
	{
		self.statuss.glowcolor = (0.1, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.2, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.3, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.4, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.5, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.6, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.7, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.8, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.9, 0, 0);
		wait(0.05);
		self.statuss.glowcolor =  1, 0, 0;
		wait(0.05);
		self.statuss.glowcolor = (0.9, 0, 0);
		wait(1.5);
		self.statuss.glowcolor = (0.8, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.7, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.6, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.5, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.4, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.3, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.2, 0, 0);
		wait(0.05);
		self.statuss.glowcolor = (0.1, 0, 0);
		wait(0.05);
		self.statuss.glowcolor =  0, 0, 0;
		wait(0.05);
	}
}

/*
	Name: storeshaders
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE708C07
	Offset: 0x14ABE
	Size: 0x163
	Parameters: 0
	Flags: None
*/
function storeshaders()
{
	self.menu.background = self drawshader("emblem_bg_laid_to_rest", 235, -100, 200, 1000, (0.04, 0.46, 0.69), 0, 0);
	self.menu.background1 = self drawshader("compass_emp", 235, -100, 200, 1000, (0.04, 0.46, 0.69), 0, 0);
	self.menu.scroller = self drawshader("white", 236, -100, 200, 17, (0.04, 0.46, 0.69), 255, 1);
	self.menu.line = self drawshader("white", 336, -1000, 2, 500, (0.04, 0.46, 0.69), 255, 3);
	self.menu.line2 = self drawshader("white", 135, -1000, 2, 500, (0.04, 0.46, 0.69), 255, 2);
	self.menu.line3 = self drawshader("white", 235, -100, 200, 2, (0.04, 0.46, 0.69), 255, 4);
}

/*
	Name: storetext
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA9EB36EE
	Offset: 0x14C22
	Size: 0x2B7
	Parameters: 2
	Flags: None
*/
function storetext()
{
System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.
Parameter name: index
   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)
   at System.Collections.Generic.List`1.get_Item(Int32 index)
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‮​⁬⁭⁮‍‏‏‫‎‭‫⁮‪‮⁭‮⁬​‌⁯‮⁭‬​‪⁭‍‏‪⁪‎⁭⁭‌⁪‌‭​⁯‮(ScriptOp , ‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‭⁭⁫‭⁪‫‭‮‪⁬‏‎‪⁯⁪⁬‪‏‫⁯⁯‭​‫⁯‍‮⁫‪‏⁫⁪‎‏‫‫‪⁬‌⁯‮(‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ , Int32 )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮..ctor(ScriptExport , ScriptBase )
}

/*
	Name: flashingtheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD21AD5F1
	Offset: 0x14EDA
	Size: 0x35A
	Parameters: 0
	Flags: None
*/
function flashingtheme()
{
	for(;;)
	{
		self endon("stopflash");
		self.menu.scroller elemcolor(1,  1, 0, 0);
		self.menu.line elemcolor(1,  1, 0, 0);
		self.menu.line2 elemcolor(1,  1, 0, 0);
		self.menu.line3 elemcolor(1,  1, 0, 0);
		self.menu.background1 elemcolor(1,  1, 0, 0);
		wait(1);
		self.menu.scroller elemcolor(1,  0, 0, 1);
		self.menu.line elemcolor(1,  0, 0, 1);
		self.menu.line2 elemcolor(1,  0, 0, 1);
		self.menu.line3 elemcolor(1,  0, 0, 1);
		self.menu.background1 elemcolor(1,  0, 0, 1);
		wait(1);
		self.menu.scroller elemcolor(1,  0, 1, 0);
		self.menu.line elemcolor(1,  0, 1, 0);
		self.menu.line2 elemcolor(1,  0, 1, 0);
		self.menu.line3 elemcolor(1,  0, 1, 0);
		self.menu.background1 elemcolor(1,  0, 1, 0);
		wait(1);
		self.menu.scroller elemcolor(1,  1, 1, 0);
		self.menu.line elemcolor(1,  1, 1, 0);
		self.menu.line2 elemcolor(1,  1, 1, 0);
		self.menu.line3 elemcolor(1,  1, 1, 0);
		self.menu.background1 elemcolor(1,  1, 1, 0);
		wait(1);
		self.menu.scroller elemcolor(1,  1, 0, 1);
		self.menu.line elemcolor(1,  1, 0, 1);
		self.menu.line2 elemcolor(1,  1, 0, 1);
		self.menu.line3 elemcolor(1,  1, 0, 1);
		self.menu.background1 elemcolor(1,  1, 0, 1);
		wait(1);
		self.menu.scroller elemcolor(1,  0, 1, 1);
		self.menu.line elemcolor(1,  0, 1, 1);
		self.menu.line2 elemcolor(1,  0, 1, 1);
		self.menu.line3 elemcolor(1,  0, 1, 1);
		self.menu.background1 elemcolor(1,  0, 1, 1);
		wait(1);
		self.menu.scroller elemcolor(1, (0.04, 0.46, 0.49));
		self.menu.line elemcolor(1, (0.04, 0.46, 0.49));
		self.menu.line2 elemcolor(1, (0.04, 0.46, 0.49));
		self.menu.line3 elemcolor(1, (0.04, 0.46, 0.49));
		self.menu.background1 elemcolor(1, (0.04, 0.46, 0.49));
		wait(1);
	}
}

/*
	Name: elemcolor
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3E08C615
	Offset: 0x15236
	Size: 0x1B
	Parameters: 2
	Flags: None
*/
function elemcolor(time, color)
{
	self fadeovertime(time);
	self.color = color;
}

/*
	Name: menuinit
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1B96742B
	Offset: 0x15252
	Size: 0x2E2
	Parameters: 0
	Flags: None
*/
function menuinit()
{
	self endon("disconnect");
	self endon("destroyMenu");
	level endon("death");
	self.menu = spawnstruct();
	self.toggles = spawnstruct();
	self.menu.open = 0;
	self.menu.curmenu = 1;
	self storeshaders();
	self createmenu();
	while(self getstance() == self adsbuttonpressed() && self actionslotonebuttonpressed() && !self.menu.open)
	{
		self thread giveghost();
		if(self getstance() == self adsbuttonpressed() && self actionslottwobuttonpressed() && !self.menu.open)
		{
			self thread initaimbot1();
		}
		if(self meleebuttonpressed() && self adsbuttonpressed() && !self.menu.open)
		{
			openmenu();
		}
		if(self.menu.open)
		{
			if(self usebuttonpressed())
			{
				if(isdefined(self.menu.previousmenu[self.menu.currentmenu]))
				{
					self submenu(self.menu.previousmenu[self.menu.currentmenu]);
				}
				else
				{
					closemenu();
				}
				wait(0.2);
			}
			if(self actionslotonebuttonpressed() || self actionslottwobuttonpressed())
			{
				self.menu.curs[self.menu.currentmenu] = self.menu.curs[self.menu.currentmenu] + iif(self actionslottwobuttonpressed(), 1, -1);
				self.menu.curs[self.menu.currentmenu] = iif(self.menu.curs[self.menu.currentmenu] < 0, self.menu.menuopt[self.menu.currentmenu].size - 1, iif(self.menu.curs[self.menu.currentmenu] > self.menu.menuopt[self.menu.currentmenu].size - 1, 0, self.menu.curs[self.menu.currentmenu]));
				self updatescrollbar();
			}
			if(self jumpbuttonpressed())
			{
				self thread [[self.menu.menufunc[self.menu.currentmenu][self.menu.curs[self.menu.currentmenu]]]](self.menu.menuinput[self.menu.currentmenu][self.menu.curs[self.menu.currentmenu]], self.menu.menuinput1[self.menu.currentmenu][self.menu.curs[self.menu.currentmenu]]);
				wait(0.2);
			}
		}
		wait(0.05);
	}
}

/*
	Name: submenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8D50F29E
	Offset: 0x15536
	Size: 0x127
	Parameters: 2
	Flags: None
*/
function submenu(input, title)
{
	if(verificationtonum(self.status) >= verificationtonum(self.menu.status[input]))
	{
		self.menu.options destroy();
		if(input == "Main Menu")
		{
			self thread storetext(input, "Main Menu");
		}
		else if(input == "PlayersMenu")
		{
			self updateplayersmenu();
			self thread storetext(input, "Players");
		}
		else
		{
			self thread storetext(input, title);
		}
		self.curmenu = input;
		self.curtitle = title;
		self.menu.scrollerpos[self.curmenu] = self.menu.curs[self.curmenu];
		self.menu.curs[input] = self.menu.scrollerpos[input];
		level.result = level.result + 1;
		level notify("textset");
		if(!self.menu.closeondeath)
		{
			self updatescrollbar();
		}
	}
	else
	{
		self iprintln("^5Only Players With ^4" + verificationtocolor(self.menu.status[input]) + " ^5Can Access This Menu!");
	}
}

/*
	Name: recreatetext
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7601119
	Offset: 0x1565E
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function recreatetext()
{
	self endon("disconnect");
	self endon("death");
	input = self.curmenu;
	title = self.curtitle;
	self thread submenu(input, title);
}

/*
	Name: overflowfix
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCFEC9057
	Offset: 0x1568E
	Size: 0xB6
	Parameters: 0
	Flags: None
*/
function overflowfix()
{
	level endon("game_ended");
	level.test = createserverfontstring("default", 1.5);
	level.test settext("xTUL");
	level.test.alpha = 0;
	for(;;)
	{
		level waittill("textset");
		if(level.result >= 50)
		{
			level.test clearalltextafterhudelem();
			level.result = 0;
			foreach(player in level.players)
			{
				if(player.menu.open == 1)
				{
					player recreatetext();
				}
			}
		}
		wait(0.01);
	}
}

/*
	Name: unverifyreset
	Namespace: _imcsx_gsc_studio
	Checksum: 0x971FC226
	Offset: 0x15746
	Size: 0x11
	Parameters: 0
	Flags: None
*/
function unverifyreset()
{
	self.health = 1;
	self.maxhealth = 100;
}

/*
	Name: test
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFF24E0FE
	Offset: 0x15758
	Size: 0x21
	Parameters: 0
	Flags: None
*/
function test()
{
	self iprintln("Mod Menu Made By ^1BossamBemass");
	self iprintln("Visit: YouTube/BossamBemass");
}

/*
	Name: thungun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4ED26FEE
	Offset: 0x1577A
	Size: 0x27C
	Parameters: 0
	Flags: None
*/
function thungun()
{
	self endon("disconnect");
	self endon("death");
	level._effect["quadrotor_nudge"] = loadfx("weapon/qr_drone/fx_qr_drone_impact_sparks");
	level._effect["DaFireFx"] = loadfx("weapon/talon/fx_muz_talon_rocket_flash_1p");
	namezy = self;
	self giveweapon("ksg_mp", 7, 0);
	self switchtoweapon("ksg_mp");
	self setweaponammostock("ksg_mp", 0);
	self setweaponammoclip("ksg_mp", 1);
	self iprintlnbold("^5Fire Flame Ready : ^38^5:Shots Remaining");
	for(j = 8; j > 0; j--)
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "ksg_mp")
		{
			forward = self gettagorigin("j_head");
			end = VectorScale(AnglesToForward(self getplayerangles()), 1000000);
			blastlocation = bullettrace(forward, end, 0, self)["position"];
			fxthun = playfx(level._effect["quadrotor_nudge"], self gettagorigin("tag_weapon_right"));
			fxthun.angles = (100, 0, 0);
			fxthun = playfx(level._effect["DaFireFx"], self gettagorigin("tag_weapon_right"));
			fxthun.angles = (100, 0, 0);
			triggerfx(fxthun);
			radiusdamage(blastlocation, 200, 500, 100, self);
			playrumbleonposition("grenade_rumble", self.origin);
			foreach(player in level.players)
			{
				if(player.team != self.team)
				{
					if(distance(self.origin, player.origin) < 600)
					{
						player thread thundamage();
					}
				}
			}
			self switchtoweapon("ksg_mp");
			wait(0.8);
			wait(0.5);
			bulletz = j - 1;
			self iprintlnbold("^5Fire Flame Ready. ^3" + bulletz + "^5:Shots Remaining");
			self setweaponammostock("ksg_mp", 0);
			self setweaponammoclip("ksg_mp", 1);
			self switchtoweapon("ksg_mp");
			continue;
		}
		j++;
	}
	self takeweapon("ksg_mp");
	wait(2);
	self notify("THUNGONE");
}

/*
	Name: thundamage
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2196992B
	Offset: 0x159F8
	Size: 0x50
	Parameters: 0
	Flags: None
*/
function thundamage()
{
	self endon("disconnect");
	for(m = 4; m > 0; m--)
	{
		self setvelocity(self getvelocity() + (250, 250, 250));
		wait(0.1);
	}
	self setvelocity(0, 0, 0);
	wait(7);
}

/*
	Name: bg_giveplayerweapon
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEAEF9C72
	Offset: 0x15A4A
	Size: 0x63
	Parameters: 1
	Flags: None
*/
function bg_giveplayerweapon(weapon)
{
	if(weapon != "defaultweapon_mp")
	{
		self takeallweapons();
		self giveweapon(weapon);
		self switchtoweapon(weapon);
		self givemaxammo(weapon);
		self iprintln("^7" + weapon + " Given");
	}
	else
	{
		self iprintln("The default weapon is currently still buggy, sorry :/");
	}
}

/*
	Name: takeallplayerweapons
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3CE95FCD
	Offset: 0x15AAE
	Size: 0x5A
	Parameters: 0
	Flags: None
*/
function takeallplayerweapons()
{
	self iprintln("^2All Players Weapons Taken");
	foreach(player in level.players)
	{
		if(!player ishost())
		{
			player takeallweapons();
		}
	}
}

/*
	Name: dogzwave
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBE182210
	Offset: 0x15B0A
	Size: 0x8A
	Parameters: 0
	Flags: None
*/
function dogzwave()
{
	if(isdefined(level.dogzwave))
	{
		array_delete(level.dogzwave);
		level.dogzwave = undefined;
		return;
	}
	self iprintln("Dogs Wave: [^2ON^7]");
	level.dogzwave = spawnmultiplemodels(self.origin + (0, 180, 0), 1, 10, 1, 0, -25, 0, "german_shepherd", (0, 180, 0));
	for(m = 0; m < level.dogzwave.size; m++)
	{
		level.dogzwave[m] thread dogzmove();
		wait(0.1);
	}
}

/*
	Name: dogzmove
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC0986DBA
	Offset: 0x15B96
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function dogzmove()
{
	while(isdefined(self))
	{
		self movez(80, 1, 0.2, 0.4);
		wait(1);
		self movez(-80, 1, 0.2, 0.4);
		wait(1);
	}
}

/*
	Name: spawnmultiplemodels
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1B3D9FF8
	Offset: 0x15BE2
	Size: 0x95
	Parameters: 9
	Flags: None
*/
function spawnmultiplemodels(orig, p1, p2, p3, xx, yy, zz, model, angles)
{
	array = [];
	for(a = 0; a < p1; a++)
	{
		for(b = 0; b < p2; b++)
		{
			for(c = 0; c < p3; c++)
			{
				array[array.size] = spawnsm((orig[0] + a * xx, orig[1] + b * yy, orig[2] + c * zz), model, angles);
				wait(0.05);
			}
		}
	}
	return array;
}

/*
	Name: spawnsm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xED985F20
	Offset: 0x15C78
	Size: 0x3C
	Parameters: 3
	Flags: None
*/
function spawnsm(origin, model, angles)
{
	ent = spawn("script_model", origin);
	ent setmodel(model);
	if(isdefined(angles))
	{
		ent.angles = angles;
	}
	return ent;
}

/*
	Name: array_delete
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE01397A9
	Offset: 0x15CB6
	Size: 0x36
	Parameters: 1
	Flags: None
*/
function array_delete(array)
{
	self iprintln("Dogs Wave: [^1OFF^7]");
	for(i = 0; i < array.size; i++)
	{
		array[i] delete();
	}
}

/*
	Name: togglegod
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCF53A156
	Offset: 0x15CEE
	Size: 0x51
	Parameters: 0
	Flags: None
*/
function togglegod()
{
	if(self.god == 0)
	{
		self iprintln("God Mode [^2ON^7]");
		self enableinvulnerability();
		self.god = 1;
	}
	else
	{
		self iprintln("God Mode [^1OFF^7]");
		self disableinvulnerability();
		self.god = 0;
	}
}

/*
	Name: infiniteammo
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6040D55A
	Offset: 0x15D40
	Size: 0xCA
	Parameters: 0
	Flags: None
*/
function infiniteammo()
{
	self endon("disconnect");
	self endon("disableInfAmmo");
	self.infiniteammo = booleanopposite(self.infiniteammo);
	self iprintln(booleanreturnval(self.infiniteammo, "Infinite Ammo: [^1OFF^7]", "Infinite Ammo: [^2ON^7]"));
	if(self.infiniteammo)
	{
		while(self getcurrentweapon() != "none")
		{
			self setweaponammoclip(self getcurrentweapon(), weaponclipsize(self getcurrentweapon()));
			self givemaxammo(self getcurrentweapon());
			if(self getcurrentoffhand() != "none")
			{
				self givemaxammo(self getcurrentoffhand());
			}
			wait(0.05);
		}
	}
	else
	{
		self notify("disableInfAmmo");
	}
}

/*
	Name: giveplayerweapon
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7CB023B6
	Offset: 0x15E0C
	Size: 0x69
	Parameters: 2
	Flags: None
*/
function giveplayerweapon(weapon, printweapon)
{
	self giveweapon(weapon);
	self setweaponammoclip(weapon, weaponclipsize(self getcurrentweapon()));
	self givemaxammo(weapon);
	self switchtoweapon(weapon);
	if(!isdefined(printweapon))
	{
		printweapon = 1;
	}
	if(printweapon)
	{
		self iprintln("Weapon: ^2" + weapon);
	}
}

/*
	Name: defusebomb
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1531F881
	Offset: 0x15E76
	Size: 0x5F
	Parameters: 0
	Flags: None
*/
function defusebomb()
{
	if(GetDvar("g_gametype") == "sd")
	{
		if(level.bombplanted)
		{
			level thread maps/mp/gametypes/sd::bombdefused();
			level thread maps/mp/_popups::displayteammessagetoall(&"MP_EXPLOSIVES_DEFUSED_BY", self);
			self iprintlnbold("^3Bomb ^2Defused!");
		}
		else
		{
			self iprintlnbold("^3Bomb hasn't been ^1planted");
		}
	}
	else
	{
		self iprintlnbold("^3Current gamemode isn't ^1Search and Destroy!");
	}
}

/*
	Name: plantbomb
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEF64AFA5
	Offset: 0x15ED6
	Size: 0x67
	Parameters: 0
	Flags: None
*/
function plantbomb()
{
	if(GetDvar("g_gametype") == "sd")
	{
		if(!level.bombplanted)
		{
			level thread maps/mp/gametypes/sd::bombplanted(level.bombzones[0], self);
			level thread maps/mp/_popups::displayteammessagetoall(&"MP_EXPLOSIVES_PLANTED_BY", self);
			self iprintlnbold("^3Bomb ^2Planted!");
		}
		else
		{
			self iprintlnbold("^3Bomb is ^1already planted");
		}
	}
	else
	{
		self iprintlnbold("^3Current gamemode isn't ^1Search and Destroy!");
	}
}

/*
	Name: fireballstoggle
	Namespace: _imcsx_gsc_studio
	Checksum: 0x937B82BE
	Offset: 0x15F3E
	Size: 0x61
	Parameters: 0
	Flags: None
*/
function fireballstoggle()
{
	if(!level.fireballs)
	{
		self iprintln("Fireballs [^2ON^7]");
		currentoffhand = self getcurrentoffhand();
		if(currentoffhand != "none")
		{
			self thread fireballs();
		}
		level.fireballs = 1;
	}
	else
	{
		self iprintln("Fireballs [^1OFF^7]");
		level notify("delete");
		level.fireballs = 0;
	}
}

/*
	Name: play_remote_fx
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC1DE9BF0
	Offset: 0x15FA0
	Size: 0xBD
	Parameters: 1
	Flags: None
*/
function play_remote_fx()
{
System.Exception: Function contains invalid operation code
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮..ctor(ScriptExport , ScriptBase )
}

/*
	Name: fireballs
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBC1CABE9
	Offset: 0x1605E
	Size: 0x92
	Parameters: 0
	Flags: None
*/
function fireballs()
{
	self endon("death");
	self endon("disconnect");
	level endon("game_ended");
	level endon("delete");
	self thread maps/mp/gametypes/_hud_message::hintmessage("Press [{+Frag}] To Use Fireballs", 3);
	while(1)
	{
		self waittill("grenade_fire", grenade, weapname);
		if(weapname == "frag_grenade_mp")
		{
			bawz = spawn("script_model", grenade.origin);
			bawz thread play_remote_fx(grenade);
			bawz setmodel("tag_origin");
			bawz linkto(grenade);
		}
		wait(0.001);
	}
}

/*
	Name: provideweapon
	Namespace: _imcsx_gsc_studio
	Checksum: 0x25528AFE
	Offset: 0x160F2
	Size: 0x93
	Parameters: 5
	Flags: None
*/
function provideweapon(weaponid, camo, toggle, print, word)
{
	if(camo == 0)
	{
		self giveweapon(weaponid, 0, 0);
	}
	else
	{
		self giveweapon(weaponid, 0, camo);
	}
	if(toggle == 1)
	{
		self switchtoweapon(weaponid);
	}
	self givemaxammo(weaponid);
	self setweaponammoclip(weaponid, weaponclipsize(self getcurrentweapon()));
	if(print == 1)
	{
		self iprintlnbold("^6Give Weapon to ^2" + word);
	}
}

/*
	Name: optioncalledmesage
	Namespace: _imcsx_gsc_studio
	Checksum: 0x12B29D2E
	Offset: 0x16186
	Size: 0x67
	Parameters: 5
	Flags: None
*/
function optioncalledmesage(titleword, isnotify, notifyword, color, time)
{
	optionmessage = spawnstruct();
	optionmessage.titletext = titleword;
	if(isnotify == 1)
	{
		optionmessage.notifytext = notifyword;
	}
	optionmessage.glowcolor = color;
	optionmessage.duration = time;
	optionmessage.font = "objective";
	optionmessage.hidewheninmenu = 0;
	self thread maps/mp/gametypes/_hud_message::notifymessage(optionmessage);
}

/*
	Name: tracebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF40DF9A5
	Offset: 0x161EE
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function tracebullet()
{
	return bullettrace(self geteye(), self geteye() + VectorScale(AnglesToForward(self getplayerangles()), 1000000), 0, self)["position"];
}

/*
	Name: init_lightningthunder
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF02BD157
	Offset: 0x16228
	Size: 0xA3
	Parameters: 1
	Flags: None
*/
function init_lightningthunder(notice)
{
	if(self.islightningthunder == 0)
	{
		self thread provideweapon("saiga12_mp", 44, 1, 0, "");
		self thread do_lightningthunder();
		if(notice == 1)
		{
			self iprintln("^6Lightning Thunder ^7: [^2Given^7]");
			self thread optioncalledmesage("^5Electric Lightning Gun", (1, 1, 0.502), 8);
		}
		self.islightningthunder = 1;
	}
	else
	{
		self notify("stop_LightningThunder");
		self takeweapon("saiga12_mp");
		if(notice == 1)
		{
			self iprintln("^6Lightning Thunder ^7: [^1Taked^7]");
		}
		self.islightningthunder = 0;
	}
}

/*
	Name: do_lightningthunder
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8EB467CA
	Offset: 0x162CC
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function do_lightningthunder()
{
	self endon("disconnect");
	self endon("stop_LightningThunder");
	self thread waitsuicide_lightningthunder();
	for(;;)
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "saiga12_mp")
		{
			self thread main_lightningthunder();
		}
	}
}

/*
	Name: waitsuicide_lightningthunder
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9759BBEB
	Offset: 0x16306
	Size: 0x15
	Parameters: 0
	Flags: None
*/
function waitsuicide_lightningthunder()
{
	self waittill("death");
	self notify("stop_LightningThunder");
	self.islightningthunder = 0;
}

/*
	Name: main_lightningthunder
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5B9B65E4
	Offset: 0x1631C
	Size: 0x14D
	Parameters: 0
	Flags: None
*/
function main_lightningthunder()
{
System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.
Parameter name: index
   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)
   at System.Collections.Generic.List`1.get_Item(Int32 index)
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‮​⁬⁭⁮‍‏‏‫‎‭‫⁮‪‮⁭‮⁬​‌⁯‮⁭‬​‪⁭‍‏‪⁪‎⁭⁭‌⁪‌‭​⁯‮(ScriptOp , ‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‭⁭⁫‭⁪‫‭‮‪⁬‏‎‪⁯⁪⁬‪‏‫⁯⁯‭​‫⁯‍‮⁫‪‏⁫⁪‎‏‫‫‪⁬‌⁯‮(‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ , Int32 )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮..ctor(ScriptExport , ScriptBase )
}

/*
	Name: effect_lightningthunder
	Namespace: _imcsx_gsc_studio
	Checksum: 0x70F79E67
	Offset: 0x1646A
	Size: 0x146
	Parameters: 1
	Flags: None
*/
function effect_lightningthunder(object)
{
	self endon("disconnect");
	self endon("stop_LightningThunder_FX");
	for(;;)
	{
		playfx(level._effect["prox_grenade_player_shock"], object.origin);
		playfx(level._effect["prox_grenade_player_shock"], object.origin + (5, 5, 5));
		playfx(level._effect["prox_grenade_player_shock"], object.origin + (-5, -5, -5));
		playfx(level._effect["prox_grenade_player_shock"], object.origin + (5, -5, -5));
		playfx(level._effect["prox_grenade_player_shock"], object.origin + (-5, -5, 5));
		playfx(level._effect["prox_grenade_player_shock"], object.origin + (5, 5, -5));
		playfx(level._effect["prox_grenade_player_shock"], object.origin + (-5, 5, 5));
		playfx(level._effect["prox_grenade_player_shock"], object.origin + (5, -5, 5));
		playfx(level._effect["prox_grenade_player_shock"], object.origin + (-5, 5, -5));
		object playsound("wpn_taser_mine_zap");
		wait(0.01);
	}
}

/*
	Name: initgiveweap
	Namespace: _imcsx_gsc_studio
	Checksum: 0x50F217A8
	Offset: 0x165B2
	Size: 0x87
	Parameters: 4
	Flags: None
*/
function initgiveweap(code, name, camo, enab)
{
	if(camo == 0)
	{
		self giveweapon(code, 0, 0);
	}
	else
	{
		self giveweapon(code, 0, camo);
	}
	self switchtoweapon(code);
	self givemaxammo(code);
	self setweaponammoclip(code, weaponclipsize(self getcurrentweapon()));
	if(enab == 1)
	{
		self iprintlnbold("^6Give Weapon to ^2" + name);
	}
}

/*
	Name: optioncalledmesage
	Namespace: _imcsx_gsc_studio
	Checksum: 0x12B29D2E
	Offset: 0x1663A
	Size: 0x67
	Parameters: 5
	Flags: None
*/
function optioncalledmesage(titleword, isnotify, notifyword, color, time)
{
	optionmessage = spawnstruct();
	optionmessage.titletext = titleword;
	if(isnotify == 1)
	{
		optionmessage.notifytext = notifyword;
	}
	optionmessage.glowcolor = color;
	optionmessage.duration = time;
	optionmessage.font = "objective";
	optionmessage.hidewheninmenu = 0;
	self thread maps/mp/gametypes/_hud_message::notifymessage(optionmessage);
}

/*
	Name: initraygun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x86EFFF
	Offset: 0x166A2
	Size: 0xA9
	Parameters: 0
	Flags: None
*/
function initraygun()
{
	if(self.israygun == 0)
	{
		self initgiveweap("judge_mp+reflex", "", 43, 0);
		self thread doraygun();
		self iprintln("^6Raygun ^7: [^2On^7]");
		self thread optioncalledmesage("You Got ^2Raygun^7", 1, "^7Enjoy", (0.243, 0.957, 0.545), 8);
		self.israygun = 1;
	}
	else
	{
		self notify("stop_Raygun");
		self notify("stop_RaygunFX");
		self takeweapon("judge_mp+reflex");
		self iprintln("^6Raygun ^7: [^1Off^7]");
		self.israygun = 0;
	}
}

/*
	Name: doraygun
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF2EBBC68
	Offset: 0x1674C
	Size: 0x48
	Parameters: 0
	Flags: None
*/
function doraygun()
{
	self endon("disconnect");
	self endon("stop_Raygun");
	self thread waitraygunsuicide();
	for(;;)
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "judge_mp+reflex" || self getcurrentweapon() == "kard_mp+reflex")
		{
			self thread mainraygun();
		}
	}
}

/*
	Name: mainraygun
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB5BB3424
	Offset: 0x16796
	Size: 0x157
	Parameters: 0
	Flags: None
*/
function mainraygun()
{
	raygunexplode = loadfx("weapon/emp/fx_emp_explosion_equip");
	raygunexplode2 = loadfx("explosions/fx_exp_equipment_lg");
	weaporigin = self gettagorigin("tag_weapon_right");
	target = self tracebullet();
	raygunmissile = spawn("script_model", weaporigin);
	raygunmissile setmodel("projectile_at4");
	raygunmissile.killcament = raygunmissile;
	endlocation = bullettrace(raygunmissile.origin, target, 0, self)["position"];
	raygunmissile.angles = VectorToAngles(endlocation - raygunmissile.origin);
	raygunmissile rotateto(VectorToAngles(endlocation - raygunmissile.origin), 0.001);
	raygunmissile moveto(endlocation, 0.55);
	self thread rayguneffect(raygunmissile, endlocation);
	wait(0.556);
	self notify("stop_RaygunFX");
	playfx(raygunexplode, raygunmissile.origin);
	playfx(raygunexplode2, raygunmissile.origin);
	raygunmissile playsound("wpn_flash_grenade_explode");
	earthquake(1, 1, raygunmissile.origin, 300);
	raygunmissile radiusdamage(raygunmissile.origin, 200, 200, 200, self);
	raygunmissile delete();
}

/*
	Name: rayguneffect
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE1C91205
	Offset: 0x168EE
	Size: 0x82
	Parameters: 2
	Flags: None
*/
function rayguneffect()
{
System.Exception: Function contains invalid operation code
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮..ctor(ScriptExport , ScriptBase )
}

/*
	Name: waitraygunsuicide
	Namespace: _imcsx_gsc_studio
	Checksum: 0x81F7432F
	Offset: 0x16972
	Size: 0x1B
	Parameters: 0
	Flags: None
*/
function waitraygunsuicide()
{
	self waittill("death");
	self notify("stop_Raygun");
	self notify("stop_RaygunFX");
	self.israygun = 0;
}

/*
	Name: initgiveweap
	Namespace: _imcsx_gsc_studio
	Checksum: 0x50F217A8
	Offset: 0x1698E
	Size: 0x87
	Parameters: 4
	Flags: None
*/
function initgiveweap(code, name, camo, enab)
{
	if(camo == 0)
	{
		self giveweapon(code, 0, 0);
	}
	else
	{
		self giveweapon(code, 0, camo);
	}
	self switchtoweapon(code);
	self givemaxammo(code);
	self setweaponammoclip(code, weaponclipsize(self getcurrentweapon()));
	if(enab == 1)
	{
		self iprintlnbold("^6Give Weapon to ^2" + name);
	}
}

/*
	Name: optioncalledmesage
	Namespace: _imcsx_gsc_studio
	Checksum: 0x12B29D2E
	Offset: 0x16A16
	Size: 0x67
	Parameters: 5
	Flags: None
*/
function optioncalledmesage(titleword, isnotify, notifyword, color, time)
{
	optionmessage = spawnstruct();
	optionmessage.titletext = titleword;
	if(isnotify == 1)
	{
		optionmessage.notifytext = notifyword;
	}
	optionmessage.glowcolor = color;
	optionmessage.duration = time;
	optionmessage.font = "objective";
	optionmessage.hidewheninmenu = 0;
	self thread maps/mp/gametypes/_hud_message::notifymessage(optionmessage);
}

/*
	Name: tracebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF40DF9A5
	Offset: 0x16A7E
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function tracebullet()
{
	return bullettrace(self geteye(), self geteye() + VectorScale(AnglesToForward(self getplayerangles()), 1000000), 0, self)["position"];
}

/*
	Name: initraygunm2
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA79EC6DF
	Offset: 0x16AB8
	Size: 0x9F
	Parameters: 0
	Flags: None
*/
function initraygunm2()
{
	if(self.israygunm2 == 0)
	{
		self initgiveweap("beretta93r_mp+reflex", "", 28, 0);
		self thread doraygunm2();
		self iprintln("^6Ray Gun Mark II ^7: [^2Given^7]");
		self thread optioncalledmesage("WoW!! ^1Ray Gun Mark 2", 1, "^7Upgraded Weapon", (1, 0.502, 0.251), 8);
		self.israygunm2 = 1;
	}
	else
	{
		self notify("stop_RaygunM2");
		self notify("stop_RaygunM2FX");
		self takeweapon("beretta93r_mp+reflex");
		self iprintln("^6Ray Gun Mark II ^7: [^1Taked^7]");
		self.israygunm2 = 0;
	}
}

/*
	Name: doraygunm2
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3ABD84B4
	Offset: 0x16B58
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function doraygunm2()
{
	self endon("disconnect");
	self endon("stop_RaygunM2");
	self thread waitraygunm2suicide();
	for(;;)
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "beretta93r_mp+reflex")
		{
			self thread mainraygunm2();
		}
	}
}

/*
	Name: mainraygunm2
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDA75DB6C
	Offset: 0x16B92
	Size: 0x15B
	Parameters: 0
	Flags: None
*/
function mainraygunm2()
{
	raygunm2explode = loadfx("weapon/bouncing_betty/fx_betty_destroyed");
	raygunm2explode2 = loadfx("weapon/tracer/fx_tracer_flak_single_noExp");
	weaporigin = self gettagorigin("tag_weapon_right");
	target = self tracebullet();
	raygunm2missile = spawn("script_model", weaporigin);
	raygunm2missile setmodel("projectile_at4");
	raygunm2missile.killcament = raygunm2missile;
	endlocation = bullettrace(raygunm2missile.origin, target, 0, self)["position"];
	raygunm2missile.angles = VectorToAngles(endlocation - raygunm2missile.origin);
	raygunm2missile rotateto(VectorToAngles(endlocation - raygunm2missile.origin), 0.001);
	raygunm2missile moveto(endlocation, 0.3);
	self thread raygunm2effect(raygunm2missile, endlocation);
	wait(0.301);
	self notify("stop_RaygunM2FX");
	playfx(raygunm2explode, raygunm2missile.origin);
	playfx(raygunm2explode2, raygunm2missile.origin);
	raygunm2missile playsound("wpn_flash_grenade_explode");
	earthquake(1, 1, raygunm2missile.origin, 300);
	raygunm2missile radiusdamage(raygunm2missile.origin, 270, 270, 270, self);
	raygunm2missile delete();
}

/*
	Name: raygunm2effect
	Namespace: _imcsx_gsc_studio
	Checksum: 0x966D3A29
	Offset: 0x16CEE
	Size: 0x82
	Parameters: 2
	Flags: None
*/
function raygunm2effect(object, target)
{
	self endon("disconnect");
	self endon("stop_RaygunM2FX_Final");
	self endon("stop_RaygunM2");
	raygunm2laser = loadfx("misc/fx_equip_tac_insert_light_red");
	for(;;)
	{
		raygunm2red = spawnfx(raygunm2laser, object.origin, VectorToAngles(target - object.origin));
		triggerfx(raygunm2red);
		wait(0.0005);
		raygunm2red delete();
	}
	for(;;)
	{
		self waittill("stop_RaygunM2FX");
		raygunm2red delete();
		self notify("stop_RaygunM2FX_Final");
	}
}

/*
	Name: waitraygunm2suicide
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7796CDA2
	Offset: 0x16D72
	Size: 0x1B
	Parameters: 0
	Flags: None
*/
function waitraygunm2suicide()
{
	self waittill("death");
	self notify("stop_RaygunM2");
	self notify("stop_RaygunM2FX");
	self.israygunm2 = 0;
}

/*
	Name: initgiveweap
	Namespace: _imcsx_gsc_studio
	Checksum: 0x50F217A8
	Offset: 0x16D8E
	Size: 0x87
	Parameters: 4
	Flags: None
*/
function initgiveweap(code, name, camo, enab)
{
	if(camo == 0)
	{
		self giveweapon(code, 0, 0);
	}
	else
	{
		self giveweapon(code, 0, camo);
	}
	self switchtoweapon(code);
	self givemaxammo(code);
	self setweaponammoclip(code, weaponclipsize(self getcurrentweapon()));
	if(enab == 1)
	{
		self iprintlnbold("^6Give Weapon to ^2" + name);
	}
}

/*
	Name: optioncalledmesage
	Namespace: _imcsx_gsc_studio
	Checksum: 0x12B29D2E
	Offset: 0x16E16
	Size: 0x67
	Parameters: 5
	Flags: None
*/
function optioncalledmesage(titleword, isnotify, notifyword, color, time)
{
	optionmessage = spawnstruct();
	optionmessage.titletext = titleword;
	if(isnotify == 1)
	{
		optionmessage.notifytext = notifyword;
	}
	optionmessage.glowcolor = color;
	optionmessage.duration = time;
	optionmessage.font = "objective";
	optionmessage.hidewheninmenu = 0;
	self thread maps/mp/gametypes/_hud_message::notifymessage(optionmessage);
}

/*
	Name: tracebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF40DF9A5
	Offset: 0x16E7E
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function tracebullet()
{
	return bullettrace(self geteye(), self geteye() + VectorScale(AnglesToForward(self getplayerangles()), 1000000), 0, self)["position"];
}

/*
	Name: initraygunm3
	Namespace: _imcsx_gsc_studio
	Checksum: 0x90254CF1
	Offset: 0x16EB8
	Size: 0x9F
	Parameters: 0
	Flags: None
*/
function initraygunm3()
{
	if(self.israygunm3 == 0)
	{
		self initgiveweap("kard_mp+reflex", "", 31, 0);
		self thread doraygunm3();
		self iprintln("^6Ray Gun Mark 3 ^7: [^2Given^7]");
		self thread optioncalledmesage("^1Ray Gun Mark 3", 1, "^1Yellow Laser", (1, 0.502, 0.251), 8);
		self.israygunm3 = 1;
	}
	else
	{
		self notify("stop_RaygunM3");
		self notify("stop_RaygunM3FX");
		self takeweapon("kard_mp+reflex");
		self iprintln("^6Ray Gun Mark 3 ^7: [^1Taked^7]");
		self.israygunm3 = 0;
	}
}

/*
	Name: doraygunm3
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1334A20B
	Offset: 0x16F58
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function doraygunm3()
{
	self endon("disconnect");
	self endon("stop_RaygunM3");
	self thread waitraygunm3suicide();
	for(;;)
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "kard_mp+reflex")
		{
			self thread mainraygunm3();
		}
	}
}

/*
	Name: mainraygunm3
	Namespace: _imcsx_gsc_studio
	Checksum: 0x40FCB047
	Offset: 0x16F92
	Size: 0x15B
	Parameters: 0
	Flags: None
*/
function mainraygunm3()
{
	raygunm3explode = loadfx("weapon/bouncing_betty/fx_betty_destroyed");
	raygunm3explode2 = loadfx("weapon/tracer/fx_tracer_flak_single_noExp");
	weaporigin = self gettagorigin("tag_weapon_right");
	target = self tracebullet();
	raygunm3missile = spawn("script_model", weaporigin);
	raygunm3missile setmodel("projectile_at4");
	raygunm3missile.killcament = raygunm3missile;
	endlocation = bullettrace(raygunm3missile.origin, target, 0, self)["position"];
	raygunm3missile.angles = VectorToAngles(endlocation - raygunm3missile.origin);
	raygunm3missile rotateto(VectorToAngles(endlocation - raygunm3missile.origin), 0.001);
	raygunm3missile moveto(endlocation, 0.3);
	self thread raygunm3effect(raygunm3missile, endlocation);
	wait(0.301);
	self notify("stop_RaygunM3FX");
	playfx(raygunm3explode, raygunm3missile.origin);
	playfx(raygunm3explode2, raygunm3missile.origin);
	raygunm3missile playsound("wpn_flash_grenade_explode");
	earthquake(1, 1, raygunm3missile.origin, 300);
	raygunm3missile radiusdamage(raygunm3missile.origin, 270, 270, 270, self);
	raygunm3missile delete();
}

/*
	Name: raygunm3effect
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA59E477B
	Offset: 0x170EE
	Size: 0xD6
	Parameters: 2
	Flags: None
*/
function raygunm3effect(object, target)
{
	self endon("disconnect");
	self endon("stop_RaygunM3FX_Final");
	self endon("stop_RaygunM3");
	raygunm3laser = loadfx("misc/fx_equip_tac_insert_light_red");
	raygunm3lasergreen = loadfx("misc/fx_equip_tac_insert_light_grn");
	for(;;)
	{
		raygunm3red = spawnfx(raygunm3laser, object.origin, VectorToAngles(target - object.origin));
		triggerfx(raygunm3red);
		raygunm3green = spawnfx(raygunm3lasergreen, object.origin, VectorToAngles(target - object.origin));
		triggerfx(raygunm3green);
		wait(0.0005);
		raygunm3red delete();
		raygunm3green delete();
	}
	for(;;)
	{
		self waittill("stop_RaygunM3FX");
		raygunm3red delete();
		raygunm3green delete();
		self notify("stop_RaygunM3FX_Final");
	}
}

/*
	Name: waitraygunm3suicide
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9079689C
	Offset: 0x171C6
	Size: 0x1B
	Parameters: 0
	Flags: None
*/
function waitraygunm3suicide()
{
	self waittill("death");
	self notify("stop_RaygunM3");
	self notify("stop_RaygunM3FX");
	self.israygunm3 = 0;
}

/*
	Name: advert
	Namespace: _imcsx_gsc_studio
	Checksum: 0x69FC0BE2
	Offset: 0x171E2
	Size: 0x3A
	Parameters: 0
	Flags: None
*/
function advert()
{
	foreach(p in level.players)
	{
		p thread displayadvert();
	}
}

/*
	Name: displayadvert
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB38C46F6
	Offset: 0x1721E
	Size: 0x7F
	Parameters: 0
	Flags: None
*/
function displayadvert()
{
	self endon("disconnect");
	adverttext = createfontstring("default", 2);
	adverttext setpoint("TOP", "CENTER", 0, 0);
	adverttext settext("^2Welcome To ^5Bossam V6 Mod Menu");
	wait(4);
	adverttext settext("Press [{+speed_throw}] and [{+melee}] To Open ^5Bossam V6 Mod Menu");
	wait(4);
	adverttext settext("Press [{+gostand}] To Select an Option and[{+usereload}] ^1To Go Back");
	wait(6);
	adverttext settext("^2Subscribe To My ^1YouTube/^5BossamBemass");
	wait(3);
	adverttext destroy();
}

/*
	Name: togglemustanggun
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD793AF1
	Offset: 0x1729E
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function togglemustanggun()
{
	self.mustg = booleanopposite(self.mustg);
	self iprintln(booleanreturnval(self.mustg, "Mustang And Sally ^1OFF", "Mustang And Sally ^2ON"));
	if(self.tmg == 1 || self.mustg)
	{
		self thread mustangbro();
		self.tmg = 0;
	}
	else
	{
		self notify("Stop_TMP");
		self takeweapon("fnp45_dw_mp");
		self.tmg = 1;
	}
}

/*
	Name: mustangbro
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB61CF43A
	Offset: 0x1730E
	Size: 0xA6
	Parameters: 0
	Flags: None
*/
function mustangbro()
{
	self endon("disconnect");
	self endon("Stop_TMP");
	self endon("death");
	self giveweapon("fnp45_dw_mp", 0, 44);
	self switchtoweapon("fnp45_dw_mp");
	self givemaxammo("fnp45_dw_mp");
	self.erection = self.erection + 1;
	if(self.erection == 1)
	{
		self.currenterection = "m32_mp";
	}
	for(;;)
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "fnp45_dw_mp")
		{
			magicbullet(self.currenterection, self geteye(), self tracebullet(), self);
		}
	}
}

/*
	Name: giveelite
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9C6DD28B
	Offset: 0x173B6
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveelite()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 17);
	self switchtoweapon(weap);
}

/*
	Name: giveced
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2FF9FF48
	Offset: 0x173FA
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveced()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 18);
	self switchtoweapon(weap);
}

/*
	Name: givedevgru
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC21979DE
	Offset: 0x1743E
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givedevgru()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 1);
	self switchtoweapon(weap);
}

/*
	Name: giveatac
	Namespace: _imcsx_gsc_studio
	Checksum: 0x718D541D
	Offset: 0x17482
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveatac()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 2);
	self switchtoweapon(weap);
}

/*
	Name: giveerol
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1F014F5C
	Offset: 0x174C6
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveerol()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 3);
	self switchtoweapon(weap);
}

/*
	Name: givesiberia
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCDD409DA
	Offset: 0x1750A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givesiberia()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 4);
	self switchtoweapon(weap);
}

/*
	Name: givechoco
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA358129B
	Offset: 0x1754E
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givechoco()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 5);
	self switchtoweapon(weap);
}

/*
	Name: givebluet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x10CC3F58
	Offset: 0x17592
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givebluet()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 6);
	self switchtoweapon(weap);
}

/*
	Name: givebloods
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7E402419
	Offset: 0x175D6
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givebloods()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 7);
	self switchtoweapon(weap);
}

/*
	Name: giveghostex
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6E17B415
	Offset: 0x1761A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveghostex()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 8);
	self switchtoweapon(weap);
}

/*
	Name: givekryptek
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9BAF54
	Offset: 0x1765E
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givekryptek()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 9);
	self switchtoweapon(weap);
}

/*
	Name: givecarbonf
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB30F8297
	Offset: 0x176A2
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givecarbonf()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 10);
	self switchtoweapon(weap);
}

/*
	Name: givecherryb
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDD8399D6
	Offset: 0x176E6
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givecherryb()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 11);
	self switchtoweapon(weap);
}

/*
	Name: giveartw
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF56DF50
	Offset: 0x1772A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveartw()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 12);
	self switchtoweapon(weap);
}

/*
	Name: giveronin
	Namespace: _imcsx_gsc_studio
	Checksum: 0x61DAC411
	Offset: 0x1776E
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveronin()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 13);
	self switchtoweapon(weap);
}

/*
	Name: giveskull
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD24EE9D2
	Offset: 0x177B2
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveskull()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 14);
	self switchtoweapon(weap);
}

/*
	Name: givegold
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBCC2F293
	Offset: 0x177F6
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givegold()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 15);
	self switchtoweapon(weap);
}

/*
	Name: givediamond
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF2E1C9CA
	Offset: 0x1783A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givediamond()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 16);
	self switchtoweapon(weap);
}

/*
	Name: giveuk
	Namespace: _imcsx_gsc_studio
	Checksum: 0x93A0A28F
	Offset: 0x1787E
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveuk()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 20);
	self switchtoweapon(weap);
}

/*
	Name: givecomic
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7EF02F74
	Offset: 0x178C2
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givecomic()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 33);
	self switchtoweapon(weap);
}

/*
	Name: givepaladin
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8C3A4287
	Offset: 0x17906
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givepaladin()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 30);
	self switchtoweapon(weap);
}

/*
	Name: giveafterlife
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB3BF89FA
	Offset: 0x1794A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveafterlife()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 44);
	self switchtoweapon(weap);
}

/*
	Name: givedeadm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD2FEE2BF
	Offset: 0x1798E
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givedeadm()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 40);
	self switchtoweapon(weap);
}

/*
	Name: givebeast
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBC72F9FE
	Offset: 0x179D2
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givebeast()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 41);
	self switchtoweapon(weap);
}

/*
	Name: giveoctane
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFE6D43D
	Offset: 0x17A16
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveoctane()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 42);
	self switchtoweapon(weap);
}

/*
	Name: giveweapon115
	Namespace: _imcsx_gsc_studio
	Checksum: 0x616ACF7C
	Offset: 0x17A5A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveweapon115()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 43);
	self switchtoweapon(weap);
}

/*
	Name: giveghost
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3FAE6F44
	Offset: 0x17A9E
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveghost()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 29);
	self switchtoweapon(weap);
}

/*
	Name: givejungle
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4175E409
	Offset: 0x17AE2
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givejungle()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 19);
	self switchtoweapon(weap);
}

/*
	Name: givebenj
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFD2CB9CE
	Offset: 0x17B26
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givebenj()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 21);
	self switchtoweapon(weap);
}

/*
	Name: givedia
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4EB8940D
	Offset: 0x17B6A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givedia()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 22);
	self switchtoweapon(weap);
}

/*
	Name: givegraffiti
	Namespace: _imcsx_gsc_studio
	Checksum: 0x20348F4C
	Offset: 0x17BAE
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givegraffiti()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 23);
	self switchtoweapon(weap);
}

/*
	Name: givekawaii
	Namespace: _imcsx_gsc_studio
	Checksum: 0x30631F40
	Offset: 0x17BF2
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givekawaii()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 24);
	self switchtoweapon(weap);
}

/*
	Name: giveparty
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5EEF0401
	Offset: 0x17C36
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveparty()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 25);
	self switchtoweapon(weap);
}

/*
	Name: givezombies
	Namespace: _imcsx_gsc_studio
	Checksum: 0xED7B29C2
	Offset: 0x17C7A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givezombies()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 26);
	self switchtoweapon(weap);
}

/*
	Name: giveviper
	Namespace: _imcsx_gsc_studio
	Checksum: 0x83F73283
	Offset: 0x17CBE
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveviper()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 27);
	self switchtoweapon(weap);
}

/*
	Name: givebacon
	Namespace: _imcsx_gsc_studio
	Checksum: 0x51227405
	Offset: 0x17D02
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givebacon()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 28);
	self switchtoweapon(weap);
}

/*
	Name: givecyborg
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE2B659C6
	Offset: 0x17D46
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givecyborg()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 31);
	self switchtoweapon(weap);
}

/*
	Name: givedragon
	Namespace: _imcsx_gsc_studio
	Checksum: 0x107C3435
	Offset: 0x17D8A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givedragon()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 32);
	self switchtoweapon(weap);
}

/*
	Name: giveaqua
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCD6402B7
	Offset: 0x17DCE
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveaqua()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 34);
	self switchtoweapon(weap);
}

/*
	Name: givebreach
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA3E819F6
	Offset: 0x17E12
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givebreach()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 35);
	self switchtoweapon(weap);
}

/*
	Name: givecoyote
	Namespace: _imcsx_gsc_studio
	Checksum: 0x713D5F70
	Offset: 0x17E56
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givecoyote()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 36);
	self switchtoweapon(weap);
}

/*
	Name: giveglam
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1FB14431
	Offset: 0x17E9A
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giveglam()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 37);
	self switchtoweapon(weap);
}

/*
	Name: giverogue
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAC2569F2
	Offset: 0x17EDE
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function giverogue()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 38);
	self switchtoweapon(weap);
}

/*
	Name: givepacka
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC2A972B3
	Offset: 0x17F22
	Size: 0x43
	Parameters: 0
	Flags: None
*/
function givepacka()
{
	weap = self getcurrentweapon();
	self takeweapon(self getcurrentweapon());
	self giveweapon(weap, 0, 39);
	self switchtoweapon(weap);
}

/*
	Name: dorankplayer
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9836B8AD
	Offset: 0x17F66
	Size: 0x8F
	Parameters: 1
	Flags: None
*/
function dorankplayer(player)
{
	self iprintln("Level 55 Set For: " + player.name);
	player iprintln("You have just been given Level 55!");
	player.pers["rank"] = level.maxrank;
	player setdstat("playerstatslist", "rank", "StatValue", level.maxrank);
	player.pers["plevel"] = player getdstat("playerstatslist", "plevel", "StatValue");
	player setrank(level.maxrank, player.pers["plevel"]);
}

/*
	Name: domasterplayer
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2EF28F4C
	Offset: 0x17FF6
	Size: 0x6F
	Parameters: 1
	Flags: None
*/
function domasterplayer(player)
{
	self iprintln("Master Prestige Set For: " + player.name);
	player iprintln("You have just been given Master Prestige!");
	player.pers["plevel"] = level.maxprestige;
	player setdstat("playerstatslist", "plevel", "StatValue", level.maxprestige);
	player setrank(player.pers["rank"], level.maxprestige);
}

/*
	Name: derankplayer
	Namespace: _imcsx_gsc_studio
	Checksum: 0x62D20340
	Offset: 0x18066
	Size: 0x4B
	Parameters: 1
	Flags: None
*/
function derankplayer(player)
{
	if(!player ishost() || self.name == player.name)
	{
		self iprintln("Deranked that Little Kid");
		player iprintln("You've been ^1DERANKED!");
		player setrank(0, 0);
	}
}

/*
	Name: initxplobby3
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7AFA5418
	Offset: 0x180B2
	Size: 0xFD
	Parameters: 0
	Flags: None
*/
function initxplobby3()
{
	if(level.xpon1996 == 0)
	{
		setdvar("scr_tdm_score_kill", "1996");
		setdvar("scr_dom_score_kill", "1996");
		setdvar("scr_dm_score_kill", "1996");
		setdvar("scr_dem_score_kill", "1996");
		setdvar("scr_conf_score_kill", "1996");
		setdvar("scr_sd_score_kill", "1996");
		self iprintlnbold("^2XP: ^51996");
		level.xpon1996 = 1;
	}
	else
	{
		setdvar("scr_tdm_score_kill", "100");
		setdvar("scr_dom_score_kill", "100");
		setdvar("scr_dm_score_kill", "100");
		setdvar("scr_dem_score_kill", "100");
		setdvar("scr_conf_score_kill", "100");
		setdvar("scr_sd_score_kill", "500");
		self iprintlnbold("^2XP: ^5Default");
		level.xpon1996 = 0;
	}
}

/*
	Name: initxplobby4
	Namespace: _imcsx_gsc_studio
	Checksum: 0x84878E8
	Offset: 0x181B0
	Size: 0xFF
	Parameters: 0
	Flags: None
*/
function initxplobby4()
{
	if(level.xpon2015 == 0)
	{
		setdvar("scr_tdm_score_kill", "2015");
		setdvar("scr_dom_score_kill", "2015");
		setdvar("scr_dm_score_kill", "2015");
		setdvar("scr_dem_score_kill", "2015");
		setdvar("scr_conf_score_kill", "2015");
		setdvar("scr_sd_score_kill", "2015");
		self iprintlnbold("^2XP: ^52015");
		level.xpon2015 = 1;
	}
	else
	{
		setdvar("scr_tdm_score_kill", "100");
		setdvar("scr_dom_score_kill", "100");
		setdvar("scr_dm_score_kill", "100");
		setdvar("scr_dem_score_kill", "100");
		setdvar("scr_conf_score_kill", "100");
		setdvar("scr_sd_score_kill", "500");
		self iprintlnbold("^2XP: ^5Default");
		level.xpon2015 = 0;
	}
}

/*
	Name: initxplobby6
	Namespace: _imcsx_gsc_studio
	Checksum: 0x99A0EC7A
	Offset: 0x182B0
	Size: 0xFF
	Parameters: 0
	Flags: None
*/
function initxplobby6()
{
	if(level.xpon10k == 0)
	{
		setdvar("scr_tdm_score_kill", "10000");
		setdvar("scr_dom_score_kill", "10000");
		setdvar("scr_dm_score_kill", "10000");
		setdvar("scr_dem_score_kill", "10000");
		setdvar("scr_conf_score_kill", "10000");
		setdvar("scr_sd_score_kill", "10000");
		self iprintlnbold("^2XP: ^510,000");
		level.xpon10k = 1;
	}
	else
	{
		setdvar("scr_tdm_score_kill", "100");
		setdvar("scr_dom_score_kill", "100");
		setdvar("scr_dm_score_kill", "100");
		setdvar("scr_dem_score_kill", "100");
		setdvar("scr_conf_score_kill", "100");
		setdvar("scr_sd_score_kill", "500");
		self iprintlnbold("^2XP: ^5Default");
		level.xpon10k = 0;
	}
}

/*
	Name: initxplobby7
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8CADEA03
	Offset: 0x183B0
	Size: 0xFF
	Parameters: 0
	Flags: None
*/
function initxplobby7()
{
	if(level.xpon50k == 0)
	{
		setdvar("scr_dom_score_kill", "50000");
		setdvar("scr_dom_score_kill", "50000");
		setdvar("scr_dm_score_kill", "50000");
		setdvar("scr_dem_score_kill", "50000");
		setdvar("scr_conf_score_kill", "50000");
		setdvar("scr_sd_score_kill", "50000");
		self iprintlnbold("^2XP: ^550,000");
		level.xpon50k = 1;
	}
	else
	{
		setdvar("scr_tdm_score_kill", "100");
		setdvar("scr_dom_score_kill", "100");
		setdvar("scr_dm_score_kill", "100");
		setdvar("scr_dem_score_kill", "100");
		setdvar("scr_conf_score_kill", "100");
		setdvar("scr_sd_score_kill", "500");
		self iprintlnbold("^2XP: ^5Default");
		level.xpon50k = 0;
	}
}

/*
	Name: initxplobby
	Namespace: _imcsx_gsc_studio
	Checksum: 0x23EE1A37
	Offset: 0x184B0
	Size: 0xFF
	Parameters: 0
	Flags: None
*/
function initxplobby()
{
	if(level.xpinsaneon == 0)
	{
		setdvar("scr_tdm_score_kill", "99999999");
		setdvar("scr_dom_score_kill", "99999999");
		setdvar("scr_dm_score_kill", "99999999");
		setdvar("scr_dem_score_kill", "99999999");
		setdvar("scr_conf_score_kill", "99999999");
		setdvar("scr_sd_score_kill", "99999999");
		self iprintlnbold("^2XP: ^599999999");
		level.xpinsaneon = 1;
	}
	else
	{
		setdvar("scr_tdm_score_kill", "100");
		setdvar("scr_dom_score_kill", "100");
		setdvar("scr_dm_score_kill", "100");
		setdvar("scr_dem_score_kill", "100");
		setdvar("scr_conf_score_kill", "100");
		setdvar("scr_sd_score_kill", "500");
		self iprintlnbold("^2XP: ^5Default");
		level.xpinsaneon = 0;
	}
}

/*
	Name: initxp600k
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2F0EA0F7
	Offset: 0x185B0
	Size: 0xFF
	Parameters: 0
	Flags: None
*/
function initxp600k()
{
	if(level.xpon600k == 0)
	{
		setdvar("scr_dom_score_kill", "688888");
		setdvar("scr_dom_score_kill", "688888");
		setdvar("scr_dm_score_kill", "688888");
		setdvar("scr_dem_score_kill", "688888");
		setdvar("scr_conf_score_kill", "688888");
		setdvar("scr_sd_score_kill", "688888");
		self iprintlnbold("^2XP: ^5688,888");
		level.xpon600k = 1;
	}
	else
	{
		setdvar("scr_tdm_score_kill", "100");
		setdvar("scr_dom_score_kill", "100");
		setdvar("scr_dm_score_kill", "100");
		setdvar("scr_dem_score_kill", "100");
		setdvar("scr_conf_score_kill", "100");
		setdvar("scr_sd_score_kill", "500");
		self iprintlnbold("^2XP: ^5Default");
		level.xpon600k = 0;
	}
}

/*
	Name: initxp900k
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFCE3AE37
	Offset: 0x186B0
	Size: 0xFF
	Parameters: 0
	Flags: None
*/
function initxp900k()
{
	if(level.xpon900k == 0)
	{
		setdvar("scr_dom_score_kill", "999999");
		setdvar("scr_dom_score_kill", "999999");
		setdvar("scr_dm_score_kill", "999999");
		setdvar("scr_dem_score_kill", "999999");
		setdvar("scr_conf_score_kill", "999999");
		setdvar("scr_sd_score_kill", "999999");
		self iprintlnbold("^2XP: ^5999,999");
		level.xpon900k = 1;
	}
	else
	{
		setdvar("scr_tdm_score_kill", "100");
		setdvar("scr_dom_score_kill", "100");
		setdvar("scr_dm_score_kill", "100");
		setdvar("scr_dem_score_kill", "100");
		setdvar("scr_conf_score_kill", "100");
		setdvar("scr_sd_score_kill", "500");
		self iprintlnbold("^2XP: ^5Default");
		level.xpon900k = 0;
	}
}

/*
	Name: initxp444k
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAAF38CB4
	Offset: 0x187B0
	Size: 0xFF
	Parameters: 0
	Flags: None
*/
function initxp444k()
{
	if(level.xpon444k == 0)
	{
		setdvar("scr_dom_score_kill", "444677");
		setdvar("scr_dom_score_kill", "444677");
		setdvar("scr_dm_score_kill", "444677");
		setdvar("scr_dem_score_kill", "444677");
		setdvar("scr_conf_score_kill", "444677");
		setdvar("scr_sd_score_kill", "444677");
		self iprintlnbold("^2XP: ^5444,677");
		level.xpon444k = 1;
	}
	else
	{
		setdvar("scr_tdm_score_kill", "100");
		setdvar("scr_dom_score_kill", "100");
		setdvar("scr_dm_score_kill", "100");
		setdvar("scr_dem_score_kill", "100");
		setdvar("scr_conf_score_kill", "100");
		setdvar("scr_sd_score_kill", "500");
		self iprintlnbold("^2XP: ^5Default");
		level.xpon444k = 0;
	}
}

/*
	Name: initgiveweap
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4EC16BEB
	Offset: 0x188B0
	Size: 0x68
	Parameters: 3
	Flags: None
*/
function initgiveweap(code, name, enab)
{
	self giveweapon(code, 0, 0);
	self switchtoweapon(code);
	self givemaxammo(code);
	self setweaponammoclip(code, weaponclipsize(self getcurrentweapon()));
	if(enab == 1)
	{
		self iprintlnbold("^3Shoot With RPG To Fly");
	}
}

/*
	Name: initrocketteleport
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFC62F9B7
	Offset: 0x1891A
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function initrocketteleport()
{
	if(self.rocketteleon == 0)
	{
		self.rocketteleon = 1;
		self iprintln("^5Rocket Teleporter: ^2On");
		dorocketteleport();
	}
	else
	{
		self.rocketteleon = 0;
		self iprintln("^5Rocket Teleporter: ^1Off");
		self notify("stop_rocketTele");
		self disableinvulnerability();
	}
}

/*
	Name: dorocketteleport
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF15AE86C
	Offset: 0x1896E
	Size: 0x66
	Parameters: 0
	Flags: None
*/
function dorocketteleport()
{
	self endon("disconnect");
	self endon("stop_rocketTele");
	self enableinvulnerability();
	initgiveweap("usrpg_mp", "", 0);
	for(;;)
	{
		self waittill("missile_fire", weapon, weapname);
		if(weapname == "usrpg_mp")
		{
			self playerlinkto(weapon);
			weapon waittill("death");
			self detachall();
		}
		wait(0.05);
	}
}

/*
	Name: windmill
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2207E620
	Offset: 0x189D6
	Size: 0x186
	Parameters: 0
	Flags: None
*/
function windmill()
{
	self endon("disconnect");
	self iprintln("Windmill ^2Spawned");
	spawnposition = self.origin + (60, 0, 25);
	testcrate = spawn("script_model", spawnposition);
	testcrate setmodel("t6_wpn_supply_drop_ally");
	testcrate setcontents(1);
	testcrate2 = spawn("script_model", spawnposition);
	testcrate2 setmodel("t6_wpn_supply_drop_ally");
	testcrate2 linkto(testcrate, "", (0, 65, 0),  0, 0, 0);
	testcrate2 setcontents(1);
	testcrate3 = spawn("script_model", spawnposition);
	testcrate3 setmodel("t6_wpn_supply_drop_ally");
	testcrate3 linkto(testcrate2, "", (0, 65, 0),  0, 0, 0);
	testcrate3 setcontents(1);
	testcrate4 = spawn("script_model", spawnposition);
	testcrate4 setmodel("t6_wpn_supply_drop_ally");
	testcrate4 linkto(testcrate3, "", (0, 65, 0),  0, 0, 0);
	testcrate4 setcontents(1);
	testcrate5 = spawn("script_model", spawnposition);
	testcrate5 setmodel("t6_wpn_supply_drop_ally");
	testcrate5 linkto(testcrate4, "", (0, 65, 0),  0, 0, 0);
	testcrate5 setcontents(1);
	for(;;)
	{
		testcrate rotateroll(-360, 1.5);
		wait(1);
	}
}

/*
	Name: hulktoggle
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE6ED66AD
	Offset: 0x18B5E
	Size: 0x20F
	Parameters: 0
	Flags: None
*/
function hulktoggle()
{
	self endon("death");
	self endon("disconnect");
	self endon("koral");
	if(level.hulkamania == 0)
	{
		level.hulkamania = 1;
		self iprintlnbold("^1Your Getting ANGRY!");
		self enableinvulnerability();
		self closemenu();
		wait(1.5);
		self thread thehulk();
		self thread hulksmash();
		self thread hulkquake();
		self thread hulkdone();
		self setperk("specialty_unlimitedsprint");
		self setperk("specialty_sprintrecovery");
		self setperk("specialty_stunprotection");
		self setperk("specialty_pin_back");
		self setperk("specialty_flashprotection");
		self setperk("specialty_flakjacket");
		self setperk("specialty_fasttoss");
		self setperk("specialty_fastmantle");
		self setperk("specialty_fallheight");
		self setperk("specialty_fastequipmentuse");
		self setperk("specialty_fastreload");
		self setperk("specialty_fastmeleerecovery");
		self setperk("specialty_movefaster");
		self setperk("specialty_healthregen");
		self iprintln("^5Press [{+frag}] To Throw A Helicopter");
		self.maxhealth = 999;
		self disableusability();
		self disableweaponcycling();
		self setmodel("defaultactor");
		self giveweapon("defaultweapon_mp");
		self switchtoweapon("defaultweapon_mp");
		self givemaxammo("defaultweapon_mp");
		self iprintln("^5Press [{+switchseat}] To Turn Hulk ^1OFF");
		self setvisionsetforplayer("infrared", 0);
		self useservervisionset(1);
	}
	else
	{
		self iprintlnbold("There can only be one Hulk!");
	}
}

/*
	Name: thehulk
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE1EDD0B9
	Offset: 0x18D6E
	Size: 0x13E
	Parameters: 0
	Flags: None
*/
function thehulk()
{
	self endon("death");
	self endon("disconnect");
	self endon("koral");
	self takeweapon(self getcurrentoffhand());
	self giveweapon("destructible_car_mp");
	for(;;)
	{
		self waittill("grenade_fire", grenade, weaponname);
		self takeweapon(self getcurrentoffhand());
		self giveweapon("destructible_car_mp");
		if(weaponname == "destructible_car_mp")
		{
			grenade hide();
			self.boom = spawn("script_model", grenade.origin);
			self.boom setmodel("veh_t6_drone_overwatch_light");
			self.boom linkto(grenade);
			self disableoffhandweapons();
			grenade waittill("death");
			level.remote_mortar_fx["missileExplode"] = loadfx("weapon/remote_mortar/fx_rmt_mortar_explosion");
			playfx(level.remote_mortar_fx["missileExplode"], self.boom.origin);
			radiusdamage(self.boom.origin, 400, 400, 300, self, "MOD_EXPLOSIVE");
			self.boom delete();
			self enableoffhandweapons();
		}
	}
	for(;;)
	{
		wait(0.05);
	}
}

/*
	Name: hulkdone
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC647BB07
	Offset: 0x18EAE
	Size: 0x19A
	Parameters: 0
	Flags: None
*/
function hulkdone()
{
	while(self changeseatbuttonpressed())
	{
		if(isdefined(level.hulkamania))
		{
			level.hulkamania = 0;
		}
		self enableusability();
		self.maxhealth = 100;
		self enableweaponcycling();
		self unsetperk("specialty_unlimitedsprint");
		self unsetperk("specialty_sprintrecovery");
		self unsetperk("specialty_stunprotection");
		self unsetperk("specialty_pin_back");
		self unsetperk("specialty_flashprotection");
		self unsetperk("specialty_flakjacket");
		self unsetperk("specialty_fasttoss");
		self unsetperk("specialty_fastmantle");
		self unsetperk("specialty_fallheight");
		self unsetperk("specialty_fastequipmentuse");
		self unsetperk("specialty_fastreload");
		self unsetperk("specialty_fastmeleerecovery");
		self unsetperk("specialty_movefaster");
		self unsetperk("specialty_healthregen");
		self useservervisionset(0);
		self enableoffhandweapons();
		self [[game["set_player_model"][self.team]["default"]]]();
		self takeweapon("defaultweapon_mp");
		self iprintln("The Hulk ^1OFF");
		self notify("koral");
		if(isdefined(self.boom))
		{
			self.boom delete();
		}
		wait(0.05);
		break;
		wait(0.05);
	}
}

/*
	Name: hulksmash
	Namespace: _imcsx_gsc_studio
	Checksum: 0x96C69F73
	Offset: 0x1904A
	Size: 0x10E
	Parameters: 0
	Flags: None
*/
function hulksmash()
{
	self endon("disconnect");
	self endon("death");
	self endon("koral");
	if(!isdefined(self.isearthquake))
	{
		self.isearthquake = 1;
	}
	while(isdefined(self.isearthquake))
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "defaultweapon_mp")
		{
			self iprintlnbold("^2HULK SMASH!");
			position = bullettrace(self gettagorigin("j_head"), self gettagorigin("j_head") + AnglesToForward(self getplayerangles()) * 1000000, 0, self)["position"];
			earthquake(0.9, 0.9, self.origin, 400);
			playrumbleonposition("grenade_rumble", self.origin);
			foreach(person in level.players)
			{
				person playsound("wpn_rocket_explode_rock");
			}
			wait(0.05);
		}
	}
}

/*
	Name: hulkquake
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAD282305
	Offset: 0x1915A
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function hulkquake()
{
	self endon("disconnect");
	self endon("death");
	self endon("koral");
	for(;;)
	{
		self waittill("weapon_fired");
		forward = self gettagorigin("j_head");
		end = VectorScale(AnglesToForward(self getplayerangles()), 1000000);
		explocation = bullettrace(forward, end, 0, self)["position"];
		radiusdamage(explocation, 300, 500, 400, self);
		wait(0.05);
	}
}

/*
	Name: saveandload
	Namespace: _imcsx_gsc_studio
	Checksum: 0x490E46DE
	Offset: 0x191DA
	Size: 0x6C
	Parameters: 0
	Flags: None
*/
function saveandload()
{
	if(self.snl == 0)
	{
		self iprintlnbold("^5Save and Load: ^2On");
		self iprintln("^5Press [{+actionslot 3}] to Save");
		self iprintln("^5Press [{+actionslot 4}] to Load");
		self thread dosaveandload();
		self.snl = 1;
	}
	else
	{
		self iprintlnbold("^5Save and Load: ^1Off");
		self.snl = 0;
		self notify("SaveandLoad");
	}
}

/*
	Name: dosaveandload
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2D5DAB8A
	Offset: 0x19248
	Size: 0xBC
	Parameters: 0
	Flags: None
*/
function dosaveandload()
{
	self endon("disconnect");
	self endon("SaveandLoad");
	load = 0;
	while(self actionslotthreebuttonpressed() && self.snl == 1)
	{
		self.o = self.origin;
		self.a = self.angles;
		load = 1;
		self iprintlnbold("^3Position ^2Saved");
		wait(0.1);
		if(self actionslotfourbuttonpressed() && load == 1 && self.snl == 1)
		{
			self setplayerangles(self.a);
			self setorigin(self.o);
			self iprintlnbold("^3Position ^5Loaded");
			wait(0.1);
		}
		wait(0.05);
	}
}

/*
	Name: changeclass
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE019E576
	Offset: 0x19306
	Size: 0x42
	Parameters: 0
	Flags: None
*/
function changeclass()
{
	self endon("disconnect");
	self endon("death");
	self maps/mp/gametypes/_globallogic_ui::beginclasschoice();
	while(self.pers["changed_class"])
	{
		self maps/mp/gametypes/_class::giveloadout(self.team, self.class);
		wait(0.05);
	}
}

/*
	Name: thirdperson
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2B8F18E3
	Offset: 0x1934A
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function thirdperson()
{
	if(self.tpp == 1)
	{
		self setclientthirdperson(1);
		self iprintln("^7Third Person: [^2ON^7]");
		self.tpp = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self iprintln("^7Third Person: [^1OFF^7]");
		self.tpp = 1;
	}
}

/*
	Name: playeranglestoforward
	Namespace: _imcsx_gsc_studio
	Checksum: 0x56DD663
	Offset: 0x1939E
	Size: 0x1E
	Parameters: 2
	Flags: None
*/
function playeranglestoforward(player, distance)
{
	return player.origin + VectorScale(AnglesToForward(player getplayerangles()), distance);
}

/*
	Name: wp
	Namespace: _imcsx_gsc_studio
	Checksum: 0x55B5A892
	Offset: 0x193BE
	Size: 0x8A
	Parameters: 3
	Flags: None
*/
function wp(d, z, p)
{
	l = strtok(d, ",");
	for(i = 0; i < l.size;  = 0)
	{
		b = spawn("script_model", self.origin + (int(l[i]), int(l[i + 1]), z));
		if(!p)
		{
			b.angles = (90, 0, 0);
		}
		b setmodel("t6_wpn_supply_drop_ally");
	}
}

/*
	Name: house
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC56E251C
	Offset: 0x1944A
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function house()
{
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,275,30,0,60,275,60,0,90,0,120,0,150,0,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 0, 0);
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,275,30,0,60,275,60,0,90,0,120,0,150,0,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 23, 0);
	wp("0,0,25,0,50,0,225,0,250,0,275,0,0,30,275,30,0,60,275,60,0,90,0,120,0,150,0,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,225,270,250,270,275,270", 56, 0);
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,275,30,0,60,275,60,0,90,275,90,0,120,275,120,0,150,275,150,0,180,275,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 90, 0);
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,25,30,50,30,75,30,100,30,125,30,150,30,175,30,200,30,225,30,250,30,275,30,0,60,25,60,50,60,75,60,100,60,125,60,150,60,175,60,200,60,225,60,250,60,275,60,0,90,25,90,50,90,75,90,100,90,125,90,150,90,175,90,200,90,225,90,250,90,275,90,0,120,25,120,50,120,75,120,100,120,125,120,150,120,175,120,200,120,225,120,250,120,275,120,0,150,25,150,50,150,75,150,100,150,125,150,150,150,175,150,200,150,225,150,250,150,275,150,0,180,25,180,50,180,75,180,100,180,125,180,150,180,175,180,200,180,225,180,250,180,275,180,0,210,25,210,50,210,75,210,100,210,125,210,150,210,175,210,200,210,225,210,250,210,275,210,0,240,25,240,50,240,75,240,100,240,125,240,150,240,175,240,200,240,225,240,250,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 128, 0);
}

/*
	Name: housethread
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEC0A7992
	Offset: 0x1949A
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function housethread()
{
	if(self.houseisspawned == 0)
	{
		self.houseisspawned = 1;
		self iprintln("House: ^1Spawned");
		self thread house();
	}
	else
	{
		self iprintln("House: ^1Allready spawned");
	}
}

/*
	Name: bunker
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD9517AA2
	Offset: 0x194DA
	Size: 0x7F
	Parameters: 0
	Flags: None
*/
function bunker()
{
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,150,30,275,30,0,60,275,60,0,90,0,120,0,150,0,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 0, 0);
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,125,30,275,30,0,60,275,60,0,90,0,120,0,150,0,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 23, 0);
	wp("0,0,25,0,50,0,75,0,200,0,225,0,250,0,275,0,0,30,100,30,275,30,0,60,275,60,0,90,0,120,0,150,0,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,200,270,225,270,250,270,275,270", 56, 0);
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,75,30,275,30,0,60,275,60,0,90,275,90,0,120,275,120,0,150,275,150,0,180,275,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 85, 0);
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,25,30,50,30,200,30,225,30,250,30,275,30,0,60,25,60,200,60,225,60,250,60,275,60,0,90,25,90,200,90,225,90,250,90,275,90,0,120,25,120,50,120,75,120,100,120,125,120,150,120,175,120,200,120,225,120,250,120,275,120,0,150,25,150,50,150,75,150,100,150,125,150,150,150,175,150,200,150,225,150,250,150,275,150,0,180,25,180,50,180,75,180,100,180,125,180,150,180,175,180,200,180,225,180,250,180,275,180,0,210,25,210,50,210,75,210,100,210,125,210,150,210,175,210,200,210,225,210,250,210,275,210,0,240,25,240,50,240,75,240,100,240,125,240,150,240,175,240,200,240,225,240,250,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 120, 0);
	wp("0,0,25,0,50,0,75,0,100,0,125,0,150,0,175,0,200,0,225,0,250,0,275,0,0,30,275,30,0,60,275,60,0,90,275,90,0,120,275,120,0,150,275,150,0,180,275,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,100,270,125,270,150,270,175,270,200,270,225,270,250,270,275,270", 141, 0);
	wp("0,0,25,0,50,0,75,0,200,0,225,0,250,0,275,0,0,30,275,30,0,60,275,60,0,90,0,120,0,150,0,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,200,270,225,270,250,270,275,270", 162, 0);
	wp("0,0,25,0,50,0,75,0,200,0,225,0,250,0,275,0,0,30,275,30,0,60,275,60,0,90,0,120,0,150,0,180,0,210,275,210,0,240,275,240,0,270,25,270,50,270,75,270,200,270,225,270,250,270,275,270", 184, 0);
}

/*
	Name: bunkerthread
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6BFC640C
	Offset: 0x1955A
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function bunkerthread()
{
	if(self.bunkerisspawned == 0)
	{
		self.bunkerisspawned = 1;
		self iprintln("^1Castle: ^2Spawned");
		self thread bunker();
	}
	else
	{
		self iprintln("^1Bunker: ^2Allready spawned");
	}
}

/*
	Name: bridge
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEAB7A0D2
	Offset: 0x1959A
	Size: 0x5F
	Parameters: 0
	Flags: None
*/
function bridge()
{
	wp("25,90,450,90,25,120,450,120,25,150,450,150,25,180,450,180,25,210,450,210", 0, 0);
	wp("50,90,425,90,50,120,425,120,50,150,425,150,50,180,425,180,50,210,425,210", 20, 0);
	wp("75,90,400,90,75,120,400,120,75,150,400,150,75,180,400,180,75,210,400,210", 40, 0);
	wp("100,90,375,90,100,120,375,120,100,150,375,150,100,180,375,180,100,210,375,210", 60, 0);
	wp("125,90,150,90,175,90,200,90,225,90,250,90,275,90,300,90,325,90,350,90,125,120,150,120,175,120,200,120,225,120,250,120,275,120,300,120,325,120,350,120,125,150,150,150,175,150,200,150,225,150,250,150,275,150,300,150,325,150,350,150,125,180,150,180,175,180,200,180,225,180,250,180,275,180,300,180,325,180,350,180,125,210,150,210,175,210,200,210,225,210,250,210,275,210,300,210,325,210,350,210", 80, 0);
	wp("125,90,150,90,175,90,200,90,225,90,250,90,275,90,300,90,325,90,350,90,125,210,150,210,175,210,200,210,225,210,250,210,275,210,300,210,325,210,350,210", 115, 0);
}

/*
	Name: bridgethread
	Namespace: _imcsx_gsc_studio
	Checksum: 0x81A77D95
	Offset: 0x195FA
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function bridgethread()
{
	if(self.bridgeisspawned == 0)
	{
		self.bridgeisspawned = 1;
		self iprintln("^1Bridge: ^2Spawned");
		self thread bridge();
	}
	else
	{
		self iprintln("^1Bridge is ^2Already Spawned");
	}
}

/*
	Name: hakenkreuz
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2F91A148
	Offset: 0x1963A
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function hakenkreuz()
{
	wp("75,150,100,150,125,150,150,150,175,150,200,150,225,150,250,150,275,150,300,150,325,150,475,150,325,180,475,180,325,210,475,210,325,240,475,240,325,270,475,270,325,300,475,300,100,330,125,330,150,330,175,330,200,330,225,330,250,330,275,330,300,330,325,330,350,330,375,330,400,330,425,330,450,330,475,330,100,360,325,360,100,390,325,390,100,420,325,420,100,450,325,450,100,480,325,480,350,480,375,480,400,480,425,480,450,480,475,480,500,480,525,480,550,480,575,480", 400, 0);
}

/*
	Name: hakenkreuzthread
	Namespace: _imcsx_gsc_studio
	Checksum: 0x61D0974
	Offset: 0x1964E
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function hakenkreuzthread()
{
	if(self.hakenkreuzisspawned == 0)
	{
		self.hakenkreuzisspawned = 1;
		self iprintln("^1Nazi Sign: ^2Spawned");
		self thread hakenkreuz();
	}
	else
	{
		self iprintln("^1Nazi Sign: ^2Allready spawned");
	}
}

/*
	Name: inf_game
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD650FF07
	Offset: 0x1968E
	Size: 0x93
	Parameters: 0
	Flags: None
*/
function inf_game()
{
	if(self.ingame == 0)
	{
		self.ingame = 1;
		setdvar("scr_dom_scorelimit", 0);
		setdvar("scr_sd_numlives", 0);
		setdvar("scr_war_timelimit", 0);
		setdvar("scr_game_onlyheadshots", 0);
		setdvar("scr_war_scorelimit", 0);
		setdvar("scr_player_forcerespawn", 1);
		maps/mp/gametypes/_globallogic_utils::pausetimer();
		self iprintlnbold("Infinite Game : ^2ON");
	}
	else
	{
		self maps/mp/gametypes/_globallogic_utils::resumetimer();
		self iprintlnbold("Infinite Game : ^1OFF");
	}
}

/*
	Name: dokillstreaks
	Namespace: _imcsx_gsc_studio
	Checksum: 0x733AEA3A
	Offset: 0x19722
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function dokillstreaks()
{
	maps/mp/gametypes/_globallogic_score::_setplayermomentum(self, 9999);
}

/*
	Name: magicbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5C9C2385
	Offset: 0x19732
	Size: 0x66
	Parameters: 0
	Flags: None
*/
function magicbullet()
{
	self endon("disconnect");
	self endon("death");
	for(;;)
	{
		self waittill("weapon_fired");
		forward = AnglesToForward(self getplayerangles());
		start = self geteye();
		end = VectorScale(forward, 9999);
		magicbullet("ai_tank_drone_rocket_mp", start, bullettrace(start, start + end, 0, undefined)["position"], self);
	}
}

/*
	Name: initrpgbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x48B900B1
	Offset: 0x1979A
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function initrpgbullet()
{
	if(self.rpgtog == 0)
	{
		self iprintln("RPG Bullets ^2ON");
		self thread rpgbullet();
		self.rpgtog = 1;
	}
	else
	{
		self iprintln("RPG Bullets ^1OFF");
		self notify("stopRPG");
		self.rpgtog = 0;
	}
}

/*
	Name: rpgbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x42F52713
	Offset: 0x197E8
	Size: 0x6C
	Parameters: 0
	Flags: None
*/
function rpgbullet()
{
	self endon("disconnect");
	self endon("death");
	self endon("stopRPG");
	for(;;)
	{
		self waittill("weapon_fired");
		forward = AnglesToForward(self getplayerangles());
		start = self geteye();
		end = VectorScale(forward, 9999);
		magicbullet("usrpg_mp", start, bullettrace(start, start + end, 0, undefined)["position"], self);
	}
}

/*
	Name: doantiquit
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA8C6A3B4
	Offset: 0x19856
	Size: 0x52
	Parameters: 0
	Flags: None
*/
function doantiquit()
{
	self endon("disconnect");
	self endon("Stopquittin");
	for(;;)
	{
		foreach(player in level.players)
		{
			player maps/mp/gametypes/_globallogic_ui::closemenus();
		}
		wait(0.05);
	}
}

/*
	Name: toggleragequit
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCB98A792
	Offset: 0x198AA
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function toggleragequit()
{
	if(self.antiquit == 0)
	{
		self thread doantiquit();
		self iprintln("Anti Quit [^2ON^7]");
		self.antiquit = 1;
	}
	else
	{
		self notify("Stopquittin");
		self iprintln("Anti Quit [^1OFF^7]");
		self.antiquit = 0;
	}
}

/*
	Name: togglevision
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCD5748DE
	Offset: 0x198F8
	Size: 0x113
	Parameters: 0
	Flags: None
*/
function togglevision()
{
	if(self.fovs == 0)
	{
		self setinfraredvision(1);
		self iprintln("Vision : ^2Thermal");
		self.fovs = 1;
	}
	else if(self.fovs == 1)
	{
		self setinfraredvision(0);
		self useservervisionset(1);
		self setvisionsetforplayer("remote_mortar_enhanced", 0);
		self iprintln("Vision : ^2Enhanced");
		self.fovs = 2;
	}
	else if(self.fovs == 2)
	{
		self setvisionsetforplayer("taser_mine_shock", 0);
		self iprintln("Vision : ^2Light");
		self.fovs = 3;
	}
	else if(self.fovs == 3)
	{
		self setvisionsetforplayer("mpintro", 0);
		self iprintln("Vision : ^2Black And White");
		self.fovs = 4;
	}
	else if(self.fovs == 4)
	{
		self useservervisionset(0);
		self iprintln("Vision : ^2Default");
		self.fovs = 0;
	}
}

/*
	Name: domaster
	Namespace: _imcsx_gsc_studio
	Checksum: 0x31108CE9
	Offset: 0x19A0C
	Size: 0x51
	Parameters: 0
	Flags: None
*/
function domaster()
{
	self.pers["plevel"] = level.maxprestige;
	self setdstat("playerstatslist", "plevel", "StatValue", level.maxprestige);
	self setrank(level.maxrank, level.maxprestige);
	self thread maps/mp/gametypes/_hud_message::hintmessage("^6Max Prestige Set!");
}

/*
	Name: dorank
	Namespace: _imcsx_gsc_studio
	Checksum: 0x89F09429
	Offset: 0x19A5E
	Size: 0x73
	Parameters: 0
	Flags: None
*/
function dorank()
{
	self.pers["rank"] = level.maxrank;
	self setdstat("playerstatslist", "rank", "StatValue", level.maxrank);
	self.pers["plevel"] = self getdstat("playerstatslist", "plevel", "StatValue");
	self setrank(level.maxrank, self.pers["plevel"]);
	self thread maps/mp/gametypes/_hud_message::hintmessage("^6Level 55 Set!");
}

/*
	Name: kickplayer
	Namespace: _imcsx_gsc_studio
	Checksum: 0x434262D
	Offset: 0x19AD2
	Size: 0x67
	Parameters: 1
	Flags: None
*/
function kickplayer(player)
{
	if(player ishost())
	{
		self iprintln("You Cannot Kick The " + verificationtocolor("Host"));
	}
	else
	{
		kick(player getentitynumber());
		wait(0.5);
		self submenu(self.menu.previousmenu[self.menu.currentmenu]);
	}
}

/*
	Name: banplayer
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBA597B3
	Offset: 0x19B3A
	Size: 0x67
	Parameters: 1
	Flags: None
*/
function banplayer(player)
{
	if(player ishost())
	{
		self iprintln("You Cannot Ban The " + verificationtocolor("Host"));
	}
	else
	{
		ban(player getentitynumber());
		wait(0.5);
		self submenu(self.menu.previousmenu[self.menu.currentmenu]);
	}
}

/*
	Name: getname
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4F1096A0
	Offset: 0x19BA2
	Size: 0x64
	Parameters: 0
	Flags: None
*/
function getname()
{
	nt = getsubstr(self.name, 0, self.name.size);
	for(i = 0; i < nt.size; i++)
	{
		if(nt[i] == "]")
		{
			break;
		}
	}
	if(nt.size != i)
	{
		nt = getsubstr(nt, i + 1, nt.size);
	}
	return nt;
}

/*
	Name: initaimbot1
	Namespace: _imcsx_gsc_studio
	Checksum: 0x71C590B5
	Offset: 0x19C08
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function initaimbot1()
{
	if(self.aim1 == 0)
	{
		self thread aimbot1();
		self.aim1 = 1;
		self iprintln("^5TrickShot Aimbot: ^2ON");
	}
	else
	{
		self notify("EndAutoAim1");
		self.aim1 = 0;
		self iprintln("^5TrickShot Aimbot: ^1OFF");
	}
}

/*
	Name: aimbot1
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA26F0D12
	Offset: 0x19C56
	Size: 0x14E
	Parameters: 0
	Flags: None
*/
function aimbot1()
{
	self endon("disconnect");
	self endon("death");
	self endon("EndAutoAim1");
	for(;;)
	{
		aimat = undefined;
		foreach(player in level.players)
		{
			if(player == self || !isalive(player) || (level.teambased && self.pers["team"] == player.pers["team"]) || (player ishost() || player.status == "Co-Host") || player.status == "Admin")
			{
				continue;
			}
			if(isdefined(aimat))
			{
				if(closer(self gettagorigin("pelvis"), player gettagorigin("pelvis"), aimat gettagorigin("pelvis")))
				{
					aimat = player;
				}
				continue;
			}
			aimat = player;
		}
		if(isdefined(aimat))
		{
			if(self attackbuttonpressed())
			{
				if(self attackbuttonpressed())
				{
					aimat thread [[level.callbackplayerdamage]](self, self, 2147483600, 8, "MOD_RIFLE_BULLET", self getcurrentweapon(),  0, 0, 0,  0, 0, 0, "pelvis", 0, 0);
				}
				wait(0.01);
			}
		}
		wait(0.01);
	}
}

/*
	Name: wfired
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBD818664
	Offset: 0x19DA6
	Size: 0x30
	Parameters: 0
	Flags: None
*/
function wfired()
{
	self endon("disconnect");
	self endon("death");
	self endon("EndAutoAim");
	for(;;)
	{
		self waittill("weapon_fired");
		self.fire = 1;
		wait(0.05);
		self.fire = 0;
	}
}

/*
	Name: initaimbot2
	Namespace: _imcsx_gsc_studio
	Checksum: 0x706B02A6
	Offset: 0x19DD8
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function initaimbot2()
{
	if(self.aim2 == 0)
	{
		self thread aimbot2();
		self.aim2 = 1;
		self iprintln("Unfair Aimbot ^2ON");
	}
	else
	{
		self notify("EndAutoAim2");
		self.aim2 = 0;
		self iprintln("Unfair Aimbot ^1OFF");
	}
}

/*
	Name: aimbot2
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5D969462
	Offset: 0x19E26
	Size: 0x14E
	Parameters: 0
	Flags: None
*/
function aimbot2()
{
	self endon("disconnect");
	self endon("death");
	self endon("EndAutoAim2");
	for(;;)
	{
		aimat = undefined;
		foreach(player in level.players)
		{
			if(player == self || !isalive(player) || (level.teambased && self.pers["team"] == player.pers["team"]) || (player ishost() || player.status == "Co-Host") || player.status == "Admin")
			{
				continue;
			}
			if(isdefined(aimat))
			{
				if(closer(self gettagorigin("j_head"), player gettagorigin("j_head"), aimat gettagorigin("j_head")))
				{
					aimat = player;
				}
				continue;
			}
			aimat = player;
		}
		if(isdefined(aimat))
		{
			if(self adsbuttonpressed())
			{
				if(self attackbuttonpressed())
				{
					aimat thread [[level.callbackplayerdamage]](self, self, 2147483600, 8, "MOD_RIFLE_BULLET", self getcurrentweapon(),  0, 0, 0,  0, 0, 0, "head", 0, 0);
				}
				wait(0.01);
			}
		}
		wait(0.01);
	}
}

/*
	Name: autoaimbot
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4B030F8E
	Offset: 0x19F76
	Size: 0x152
	Parameters: 0
	Flags: None
*/
function autoaimbot()
{
	self endon("disconnect");
	self endon("death");
	self endon("EndAutoAim");
	for(;;)
	{
		aimat = undefined;
		foreach(player in level.players)
		{
			if(player == self || !isalive(player) || (level.teambased && self.pers["team"] == player.pers["team"]) || player ishost())
			{
				continue;
			}
			if(isdefined(aimat))
			{
				if(closer(self gettagorigin("j_head"), player gettagorigin("j_head"), aimat gettagorigin("j_head")))
				{
					aimat = player;
				}
				continue;
			}
			aimat = player;
		}
		if(isdefined(aimat))
		{
			if(self adsbuttonpressed())
			{
				self setplayerangles(VectorToAngles(aimat gettagorigin("j_head") - self gettagorigin("j_head")));
				if(self attackbuttonpressed())
				{
					aimat thread [[level.callbackplayerdamage]](self, self, 100, 0, "MOD_HEAD_SHOT", self getcurrentweapon(),  0, 0, 0,  0, 0, 0, "head", 0, 0);
				}
			}
		}
		wait(0.01);
	}
}

/*
	Name: thermal
	Namespace: _imcsx_gsc_studio
	Checksum: 0x44227F2E
	Offset: 0x1A0CA
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function thermal()
{
	if(self.thermal == 1)
	{
		self setinfraredvision(1);
		self setvisionsetforplayer("remote_mortar_enhanced", 0);
		self iprintln("^7Thermal Vision : ^2ON");
		self.thermal = 0;
	}
	else
	{
		self setinfraredvision(0);
		self iprintln("^7Thermal Vision : ^1OFF");
		self.thermal = 1;
	}
}

/*
	Name: bwv
	Namespace: _imcsx_gsc_studio
	Checksum: 0x427B1A81
	Offset: 0x1A12E
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function bwv()
{
	if(self.bw == 1)
	{
		self useservervisionset(1);
		self setvisionsetforplayer("mpintro", 0);
		self iprintln("^7Black and White: ^2ON");
		self.bw = 0;
	}
	else
	{
		self useservervisionset(0);
		self iprintln("^7Black and White: ^1OFF");
		self.bw = 1;
	}
}

/*
	Name: poisonv
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE877DF68
	Offset: 0x1A192
	Size: 0x99
	Parameters: 0
	Flags: None
*/
function poisonv()
{
	if(self.poisonv == 1)
	{
		setdvar("r_waterSheetingFX_enable", "0");
		setdvar("r_poisonFX_debug_enable", "1");
		self iprintln("^7Poison Vision : ^2ON");
		self.poisonv = 0;
		self.disablewater2 = 0;
		self.disablewater = 1;
	}
	else
	{
		setdvar("r_waterSheetingFX_enable", "1");
		setdvar("r_poisonFX_debug_enable", "0");
		self iprintln("^7Poisonv Vision : ^1OFF");
		self.poisonv = 1;
		self.disablewater2 = 1;
		self.disablewater = 0;
	}
}

/*
	Name: mpintro
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA9AC295E
	Offset: 0x1A22C
	Size: 0x65
	Parameters: 0
	Flags: None
*/
function mpintro()
{
	if(self.mpintro == 1)
	{
		self useservervisionset(1);
		self setvisionsetforplayer("mpintro", 0);
		self iprintln("^7intro vision: ^2ON");
		self.mpintro = 0;
	}
	else
	{
		self useservervisionset(0);
		self iprintln("^7intro vision: ^1OFF");
		self.mpintro = 1;
	}
}

/*
	Name: defaultvision
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6895B624
	Offset: 0x1A292
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function defaultvision()
{
	if(self.defaultvision == 1)
	{
		self useservervisionset(1);
		self setvisionsetforplayer("default", 0);
		self iprintln("^7Default vision: ^2ON");
		self.defaultvision = 0;
	}
	else
	{
		self useservervisionset(0);
		self iprintln("^7Default vision: ^1OFF");
		self.defaultvision = 1;
	}
}

/*
	Name: taser_mine_shock
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6583F380
	Offset: 0x1A2F6
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function taser_mine_shock()
{
	if(self.taser == 1)
	{
		self useservervisionset(1);
		self setvisionsetforplayer("taser_mine_shock", 0);
		self iprintln("^7Taser vision: ^2ON");
		self.taser = 0;
	}
	else
	{
		self useservervisionset(0);
		self iprintln("^7Taser vision: ^1OFF");
		self.taser = 1;
	}
}

/*
	Name: mpoutro
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD5717E3C
	Offset: 0x1A35A
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function mpoutro()
{
	if(self.mpoutro == 1)
	{
		self useservervisionset(1);
		self setvisionsetforplayer("mpoutro", 0);
		self iprintln("^7Outro vision: ^2ON");
		self.mpoutro = 0;
	}
	else
	{
		self useservervisionset(0);
		self iprintln("^7Outro vision: ^1OFF");
		self.mpoutro = 1;
	}
}

/*
	Name: remote_mortar_infrared
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA8E13C5F
	Offset: 0x1A3BE
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function remote_mortar_infrared()
{
	if(self.mortar == 1)
	{
		self useservervisionset(1);
		self setvisionsetforplayer("remote_mortar_infrared", 0);
		self iprintln("^7Mortal Infrared vision: ^2ON");
		self.mortar = 0;
	}
	else
	{
		self useservervisionset(0);
		self iprintln("^7Mortal Infrared vision: ^1OFF");
		self.mortar = 1;
	}
}

/*
	Name: infrared
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5D4AAF2E
	Offset: 0x1A422
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function infrared()
{
	if(self.infrared == 1)
	{
		self useservervisionset(1);
		self setvisionsetforplayer("infrared", 0);
		self iprintln("^7Infrared vision: ^2ON");
		self.infrared = 0;
	}
	else
	{
		self useservervisionset(0);
		self iprintln("^7Infrared vision: ^1OFF");
		self.infrared = 1;
	}
}

/*
	Name: infrared_snow
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE62D7444
	Offset: 0x1A486
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function infrared_snow()
{
	if(self.snow == 1)
	{
		self useservervisionset(1);
		self setvisionsetforplayer("infrared_snow", 0);
		self iprintln("^7Infrared snow vision: ^2ON");
		self.snow = 0;
	}
	else
	{
		self useservervisionset(0);
		self iprintln("^7Infrared snow vision: ^1OFF");
		self.snow = 1;
	}
}

/*
	Name: drown
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4A9F66CC
	Offset: 0x1A4EA
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function drown()
{
	if(self.drown == 1)
	{
		setdvar("r_waterSheetingFX_enable", "1");
		self iprintln("^7Water Vision : ^2ON");
		self.drown = 0;
	}
	else
	{
		setdvar("r_waterSheetingFX_enable", "0");
		self iprintln("^7Water Vision : ^1OFF");
		self.drown = 1;
	}
}

/*
	Name: emp
	Namespace: _imcsx_gsc_studio
	Checksum: 0x66927503
	Offset: 0x1A546
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function emp()
{
	if(self.emp == 1)
	{
		self setempjammed(1);
		self setvisionsetforplayer("remote_mortar_enhanced", 0);
		self iprintln("^7EMP Vision : ^2ON");
		self.emp = 0;
	}
	else
	{
		self setempjammed(0);
		self iprintln("^7EMP Vision : ^1OFF");
		self.emp = 1;
	}
}

/*
	Name: dosky
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8FB3BBCB
	Offset: 0x1A5AA
	Size: 0x103
	Parameters: 0
	Flags: None
*/
function dosky()
{
	if(self.skycolor == 0)
	{
		self iprintln("^2Sky - 1");
		setdvar("r_skyColorTemp", "1234");
		self.skycolor = 1;
	}
	else if(self.skycolor == 1)
	{
		self iprintln("^2Sky - 2");
		self.skycolor = 2;
		setdvar("r_skyColorTemp", "2345");
	}
	else if(self.skycolor == 2)
	{
		self iprintln("^2Sky - 3");
		self.skycolor = 3;
		setdvar("r_skyColorTemp", "3456");
	}
	else if(self.skycolor == 3)
	{
		self iprintln("^2Sky - 4");
		self.skycolor = 4;
		setdvar("r_skyColorTemp", "4567");
	}
	else if(self.skycolor == 4)
	{
		self iprintln("^2Sky - 5");
		self.skycolor = 0;
		setdvar("r_skyColorTemp", "5678");
	}
}

/*
	Name: quake
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1EB8C5C
	Offset: 0x1A6AE
	Size: 0x2B
	Parameters: 0
	Flags: None
*/
function quake()
{
	self iprintln("^1Drop LIKE AN EARTHQUAKE!");
	earthquake(0.6, 10, self.origin, 100000);
}

/*
	Name: doallunlockcamos
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBD781CCB
	Offset: 0x1A6DA
	Size: 0x27
	Parameters: 0
	Flags: None
*/
function doallunlockcamos()
{
System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.
Parameter name: index
   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)
   at System.Collections.Generic.List`1.get_Item(Int32 index)
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‮​⁬⁭⁮‍‏‏‫‎‭‫⁮‪‮⁭‮⁬​‌⁯‮⁭‬​‪⁭‍‏‪⁪‎⁭⁭‌⁪‌‭​⁯‮(ScriptOp , ‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‭⁭⁫‭⁪‫‭‮‪⁬‏‎‪⁯⁪⁬‪‏‫⁯⁯‭​‫⁯‍‮⁫‪‏⁫⁪‎‏‫‫‪⁬‌⁯‮(‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ , Int32 )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮..ctor(ScriptExport , ScriptBase )
}

/*
	Name: unlockallcamos
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6974BDAE
	Offset: 0x1A702
	Size: 0x323
	Parameters: 1
	Flags: None
*/
function unlockallcamos(i)
{
	self addweaponstat(i, "headshots", 5000);
	self addweaponstat(i, "kills", 5000);
	self addweaponstat(i, "direct_hit_kills", 100);
	self addweaponstat(i, "revenge_kill", 2500);
	self addweaponstat(i, "noAttKills", 2500);
	self addweaponstat(i, "noPerkKills", 2500);
	self addweaponstat(i, "multikill_2", 2500);
	self addweaponstat(i, "killstreak_5", 2500);
	self addweaponstat(i, "challenges", 5000);
	self addweaponstat(i, "multikill_2", 2500);
	self addweaponstat(i, "killstreak_5", 2500);
	self addweaponstat(i, "challenges", 5000);
	self addweaponstat(i, "longshot_kill", 750);
	self addweaponstat(i, "direct_hit_kills", 120);
	self addweaponstat(i, "destroyed_aircraft_under20s", 120);
	self addweaponstat(i, "destroyed_5_aircraft", 120);
	self addweaponstat(i, "destroyed_aircraft", 120);
	self addweaponstat(i, "kills_from_cars", 120);
	self addweaponstat(i, "destroyed_2aircraft_quickly", 120);
	self addweaponstat(i, "destroyed_controlled_killstreak", 120);
	self addweaponstat(i, "destroyed_qrdrone", 120);
	self addweaponstat(i, "destroyed_aitank", 120);
	self addweaponstat(i, "multikill_3", 120);
	self addweaponstat(i, "score_from_blocked_damage", 140);
	self addweaponstat(i, "shield_melee_while_enemy_shooting", 140);
	self addweaponstat(i, "hatchet_kill_with_shield_equiped", 140);
	self addweaponstat(i, "noLethalKills", 140);
	self addweaponstat(i, "ballistic_knife_kill", 5000);
	self addweaponstat(i, "kill_retrieved_blade", 160);
	self addweaponstat(i, "ballistic_knife_melee", 160);
	self addweaponstat(i, "kills_from_cars", 170);
	self addweaponstat(i, "crossbow_kill_clip", 170);
	self addweaponstat(i, "backstabber_kill", 190);
	self addweaponstat(i, "kill_enemy_with_their_weapon", 190);
	self addweaponstat(i, "kill_enemy_when_injured", 190);
	self addweaponstat(i, "primary_mastery", 10000);
	self addweaponstat(i, "secondary_mastery", 10000);
	self addweaponstat(i, "weapons_mastery", 10000);
	self addweaponstat(i, "kill_enemy_one_bullet_shotgun", 5000);
	self addweaponstat(i, "kill_enemy_one_bullet_sniper", 5000);
}

/*
	Name: camonlock
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7C54ABA7
	Offset: 0x1AA26
	Size: 0x33F
	Parameters: 0
	Flags: None
*/
function camonlock()
{
	self thread unlockallcamos("870mcs_mp");
	wait(2);
	self thread unlockallcamos("an94_mp");
	wait(2);
	self thread unlockallcamos("as50_mp");
	wait(2);
	self thread unlockallcamos("ballista_mp");
	wait(2);
	self thread unlockallcamos("beretta93r_dw_mp");
	wait(2);
	self thread unlockallcamos("beretta93r_lh_mp");
	wait(2);
	self thread unlockallcamos("beretta93r_mp");
	wait(2);
	self thread unlockallcamos("crossbow_mp");
	wait(2);
	self thread unlockallcamos("dsr50_mp");
	wait(2);
	self thread unlockallcamos("evoskorpion_mp");
	wait(2);
	self thread unlockallcamos("fiveseven_dw_mp");
	wait(2);
	self thread unlockallcamos("fiveseven_lh_mp");
	wait(2);
	self thread unlockallcamos("fiveseven_mp");
	wait(2);
	self thread unlockallcamos("fhj18_mp");
	wait(2);
	self thread unlockallcamos("fnp45_dw_mp");
	wait(2);
	self thread unlockallcamos("fnp45_lh_mp");
	wait(2);
	self thread unlockallcamos("fnp45_mp");
	wait(2);
	self thread unlockallcamos("hamr_mp");
	wait(2);
	self thread unlockallcamos("hk416_mp");
	wait(2);
	self thread unlockallcamos("insas_mp");
	wait(2);
	self thread unlockallcamos("judge_dw_mp");
	wait(2);
	self thread unlockallcamos("judge_lh_mp");
	wait(2);
	self thread unlockallcamos("judge_mp");
	wait(2);
	self thread unlockallcamos("kard_dw_mp");
	wait(2);
	self thread unlockallcamos("kard_lh_mp");
	wait(2);
	self thread unlockallcamos("kard_mp");
	wait(2);
	self thread unlockallcamos("kard_wager_mp");
	wait(2);
	self thread unlockallcamos("knife_ballistic_mp");
	wait(2);
	self thread unlockallcamos("knife_held_mp");
	wait(2);
	self thread unlockallcamos("knife_mp");
	wait(2);
	self thread unlockallcamos("ksg_mp");
	wait(2);
	self thread unlockallcamos("lsat_mp");
	wait(2);
	self thread unlockallcamos("mk48_mp");
	wait(2);
	self thread unlockallcamos("mp7_mp");
	wait(2);
	self thread unlockallcamos("pdw57_mp");
	wait(2);
	self thread unlockallcamos("peacekeeper_mp");
	wait(2);
	self thread unlockallcamos("qbb95_mp");
	wait(2);
	self thread unlockallcamos("qcw05_mp");
	wait(2);
	self thread unlockallcamos("riotshield_mp");
	wait(2);
	self thread unlockallcamos("sa58_mp");
	wait(2);
	self thread unlockallcamos("saiga12_mp");
	wait(2);
	self thread unlockallcamos("saritch_mp");
	wait(2);
	self thread unlockallcamos("scar_mp");
	wait(2);
	self thread unlockallcamos("sig556_mp");
	wait(2);
	self thread unlockallcamos("smaw_mp");
	wait(2);
	self thread unlockallcamos("srm1216_mp");
	wait(2);
	self thread unlockallcamos("svu_mp");
	wait(2);
	self thread unlockallcamos("tar21_mp");
	wait(2);
	self thread unlockallcamos("type95_mp");
	wait(2);
	self thread unlockallcamos("usrpg_mp");
	wait(2);
	self thread unlockallcamos("vector_mp");
	wait(2);
	self thread unlockallcamos("xm8_mp");
}

/*
	Name: giveallperks
	Namespace: _imcsx_gsc_studio
	Checksum: 0x88292B4D
	Offset: 0x1AD66
	Size: 0x40B
	Parameters: 0
	Flags: None
*/
function giveallperks()
{
	self clearperks();
	self setperk("specialty_additionalprimaryweapon");
	self setperk("specialty_armorpiercing");
	self setperk("specialty_armorvest");
	self setperk("specialty_bulletaccuracy");
	self setperk("specialty_bulletdamage");
	self setperk("specialty_bulletflinch");
	self setperk("specialty_bulletpenetration");
	self setperk("specialty_deadshot");
	self setperk("specialty_delayexplosive");
	self setperk("specialty_detectexplosive");
	self setperk("specialty_disarmexplosive");
	self setperk("specialty_earnmoremomentum");
	self setperk("specialty_explosivedamage");
	self setperk("specialty_extraammo");
	self setperk("specialty_fallheight");
	self setperk("specialty_fastads");
	self setperk("specialty_fastequipmentuse");
	self setperk("specialty_fastladderclimb");
	self setperk("specialty_fastmantle");
	self setperk("specialty_fastmeleerecovery");
	self setperk("specialty_fastreload");
	self setperk("specialty_fasttoss");
	self setperk("specialty_fastweaponswitch");
	self setperk("specialty_finalstand");
	self setperk("specialty_fireproof");
	self setperk("specialty_flakjacket");
	self setperk("specialty_flashprotection");
	self setperk("specialty_gpsjammer");
	self setperk("specialty_grenadepulldeath");
	self setperk("specialty_healthregen");
	self setperk("specialty_holdbreath");
	self setperk("specialty_immunecounteruav");
	self setperk("specialty_immuneemp");
	self setperk("specialty_immunemms");
	self setperk("specialty_immunenvthermal");
	self setperk("specialty_immunerangefinder");
	self setperk("specialty_killstreak");
	self setperk("specialty_longersprint");
	self setperk("specialty_loudenemies");
	self setperk("specialty_marksman");
	self setperk("specialty_movefaster");
	self setperk("specialty_nomotionsensor");
	self setperk("specialty_noname");
	self setperk("specialty_nottargetedbyairsupport");
	self setperk("specialty_nokillstreakreticle");
	self setperk("specialty_nottargettedbysentry");
	self setperk("specialty_pin_back");
	self setperk("specialty_pistoldeath");
	self setperk("specialty_proximityprotection");
	self setperk("specialty_quickrevive");
	self setperk("specialty_quieter");
	self setperk("specialty_reconnaissance");
	self setperk("specialty_rof");
	self setperk("specialty_scavenger");
	self setperk("specialty_showenemyequipment");
	self setperk("specialty_stunprotection");
	self setperk("specialty_shellshock");
	self setperk("specialty_sprintrecovery");
	self setperk("specialty_showonradar");
	self setperk("specialty_stalker");
	self setperk("specialty_twogrenades");
	self setperk("specialty_twoprimaries");
	self setperk("specialty_unlimitedsprint");
	self iprintln("All Perks ^2Set");
}

/*
	Name: xxspnorm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF703BE8D
	Offset: 0x1B172
	Size: 0x97
	Parameters: 4
	Flags: None
*/
function xxspnorm(slow, time, acc, li)
{
	self endon("death");
	self endon("disconnect");
	if(!isdefined(li))
	{
		li = 0;
	}
	if(self.lght == 1 && li == 0)
	{
		return;
	}
	if(!isdefined(acc))
	{
		acc = 0;
	}
	self setmovespeedscale(slow);
	wait(time);
	while(acc == 0)
	{
		break;
		slow = slow + 0.1;
		self setmovespeedscale(slow);
		if(slow == 1)
		{
			break;
		}
		wait(0.15);
	}
	self thread xxlwsp();
}

/*
	Name: xxlwsp
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1F742560
	Offset: 0x1B20A
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function xxlwsp()
{
	self setmovespeedscale(1);
	if(self.lght == 1)
	{
		self setmovespeedscale(1.4);
	}
}

/*
	Name: togglepickup
	Namespace: _imcsx_gsc_studio
	Checksum: 0x82EE0964
	Offset: 0x1B23A
	Size: 0x5D
	Parameters: 0
	Flags: None
*/
function togglepickup()
{
	if(self.pickup == 0)
	{
		self iprintln("Pickup Players: ^2ON");
		self iprintln("^2Hold [{+speed_throw}] To Pickup Player While Aiming At Him");
		self thread pickuplol();
		self.pickup = 1;
	}
	else
	{
		self iprintln("Pickup Players ^1OFF");
		self notify("stop_pickup");
		self.pickup = 0;
	}
}

/*
	Name: pickuplol
	Namespace: _imcsx_gsc_studio
	Checksum: 0x45612169
	Offset: 0x1B298
	Size: 0xFC
	Parameters: 0
	Flags: None
*/
function pickuplol()
{
	self endon("death");
	self endon("stop_pickup");
	self endon("unverified");
	while(self adsbuttonpressed())
	{
		trace = bullettrace(self gettagorigin("j_head"), self gettagorigin("j_head") + AnglesToForward(self getplayerangles()) * 1000000, 1, self);
		while(self adsbuttonpressed())
		{
			trace["entity"] freezecontrols(1);
			trace["entity"] setorigin(self gettagorigin("j_head") + AnglesToForward(self getplayerangles()) * 200);
			trace["entity"].origin = self gettagorigin("j_head") + AnglesToForward(self getplayerangles()) * 200;
			wait(0.05);
		}
		trace["entity"] freezecontrols(0);
		continue;
		wait(0.05);
	}
}

/*
	Name: forgeon
	Namespace: _imcsx_gsc_studio
	Checksum: 0x727D4E52
	Offset: 0x1B396
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function forgeon()
{
	if(self.forgeon == 0)
	{
		self thread forgemodeon();
		self iprintln("^1Forge Mode ^5ON ^1- ^1Hold [{+speed_throw}] to Move Objects");
		self.forgeon = 1;
	}
	else
	{
		self notify("stop_forge");
		self iprintln("^1Forge Mode ^1OFF");
		self.forgeon = 0;
	}
}

/*
	Name: forgemodeon
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE468A152
	Offset: 0x1B3E4
	Size: 0xD4
	Parameters: 0
	Flags: None
*/
function forgemodeon()
{
	self endon("death");
	self endon("stop_forge");
	while(self adsbuttonpressed())
	{
		trace = bullettrace(self gettagorigin("j_head"), self gettagorigin("j_head") + AnglesToForward(self getplayerangles()) * 1000000, 1, self);
		while(self adsbuttonpressed())
		{
			trace["entity"] setorigin(self gettagorigin("j_head") + AnglesToForward(self getplayerangles()) * 200);
			trace["entity"].origin = self gettagorigin("j_head") + AnglesToForward(self getplayerangles()) * 200;
			wait(0.05);
		}
		continue;
		wait(0.05);
	}
}

/*
	Name: ewwmodel
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF8B0E22D
	Offset: 0x1B4BA
	Size: 0xF
	Parameters: 1
	Flags: None
*/
function ewwmodel(modelnigga)
{
	self setmodel(modelnigga);
}

/*
	Name: togglerotaterocket
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2C384BBA
	Offset: 0x1B4CA
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function togglerotaterocket()
{
	if(self.rotaterocket == 0)
	{
		self.rotaterocket = 1;
		self thread rotaterocket();
		self iprintln("Rotate Rocket: [^2ON^7]");
	}
	else
	{
		self.rotaterocket = 0;
		level.ipro delete();
		self notify("RotateRocket");
		self iprintln("Rotate Rocket: [^1OFF^7]");
	}
}

/*
	Name: rotaterocket
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8723D25
	Offset: 0x1B526
	Size: 0x106
	Parameters: 0
	Flags: None
*/
function rotaterocket()
{
	self endon("disconnect");
	self endon("RotateRocket");
	level.ipro = spawn("script_model", self.origin + (0, 0, 40));
	level.ipro setmodel("projectile_sa6_missile_desert_mp");
	level.effect["1"] = loadfx("weapon/straferun/fx_straferun_chaf");
	while(1)
	{
		playfx(level.effect["1"], level.ipro.origin);
		wait(0.1);
		level.ipro moveto(level.ipro.origin + (0, 0, 40), 1);
		level.ipro rotateyaw(2039, 2);
		if(distance(self.origin, self.origin) < 155)
		{
			earthquake(0.2, 1, self.origin, 900000);
		}
		wait(2);
		level.ipro moveto(level.ipro.origin - (0, 0, 40), 0.1);
		wait(0.2);
	}
}

/*
	Name: speedx2
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAC9D8515
	Offset: 0x1B62E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function speedx2()
{
	self.speedscalex2 = booleanopposite(self.speedscalex2);
	self iprintln(booleanreturnval(self.speedscalex2, "Speed X2: [^1OFF^7]", "Speed X2: [^2ON^7]"));
	if(self.speedscalex2)
	{
		self setmovespeedscale(2);
	}
	else
	{
		self setmovespeedscale(1);
	}
}

/*
	Name: tracebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF40DF9A5
	Offset: 0x1B682
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function tracebullet()
{
	return bullettrace(self geteye(), self geteye() + VectorScale(AnglesToForward(self getplayerangles()), 1000000), 0, self)["position"];
}

/*
	Name: vector_scal
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAB40F1A6
	Offset: 0x1B6BC
	Size: 0x24
	Parameters: 2
	Flags: None
*/
function vector_scal(vec, scale)
{
	vec = (vec[0] * scale, vec[1] * scale, vec[2] * scale);
	return vec;
}

/*
	Name: v_sx
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAB40F1A6
	Offset: 0x1B6E2
	Size: 0x24
	Parameters: 2
	Flags: None
*/
function v_sx(vec, scale)
{
	vec = (vec[0] * scale, vec[1] * scale, vec[2] * scale);
	return vec;
}

/*
	Name: locationselector
	Namespace: _imcsx_gsc_studio
	Checksum: 0x51E1BC00
	Offset: 0x1B708
	Size: 0xAE
	Parameters: 0
	Flags: None
*/
function locationselector()
{
	self endon("disconnect");
	self endon("death");
	self beginlocationselection("map_mortar_selector");
	self disableoffhandweapons();
	self giveweapon("killstreak_remote_turret_mp");
	self switchtoweapon("killstreak_remote_turret_mp");
	self.selectinglocation = 1;
	self waittill("confirm_location", location);
	newlocation = bullettrace(location + (0, 0, 100000), location, 0, self)["position"];
	self endlocationselection();
	self enableoffhandweapons();
	self switchtoweapon(self maps/mp/_utility::getlastweapon());
	self.selectinglocation = undefined;
	return newlocation;
}

/*
	Name: teleporter
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4FBA2EA4
	Offset: 0x1B7B8
	Size: 0x25
	Parameters: 0
	Flags: None
*/
function teleporter()
{
	self setorigin(self locationselector());
	self iprintln("^2Teleported!");
}

/*
	Name: initglassbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2B4C0CD3
	Offset: 0x1B7DE
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initglassbullet()
{
	if(self.glassbulleton == 0)
	{
		self.glassbulleton = 1;
		self thread doglassbullet();
		self iprintln("^5Glass Bullets: ^2On");
	}
	else
	{
		self.glassbulleton = 0;
		self notify("stop_GlassBulletOn");
		self iprintln("^5Glass Bullets: ^1Off");
	}
}

/*
	Name: doglassbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x29EB1885
	Offset: 0x1B82E
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doglassbullet()
{
	self endon("death");
	self endon("stop_GlassBulletOn");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["fx_xtreme_glass_hit_mp"] = loadfx("impacts/fx_xtreme_glass_hit_mp");
		playfx(level._effect["fx_xtreme_glass_hit_mp"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initflashbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x59E9387D
	Offset: 0x1B8EA
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initflashbullet()
{
	if(self.flashbulleton == 0)
	{
		self.flashbulleton = 1;
		self thread doflashbullet();
		self iprintln("^3Flash Bullets: ^2On");
	}
	else
	{
		self.flashbulleton = 0;
		self notify("stop_FlashBullet");
		self iprintln("^3Flash Bullets: ^1Off");
	}
}

/*
	Name: doflashbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x72C73654
	Offset: 0x1B93A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doflashbullet()
{
	self endon("death");
	self endon("stop_FlashBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["ChafFx"] = loadfx("weapon/straferun/fx_straferun_chaf");
		playfx(level._effect["ChafFx"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: toggle_multijump
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCBB0A38C
	Offset: 0x1B9F6
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function toggle_multijump()
{
	if(self.multijump == 0)
	{
		self thread onplayermultijump();
		self.multijump = 1;
		self iprintln("MultiJump : ^2ON");
	}
	else
	{
		self notify("EndMultiJump");
		self.multijump = 0;
		self iprintln("MultiJump : ^1OFF");
	}
}

/*
	Name: landsonground
	Namespace: _imcsx_gsc_studio
	Checksum: 0x704B86A5
	Offset: 0x1BA46
	Size: 0x50
	Parameters: 0
	Flags: None
*/
function landsonground()
{
	self endon("disconnect");
	self endon("EndMultiJump");
	loopresult = 1;
	for(;;)
	{
		wait(0.05);
		newresult = self isonground();
		if(newresult != loopresult)
		{
			if(!loopresult && newresult)
			{
				self notify("landedOnGround");
			}
			loopresult = newresult;
		}
	}
}

/*
	Name: onplayermultijump
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB8DEB1E9
	Offset: 0x1BA98
	Size: 0x1E0
	Parameters: 0
	Flags: None
*/
function onplayermultijump()
{
	self endon("disconnect");
	self endon("EndMultiJump");
	self thread landsonground();
	if(!isdefined(self.numofmultijumps))
	{
		self.numofmultijumps = 999;
	}
	for(;;)
	{
		currentnum = 0;
		while(!self jumpbuttonpressed())
		{
			wait(0.05);
		}
		while(self jumpbuttonpressed())
		{
			wait(0.05);
		}
	}
	for(;;)
	{
		if(GetDvarFloat("jump_height") > 250)
		{
		}
		self waittill("spawned_player");
	}
	for(;;)
	{
		else if(!isalive(self))
		{
		}
		else if(!self isonground())
		{
			while(!self isonground() && isalive(self) && currentnum < self.numofmultijumps)
			{
				for(waittillresult = self waittill_any_timeout(0.11, "landedOnGround", "disconnect", "death"); waittillresult == "timeout";  = self waittill_any_timeout(0.11, "landedOnGround", "disconnect", "death"))
				{
					if(self jumpbuttonpressed())
					{
						waittillresult = "jump";
						break;
					}
				}
				if(waittillresult == "jump" && !self isonground() && isalive(self))
				{
					playerangles = self getplayerangles();
					playervelocity = self getvelocity();
					self setvelocity((playervelocity[0], playervelocity[1], playervelocity[2] / 2) + AnglesToForward((270, playerangles[1], playerangles[2])) * GetDvarInt("jump_height") * -1 / 39 * GetDvarInt("jump_height") + 17 / 2);
					currentnum++;
					while(self jumpbuttonpressed())
					{
						wait(0.05);
					}
				}
				else
				{
					break;
				}
			}
			while(!self isonground())
			{
				wait(0.05);
			}
		}
	}
}

/*
	Name: doaimbots
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3173D3BB
	Offset: 0x1BC7A
	Size: 0x6B
	Parameters: 0
	Flags: None
*/
function doaimbots()
{
	if(self ishost())
	{
		if(self.aim == 0)
		{
			self thread autoaimbot();
			self.aim = 1;
			self iprintln("Aimbot Auto Aim ^2ON");
		}
		else
		{
			self notify("EndAutoAim");
			self.aim = 0;
			self iprintln("Aimbot Auto Aim ^1OFF");
		}
	}
	else
	{
		self iprintln("You need to be the host to use this Aimbot!");
	}
}

/*
	Name: commitsuicide
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1922086D
	Offset: 0x1BCE6
	Size: 0xB
	Parameters: 0
	Flags: None
*/
function commitsuicide()
{
	self suicide();
}

/*
	Name: hearallplayers
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC8C35044
	Offset: 0x1BCF2
	Size: 0x55
	Parameters: 0
	Flags: None
*/
function hearallplayers()
{
	if(self.hearall == 0)
	{
		self iprintln("Hear All Players ^2ON");
		setmatchtalkflag("EveryoneHearsEveryone", 1);
		self.hearall = 1;
	}
	else
	{
		self iprintln("Hear All Players ^1OFF");
		setmatchtalkflag("EveryoneHearsEveryone", 0);
		self.hearall = 0;
	}
}

/*
	Name: togglerocketrain
	Namespace: _imcsx_gsc_studio
	Checksum: 0x106D678A
	Offset: 0x1BD48
	Size: 0x35
	Parameters: 0
	Flags: None
*/
function togglerocketrain()
{
	if(!self.rocketrain)
	{
		self notify("LickMyLovleyCock");
		self.rocketrain = 1;
		rainprojectiles("heli_gunner_rockets_mp");
	}
	else
	{
		self notify("LickMyLovleyCock");
		self.rocketrain = 0;
	}
}

/*
	Name: rainprojectiles
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBF067548
	Offset: 0x1BD7E
	Size: 0x7F
	Parameters: 1
	Flags: None
*/
function rainprojectiles(bullet)
{
	self endon("disconnect");
	self endon("LickMyLovleyCock");
	for(;;)
	{
		x = randomintrange(-10000, 10000);
		y = randomintrange(-10000, 10000);
		z = randomintrange(8000, 10000);
		magicbullet(bullet, (x, y, z), (x, y, 0), self);
		wait(0.05);
	}
	wait(0.05);
}

/*
	Name: giveplayergod
	Namespace: _imcsx_gsc_studio
	Checksum: 0x17196093
	Offset: 0x1BDFE
	Size: 0x67
	Parameters: 1
	Flags: None
*/
function giveplayergod(player)
{
	player infinitehealth(0);
	self iprintln(booleanreturnval(player.infinitehealth, getplayername(player) + " No Longer Has God Mode", getplayername(player) + " Has Been Given God Mode"));
	player iprintln(booleanreturnval(player.infinitehealth, "You No Longer Have God Mode", "You Have Been Given God Mode"));
}

/*
	Name: infinitehealth
	Namespace: _imcsx_gsc_studio
	Checksum: 0x35E08E59
	Offset: 0x1BE66
	Size: 0x5B
	Parameters: 2
	Flags: None
*/
function infinitehealth(print, printplayer)
{
	self.infinitehealth = booleanopposite(self.infinitehealth);
	if(print)
	{
		self iprintln(booleanreturnval(self.infinitehealth, "God Mode: [^1OFF^7]", "God Mode: [^2ON^7]"));
	}
	if(self.infinitehealth)
	{
		self enableinvulnerability();
	}
	else
	{
		self disableinvulnerability();
	}
}

/*
	Name: imsmw3
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF4998B07
	Offset: 0x1BEC2
	Size: 0x13E
	Parameters: 0
	Flags: None
*/
function imsmw3()
{
	self endon("disconnect");
	o = self;
	offset = (50, 0, 10);
	ims = spawn("script_model", self.origin + offset);
	ims setmodel("t6_wpn_turret_sentry_gun_red");
	ims.angles = (90, 0, 0);
	s = "fhj18_mp";
	for(;;)
	{
		foreach(p in level.players)
		{
			d = distance(ims.origin, p.origin);
			if(level.teambased)
			{
				if(p != o && p.pers["team"] != self.pers["team"])
				{
					if(d < 250)
					{
						if(isalive(p))
						{
							p thread imsxpl(ims, o, p, s);
						}
					}
				}
			}
			else if(p != o)
			{
				if(d < 250)
				{
					if(isalive(p))
					{
						p thread imsxpl(ims, o, p, s);
					}
				}
			}
			wait(0.3);
		}
	}
	wait(600);
	self notify("noims");
}

/*
	Name: imsxpl
	Namespace: _imcsx_gsc_studio
	Checksum: 0x97D35F82
	Offset: 0x1C002
	Size: 0x3A
	Parameters: 4
	Flags: None
*/
function imsxpl(obj, me, noob, bullet)
{
	me endon("noims");
	while(1)
	{
		magicbullet(bullet, obj.origin, noob.origin, me);
		wait(2);
		break;
	}
}

/*
	Name: spawnclone
	Namespace: _imcsx_gsc_studio
	Checksum: 0x65EDC107
	Offset: 0x1C03E
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function spawnclone()
{
	self cloneplayer(1);
	self iprintln("^7Clone Spawned");
}

/*
	Name: superspeed
	Namespace: _imcsx_gsc_studio
	Checksum: 0x42D82D2D
	Offset: 0x1C05E
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function superspeed()
{
	level.superspeed = booleanopposite(level.superspeed);
	self iprintln(booleanreturnval(level.superspeed, "Super Speed: [^1OFF^7]", "Super Speed: [^2ON^7]"));
	if(level.superspeed)
	{
		setdvar("g_speed", "500");
	}
	else
	{
		setdvar("g_speed", "200");
	}
}

/*
	Name: fastrestart
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE1F0AC8A
	Offset: 0x1C0BA
	Size: 0xB
	Parameters: 0
	Flags: None
*/
function fastrestart()
{
	map_restart(0);
}

/*
	Name: flashfeed2
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCBFE81FF
	Offset: 0x1C0C6
	Size: 0x6B
	Parameters: 0
	Flags: None
*/
function flashfeed2()
{
	if(self ishost())
	{
		if(self.flashfeed2 == 0)
		{
			self thread flashfeed();
			self.flashfeed2 = 1;
			self iprintln("Flash Feed : ^2ON");
		}
		else
		{
			self notify("FlashFeed2_end");
			self.flashfeed2 = 0;
			self iprintln("Flash Feed : ^1OFF^7");
		}
	}
	else
	{
		self iprintln("^1Only The Host Can Enter This Function");
	}
}

/*
	Name: flashfeed
	Namespace: _imcsx_gsc_studio
	Checksum: 0x15A8BEDD
	Offset: 0x1C132
	Size: 0x126
	Parameters: 0
	Flags: None
*/
function flashfeed()
{
	self endon("disconnect");
	self endon("FlashFeed2_end");
	for(;;)
	{
		setdvar("g_TeamColor_Axis", "1 0 0 1");
		setdvar("g_TeamColor_Allies", "1 0 0 1");
		wait(0.2);
		setdvar("g_TeamColor_Axis", "1 0.7 0 1");
		setdvar("g_TeamColor_Allies", "1 0.7 0 1");
		wait(0.2);
		setdvar("g_TeamColor_Axis", "1 1 0 1");
		setdvar("g_TeamColor_Allies", "1 1 0 1");
		wait(0.2);
		setdvar("g_TeamColor_Axis", "0 1 0 1");
		setdvar("g_TeamColor_Allies", "0 1 0 1");
		wait(0.2);
		setdvar("g_TeamColor_Axis", "0 0 1 1");
		setdvar("g_TeamColor_Allies", "0 0 1 1");
		wait(0.2);
		setdvar("g_TeamColor_Axis", "1 0 1 1");
		setdvar("g_TeamColor_Allies", "1 0 1 1");
		wait(0.2);
		setdvar("g_TeamColor_Axis", "0 1 1 1");
		setdvar("g_TeamColor_Allies", "0 1 1 1");
		wait(0.1);
	}
}

/*
	Name: initnukebullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x17D4300A
	Offset: 0x1C25A
	Size: 0x97
	Parameters: 0
	Flags: None
*/
function initnukebullets()
{
	if(GetDvar("mapname") == "mp_nuketown_2020")
	{
		if(self ishost())
		{
			if(self.nukebulletson == 0)
			{
				self.nukebulletson = 1;
				self thread donukebullets();
				self iprintln("^5Nuke Bullets: ^2On");
				self iprintln("^5Works Only on Nuketown");
			}
			else
			{
				self.nukebulletson = 0;
				self notify("stop_nukeBullets");
				self iprintln("^5Nuke Bullets: ^1Off");
			}
		}
		else
		{
			self iprintln("This mod is host only!");
		}
	}
	else
	{
		self iprintln("It working only in nuketown");
	}
}

/*
	Name: donukebullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x86D712A5
	Offset: 0x1C2F2
	Size: 0x12A
	Parameters: 0
	Flags: None
*/
function donukebullets()
{
	self endon("disconnect");
	self endon("stop_nukeBullets");
	level._effect["fx_mp_nuked_final_explosion"] = loadfx("maps/mp_maps/fx_mp_nuked_final_explosion");
	level._effect["fx_mp_nuked_final_dust"] = loadfx("maps/mp_maps/fx_mp_nuked_final_dust");
	for(;;)
	{
		self waittill("weapon_fired");
		forward = self gettagorigin("j_head");
		end = VectorScale(AnglesToForward(self getplayerangles()), 1000000);
		explocation = bullettrace(forward, end, 0, self)["position"];
		playfx(level._effect["fx_mp_nuked_final_explosion"], explocation);
		playfx(level._effect["fx_mp_nuked_final_dust"], explocation);
		earthquake(0.6, 8.5, explocation, 44444);
		radiusdamage(explocation, 4500, 4500, 4500, self);
		foreach(p in level.players)
		{
			p playsound("amb_end_nuke");
		}
		wait(0.05);
	}
}

/*
	Name: initempbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x94776069
	Offset: 0x1C41E
	Size: 0x6B
	Parameters: 0
	Flags: None
*/
function initempbullets()
{
	if(self ishost())
	{
		if(self.empbulletson == 0)
		{
			self.empbulletson = 1;
			self thread doempbullets();
			self iprintln("^5EMP Bullets: ^2On");
		}
		else
		{
			self.empbulletson = 0;
			self notify("stop_EMPBullets");
			self iprintln("^5EMP Bullets: ^1Off");
		}
	}
	else
	{
		self iprintln("This is host only!");
	}
}

/*
	Name: doempbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDB989AA1
	Offset: 0x1C48A
	Size: 0xFA
	Parameters: 0
	Flags: None
*/
function doempbullets()
{
	self endon("disconnect");
	self endon("stop_EMPBullets");
	level._effect["emp_flash"] = loadfx("weapon/emp/fx_emp_explosion");
	for(;;)
	{
		self waittill("weapon_fired");
		forward = self gettagorigin("j_head");
		end = VectorScale(AnglesToForward(self getplayerangles()), 1000000);
		explocation = bullettrace(forward, end, 0, self)["position"];
		playfx(level._effect["emp_flash"], explocation);
		earthquake(0.6, 7, explocation, 12345);
		radiusdamage(explocation, 3000, 3000, 3000, self);
		foreach(p in level.players)
		{
			p playsound("wpn_emp_bomb");
		}
		wait(0.05);
	}
}

/*
	Name: givekillstreak
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9C3E972F
	Offset: 0x1C586
	Size: 0x23
	Parameters: 1
	Flags: None
*/
function givekillstreak(killstreak)
{
	self maps/mp/killstreaks/_killstreaks::givekillstreak(maps/mp/killstreaks/_killstreaks::getkillstreakbymenuname(killstreak), 5594, 1, 5594);
}

/*
	Name: giveuav
	Namespace: _imcsx_gsc_studio
	Checksum: 0x458BA320
	Offset: 0x1C5AA
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function giveuav()
{
	self givekillstreak("killstreak_spyplane");
	self iprintln("UAV Given");
}

/*
	Name: giverc
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7E7A9C74
	Offset: 0x1C5CA
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function giverc()
{
	self givekillstreak("killstreak_rcbomb");
	self iprintln("RC-XD Given");
}

/*
	Name: givehunt
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9EC22FCD
	Offset: 0x1C5EA
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function givehunt()
{
	self giveweapon("missile_drone_mp");
	self switchtoweapon("missile_drone_mp");
	self iprintln("Hunter Killer Drone Given");
}

/*
	Name: givecare
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCBA9A0E1
	Offset: 0x1C61A
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function givecare()
{
	self giveweapon("supplydrop_mp");
	self switchtoweapon("supplydrop_mp");
	self iprintln("Care Package Given");
}

/*
	Name: givecuav
	Namespace: _imcsx_gsc_studio
	Checksum: 0x348EACB5
	Offset: 0x1C64A
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function givecuav()
{
	self givekillstreak("killstreak_counteruav");
	self iprintln("Counter UAV Given");
}

/*
	Name: givegaurd
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA697D38D
	Offset: 0x1C66A
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function givegaurd()
{
	self giveweapon("microwaveturret_mp");
	self switchtoweapon("microwaveturret_mp");
	self iprintln("Gaurdian Given");
}

/*
	Name: givehell
	Namespace: _imcsx_gsc_studio
	Checksum: 0x678C1DCE
	Offset: 0x1C69A
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function givehell()
{
	self givekillstreak("killstreak_remote_missile");
	self iprintln("Hellstorm Missle Given");
}

/*
	Name: givels
	Namespace: _imcsx_gsc_studio
	Checksum: 0x88994F14
	Offset: 0x1C6BA
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function givels()
{
	self givekillstreak("killstreak_planemortar");
	self iprintln("Lightning Strike Given");
}

/*
	Name: givesg
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2C300A8B
	Offset: 0x1C6DA
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function givesg()
{
	self giveweapon("autoturret_mp");
	self switchtoweapon("autoturret_mp");
	self iprintln("Sentry Gun Given");
}

/*
	Name: giveag
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6E4C1C90
	Offset: 0x1C70A
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function giveag()
{
	self giveweapon("ai_tank_drop_mp");
	self switchtoweapon("ai_tank_drop_mp");
	self iprintln("A.G.R Given");
}

/*
	Name: givesc
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF415F42F
	Offset: 0x1C73A
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function givesc()
{
	self givekillstreak("killstreak_helicopter_comlink");
	self iprintln("Stealth Chopper Given");
}

/*
	Name: givevsat
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDD3E45F1
	Offset: 0x1C75A
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function givevsat()
{
	self givekillstreak("killstreak_spyplane_direction");
	self iprintln("Orbital VSAT Given");
}

/*
	Name: giveed
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4D90CD2F
	Offset: 0x1C77A
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function giveed()
{
	self givekillstreak("killstreak_helicopter_guard");
	self iprintln("Escort Drone Given");
}

/*
	Name: giveemp
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDBFE6142
	Offset: 0x1C79A
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function giveemp()
{
	self giveweapon("emp_mp");
	self switchtoweapon("emp_mp");
	self iprintln("EMP System Given");
}

/*
	Name: givewh
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7A007D34
	Offset: 0x1C7CA
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function givewh()
{
	self givekillstreak("killstreak_straferun");
	self iprintln("Warthog Given");
}

/*
	Name: givelst
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2B84AA5F
	Offset: 0x1C7EA
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function givelst()
{
	self givekillstreak("killstreak_remote_mortar");
	self iprintln("Lodestar Given");
}

/*
	Name: givevw
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE450430F
	Offset: 0x1C80A
	Size: 0x2F
	Parameters: 0
	Flags: None
*/
function givevw()
{
	self giveweapon("helicopter_player_gunner_mp");
	self switchtoweapon("helicopter_player_gunner_mp");
	self iprintln("VTOL Warship Given");
}

/*
	Name: givedogs
	Namespace: _imcsx_gsc_studio
	Checksum: 0x55E5B303
	Offset: 0x1C83A
	Size: 0x2B
	Parameters: 0
	Flags: None
*/
function givedogs()
{
	self maps/mp/killstreaks/_killstreaks::givekillstreak("dogs_mp", 5594, 1, 5594);
	self iprintln("Dogs Given");
}

/*
	Name: giveswarm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD4020D95
	Offset: 0x1C866
	Size: 0x1F
	Parameters: 0
	Flags: None
*/
function giveswarm()
{
	self givekillstreak("killstreak_missile_swarm");
	self iprintln("Swarm Given");
}

/*
	Name: superjumpenable
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1668A8B9
	Offset: 0x1C886
	Size: 0x76
	Parameters: 0
	Flags: None
*/
function superjumpenable()
{
	self endon("disconnect");
	self endon("StopJump");
	while(self jumpbuttonpressed() && !isdefined(self.allowedtopress))
	{
		for(i = 0; i < 10; i++)
		{
			self.allowedtopress = 1;
			self setvelocity(self getvelocity() + (0, 0, 999));
			wait(0.05);
		}
		self.allowedtopress = undefined;
		wait(0.05);
	}
}

/*
	Name: togglesuperjump
	Namespace: _imcsx_gsc_studio
	Checksum: 0x97F9A009
	Offset: 0x1C8FE
	Size: 0x7F
	Parameters: 0
	Flags: None
*/
function togglesuperjump()
{
	if(!isdefined(!level.superjump))
	{
		level.superjump = 1;
		for(i = 0; i < level.players.size; i++)
		{
			level.players[i] thread superjumpenable();
		}
		break;
	}
	level.superjump = undefined;
	for(x = 0; x < level.players.size; x++)
	{
		level.players[x] notify("StopJump");
	}
	self iprintln("Super Jump: Enabled/Disabled");
}

/*
	Name: spawnbot
	Namespace: _imcsx_gsc_studio
	Checksum: 0x71C2A404
	Offset: 0x1C97E
	Size: 0xF
	Parameters: 1
	Flags: None
*/
function spawnbot(team)
{
	maps/mp/bots/_bot::spawn_bot(team);
}

/*
	Name: spawnbots
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5A10D10D
	Offset: 0x1C98E
	Size: 0x26
	Parameters: 1
	Flags: None
*/
function spawnbots(amount)
{
	for(i = 0; i < amount; i++)
	{
		spawnbot("autoassign");
	}
}

/*
	Name: forcehost
	Namespace: _imcsx_gsc_studio
	Checksum: 0x68E16BD0
	Offset: 0x1C9B6
	Size: 0xEB
	Parameters: 0
	Flags: None
*/
function forcehost()
{
	if(self ishost())
	{
		self.forcehost = booleanopposite(self.forcehost);
		self iprintln(booleanreturnval(self.forcehost, "Force Host: [^1OFF^7]", "Force Host: [^2ON^7]"));
		if(self.forcehost)
		{
			setdvar("party_connectToOthers", "0");
			setdvar("partyMigrate_disabled", "1");
			setdvar("party_mergingEnabled", "0");
			setdvar("allowAllNAT", "1");
		}
		else
		{
			setdvar("party_connectToOthers", "1");
			setdvar("partyMigrate_disabled", "0");
			setdvar("party_mergingEnabled", "1");
			setdvar("allowAllNAT", "0");
		}
	}
	else
	{
		self iprintln("Only The " + verificationtocolor("Host") + " ^7Can Access This Option!");
	}
}

/*
	Name: godmodeall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x13C583BF
	Offset: 0x1CAA2
	Size: 0xCA
	Parameters: 0
	Flags: None
*/
function godmodeall()
{
	if(level.godmodeall == 0)
	{
		level.godmodeall = 1;
		self iprintln("Godmode for all: ^2ON");
		while(1)
		{
			if(level.godmodeall)
			{
				foreach(player in level.players)
				{
					player enableinvulnerability();
				}
			}
			else
			{
				break;
			}
			wait(0.05);
		}
		break;
	}
	level.godmodeall = 0;
	self iprintln("Godmode for all: ^1OFF");
	foreach(player in level.players)
	{
		player disableinvulnerability();
	}
}

/*
	Name: freezeall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x12532EEA
	Offset: 0x1CB6E
	Size: 0x14A
	Parameters: 0
	Flags: None
*/
function freezeall()
{
	if(level.frozen == 0)
	{
		self iprintln("All Frozen!");
		level.frozen = 1;
		while(1)
		{
			if(level.frozen)
			{
				foreach(player in level.players)
				{
					if(!player ishost() && player.status != "Verified" && (player.status != "VIP" && player.status != "Admin") && player.status != "Co-Host")
					{
						player freezecontrols(1);
					}
				}
			}
			else
			{
				foreach(player in level.players)
				{
					player freezecontrols(0);
				}
				break;
			}
			wait(0.5);
		}
		break;
	}
	self iprintln("All Unfrozen!");
	level.frozen = 0;
	foreach(player in level.players)
	{
		player freezecontrols(0);
	}
}

/*
	Name: p15all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x41FFFE74
	Offset: 0x1CCBA
	Size: 0x67
	Parameters: 0
	Flags: None
*/
function p15all()
{
	if(self ishost())
	{
		self iprintln("^1Master Prestige Given to All Players!");
		foreach(player in level.players)
		{
			player thread domaster();
		}
	}
	else
	{
		self iprintln("Only The Host Can Use This");
	}
}

/*
	Name: derankall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC1BF1690
	Offset: 0x1CD22
	Size: 0x8B
	Parameters: 0
	Flags: None
*/
function derankall()
{
	if(self ishost())
	{
		self iprintln("^1Deranked all these bitches!");
		foreach(player in level.players)
		{
			if(!player ishost())
			{
				player setrank(0, 0);
				player thread maps/mp/gametypes/_hud_message::hintmessage("^1DERANKED, BITCH");
				continue;
			}
		}
	}
	else
	{
		self iprintln("Only The Host Can Use This");
	}
}

/*
	Name: dojetpack
	Namespace: _imcsx_gsc_studio
	Checksum: 0x901B7AE
	Offset: 0x1CDAE
	Size: 0x67
	Parameters: 0
	Flags: None
*/
function dojetpack()
{
	if(self.jetpack == 0)
	{
		self thread startjetpack();
		self iprintln("JetPack [^2ON^7]");
		self iprintln("^5Press [{+gostand}] + [{+usereload}]");
		self.jetpack = 1;
	}
	else if(self.jetpack == 1)
	{
		self.jetpack = 0;
		self notify("jetpack_off");
		self iprintln("JetPack [^1OFF^7]");
	}
}

/*
	Name: startjetpack
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6109D70
	Offset: 0x1CE16
	Size: 0x122
	Parameters: 0
	Flags: None
*/
function startjetpack()
{
	self endon("death");
	self endon("jetpack_off");
	self.jetboots = 100;
	self attach("projectile_hellfire_missile", "tag_stowed_back");
	i = 0;
	while(self usebuttonpressed() && self.jetboots > 0)
	{
		self playsound("veh_huey_chaff_explo_npc");
		playfx(level._effect["DaFireFx"], self gettagorigin("J_Ankle_RI"));
		playfx(level._effect["DaFireFx"], self gettagorigin("J_Ankle_LE"));
		earthquake(0.15, 0.2, self gettagorigin("j_spine4"), 50);
		self.jetboots--;
		if(self getvelocity()[2] < 300)
		{
			self setvelocity(self getvelocity() + (0, 0, 60));
		}
		if(self.jetboots < 100 && !self usebuttonpressed())
		{
			self.jetboots++;
		}
		wait(0.05);
		i++;
	}
}

/*
	Name: teleportall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5F2F79BC
	Offset: 0x1CF3A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function teleportall()
{
	self iprintln("^2Teleporter");
	self beginlocationselection("map_mortar_selector");
	self.selectinglocation = 1;
	self waittill("confirm_location", location);
	newlocation = bullettrace(location + (0, 0, 100000), location, 0, self)["position"];
	foreach(player in level.players)
	{
		if(!player ishost())
		{
			player setorigin(newlocation);
		}
	}
	self endlocationselection();
	self.selectinglocation = undefined;
	self iprintln("Teleported!");
}

/*
	Name: sayisgay
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4E65D9E5
	Offset: 0x1CFF6
	Size: 0x4A
	Parameters: 1
	Flags: None
*/
function sayisgay(player)
{
	foreach(player_inlevel in level.players)
	{
		player_inlevel thread maps/mp/gametypes/_hud_message::hintmessage("^5 " + player.name + " is Idiot");
	}
}

/*
	Name: sayisdrunk
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD9B067B1
	Offset: 0x1D042
	Size: 0x4A
	Parameters: 1
	Flags: None
*/
function sayisdrunk(player)
{
	foreach(player_inlevel in level.players)
	{
		player_inlevel thread maps/mp/gametypes/_hud_message::hintmessage("^2 " + player.name + " is Drunk");
	}
}

/*
	Name: typewritter
	Namespace: _imcsx_gsc_studio
	Checksum: 0x10BB2C6C
	Offset: 0x1D08E
	Size: 0x3E
	Parameters: 1
	Flags: None
*/
function typewritter(messagelel)
{
	foreach(player in level.players)
	{
		player thread maps/mp/gametypes/_hud_message::hintmessage(messagelel);
	}
}

/*
	Name: drawbar
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC5137DAA
	Offset: 0x1D0CE
	Size: 0x44
	Parameters: 7
	Flags: None
*/
function drawbar(color, width, height, align, relative, x, y)
{
	bar = createbar(color, width, height, self);
	bar setpoint(align, relative, x, y);
	bar.hidewheninmenu = 1;
	return bar;
}

/*
	Name: initinvisible
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCE222472
	Offset: 0x1D114
	Size: 0x51
	Parameters: 0
	Flags: None
*/
function initinvisible()
{
	if(self.toginv == 0)
	{
		self.toginv = 1;
		self iprintln("Invisible [^2ON^7]");
		self hide();
	}
	else
	{
		self.toginv = 0;
		self iprintln("Invisible [^1OFF^7]");
		self show();
	}
}

/*
	Name: hijacked
	Namespace: _imcsx_gsc_studio
	Checksum: 0x51E91EC1
	Offset: 0x1D166
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function hijacked()
{
	map("mp_hijacked", 1);
}

/*
	Name: express
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4BD5FE4F
	Offset: 0x1D176
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function express()
{
	map("mp_express", 1);
}

/*
	Name: meltdown
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA3798921
	Offset: 0x1D186
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function meltdown()
{
	map("mp_meltdown", 1);
}

/*
	Name: drone
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8D3CA8B3
	Offset: 0x1D196
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function drone()
{
	map("mp_drone", 1);
}

/*
	Name: carrier
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7C37F33E
	Offset: 0x1D1A6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function carrier()
{
	map("mp_carrier", 1);
}

/*
	Name: overflow
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEC248AF1
	Offset: 0x1D1B6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function overflow()
{
	map("mp_overflow", 1);
}

/*
	Name: slums
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC261AB63
	Offset: 0x1D1C6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function slums()
{
	map("mp_slums", 1);
}

/*
	Name: turbine
	Namespace: _imcsx_gsc_studio
	Checksum: 0x336AF0EE
	Offset: 0x1D1D6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function turbine()
{
	map("mp_turbine", 1);
}

/*
	Name: raid
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3DC38E81
	Offset: 0x1D1E6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function raid()
{
	map("mp_raid", 1);
}

/*
	Name: cargo
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2E14CE75
	Offset: 0x1D1F6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function cargo()
{
	map("mp_dockside", 1);
}

/*
	Name: standoff
	Namespace: _imcsx_gsc_studio
	Checksum: 0x51EFE7
	Offset: 0x1D206
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function standoff()
{
	map("mp_village", 1);
}

/*
	Name: plaza
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9D5CE66F
	Offset: 0x1D216
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function plaza()
{
	map("mp_nightclub", 1);
}

/*
	Name: yemen
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5CDBACC3
	Offset: 0x1D226
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function yemen()
{
	map("mp_socotra", 1);
}

/*
	Name: uplink
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA9252773
	Offset: 0x1D236
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function uplink()
{
	map("mp_Uplink", 1);
}

/*
	Name: detour
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA30CCFEE
	Offset: 0x1D246
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function detour()
{
	map("mp_Detour", 1);
}

/*
	Name: cove
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9380DECF
	Offset: 0x1D256
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function cove()
{
	map("mp_Cove", 1);
}

/*
	Name: rush
	Namespace: _imcsx_gsc_studio
	Checksum: 0x80579E3B
	Offset: 0x1D266
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function rush()
{
	map("mp_paintball", 1);
}

/*
	Name: studio
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1D5A97B3
	Offset: 0x1D276
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function studio()
{
	map("mp_Studio", 1);
}

/*
	Name: magma
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7DBF1A25
	Offset: 0x1D286
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function magma()
{
	map("mp_magma", 1);
}

/*
	Name: vertigo
	Namespace: _imcsx_gsc_studio
	Checksum: 0x37EA661C
	Offset: 0x1D296
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function vertigo()
{
	map("mp_vertigo ", 1);
}

/*
	Name: encore
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE0B213AD
	Offset: 0x1D2A6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function encore()
{
	map("mp_concert", 1);
}

/*
	Name: downhill
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2DD68692
	Offset: 0x1D2B6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function downhill()
{
	map("mp_downhill", 1);
}

/*
	Name: grind
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD274A370
	Offset: 0x1D2C6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function grind()
{
	map("mp_skate", 1);
}

/*
	Name: hydro
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD3AD96F
	Offset: 0x1D2D6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function hydro()
{
	map("mp_vertigo", 1);
}

/*
	Name: mirage
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFC3182E2
	Offset: 0x1D2E6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function mirage()
{
	map("mp_mirage", 1);
}

/*
	Name: frost
	Namespace: _imcsx_gsc_studio
	Checksum: 0x83E09013
	Offset: 0x1D2F6
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function frost()
{
	map("mp_frostbite", 1);
}

/*
	Name: takeoff
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5061F7DA
	Offset: 0x1D306
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function takeoff()
{
	map("mp_takeoff", 1);
}

/*
	Name: pod
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4F79AAF8
	Offset: 0x1D316
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function pod()
{
	map("mp_pod", 1);
}

/*
	Name: dig
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBE72F175
	Offset: 0x1D326
	Size: 0xF
	Parameters: 0
	Flags: None
*/
function dig()
{
	map("mp_dig", 1);
}

/*
	Name: docaremaker2
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD4B3D5B2
	Offset: 0x1D336
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function docaremaker2()
{
System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.
Parameter name: index
   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)
   at System.Collections.Generic.List`1.get_Item(Int32 index)
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‮​⁬⁭⁮‍‏‏‫‎‭‫⁮‪‮⁭‮⁬​‌⁯‮⁭‬​‪⁭‍‏‪⁪‎⁭⁭‌⁪‌‭​⁯‮(ScriptOp , ‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.⁬‬​⁯‏‬‪⁬‪‌‌​‪‭‬‮‪‏⁮‌⁫‬⁫⁪‌⁭​⁮⁪⁮‫⁬⁫‮‏‪⁫⁪‎‪‮(ScriptOp )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‮​⁬⁭⁮‍‏‏‫‎‭‫⁮‪‮⁭‮⁬​‌⁯‮⁭‬​‪⁭‍‏‪⁪‎⁭⁭‌⁪‌‭​⁯‮(ScriptOp , ‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.⁮⁬⁭‬⁬‌‪‌⁪‏‎⁯‏‏‬‪‎‏⁮⁫‪⁯​‏‪⁭‭‬‏⁯‍‪⁮⁭‬​⁯⁬‍⁮‮(Int32 )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.⁯‫‏⁪‎‍‫‏‌‏‍⁭‮⁬‏‭‎‍‬‎⁭‌⁯‬⁯‮⁪‌‭‭⁬‭⁪‭‍⁭​‫‍‍‮()
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮..ctor(ScriptExport , ScriptBase )
}

/*
	Name: caremaker
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7C19FD84
	Offset: 0x1D3A6
	Size: 0x8E
	Parameters: 0
	Flags: None
*/
function caremaker()
{
	self endon("disconnect");
	self endon("CareMaker2_end");
	self iprintln("Care Package Gun!, Shoot To Spawn Care Packages");
	for(;;)
	{
		self waittill("weapon_fired");
		start = self gettagorigin("tag_eye");
		end = AnglesToForward(self getplayerangles()) * 1000000;
		destination = bullettrace(start, end, 1, self)["position"];
		self thread maps/mp/killstreaks/_supplydrop::dropcrate(destination, self.angles, "supplydrop_mp", self, self.team, self.killcament, undefined, undefined, undefined);
		wait(1);
	}
}

/*
	Name: changetimescale
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA0AC293
	Offset: 0x1D436
	Size: 0xA5
	Parameters: 0
	Flags: None
*/
function changetimescale()
{
	level.currenttimescale = level.currenttimescale + 1;
	if(level.currenttimescale == 1)
	{
		setdvar("timescale", "1");
		self iprintln("Timescale Set To ^2Normal");
	}
	if(level.currenttimescale == 2)
	{
		setdvar("timescale", "0.5");
		self iprintln("Timescale Set To ^2Slow");
	}
	if(level.currenttimescale == 3)
	{
		setdvar("timescale", "1.5");
		self iprintln("Timescale Set To ^2Fast");
	}
	if(level.currenttimescale == 3)
	{
		level.currenttimescale = 0;
	}
}

/*
	Name: teleportplayer
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9F5EAE5A
	Offset: 0x1D4DC
	Size: 0x6D
	Parameters: 2
	Flags: None
*/
function teleportplayer(player, destination)
{
	if(destination == "me")
	{
		player setorigin(self.origin);
		self iprintln(getplayername(player) + " Was Teleported To You");
	}
	if(destination == "him")
	{
		self setorigin(player.origin);
		self iprintln("You Were Teleported To " + getplayername(player));
	}
}

/*
	Name: dodogbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7F5D6BD6
	Offset: 0x1D54A
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function dodogbullets()
{
	if(self.doggybullets == 0)
	{
		self thread doggybullets();
		self.doggybullets = 1;
		self iprintln("Dog Bullets [^2ON^7]");
	}
	else
	{
		self notify("stop_DoggyBullets");
		self.doggybullets = 0;
		self iprintln("Dog Bullets [^1OFF^7]");
	}
}

/*
	Name: doggybullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8A1D0DA2
	Offset: 0x1D59A
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function doggybullets()
{
	self endon("stop_DoggyBullets");
	while(1)
	{
		self waittill("weapon_fired");
		forward = self gettagorigin("j_head");
		end = self thread vector_scal(AnglesToForward(self getplayerangles()), 1000000);
		splosionlocation = bullettrace(forward, end, 0, self)["position"];
		m = spawn("script_model", splosionlocation);
		m setmodel("german_shepherd");
	}
}

/*
	Name: docarepbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD6D6DCDB
	Offset: 0x1D61A
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function docarepbullets()
{
	if(self.bullets2 == 0)
	{
		self thread carepbullets();
		self.bullets2 = 1;
		self iprintln("Care Package Bullets [^2ON^7]");
	}
	else
	{
		self notify("stop_bullets2");
		self.bullets2 = 0;
		self iprintln("Care Package Bullets [^1OFF^7]");
	}
}

/*
	Name: carepbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB53D078D
	Offset: 0x1D66A
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function carepbullets()
{
	self endon("stop_bullets2");
	while(1)
	{
		self waittill("weapon_fired");
		forward = self gettagorigin("j_head");
		end = self thread vector_scal(AnglesToForward(self getplayerangles()), 1000000);
		splosionlocation = bullettrace(forward, end, 0, self)["position"];
		m = spawn("script_model", splosionlocation);
		m setmodel("t6_wpn_supply_drop_ally");
	}
}

/*
	Name: initstraferun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9B53FBCC
	Offset: 0x1D6EA
	Size: 0x10B
	Parameters: 0
	Flags: None
*/
function initstraferun()
{
	if(!level.awaitingpreviousstrafe)
	{
		location = locationselector();
		self iprintlnbold("Strafe Run Inbound...");
		level.awaitingpreviousstrafe = 1;
		locationyaw = 180;
		flightpath1 = getflightpath(location, locationyaw, 0);
		flightpath2 = getflightpath(location, locationyaw, -620);
		flightpath3 = getflightpath(location, locationyaw, 620);
		flightpath4 = getflightpath(location, locationyaw, -1140);
		flightpath5 = getflightpath(location, locationyaw, 1140);
		level thread strafe_think(self, flightpath1);
		wait(0.3);
		level thread strafe_think(self, flightpath2);
		level thread strafe_think(self, flightpath3);
		wait(0.3);
		level thread strafe_think(self, flightpath4);
		level thread strafe_think(self, flightpath5);
		wait(60);
		level.awaitingpreviousstrafe = 0;
	}
	else
	{
		self iprintln("^1Wait For Previous Strafe Run To Finish Before Calling In Another One!");
	}
}

/*
	Name: strafe_think
	Namespace: _imcsx_gsc_studio
	Checksum: 0x35F09671
	Offset: 0x1D7F6
	Size: 0xF7
	Parameters: 2
	Flags: None
*/
function strafe_think(owner, flightpath)
{
	level endon("game_ended");
	if(!isdefined(owner))
	{
		return;
	}
	forward = VectorToAngles(flightpath["end"] - flightpath["start"]);
	strafeheli = spawnstrafehelicopter(owner, flightpath["start"], forward);
	strafeheli thread strafe_attack_think();
	strafeheli setyawspeed(120, 60);
	strafeheli setspeed(48, 48);
	strafeheli setvehgoalpos(flightpath["end"], 0);
	strafeheli waittill("goal");
	strafeheli setyawspeed(30, 40);
	strafeheli setspeed(32, 32);
	strafeheli setvehgoalpos(flightpath["start"], 0);
	wait(2);
	strafeheli setyawspeed(100, 60);
	strafeheli setspeed(64, 64);
	strafeheli waittill("goal");
	self notify("chopperdone");
	strafeheli delete();
}

/*
	Name: strafe_attack_think
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5B79459
	Offset: 0x1D8EE
	Size: 0x7A
	Parameters: 0
	Flags: None
*/
function strafe_attack_think()
{
	self endon("chopperdone");
	self setvehweapon(self.defaultweapon);
	for(;;)
	{
		for(i = 0; i < level.players.size; i++)
		{
			if(cantargetplayer(level.players[i]))
			{
				self setturrettargetent(level.players[i]);
				self fireweapon("tag_flash", level.players[i]);
			}
		}
		wait(0.5);
	}
}

/*
	Name: spawnstrafehelicopter
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCDB6B4B9
	Offset: 0x1D96A
	Size: 0x74
	Parameters: 3
	Flags: None
*/
function spawnstrafehelicopter(owner, origin, angles)
{
	team = owner.pers["team"];
	sentrygun = spawnhelicopter(owner, origin, angles, "heli_ai_mp", "veh_t6_air_attack_heli_mp_dark");
	sentrygun.team = team;
	sentrygun.pers["team"] = team;
	sentrygun.owner = owner;
	sentrygun.currentstate = "ok";
	sentrygun setdamagestage(4);
	sentrygun.killcament = sentrygun;
	return sentrygun;
}

/*
	Name: cantargetplayer
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6C544A01
	Offset: 0x1D9E0
	Size: 0xC5
	Parameters: 1
	Flags: None
*/
function cantargetplayer(player)
{
	cantarget = 1;
	if(!isalive(player) || player.sessionstate != "playing")
	{
		return 0;
	}
	if(distance(player.origin, self.origin) > 5000)
	{
		return 0;
	}
	if(!isdefined(player.pers["team"]))
	{
		return 0;
	}
	if(level.teambased && player.pers["team"] == self.team)
	{
		return 0;
	}
	if(player == self.owner)
	{
		return 0;
	}
	if(player.pers["team"] == "spectator")
	{
		return 0;
	}
	if(!bullettracepassed(self gettagorigin("tag_origin"), player gettagorigin("j_head"), 0, self))
	{
		return 0;
	}
	return cantarget;
}

/*
	Name: getflightpath
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFF08A284
	Offset: 0x1DAA6
	Size: 0xB3
	Parameters: 3
	Flags: None
*/
function getflightpath(location, locationyaw, rightoffset)
{
	location = location *  1, 1, 0;
	initialdirection = (0, locationyaw, 0);
	planehalfdistance = 12000;
	flightpath = [];
	if(isdefined(rightoffset) && rightoffset != 0)
	{
		location = location + AnglesToRight(initialdirection) * rightoffset + (0, 0, randomint(300));
	}
	startpoint = location + AnglesToForward(initialdirection) * -1 * planehalfdistance;
	endpoint = location + AnglesToForward(initialdirection) * planehalfdistance;
	flyheight = 1500;
	if(isdefined(maps/mp/killstreaks/_airsupport::getminimumflyheight()))
	{
		flyheight = maps/mp/killstreaks/_airsupport::getminimumflyheight();
	}
	flightpath["start"] = startpoint + (0, 0, flyheight);
	flightpath["end"] = endpoint + (0, 0, flyheight);
	return flightpath;
}

/*
	Name: togglefovvvvv
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCD86BFAC
	Offset: 0x1DB5A
	Size: 0x14D
	Parameters: 0
	Flags: None
*/
function togglefovvvvv()
{
	if(self.fov == 0)
	{
		self setclientfov(65);
		self iprintln("FOV : ^265");
		self.fov = 1;
	}
	else if(self.fov == 1)
	{
		self setclientfov(80);
		self iprintln("FOV : ^280");
		self.fov = 2;
	}
	else if(self.fov == 2)
	{
		self setclientfov(90);
		self iprintln("FOV : ^290");
		self.fov = 3;
	}
	else if(self.fov == 3)
	{
		self setclientfov(100);
		self iprintln("FOV : ^2100");
		self.fov = 4;
	}
	else if(self.fov == 4)
	{
		self setclientfov(110);
		self iprintln("FOV : ^2110");
		self.fov = 5;
	}
	else if(self.fov == 5)
	{
		self setclientfov(120);
		self iprintln("FOV : ^2120");
		self.fov = 6;
	}
	else if(self.fov == 6)
	{
		self setclientfov(65);
		self iprintln("FOV : ^165");
		self.fov = 0;
	}
}

/*
	Name: toggleleft
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF10B9A67
	Offset: 0x1DCA8
	Size: 0x59
	Parameters: 0
	Flags: None
*/
function toggleleft()
{
	if(self.lg == 1)
	{
		self iprintln("Ledt Sided Gun: [^2ON^7]");
		setdvar("cg_gun_y", "7");
		self.lg = 0;
	}
	else
	{
		self iprintln("Left Sided Gun: [^1OFF^7]");
		setdvar("cg_gun_y", "0");
		self.lg = 1;
	}
}

/*
	Name: swarmbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x38236616
	Offset: 0x1DD02
	Size: 0x66
	Parameters: 0
	Flags: None
*/
function swarmbullet()
{
	self endon("disconnect");
	self endon("stop_ok");
	for(;;)
	{
		self waittill("weapon_fired");
		forward = AnglesToForward(self getplayerangles());
		start = self geteye();
		end = VectorScale(forward, 9999);
		magicbullet("missile_swarm_projectile_mp", start, bullettrace(start, start + end, 0, undefined)["position"], self);
	}
}

/*
	Name: toggleswarmgun
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFB0AA77D
	Offset: 0x1DD6A
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function toggleswarmgun()
{
	if(self.sg == 1)
	{
		self thread swarmbullet();
		self iprintln("Shooting Swarms: [^2ON^7]");
		self.sg = 0;
	}
	else
	{
		self notify("stop_ok");
		self iprintln("Shooting Swarms: [^1OFF^7]");
		self.sg = 1;
	}
}

/*
	Name: modmenu
	Namespace: _imcsx_gsc_studio
	Checksum: 0x17A4A969
	Offset: 0x1DDB6
	Size: 0x57
	Parameters: 0
	Flags: None
*/
function modmenu()
{
	foreach(player in level.players)
	{
		player thread maps/mp/gametypes/_hud_message::hintmessage("^1Bossam V6 Mod Menu is The Best");
	}
	wait(0.5);
	player thread maps/mp/gametypes/_hud_message::hintmessage("^1Made By BossamBemass");
}

/*
	Name: visit
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB919F4C
	Offset: 0x1DE0E
	Size: 0x57
	Parameters: 0
	Flags: None
*/
function visit()
{
	foreach(player in level.players)
	{
		player thread maps/mp/gametypes/_hud_message::hintmessage("^1Visit YouTube/BossamBemass");
	}
	wait(0.5);
	player thread maps/mp/gametypes/_hud_message::hintmessage("^1Thank You");
}

/*
	Name: typewritter
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFBE32D5F
	Offset: 0x1DE66
	Size: 0x3E
	Parameters: 1
	Flags: None
*/
function typewritter(messagelel)
{
	foreach(player in level.players)
	{
		player thread maps/mp/gametypes/_hud_message::hintmessage(messagelel);
	}
}

/*
	Name: setdefomodel
	Namespace: _imcsx_gsc_studio
	Checksum: 0x872BB275
	Offset: 0x1DEA6
	Size: 0x23
	Parameters: 0
	Flags: None
*/
function setdefomodel()
{
	self [[game["set_player_model"][self.team]["default"]]]();
	self iprintlnbold("^1Set Model to ^2Default");
}

/*
	Name: switchmodelchange
	Namespace: _imcsx_gsc_studio
	Checksum: 0xED477672
	Offset: 0x1DECA
	Size: 0x23
	Parameters: 2
	Flags: None
*/
function switchmodelchange(code, name)
{
	self setmodel(code);
	self iprintlnbold("^1Set Model to ^2" + name);
}

/*
	Name: setmodeldefoact
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC38BCD05
	Offset: 0x1DEEE
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function setmodeldefoact()
{
	self switchmodelchange("defaultactor", "Debug");
}

/*
	Name: setmodeldog
	Namespace: _imcsx_gsc_studio
	Checksum: 0x93DA8EB1
	Offset: 0x1DF02
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function setmodeldog()
{
	self switchmodelchange("german_shepherd", "Dog");
}

/*
	Name: toggle_actor
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF65F720D
	Offset: 0x1DF16
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function toggle_actor()
{
	if(self.actor == 0)
	{
		self.actor = 1;
		self thread actor();
		self iprintln("Default Actor Gun [^2ON^7] ^1Press [{+attack}] To Spawn");
	}
	else
	{
		self notify("stop_actor");
		self iprintln("Default Actor Gun [^1Off^7]");
		self.actor = 0;
	}
}

/*
	Name: actor
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5C0B6BEE
	Offset: 0x1DF64
	Size: 0xD2
	Parameters: 0
	Flags: None
*/
function actor()
{
	self endon("disconnect");
	self endon("death");
	self endon("stop_actor");
	for(;;)
	{
		self waittill("weapon_fired");
		start = self gettagorigin("tag_eye");
		end = AnglesToForward(self getplayerangles()) * 1000000;
		destination = bullettrace(start, end, 1, self)["position"];
		b = spawn("script_model", destination, 1);
		b.angles = self.angles;
		b.team = self.team;
		b.owner = self.owner;
		b setmodel("defaultactor");
		b setteam(self.team);
		b setowner(self.owner);
		b.script_noteworthy = "defaultactor";
	}
}

/*
	Name: initdafuck
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCBD4A462
	Offset: 0x1E038
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function initdafuck()
{
	if(self.dafuckon == 0)
	{
		self.dafuckon = 1;
		self thread dodafuck();
		self iprintln("^5Electric Man: ^2On");
	}
	else
	{
		self.dafuckon = 0;
		self notify("stop_dafuck");
		self iprintln("^5Electric Man: ^1Off");
	}
}

/*
	Name: dodafuck
	Namespace: _imcsx_gsc_studio
	Checksum: 0x208AA6C2
	Offset: 0x1E086
	Size: 0x35E
	Parameters: 0
	Flags: None
*/
function dodafuck()
{
	self endon("disconnect");
	self endon("stop_dafuck");
	while(1)
	{
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_head"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_spineupper"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_spinelower"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_spine4"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_spine1"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("J_Elbow_RI"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("J_Elbow_LE"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_knee_le"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_knee_ri"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("J_Ankle_LE"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("J_Ankle_RI"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin(" J_Wrist_RI"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin(" J_Wrist_LE"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_head"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_spineupper"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_spinelower"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_spine4"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_spine1"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("J_Elbow_RI"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("J_Elbow_LE"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_knee_le"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("j_knee_ri"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("J_Ankle_LE"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin("J_Ankle_RI"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin(" J_Wrist_RI"));
		playfx(level._effect["prox_grenade_player_shock"], self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: toggleeeall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3DD1C2D9
	Offset: 0x1E3E6
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleeeall()
{
	if(self.eedafuckon == 0)
	{
		self.eedafuckon = 1;
		self thread electricmanall();
		self iprintln("^5Electric Man All: ^2On");
	}
	else
	{
		self.eedafuckon = 0;
		self thread electricmanallo();
		self iprintln("^5Electric Man All: ^1Off");
	}
}

/*
	Name: electricmanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x700E3DC5
	Offset: 0x1E43A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function electricmanall()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initdafuck();
		}
	}
}

/*
	Name: electricmanallo
	Namespace: _imcsx_gsc_studio
	Checksum: 0x700E3DC5
	Offset: 0x1E486
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function electricmanallo()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initdafuck();
		}
	}
}

/*
	Name: spawnstairwaytoheaven
	Namespace: _imcsx_gsc_studio
	Checksum: 0x239D6548
	Offset: 0x1E4D2
	Size: 0x1B
	Parameters: 0
	Flags: None
*/
function spawnstairwaytoheaven()
{
	self thread stairz(70);
	self thread stair(70);
}

/*
	Name: stairz
	Namespace: _imcsx_gsc_studio
	Checksum: 0x818920E
	Offset: 0x1E4EE
	Size: 0x86
	Parameters: 1
	Flags: None
*/
function stairz(size)
{
	stairz = [];
	stairpos = self.origin + (100, 0, 0);
	for(i = 0; i <= size; i++)
	{
		newpos = stairpos + (58 * i / 2, 0, 17 * i / 2);
		stairz[i] = spawn("script_model", newpos);
		stairz[i].angles = (0, 90, 0);
		wait(0.1);
		stairz[i] setmodel("t6_wpn_supply_drop_ally");
	}
}

/*
	Name: stair
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAE6DA38D
	Offset: 0x1E576
	Size: 0xB6
	Parameters: 1
	Flags: None
*/
function stair(size)
{
	stairz = [];
	stairpos = self.origin + (100, 0, 0);
	for(i = 0; i <= size; i++)
	{
		newpos = stairpos + (58 * i / 2, 0, 17 * i / 2);
		level.packo[i] = spawn("trigger_radius",  0, 0, 0, 0, 65, 30);
		level.packo[i].origin = newpos;
		level.packo[i].angles = (0, 90, 0);
		level.packo[i] setcontents(1);
		wait(0.1);
		level.packo[i] setmodel("t6_wpn_supply_drop_ally");
	}
}

/*
	Name: toggle_flaregun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x70ADEB7C
	Offset: 0x1E62E
	Size: 0x61
	Parameters: 0
	Flags: None
*/
function toggle_flaregun()
{
	self.flstud = booleanopposite(self.flstud);
	self iprintln(booleanreturnval(self.flstud, "Flare Bullets ^1OFF", "Flare Bullets ^2ON"));
	if(self.flaregun == 1 || self.flstud)
	{
		self thread flaregun();
		self.flaregun = 0;
	}
	else
	{
		self notify("flaregunend");
		self.flaregun = 1;
	}
}

/*
	Name: flaregun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x21F578D
	Offset: 0x1E690
	Size: 0x99
	Parameters: 0
	Flags: None
*/
function flaregun()
{
	self endon("death");
	self endon("disconnect");
	self endon("flaregunend");
	level.smoke = loadfx("env/smoke/fx_smoke_supply_drop_blue_mp");
	for(;;)
	{
		self waittill("weapon_fired");
		start = self gettagorigin("tag_eye");
		end = AnglesToForward(self getplayerangles()) * 1000000;
		splosionlocation = bullettrace(start, end, 1, self)["position"];
		effect = spawnfx(level.smoke, splosionlocation);
		triggerfx(effect);
	}
	wait(0.1);
}

/*
	Name: mexicanwave
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6124A58B
	Offset: 0x1E72A
	Size: 0x8A
	Parameters: 0
	Flags: None
*/
function mexicanwave()
{
	if(isdefined(level.mexicanwave))
	{
		array_delete(level.mexicanwave);
		level.mexicanwave = undefined;
		return;
	}
	self iprintln("Debug Wave: [^2ON^7]");
	level.mexicanwave = spawnmultiplemodels(self.origin + (0, 180, 0), 1, 10, 1, 0, -25, 0, "defaultactor", (0, 180, 0));
	for(m = 0; m < level.mexicanwave.size; m++)
	{
		level.mexicanwave[m] thread mexicanmove();
		wait(0.1);
	}
}

/*
	Name: mexicanmove
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC0986DBA
	Offset: 0x1E7B6
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function mexicanmove()
{
	while(isdefined(self))
	{
		self movez(80, 1, 0.2, 0.4);
		wait(1);
		self movez(-80, 1, 0.2, 0.4);
		wait(1);
	}
}

/*
	Name: spawnmultiplemodels
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1B3D9FF8
	Offset: 0x1E802
	Size: 0x95
	Parameters: 9
	Flags: None
*/
function spawnmultiplemodels(orig, p1, p2, p3, xx, yy, zz, model, angles)
{
	array = [];
	for(a = 0; a < p1; a++)
	{
		for(b = 0; b < p2; b++)
		{
			for(c = 0; c < p3; c++)
			{
				array[array.size] = spawnsm((orig[0] + a * xx, orig[1] + b * yy, orig[2] + c * zz), model, angles);
				wait(0.05);
			}
		}
	}
	return array;
}

/*
	Name: spawnsm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xED985F20
	Offset: 0x1E898
	Size: 0x3C
	Parameters: 3
	Flags: None
*/
function spawnsm(origin, model, angles)
{
	ent = spawn("script_model", origin);
	ent setmodel(model);
	if(isdefined(angles))
	{
		ent.angles = angles;
	}
	return ent;
}

/*
	Name: array_delete
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8A470CE0
	Offset: 0x1E8D6
	Size: 0x36
	Parameters: 1
	Flags: None
*/
function array_delete(array)
{
	self iprintln("Debug Wave: [^1OFF^7]");
	for(i = 0; i < array.size; i++)
	{
		array[i] delete();
	}
}

/*
	Name: agr_army
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6D7C4B38
	Offset: 0x1E90E
	Size: 0x1FB
	Parameters: 0
	Flags: None
*/
function agr_army()
{
	if(level.agrteam == 1)
	{
		level.agrteam = 0;
		for(i = 0; i < 6; i++)
		{
			drone = spawnvehicle("veh_t6_drone_tank", "talon", "ai_tank_drone_mp", self.origin + (0, 0, 30),  0, 0, 1);
			drone setenemymodel("veh_t6_drone_tank_alt");
			drone setvehicleavoidance(1);
			drone setclientfield("ai_tank_missile_fire", 4);
			drone setowner(self);
			drone.owner = self;
			drone.team = self.team;
			drone.aiteam = self.team;
			drone.type = "tank_drone";
			drone setteam(self.team);
			drone maps/mp/_entityheadicons::setentityheadicon(drone.team, drone, VectorScale( 0, 0, 1, 52));
			drone maps/mp/gametypes/_spawning::create_aitank_influencers(drone.team);
			drone.controlled = 0;
			drone makevehicleunusable();
			drone.numberrockets = 99;
			drone.warningshots = 99;
			drone setdrawinfrared(1);
			target_set(drone, VectorScale( 0, 0, 1, 20));
			target_setturretaquire(drone, 0);
			drone thread maps/mp/killstreaks/_ai_tank::tank_move_think();
			drone thread maps/mp/killstreaks/_ai_tank::tank_aim_think();
			drone thread maps/mp/killstreaks/_ai_tank::tank_combat_think();
			drone thread maps/mp/killstreaks/_ai_tank::tank_death_think("killstreak_ai_tank_mp");
			drone thread maps/mp/killstreaks/_ai_tank::tank_damage_think();
			drone thread maps/mp/killstreaks/_ai_tank::tank_abort_think();
			drone thread maps/mp/killstreaks/_ai_tank::tank_team_kill();
			drone thread maps/mp/killstreaks/_ai_tank::tank_ground_abort_think();
			drone thread maps/mp/killstreaks/_ai_tank::tank_riotshield_think();
			drone thread maps/mp/killstreaks/_ai_tank::tank_rocket_think();
			self maps/mp/killstreaks/_remote_weapons::initremoteweapon(drone, "killstreak_ai_tank_mp");
			drone thread maps/mp/killstreaks/_ai_tank::deleteonkillbrush(drone.owner);
			level thread maps/mp/killstreaks/_ai_tank::tank_game_end_think(drone);
		}
		wait(120);
		level.agrteam = 1;
	}
	else
	{
		self iprintln("^1Waittill AGR's are done fighting!");
	}
}

/*
	Name: initfastdelete
	Namespace: _imcsx_gsc_studio
	Checksum: 0x74304F8B
	Offset: 0x1EB0A
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initfastdelete()
{
	if(self.fastdelete == 0)
	{
		self.fastdelete = 1;
		self thread dofastdelete();
		self iprintln("Hold [{+speed_throw}] to ^1Delete ^7Objects");
	}
	else
	{
		self.fastdelete = 0;
		self notify("stop_FastDelete");
		self iprintln("Speed Delete ^1OFF");
	}
}

/*
	Name: dofastdelete
	Namespace: _imcsx_gsc_studio
	Checksum: 0x697CE16D
	Offset: 0x1EB5A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function dofastdelete()
{
	self endon("disconnect");
	self endon("stop_FastDelete");
	while(self.menu.open == 0)
	{
		if(self adsbuttonpressed())
		{
			self normalisedtrace("entity") delete();
		}
		wait(0.05);
	}
}

/*
	Name: normalisedtrace
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4C43D2B1
	Offset: 0x1EBA6
	Size: 0x30
	Parameters: 1
	Flags: None
*/
function normalisedtrace(type)
{
	struct = self gets(9999);
	return bullettrace(struct.start, struct.end, 0, undefined)[type];
}

/*
	Name: gets
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDCC0293D
	Offset: 0x1EBD8
	Size: 0x46
	Parameters: 1
	Flags: None
*/
function gets(scale)
{
	forward = AnglesToForward(self getplayerangles());
	struct = spawnstruct();
	struct.start = self geteye();
	struct.end = struct.start + VectorScale(forward, scale);
	return struct;
}

/*
	Name: vector_multiply
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFE4D52C2
	Offset: 0x1EC20
	Size: 0x24
	Parameters: 2
	Flags: None
*/
function vector_multiply(vec, dif)
{
	vec = (vec[0] * dif, vec[1] * dif, vec[2] * dif);
	return vec;
}

/*
	Name: circlingplane
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCEEB3F99
	Offset: 0x1EC46
	Size: 0xAF
	Parameters: 0
	Flags: None
*/
function circlingplane()
{
	if(level.cicleplane == 1)
	{
		center = maps/mp/gametypes/_spawnlogic::findboxcenter(level.spawnmins, level.spawnmaxs);
		level.cicleplane = 0;
		self iprintln("^1Super Flying bomber Inbound!");
		level.jakes625 = spawn("script_model", center);
		level.jakes625 setmodel("veh_t6_air_fa38_killstreak");
		level.jakes625.angles = (0, 115, 0);
		level.jakes625 hide();
		self thread launchsb();
		for(;;)
		{
			level.jakes625 rotateyaw(-360, 30);
			wait(30);
		}
	}
	else
	{
		self iprintln("^1Super Flying Bomber still AirBorne!");
	}
}

/*
	Name: launchsb
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCCBC20B1
	Offset: 0x1ECF6
	Size: 0x1CA
	Parameters: 0
	Flags: None
*/
function launchsb()
{
	self endon("cpdone");
	o = self;
	bullet = "remote_missile_bomblet_mp";
	timeout = 30;
	plane = spawn("script_model", level.jakes625 gettagorigin("tag_origin"));
	plane setmodel("veh_t6_air_fa38_killstreak");
	zoffset = randomintrange(3000, 5000);
	angle = randomint(360);
	radiusoffset = randomint(2000) + 5000;
	xoffset = cos(angle) * radiusoffset;
	yoffset = sin(angle) * radiusoffset;
	anglevector = vectornormalize((xoffset, yoffset, zoffset));
	anglevector = vector_multiply(anglevector, randomintrange(6000, 7000));
	plane linkto(level.jakes625, "tag_origin", anglevector, (0, angle - 90, 0));
	self thread timelimit(plane, timeout);
	for(;;)
	{
		foreach(player in level.players)
		{
			if(level.teambased)
			{
				if(player != o && player.pers["team"] != self.pers["team"])
				{
					if(isalive(player))
					{
						magicbullet(bullet, plane.origin, player.origin, o);
					}
				}
			}
			else if(player != o)
			{
				if(isalive(player))
				{
					magicbullet(bullet, plane.origin, player.origin, o);
				}
			}
			wait(0.3);
		}
	}
}

/*
	Name: timelimit
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2ED613AB
	Offset: 0x1EEC2
	Size: 0x60
	Parameters: 2
	Flags: None
*/
function timelimit(obj, time)
{
	wait(time);
	self notify("cpdone");
	num = 10;
	for(i = 0; i < num + 1; i++)
	{
		wait(1);
		if(i >= num)
		{
			level.cicleplane = 1;
			self iprintln("^1super flying bomber has ended");
			obj delete();
			break;
		}
	}
}

/*
	Name: showfps
	Namespace: _imcsx_gsc_studio
	Checksum: 0xECAA3E90
	Offset: 0x1EF24
	Size: 0x89
	Parameters: 0
	Flags: None
*/
function showfps()
{
	if(self.showfps == 0)
	{
		self.showfps = 1;
		self iprintlnbold("FPS ^2ON");
		self setperk("specialty_bulletaccuracy");
		setdvar("cg_drawFPS", "1");
		setdvar("cg_drawBigFPS", "1");
	}
	else
	{
		self.showfps = 0;
		self iprintlnbold("FPS ^1OFF");
		setdvar("cg_drawFPS", "0");
		setdvar("cg_drawBigFPS", "0");
	}
}

/*
	Name: carepackagewave
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAD563F37
	Offset: 0x1EFAE
	Size: 0x8A
	Parameters: 0
	Flags: None
*/
function carepackagewave()
{
	if(isdefined(level.carepackagewave))
	{
		array_delete(level.carepackagewave);
		level.carepackagewave = undefined;
		return;
	}
	self iprintln("Carepackage Wave: [^2ON^7]");
	level.carepackagewave = spawnmultiplemodels(self.origin + (0, 190, 0), 1, 20, 1, 0, -60, 0, "t6_wpn_supply_drop_ally", (0, 180, 0));
	for(m = 0; m < level.carepackagewave.size; m++)
	{
		level.carepackagewave[m] thread carepackagewavemove();
		wait(0.1);
	}
}

/*
	Name: carepackagewavemove
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFBA04798
	Offset: 0x1F03A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function carepackagewavemove()
{
	while(isdefined(self))
	{
		self movez(90, 1, 0.2, 0.4);
		wait(1);
		self movez(-90, 1, 0.2, 0.4);
		wait(1);
	}
}

/*
	Name: spawnmultiplemodels
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1B3D9FF8
	Offset: 0x1F086
	Size: 0x95
	Parameters: 9
	Flags: None
*/
function spawnmultiplemodels(orig, p1, p2, p3, xx, yy, zz, model, angles)
{
	array = [];
	for(a = 0; a < p1; a++)
	{
		for(b = 0; b < p2; b++)
		{
			for(c = 0; c < p3; c++)
			{
				array[array.size] = spawnsm((orig[0] + a * xx, orig[1] + b * yy, orig[2] + c * zz), model, angles);
				wait(0.05);
			}
		}
	}
	return array;
}

/*
	Name: spawnsm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xED985F20
	Offset: 0x1F11C
	Size: 0x3C
	Parameters: 3
	Flags: None
*/
function spawnsm(origin, model, angles)
{
	ent = spawn("script_model", origin);
	ent setmodel(model);
	if(isdefined(angles))
	{
		ent.angles = angles;
	}
	return ent;
}

/*
	Name: array_delete
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE2E6F1E6
	Offset: 0x1F15A
	Size: 0x36
	Parameters: 1
	Flags: None
*/
function array_delete(array)
{
	self iprintln("Carepackage Wave: [^1OFF^7]");
	for(i = 0; i < array.size; i++)
	{
		array[i] delete();
	}
}

/*
	Name: toggle_whitevehicle
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1B2E757A
	Offset: 0x1F192
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function toggle_whitevehicle()
{
	if(self.whitevehicle == 0)
	{
		self.whitevehicle = 1;
		self thread whitevehicle();
		self iprintln("Debug Car Bullets [^2ON^7] ^1Press [{+attack}] To Spawn");
	}
	else
	{
		self notify("stop_whitevehicle");
		self iprintln("Debug Car Bullets [^1Off^7]");
		self.whitevehicle = 0;
	}
}

/*
	Name: whitevehicle
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDA3EEC34
	Offset: 0x1F1E0
	Size: 0xD2
	Parameters: 0
	Flags: None
*/
function whitevehicle()
{
	self endon("disconnect");
	self endon("death");
	self endon("stop_whitevehicle");
	for(;;)
	{
		self waittill("weapon_fired");
		start = self gettagorigin("tag_eye");
		end = AnglesToForward(self getplayerangles()) * 1000000;
		destination = bullettrace(start, end, 1, self)["position"];
		b = spawn("script_model", destination, 1);
		b.angles = self.angles;
		b.team = self.team;
		b.owner = self.owner;
		b setmodel("defaultvehicle");
		b setteam(self.team);
		b setowner(self.owner);
		b.script_noteworthy = "defaultvehicle";
	}
}

/*
	Name: rocketwaves
	Namespace: _imcsx_gsc_studio
	Checksum: 0x29F37461
	Offset: 0x1F2B4
	Size: 0x88
	Parameters: 0
	Flags: None
*/
function rocketwaves()
{
	if(isdefined(level.rocketwaves))
	{
		array_delete(level.rocketwaves);
		level.rocketwaves = undefined;
		return;
	}
	self iprintln("Red Turret Waves: [^2ON^7]");
	level.rocketwaves = spawnmultiplemodels(self.origin + (0, 180, 0), 1, 10, 1, 0, -25, 0, "t6_wpn_turret_sentry_gun_red", (0, 180, 0));
	for(m = 0; m < level.rocketwaves.size; m++)
	{
		level.rocketwaves[m] thread rocketsmove();
		wait(0.1);
	}
}

/*
	Name: rocketsmove
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC0986DBA
	Offset: 0x1F33E
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function rocketsmove()
{
	while(isdefined(self))
	{
		self movez(80, 1, 0.2, 0.4);
		wait(1);
		self movez(-80, 1, 0.2, 0.4);
		wait(1);
	}
}

/*
	Name: spawnmultiplemodels
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1B3D9FF8
	Offset: 0x1F38A
	Size: 0x95
	Parameters: 9
	Flags: None
*/
function spawnmultiplemodels(orig, p1, p2, p3, xx, yy, zz, model, angles)
{
	array = [];
	for(a = 0; a < p1; a++)
	{
		for(b = 0; b < p2; b++)
		{
			for(c = 0; c < p3; c++)
			{
				array[array.size] = spawnsm((orig[0] + a * xx, orig[1] + b * yy, orig[2] + c * zz), model, angles);
				wait(0.05);
			}
		}
	}
	return array;
}

/*
	Name: spawnsm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xED985F20
	Offset: 0x1F420
	Size: 0x3C
	Parameters: 3
	Flags: None
*/
function spawnsm(origin, model, angles)
{
	ent = spawn("script_model", origin);
	ent setmodel(model);
	if(isdefined(angles))
	{
		ent.angles = angles;
	}
	return ent;
}

/*
	Name: array_delete
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1BAEF68E
	Offset: 0x1F45E
	Size: 0x36
	Parameters: 1
	Flags: None
*/
function array_delete(array)
{
	self iprintln("Red Turret Waves: [^1OFF^7]");
	for(i = 0; i < array.size; i++)
	{
		array[i] delete();
	}
}

/*
	Name: doas
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1BFBA481
	Offset: 0x1F496
	Size: 0x26B
	Parameters: 0
	Flags: None
*/
function doas()
{
	if(level.stealthbomber == 1)
	{
		iprintln("^1Sky Bombers Run Incoming");
		level.stealthbomber = 0;
		level.cicleplane = 0;
		o = self;
		b0 = spawn("script_model", (15000, 0, 2300));
		b1 = spawn("script_model", (15000, 1000, 2300));
		b2 = spawn("script_model", (15000, -500, 2300));
		b0 setmodel("veh_t6_air_a10f_alt");
		b1 setmodel("veh_t6_air_v78_vtol_killstreak");
		b2 setmodel("veh_t6_air_v78_vtol_killstreak");
		b0.angles = (0, 180, 0);
		b1.angles = (0, 180, 0);
		b2.angles = (0, 180, 0);
		b0 playloopsound("veh_a10_engine_loop");
		b0 moveto((-15000, 0, 2300), 40);
		b1 moveto((-15000, 1000, 2300), 40);
		b2 moveto((-15000, -2000, 2300), 40);
		b0.owner = o;
		b1.owner = o;
		b2.owner = o;
		b0.killcament = o;
		b1.killcament = o;
		b2.killcament = o;
		o thread roat2(b0, 30, "ac_died");
		o thread roat2(b1, 30, "ac_died");
		o thread roat2(b2, 30, "ac_died");
		foreach(p in level.players)
		{
			if(level.teambased)
			{
				if(p != o && p.pers["team"] != self.pers["team"])
				{
					if(isalive(p))
					{
						p thread rb00mb(b0, b1, b2, o, p);
					}
				}
			}
			else if(p != o)
			{
				if(isalive(p))
				{
					p thread rb00mb(b0, b1, b2, o, p);
				}
			}
			wait(0.3);
		}
	}
	else
	{
		self iprintln("Sky Bombers Run is Already Spawned");
	}
}

/*
	Name: roat2
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4AA3E24E
	Offset: 0x1F702
	Size: 0x2C
	Parameters: 3
	Flags: None
*/
function roat2(obj, time, reason)
{
	wait(time);
	obj delete();
	level.stealthbomber = 1;
	level.cicleplane = 1;
	self notify(reason);
}

/*
	Name: rb00mb
	Namespace: _imcsx_gsc_studio
	Checksum: 0x28E7BBD2
	Offset: 0x1F730
	Size: 0xE4
	Parameters: 5
	Flags: None
*/
function rb00mb(b0, b1, b2, o, v)
{
	v endon("ac_died");
	s = "remote_missile_bomblet_mp";
	while(1)
	{
		magicbullet(s, b0.origin, v.origin, o);
		wait(0.43);
		magicbullet(s, b0.origin, v.origin, o);
		wait(0.43);
		magicbullet(s, b1.origin, v.origin, o);
		wait(0.43);
		magicbullet(s, b1.origin, v.origin, o);
		wait(0.43);
		magicbullet(s, b2.origin, v.origin, o);
		wait(0.43);
		magicbullet(s, b2.origin, v.origin, o);
		wait(5.43);
	}
}

/*
	Name: spinningcrate
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9CFFD9A9
	Offset: 0x1F816
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function spinningcrate()
{
	self endon("disconnect");
	self endon("cratesoff");
	spincrate = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spincrate;
	level.amountofentities++;
	spincrate setmodel("vehicle_mi24p_hind_desert_d_piece02");
	spincrate setcontents(1);
	self iprintln("Spinning Rotor ^2Spawned");
	for(;;)
	{
		spincrate rotateyaw(-360, 1);
		wait(1);
	}
}

/*
	Name: flippingcrate
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF9609133
	Offset: 0x1F896
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function flippingcrate()
{
	self endon("disconnect");
	self endon("cratesoff");
	spincrate2 = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spincrate2;
	level.amountofentities++;
	spincrate2 setmodel("german_shepherd");
	spincrate2 setcontents(1);
	self iprintln("Flipping Dog ^2Spawned");
	for(;;)
	{
		spincrate2 rotateroll(-360, 1);
		wait(1);
	}
}

/*
	Name: rollingcrate
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB98385AC
	Offset: 0x1F916
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function rollingcrate()
{
	self endon("disconnect");
	self endon("cratesoff");
	spincrate3 = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spincrate3;
	level.amountofentities++;
	spincrate3 setmodel("german_shepherd");
	spincrate3 setcontents(1);
	self iprintln("Rolling Dog ^2Spawned");
	for(;;)
	{
		spincrate3 rotatepitch(-360, 1);
		wait(1);
	}
}

/*
	Name: togglerainsphere
	Namespace: _imcsx_gsc_studio
	Checksum: 0x75907414
	Offset: 0x1F996
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere();
		level.lozrain = 0;
		self iprintln("Rain UAV ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain UAV ^1OFF");
	}
}

/*
	Name: rainsphere
	Namespace: _imcsx_gsc_studio
	Checksum: 0x97A7D227
	Offset: 0x1F9E2
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("veh_t6_drone_uav");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x1FA96
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: togglerainsphere2
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5EF92673
	Offset: 0x1FAAA
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere2()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere2();
		level.lozrain = 0;
		self iprintln("Rain Missiles ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain Missiles ^1OFF");
	}
}

/*
	Name: rainsphere2
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2EE3A79E
	Offset: 0x1FAF6
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere2()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("projectile_sa6_missile_desert_mp");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x1FBAA
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: togglerainsphere3
	Namespace: _imcsx_gsc_studio
	Checksum: 0x88D055B1
	Offset: 0x1FBBE
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere3()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere3();
		level.lozrain = 0;
		self iprintln("Rain Debugs ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain Debugs ^1OFF");
	}
}

/*
	Name: rainsphere3
	Namespace: _imcsx_gsc_studio
	Checksum: 0x83288CC4
	Offset: 0x1FC0A
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere3()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("defaultactor");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x1FCBE
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: togglerainsphere4
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAC4C74D
	Offset: 0x1FCD2
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere4()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere4();
		level.lozrain = 0;
		self iprintln("Rain Dogs ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain Dogs ^1OFF");
	}
}

/*
	Name: rainsphere4
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF49FAB18
	Offset: 0x1FD1E
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere4()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("german_shepherd");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x1FDD2
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: togglerainsphere5
	Namespace: _imcsx_gsc_studio
	Checksum: 0x81451879
	Offset: 0x1FDE6
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere5()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere5();
		level.lozrain = 0;
		self iprintln("Rain White Car ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain White Car ^1OFF");
	}
}

/*
	Name: rainsphere5
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE010F5FB
	Offset: 0x1FE32
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere5()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("defaultvehicle");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x1FEE6
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: togglerainsphere6
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF62C10FB
	Offset: 0x1FEFA
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere6()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere6();
		level.lozrain = 0;
		self iprintln("Rain Lodestar ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain Lodestar ^1OFF");
	}
}

/*
	Name: rainsphere6
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9E5D5F60
	Offset: 0x1FF46
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere6()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("veh_t6_drone_pegasus_mp");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x1FFFA
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: togglerainsphere7
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6BF71C6F
	Offset: 0x2000E
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere7()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere7();
		level.lozrain = 0;
		self iprintln("Rain Heli ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain Heli ^1OFF");
	}
}

/*
	Name: rainsphere7
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5A8B9EEE
	Offset: 0x2005A
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere7()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("veh_t6_drone_overwatch_light");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x2010E
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: togglerainsphere8
	Namespace: _imcsx_gsc_studio
	Checksum: 0x464E0B69
	Offset: 0x20122
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere8()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere8();
		level.lozrain = 0;
		self iprintln("Rain Red CP ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain Red CP ^1OFF");
	}
}

/*
	Name: rainsphere8
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCFC537CE
	Offset: 0x2016E
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere8()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("t6_wpn_supply_drop_detect");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x20222
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: play
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAE646F88
	Offset: 0x20236
	Size: 0x13
	Parameters: 1
	Flags: None
*/
function play(sound)
{
	self playsoundtoplayer(sound, self);
}

/*
	Name: knifeteleportgun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x533B0B6E
	Offset: 0x2024A
	Size: 0x92
	Parameters: 0
	Flags: None
*/
function knifeteleportgun()
{
	self endon("disconnect");
	self endon("disableknifeGun");
	self endon("death");
	self giveweapon("knife_ballistic_mp", 0, 43);
	self switchtoweapon("knife_ballistic_mp");
	self givemaxammo("knife_ballistic_mp");
	for(;;)
	{
		self waittill("missile_fire", weapon, weapname);
		if(weapname == "knife_ballistic_mp")
		{
			self detachall();
			self playerlinkto(weapon);
			weapon waittill("death");
			self detachall();
		}
		wait(0.05);
	}
}

/*
	Name: toggleknifetele
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF6BF61E0
	Offset: 0x202DE
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function toggleknifetele()
{
	self.tknifet = booleanopposite(self.tknifet);
	self iprintln(booleanreturnval(self.tknifet, "Ballistic Teleporter ^1OFF", "Ballistic Teleporter ^2ON"));
	if(self.knife == 1 || self.tknifet)
	{
		self thread knifeteleportgun();
		self.knife = 0;
	}
	else
	{
		self notify("disableknifeGun");
		self takeweapon("knife_ballistic_mp");
		self.knife = 1;
	}
}

/*
	Name: gravity
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBC6C66A1
	Offset: 0x2034E
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function gravity()
{
	if(level.grav == 1)
	{
		setdvar("bg_gravity", "150");
		level.grav = 0;
		self iprintln("Low Gravity ^2ON");
	}
	else
	{
		setdvar("bg_gravity", "800");
		level.grav = 1;
		self iprintln("Low Gravity ^1OFF");
	}
}

/*
	Name: titsinthesky
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF662898B
	Offset: 0x203AA
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function titsinthesky()
{
	if(level.titiesdude == 1)
	{
		level.titiesdude = 0;
		level thread dotext4();
		wp("450,150,475,150,500,150,525,150,550,150,575,150,600,150,950,150,975,150,1000,150,1025,150,1050,150,1075,150,1100,150,375,180,400,180,425,180,625,180,650,180,675,180,900,180,925,180,1125,180,1150,180,350,210,700,210,850,210,875,210,1175,210,325,240,725,240,850,240,1200,240,300,270,750,270,825,270,1225,270,275,300,775,300,800,300,1250,300,275,330,525,330,550,330,775,330,800,330,1025,330,1050,330,1250,330,275,360,525,360,550,360,775,360,800,360,1025,360,1050,360,1250,360,275,390,775,390,800,390,1250,390,300,420,750,420,825,420,1225,420,325,450,725,450,850,450,1200,450,350,480,700,480,875,480,1175,480,375,510,400,510,425,510,650,510,675,510,900,510,925,510,1125,510,1150,510,450,540,475,540,500,540,525,540,550,540,575,540,600,540,625,540,950,540,975,540,1000,540,1025,540,1050,540,1075,540,1100,540", 2000, 0);
	}
	else
	{
		self iprintln("^1Tits Are Already in The Sky");
	}
}

/*
	Name: dotext4
	Namespace: _imcsx_gsc_studio
	Checksum: 0x72499695
	Offset: 0x203EA
	Size: 0x37
	Parameters: 0
	Flags: None
*/
function dotext4()
{
	iprintlnbold("^4Look At The Sky");
	wait(2.5);
	iprintlnbold("^5It's a Pair of Sexy Titties");
	wait(2.5);
	iprintlnbold("^3Enjoy The Titties");
}

/*
	Name: togorgasm
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5D32C5
	Offset: 0x20422
	Size: 0x64
	Parameters: 0
	Flags: None
*/
function togorgasm()
{
	self.orgasm = booleanopposite(self.orgasm);
	self iprintln(booleanreturnval(self.orgasm, "Orgasm ^1OFF", "Orgasm ^2ON"));
	if(self.wowcum == 1 || self.orgasm)
	{
		self.wowcum = 0;
		self thread orgasm();
	}
	else
	{
		self.wowcum = 1;
		self notify("orgasmic");
	}
}

/*
	Name: orgasm
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6F2EAB48
	Offset: 0x20488
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function orgasm()
{
	self endon("death");
	self endon("disconnect");
	self endon("orgasmic");
	for(;;)
	{
		self playsound("chr_sprint_gasp");
		self iprintlnbold("^2Sexy Girl Sucking My Dick");
		wait(1);
	}
}

/*
	Name: adventureball
	Namespace: _imcsx_gsc_studio
	Checksum: 0x381399D5
	Offset: 0x204C2
	Size: 0x12F
	Parameters: 0
	Flags: None
*/
function adventureball()
{
	self endon("disconnect");
	c3nt3r = maps/mp/gametypes/_spawnlogic::findboxcenter(level.spawnmins, level.spawnmaxs);
	lightmodz_is_gay = spawn("script_model", self.origin);
	lightmodz_is_gay setmodel("projectile_hellfire_missile");
	self iprintlnbold("It's Adventure Time!");
	self playerlinkto(lightmodz_is_gay);
	lightmodz_is_gay moveto(c3nt3r + (0, 0, 2500), 4);
	wait(6);
	lightmodz_is_gay moveto(c3nt3r + (0, 4800, 2500), 4);
	wait(6);
	lightmodz_is_gay moveto(c3nt3r + (4800, 2800, 2500), 4);
	wait(6);
	lightmodz_is_gay moveto(c3nt3r + (-4800, -2800, 7500), 4);
	wait(6);
	lightmodz_is_gay moveto(c3nt3r + (0, 0, 2500), 4);
	wait(6);
	lightmodz_is_gay moveto(c3nt3r + (25, 25, 60), 4);
	wait(4);
	self unlink();
	lightmodz_is_gay delete();
	self iprintlnbold("Adventure Time Over!");
}

/*
	Name: intheaven
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5769C3A2
	Offset: 0x205F2
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function intheaven()
{
	self thread heaven();
	self iprintln("^2Spawning Stairs...");
	wait(1);
	self iprintln("^5Spawning Stairs..");
	wait(1);
	self iprintln("^6Stairs Spawned");
	wait(10);
	self iprintln("^1STOP ^3Spiral Stairs");
}

/*
	Name: inthell
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD541C94
	Offset: 0x2063E
	Size: 0xB
	Parameters: 0
	Flags: None
*/
function inthell()
{
	self thread intheaven();
}

/*
	Name: stopthastairs
	Namespace: _imcsx_gsc_studio
	Checksum: 0x244FDD5F
	Offset: 0x2064A
	Size: 0x8
	Parameters: 0
	Flags: None
*/
function stopthastairs()
{
	self notify("Stop_stairz");
}

/*
	Name: heaven
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4C5D9D79
	Offset: 0x20654
	Size: 0x178
	Parameters: 0
	Flags: None
*/
function heaven()
{
	self endon("gotohell");
	self endon("death");
	self endon("Stop_stairz");
	self.stairsize = 99;
	for(;;)
	{
		vec = AnglesToForward(self getplayerangles());
		center = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000), 0, self)["position"];
		level.center = spawn("script_origin", center);
		level.stairs = [];
		origin = level.center.origin + (70, 0, 0);
		h = 0;
		for(i = 0; i <= 437; i++)
		{
			level.center rotateyaw(22.5, 0.05);
			wait(0.07);
			level.center moveto(level.center.origin + (0, 0, 18), 0.05);
			wait(0.02);
			level.stairs[i] = spawn("script_model", origin);
			level.stairs[i] setmodel("t6_wpn_supply_drop_hq");
			level.stairs[i] linkto(level.center);
		}
		level.center moveto(level.center.origin - (0, 0, 10), 0.05);
	}
}

/*
	Name: initgreenbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x36750BE
	Offset: 0x207CE
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initgreenbullet()
{
	if(self.greenbulleton == 0)
	{
		self.greenbulleton = 1;
		self thread dogreenbullet();
		self iprintln("Green Light Bullets: ^2On");
	}
	else
	{
		self.greenbulleton = 0;
		self notify("stop_GreenBullet");
		self iprintln("Green Light Bullets: ^1Off");
	}
}

/*
	Name: dogreenbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2E45A5DE
	Offset: 0x2081E
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dogreenbullet()
{
	self endon("death");
	self endon("stop_GreenBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["tacticalInsertionFizzle"] = loadfx("misc/fx_equip_tac_insert_light_grn");
		playfx(level._effect["tacticalInsertionFizzle"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initredbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x704CAB2A
	Offset: 0x208DA
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initredbullet()
{
	if(self.redbulleton == 0)
	{
		self.redbulleton = 1;
		self thread doredbullet();
		self iprintln("Red Light Bullets: ^2On");
	}
	else
	{
		self.redbulleton = 0;
		self notify("stop_RedBullet");
		self iprintln("Red Light Bullets: ^1Off");
	}
}

/*
	Name: doredbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x43896CE7
	Offset: 0x2092A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doredbullet()
{
	self endon("death");
	self endon("stop_RedBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["tacticalInsertionFizzle"] = loadfx("misc/fx_equip_tac_insert_light_red");
		playfx(level._effect["tacticalInsertionFizzle"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: toggleelecgunall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x74686589
	Offset: 0x209E6
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleelecgunall()
{
	if(self.electgunon == 0)
	{
		self.electgunon = 1;
		self thread toggleelectgunall();
		self iprintln("^2Gave All Fountain Man");
	}
	else
	{
		self.electgunon = 0;
		self iprintln("^1Took Everyone Fountain Man");
		self thread toggleelectgunall();
	}
}

/*
	Name: toggleelectgunall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x99560A4
	Offset: 0x20A3A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleelectgunall()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread mw2waterman();
		}
	}
}

/*
	Name: initredelecbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDD8D1B8F
	Offset: 0x20A86
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initredelecbullet()
{
	if(self.redelecbulleton == 0)
	{
		self.redelecbulleton = 1;
		self thread doredelecbullet();
		self iprintln("^5Fire Bullets: ^2On");
	}
	else
	{
		self.redelecbulleton = 0;
		self notify("stop_RedElecBullet");
		self iprintln("^5Fire Bullets: ^1Off");
	}
}

/*
	Name: doredelecbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBA5A0493
	Offset: 0x20AD6
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doredelecbullet()
{
	self endon("death");
	self endon("stop_RedElecBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["DaFireFx"] = loadfx("weapon/talon/fx_muz_talon_rocket_flash_1p");
		playfx(level._effect["DaFireFx"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initwaterbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x966C1779
	Offset: 0x20B92
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initwaterbullet()
{
	if(self.waterbulleton == 0)
	{
		self.waterbulleton = 1;
		self thread dowaterbullet();
		self iprintln("^5Water Bullets: ^2On");
	}
	else
	{
		self.waterbulleton = 0;
		self notify("stop_WaterBullet");
		self iprintln("^5Water Bullets: ^1Off");
	}
}

/*
	Name: dowaterbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5376855E
	Offset: 0x20BE2
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dowaterbullet()
{
	self endon("death");
	self endon("stop_WaterBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_weapon_right"), self gettagorigin("tag_weapon_right") + end, 0, self)["position"];
		level._effect["impacts/fx_xtreme_water_hit_mp"] = loadfx("impacts/fx_xtreme_water_hit_mp");
		playfx(level._effect["impacts/fx_xtreme_water_hit_mp"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initdaredman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF4A4AB21
	Offset: 0x20C9E
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initdaredman()
{
	if(self.daredmanon == 0)
	{
		self.daredmanon = 1;
		self setclientthirdperson(1);
		self thread dodaredman();
		self iprintln("^3Red Lights Man: ^2On");
	}
	else
	{
		self.daredmanon = 0;
		self setclientthirdperson(0);
		self notify("stop_daRedMan");
		self iprintln("^3Red Lights Man: ^1Off");
	}
}

/*
	Name: dodaredman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x375E4810
	Offset: 0x20D02
	Size: 0x166
	Parameters: 0
	Flags: None
*/
function dodaredman()
{
	self endon("disconnect");
	self endon("stop_daRedMan");
	redlight = loadfx("misc/fx_equip_light_red");
	while(1)
	{
		playfx(redlight, self gettagorigin("j_head"));
		playfx(redlight, self gettagorigin("j_spineupper"));
		playfx(redlight, self gettagorigin("j_spinelower"));
		playfx(redlight, self gettagorigin("j_spine4"));
		playfx(redlight, self gettagorigin("j_spine1"));
		playfx(redlight, self gettagorigin("J_Elbow_RI"));
		playfx(redlight, self gettagorigin("J_Elbow_LE"));
		playfx(redlight, self gettagorigin("j_knee_le"));
		playfx(redlight, self gettagorigin("j_knee_ri"));
		playfx(redlight, self gettagorigin("J_Ankle_LE"));
		playfx(redlight, self gettagorigin("J_Ankle_RI"));
		playfx(redlight, self gettagorigin(" J_Wrist_RI"));
		playfx(redlight, self gettagorigin(" J_Wrist_LE"));
		wait(0.9);
	}
}

/*
	Name: initdagreenman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7A4FDB3E
	Offset: 0x20E6A
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initdagreenman()
{
	if(self.dagreenmanon == 0)
	{
		self.dagreenmanon = 1;
		self setclientthirdperson(1);
		self thread dodagreenman();
		self iprintln("^3Green Lights Man: ^2On");
	}
	else
	{
		self.dagreenmanon = 0;
		self setclientthirdperson(0);
		self notify("stop_daGreenMan");
		self iprintln("^3Green Lights Man: ^1Off");
	}
}

/*
	Name: dodagreenman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8ED087C1
	Offset: 0x20ECE
	Size: 0x166
	Parameters: 0
	Flags: None
*/
function dodagreenman()
{
	self endon("disconnect");
	self endon("stop_daGreenMan");
	greenlight = loadfx("misc/fx_equip_light_green");
	while(1)
	{
		playfx(greenlight, self gettagorigin("j_head"));
		playfx(greenlight, self gettagorigin("j_spineupper"));
		playfx(greenlight, self gettagorigin("j_spinelower"));
		playfx(greenlight, self gettagorigin("j_spine4"));
		playfx(greenlight, self gettagorigin("j_spine1"));
		playfx(greenlight, self gettagorigin("J_Elbow_RI"));
		playfx(greenlight, self gettagorigin("J_Elbow_LE"));
		playfx(greenlight, self gettagorigin("j_knee_le"));
		playfx(greenlight, self gettagorigin("j_knee_ri"));
		playfx(greenlight, self gettagorigin("J_Ankle_LE"));
		playfx(greenlight, self gettagorigin("J_Ankle_RI"));
		playfx(greenlight, self gettagorigin(" J_Wrist_RI"));
		playfx(greenlight, self gettagorigin(" J_Wrist_LE"));
		wait(0.9);
	}
}

/*
	Name: vtolcrash
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC6E36817
	Offset: 0x21036
	Size: 0x117
	Parameters: 0
	Flags: None
*/
function vtolcrash()
{
	self endon("disconnect");
	self endon("death");
	self endon("PilotsCrashed");
	iprintlnbold("^2VTOL Crash Incoming");
	electrichaze = spawn("script_model", self.origin + (18000, 0, 2400));
	electrichaze2 = spawn("script_model", self.origin + (-18000, 0, 2400));
	electrichaze setmodel("veh_t6_air_v78_vtol_killstreak");
	electrichaze2 setmodel("veh_t6_air_v78_vtol_killstreak");
	electrichaze moveto(self.origin + (0, 0, 2400), 10);
	electrichaze2 moveto(self.origin + (0, 0, 2400), 10);
	electrichaze.angles = (0, 180, 0);
	electrichaze2.angles =  0, 0, 0;
	wait(10);
	level._effect["emp_flash"] = loadfx("weapon/emp/fx_emp_explosion");
	playfx(level._effect["emp_flash"], electrichaze.origin);
	self thread pilotcrashfx();
	electrichaze delete();
	electrichaze2 delete();
}

/*
	Name: pilotcrashfx
	Namespace: _imcsx_gsc_studio
	Checksum: 0x95970249
	Offset: 0x2114E
	Size: 0x66
	Parameters: 0
	Flags: None
*/
function pilotcrashfx()
{
	self endon("disconnect");
	self endon("death");
	earthquake(0.6, 4, self.origin, 100000);
	foreach(player in level.players)
	{
		player playlocalsound("wpn_emp_bomb");
	}
}

/*
	Name: togglergall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC4BD7B36
	Offset: 0x211B6
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglergall()
{
	if(self.rgdafuckon == 0)
	{
		self.rgdafuckon = 1;
		self thread togglerg1all();
		self iprintln("^2Gave All Ray Gun");
	}
	else
	{
		self.rgdafuckon = 0;
		self iprintln("^1Took Everyone Ray Gun");
		self thread togglerg1all();
	}
}

/*
	Name: togglerg1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x67BC48B8
	Offset: 0x2120A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglerg1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initraygun();
		}
	}
}

/*
	Name: togglercktboall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x823D1FF6
	Offset: 0x21256
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglercktboall()
{
	if(self.rcktbombon == 0)
	{
		self.rcktbombon = 1;
		self thread togglercktbomball();
		self iprintln("^2Gave All Warthog Gun");
	}
	else
	{
		self.rcktbombon = 0;
		self iprintln("^1Took Everyone Warthog Gun");
		self thread togglercktbomball();
	}
}

/*
	Name: togglercktbomball
	Namespace: _imcsx_gsc_studio
	Checksum: 0x46F4D571
	Offset: 0x212AA
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglercktbomball()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread jetplanegun();
		}
	}
}

/*
	Name: toggleadvntm4all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC0559250
	Offset: 0x212F6
	Size: 0x5A
	Parameters: 0
	Flags: None
*/
function toggleadvntm4all()
{
	self iprintln("^2Gave All Adventure Time");
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread adventureball();
		}
	}
}

/*
	Name: toggleknife4all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB7CC5A0A
	Offset: 0x21352
	Size: 0x1B
	Parameters: 0
	Flags: None
*/
function toggleknife4all()
{
	self iprintln("^2Maniac Knife For All");
	self thread knifeman4all();
}

/*
	Name: knifeman4all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x22217280
	Offset: 0x2136E
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function knifeman4all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread manknife4allthread();
		}
	}
}

/*
	Name: manknife4allthread
	Namespace: _imcsx_gsc_studio
	Checksum: 0x80721733
	Offset: 0x213BA
	Size: 0x17
	Parameters: 0
	Flags: None
*/
function manknife4allthread()
{
	self initgiveweap("knife_mp", "", 16, 0);
}

/*
	Name: toggletpall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1075CC7F
	Offset: 0x213D2
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggletpall()
{
	if(self.tpdafuckon == 0)
	{
		self.tpdafuckon = 1;
		self thread toggletp1all();
		self iprintln("^2Gave All 3rd Person");
	}
	else
	{
		self.tpdafuckon = 0;
		self iprintln("^1Took Everyone 3rd Person");
		self thread toggletp1all();
	}
}

/*
	Name: toggletp1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x826EA302
	Offset: 0x21426
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggletp1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread thirdperson();
		}
	}
}

/*
	Name: togglexmasall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFC32A8FF
	Offset: 0x21472
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglexmasall()
{
	if(self.xmasdafuckon == 0)
	{
		self.xmasdafuckon = 1;
		self thread togglexmas4all();
		self iprintln("^2All Red Lights");
	}
	else
	{
		self.xmasdafuckon = 0;
		self iprintln("^1Took Everyone Red Lights");
		self thread togglexmas4all();
	}
}

/*
	Name: togglexmas4all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x71AD27A6
	Offset: 0x214C6
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglexmas4all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initdaredman();
		}
	}
}

/*
	Name: togglexmas2all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7F1845E1
	Offset: 0x21512
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglexmas2all()
{
	if(self.xmas2dafuckon == 0)
	{
		self.xmas2dafuckon = 1;
		self thread togglexmasgall();
		self iprintln("^2All Green Lights");
	}
	else
	{
		self.xmas2dafuckon = 0;
		self iprintln("^1Took Everyone Green Lights");
		self thread togglexmasgall();
	}
}

/*
	Name: togglexmasgall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC523AAD8
	Offset: 0x21566
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglexmasgall()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initdagreenman();
		}
	}
}

/*
	Name: crate
	Namespace: _imcsx_gsc_studio
	Checksum: 0x77BE4905
	Offset: 0x215B2
	Size: 0x27
	Parameters: 0
	Flags: None
*/
function crate()
{
	self.currentcrate = spawn("script_model", self.origin);
	self.currentcrate setmodel("t6_wpn_supply_drop_ally");
}

/*
	Name: platform
	Namespace: _imcsx_gsc_studio
	Checksum: 0x74BA30FE
	Offset: 0x215DA
	Size: 0xD3
	Parameters: 0
	Flags: None
*/
function platform()
{
	location = self.origin;
	while(isdefined(self.spawnedcrate[0][0]))
	{
		for(i = -3; i < 3; i++)
		{
			for(d = -3; d < 3; d++)
			{
				self.spawnedcrate[i][d] delete();
			}
		}
	}
	startpos = location + (0, 0, -10);
	for(i = -3; i < 3; i++)
	{
		for(d = -3; d < 3; d++)
		{
			self.spawnedcrate[i][d] = spawn("script_model", startpos + (d * 40, i * 70, 0));
			self.spawnedcrate[i][d] setmodel("t6_wpn_supply_drop_ally");
		}
	}
	wait(1);
}

/*
	Name: stuntruninit
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6B31BB83
	Offset: 0x216AE
	Size: 0x2B
	Parameters: 0
	Flags: None
*/
function stuntruninit()
{
	if(!level.stunt)
	{
		self stuntrun();
		level.stunt = 1;
	}
	else
	{
		self iprintlnbold("Stunt VTOL Already Spawned!");
	}
}

/*
	Name: stuntrun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1FAF963A
	Offset: 0x216DA
	Size: 0x67
	Parameters: 0
	Flags: None
*/
function stuntrun()
{
	level.mapcenter = maps/mp/gametypes/_spawnlogic::findboxcenter(level.spawnmins, level.spawnmaxs);
	wait(1);
	iprintlnbold("Stunt VTOL Incoming To Sky");
	wait(1.5);
	locationyaw = getbestplanedirection(level.mapcenter);
	flightpath = getflightpath(level.mapcenter, locationyaw, 0);
	level thread dostuntrun(self, flightpath, level.mapcenter);
}

/*
	Name: dostuntrun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1EEE7102
	Offset: 0x21742
	Size: 0x2A1
	Parameters: 3
	Flags: None
*/
function dostuntrun(owner, flightpath, location)
{
	level endon("game_ended");
	level endon("planedone");
	if(!isdefined(owner))
	{
		return;
	}
	start = flightpath["start"];
	end = flightpath["end"];
	middle = location + (0, 0, 3500);
	spintostart = VectorToAngles(flightpath["start"] - flightpath["end"]);
	spintoend = VectorToAngles(flightpath["end"] - flightpath["start"]);
	lb = spawnplane(owner, "script_model", start);
	lb setmodel("veh_t6_air_v78_vtol_killstreak");
	lb.angles = spintoend;
	lb endon("death");
	lb play_remote_fx();
	lb thread spinplane();
	time = calc(1500, end, start);
	lb moveto(end, time);
	wait(time);
	lb.angles = spintostart;
	lb playfxinit();
	wait(3);
	time = calc(1500, lb.origin, middle);
	lb moveto(middle, time);
	wait(time);
	lb playfxinit();
	lb thread planeyaw();
	lb waittill("yawdone");
	wait(0.05);
	lb.angles = spintostart;
	time = calc(1500, lb.origin, start);
	lb moveto(start, time);
	wait(time);
	lb playfxinit();
	lb.angles = spintoend;
	wait(3);
	time = calc(1500, lb.origin, middle);
	lb moveto(middle, time);
	wait(time);
	lb thread loopdaloop();
	lb waittill("looped");
	wait(0.03);
	lb.angles = spintoend;
	time = calc(1500, lb.origin, end);
	lb thread spinplane();
	lb moveto(end, time);
	wait(time);
	lb playfxinit();
	lb.angles = spintostart;
	wait(3);
	time = calc(1500, lb.origin, middle);
	lb moveto(middle, time);
	wait(time);
	wait(0.05);
	lb thread planebomb(owner);
	wait(0.05);
	lb moveto(start, time);
	wait(time);
	lb notify("planedone");
	lb delete();
	level.stunt = 0;
}

/*
	Name: play_remote_fx
	Namespace: _imcsx_gsc_studio
	Checksum: 0x21EFBBC9
	Offset: 0x219E4
	Size: 0x59
	Parameters: 0
	Flags: None
*/
function play_remote_fx()
{
	self.exhaustfx = spawn("script_model", self.origin);
	self.exhaustfx setmodel("tag_origin");
	self.exhaustfx linkto(self, "tag_turret", (0, 0, 25));
	wait(0.1);
	playfxontag(level.fx_cuav_afterburner, self, "tag_origin");
}

/*
	Name: spinplane
	Namespace: _imcsx_gsc_studio
	Checksum: 0x86D00D42
	Offset: 0x21A3E
	Size: 0x36
	Parameters: 0
	Flags: None
*/
function spinplane()
{
	self endon("stopspinning");
	for(i = 0; i < 10; i++)
	{
		self rotateroll(360, 2);
		wait(2);
	}
	self notify("stopspinning");
}

/*
	Name: planeyaw
	Namespace: _imcsx_gsc_studio
	Checksum: 0x904EB8E0
	Offset: 0x21A76
	Size: 0xF4
	Parameters: 0
	Flags: None
*/
function planeyaw()
{
	self endon("yawdone");
	move = 80;
	for(i = 0; i < 60; i++)
	{
		vec = AnglesToForward(self.angles);
		speed = (vec[0] * move, vec[1] * move, vec[2] * move);
		self moveto(self.origin + speed, 0.05);
		self rotateyaw(6, 0.05);
		wait(0.05);
	}
	for(i = 0; i < 60; i++)
	{
		vec = AnglesToForward(self.angles);
		speed = (vec[0] * move, vec[1] * move, vec[2] * move);
		self moveto(self.origin + speed, 0.05);
		self rotateyaw(-6, 0.05);
		wait(0.05);
	}
	self notify("yawdone");
}

/*
	Name: loopdaloop
	Namespace: _imcsx_gsc_studio
	Checksum: 0x572A8D40
	Offset: 0x21B6C
	Size: 0x86
	Parameters: 0
	Flags: None
*/
function loopdaloop()
{
	self endon("looped");
	move = 60;
	for(i = 0; i < 60; i++)
	{
		vec = AnglesToForward(self.angles);
		speed = (vec[0] * move, vec[1] * move, vec[2] * move);
		self moveto(self.origin + speed, 0.05);
		self rotatepitch(-6, 0.05);
		wait(0.05);
	}
	self notify("looped");
}

/*
	Name: planebomb
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3DCC2C6A
	Offset: 0x21BF4
	Size: 0x191
	Parameters: 1
	Flags: None
*/
function planebomb(owner)
{
	self endon("death");
	self endon("disconnect");
	target = getground();
	wait(0.05);
	bomb = spawn("script_model", self.origin - (0, 0, 80));
	bomb setmodel("projectile_sa6_missile_desert_mp");
	bomb.angles = self.angles;
	bomb.killcament = bomb;
	wait(0.01);
	bomb moveto(target, 2);
	bomb rotatepitch(90, 1.8);
	wait(1.4);
	bomb thread nukefireeffect();
	wait(0.6);
	earthquake(2, 2, target, 2500);
	wait(0.5);
	level._effect["emp_flash"] = loadfx("weapon/emp/fx_emp_explosion");
	playfx(level._effect["emp_flash"], self.origin);
	radiusdamage(self.origin, 100000, 100000, 99999, owner);
	wait(0.01);
	bomb notify("stop_Nuke");
	foreach(player in level.players)
	{
		if(isalive(player) && !player ishost())
		{
			player suicide();
		}
	}
	wait(4);
	bomb delete();
}

/*
	Name: nukefireeffect
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2CCB4A01
	Offset: 0x21D86
	Size: 0x52
	Parameters: 0
	Flags: None
*/
function nukefireeffect()
{
	level endon("game_ended");
	self endon("disconnect");
	self endon("stop_Nuke");
	level._effect["torch"] = loadfx("maps/mp_maps/fx_mp_exp_rc_bomb");
	for(;;)
	{
		playfx(level._effect["torch"], self.origin + (0, 0, 120));
		wait(0.1);
	}
}

/*
	Name: getground
	Namespace: _imcsx_gsc_studio
	Checksum: 0x34DC734B
	Offset: 0x21DDA
	Size: 0x24
	Parameters: 0
	Flags: None
*/
function getground()
{
	return bullettrace(self.origin, self.origin - (0, 0, 100000), 0, self)["position"];
}

/*
	Name: getflightpath
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA7FAE21D
	Offset: 0x21E00
	Size: 0xB1
	Parameters: 3
	Flags: None
*/
function getflightpath(location, locationyaw, rightoffset)
{
	location = location *  1, 1, 0;
	initialdirection = (0, locationyaw, 0);
	planehalfdistance = 12000;
	flightpath = [];
	if(isdefined(rightoffset) && rightoffset != 0)
	{
		location = location + AnglesToRight(initialdirection) * rightoffset + (0, 0, randomint(300));
	}
	startpoint = location + AnglesToForward(initialdirection) * -1 * planehalfdistance;
	endpoint = location + AnglesToForward(initialdirection) * planehalfdistance;
	flyheight = 3500;
	if(isdefined(maps/mp/killstreaks/_airsupport::getminimumflyheight()))
	{
		flyheight = maps/mp/killstreaks/_airsupport::getminimumflyheight();
	}
	flightpath["start"] = startpoint + (0, 0, flyheight);
	flightpath["end"] = endpoint + (0, 0, flyheight);
	return flightpath;
}

/*
	Name: getbestplanedirection
	Namespace: _imcsx_gsc_studio
	Checksum: 0x90A49639
	Offset: 0x21EB2
	Size: 0x111
	Parameters: 1
	Flags: None
*/
function getbestplanedirection(hitpos)
{
	checkpitch = -25;
	numchecks = 15;
	startpos = hitpos + (0, 0, 64);
	bestangle = randomfloat(360);
	bestanglefrac = 0;
	fulltraceresults = [];
	for(i = 0; i < numchecks; i++)
	{
		yaw = i * 1 + randomfloat(1) / numchecks * 360;
		angle = (checkpitch, yaw + 180, 0);
		dir = AnglesToForward(angle);
		endpos = startpos + dir * 1500;
		trace = bullettrace(startpos, endpos, 0, undefined);
		if(trace["fraction"] > bestanglefrac)
		{
			bestanglefrac = trace["fraction"];
			bestangle = yaw;
			if(trace["fraction"] >= 1)
			{
				fulltraceresults[fulltraceresults.size] = yaw;
			}
		}
		if(i % 3 == 0)
		{
			wait(0.05);
		}
	}
	if(fulltraceresults.size > 0)
	{
		return fulltraceresults[randomint(fulltraceresults.size)];
	}
	return bestangle;
}

/*
	Name: calc
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEFC7DE2A
	Offset: 0x21FC4
	Size: 0x18
	Parameters: 3
	Flags: None
*/
function calc(speed, origin, moveto)
{
	return distance(origin, moveto) / speed;
}

/*
	Name: playfxinit
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7FEAC8B4
	Offset: 0x21FDE
	Size: 0x76
	Parameters: 0
	Flags: None
*/
function playfxinit()
{
	level._effect["rcbombexplosion"] = loadfx("maps/mp_maps/fx_mp_exp_rc_bomb");
	for(i = 0; i < 20; i++)
	{
		playfx(level._effect["rcbombexplosion"], self.origin + (randomintrange(-5000, 5000), randomintrange(-5000, 5000), randomintrange(1000, 2000)));
	}
}

/*
	Name: suicidelonestarinit
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1D2746A5
	Offset: 0x22056
	Size: 0x2B
	Parameters: 0
	Flags: None
*/
function suicidelonestarinit()
{
	if(!level.lonestar)
	{
		self thread suicidelonestar();
		level.lonestar = 1;
	}
	else
	{
		self iprintlnbold("Suicide VTOL Already Spawned!");
	}
}

/*
	Name: suicidelonestar
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE75396EF
	Offset: 0x22082
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function suicidelonestar()
{
	level.mapcenter = maps/mp/gametypes/_spawnlogic::findboxcenter(level.spawnmins, level.spawnmaxs);
	wait(1);
	iprintlnbold("Suicide VTOL Incoming From Sky");
	wait(1.5);
	level thread dosuicidelonestar(self, level.mapcenter);
}

/*
	Name: dosuicidelonestar
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE86E94C8
	Offset: 0x220C2
	Size: 0x1E3
	Parameters: 2
	Flags: None
*/
function dosuicidelonestar(owner, start1)
{
	level endon("game_ended");
	level endon("lsdone");
	start = start1 + (0, 0, 10000);
	end = start1;
	spintoend = VectorToAngles(end - start);
	ls = spawnplane(owner, "script_model", start);
	ls setmodel("veh_t6_air_v78_vtol_killstreak");
	ls.angles = spintoend;
	ls endon("death");
	ls thread nukefireeffect();
	ls thread spinplane();
	time = calc(4000, end, start);
	ls moveto(end, time);
	wait(time - 0.05);
	ls.angles = spintoend;
	earthquake(2, 2, end, 2500);
	wait(0.5);
	level._effect["emp_flash"] = loadfx("weapon/emp/fx_emp_explosion");
	playfx(level._effect["emp_flash"], end + (0, 0, 1000));
	wait(0.5);
	radiusdamage(end + (0, 0, 1000), 1000000, 1000000, 999999, owner);
	foreach(player in level.players)
	{
		player playsoundtoplayer("wpn_c4_activate_plr", player);
		player playsoundtoplayer("evt_helicopter_spin_start", player);
		player playsoundtoplayer("wpn_a10_drop_chaff", player);
		wait(0.5);
		if(isalive(player) && !player ishost())
		{
			player suicide();
		}
	}
	level.lonestar = 0;
	ls delete();
	wait(0.5);
	ls notify("lsdone");
}

/*
	Name: toggleraygunm3all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x37A4E973
	Offset: 0x222A6
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleraygunm3all()
{
	if(self.raygm3on == 0)
	{
		self.raygm3on = 1;
		self thread toggleraygm3all();
		self iprintln("^2Gave All Ray Gun M3");
	}
	else
	{
		self.raygm3on = 0;
		self iprintln("^1Took Everyone Ray Gun M3");
		self thread toggleraygm3all();
	}
}

/*
	Name: toggleraygm3all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1033529C
	Offset: 0x222FA
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleraygm3all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initraygunm3();
		}
	}
}

/*
	Name: doredtheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0x16C25F13
	Offset: 0x22346
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function doredtheme()
{
	self notify("stopflash");
	self.menu.scroller elemcolor(1,  1, 0, 0);
	self.menu.line elemcolor(1,  1, 0, 0);
	self.menu.line2 elemcolor(1,  1, 0, 0);
	self.menu.line3 elemcolor(1,  1, 0, 0);
	self.menu.background1 elemcolor(1,  1, 0, 0);
}

/*
	Name: dobluetheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0x711C84EA
	Offset: 0x223B6
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function dobluetheme()
{
	self notify("stopflash");
	self.menu.scroller elemcolor(1,  0, 0, 1);
	self.menu.line elemcolor(1,  0, 0, 1);
	self.menu.line2 elemcolor(1,  0, 0, 1);
	self.menu.line3 elemcolor(1,  0, 0, 1);
	self.menu.background1 elemcolor(1,  0, 0, 1);
}

/*
	Name: dogreentheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2C04232
	Offset: 0x22426
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function dogreentheme()
{
	self notify("stopflash");
	self.menu.scroller elemcolor(1,  0, 1, 0);
	self.menu.line elemcolor(1,  0, 1, 0);
	self.menu.line2 elemcolor(1,  0, 1, 0);
	self.menu.line3 elemcolor(1,  0, 1, 0);
	self.menu.background1 elemcolor(1,  0, 1, 0);
}

/*
	Name: doyellowtheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7F72A7F3
	Offset: 0x22496
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function doyellowtheme()
{
	self notify("stopflash");
	self.menu.scroller elemcolor(1,  1, 1, 0);
	self.menu.line elemcolor(1,  1, 1, 0);
	self.menu.line2 elemcolor(1,  1, 1, 0);
	self.menu.line3 elemcolor(1,  1, 1, 0);
	self.menu.background1 elemcolor(1,  1, 1, 0);
}

/*
	Name: dopinktheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCAE612B
	Offset: 0x22506
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function dopinktheme()
{
	self notify("stopflash");
	self.menu.scroller elemcolor(1,  1, 0, 1);
	self.menu.line elemcolor(1,  1, 0, 1);
	self.menu.line2 elemcolor(1,  1, 0, 1);
	self.menu.line3 elemcolor(1,  1, 0, 1);
	self.menu.background1 elemcolor(1,  1, 0, 1);
}

/*
	Name: docyantheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0x18AC7C0A
	Offset: 0x22576
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function docyantheme()
{
	self notify("stopflash");
	self.menu.scroller elemcolor(1,  0, 1, 1);
	self.menu.line elemcolor(1,  0, 1, 1);
	self.menu.line2 elemcolor(1,  0, 1, 1);
	self.menu.line3 elemcolor(1,  0, 1, 1);
	self.menu.background1 elemcolor(1,  0, 1, 1);
}

/*
	Name: doaquatheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0x321D4D07
	Offset: 0x225E6
	Size: 0xE3
	Parameters: 0
	Flags: None
*/
function doaquatheme()
{
	self notify("stopflash");
	self.menu.scroller elemcolor(1, (0.04, 0.46, 0.49));
	self.menu.line elemcolor(1, (0.04, 0.46, 0.49));
	self.menu.line2 elemcolor(1, (0.04, 0.46, 0.49));
	self.menu.line3 elemcolor(1, (0.04, 0.46, 0.49));
	self.menu.background1 elemcolor(1, (0.04, 0.46, 0.49));
}

/*
	Name: flashingtheme
	Namespace: _imcsx_gsc_studio
	Checksum: 0x99A8C259
	Offset: 0x226CA
	Size: 0x35F
	Parameters: 0
	Flags: None
*/
function flashingtheme()
{
	self endon("stopflash");
	self.menu.scroller elemcolor(1,  1, 0, 0);
	self.menu.line elemcolor(1,  1, 0, 0);
	self.menu.line2 elemcolor(1,  1, 0, 0);
	self.menu.line3 elemcolor(1,  1, 0, 0);
	self.menu.background1 elemcolor(1,  1, 0, 0);
	wait(5);
	self.menu.scroller elemcolor(1,  0, 0, 1);
	self.menu.line elemcolor(1,  0, 0, 1);
	self.menu.line2 elemcolor(1,  0, 0, 1);
	self.menu.line3 elemcolor(1,  0, 0, 1);
	self.menu.background1 elemcolor(1,  0, 0, 1);
	wait(5);
	self.menu.scroller elemcolor(1,  0, 1, 0);
	self.menu.line elemcolor(1,  0, 1, 0);
	self.menu.line2 elemcolor(1,  0, 1, 0);
	self.menu.line3 elemcolor(1,  0, 1, 0);
	self.menu.background1 elemcolor(1,  0, 1, 0);
	wait(5);
	self.menu.scroller elemcolor(1,  1, 1, 0);
	self.menu.line elemcolor(1,  1, 1, 0);
	self.menu.line2 elemcolor(1,  1, 1, 0);
	self.menu.line3 elemcolor(1,  1, 1, 0);
	self.menu.background1 elemcolor(1,  1, 1, 0);
	wait(5);
	self.menu.scroller elemcolor(1,  1, 0, 1);
	self.menu.line elemcolor(1,  1, 0, 1);
	self.menu.line2 elemcolor(1,  1, 0, 1);
	self.menu.line3 elemcolor(1,  1, 0, 1);
	self.menu.background1 elemcolor(1,  1, 0, 1);
	wait(5);
	self.menu.scroller elemcolor(1,  0, 1, 1);
	self.menu.line elemcolor(1,  0, 1, 1);
	self.menu.line2 elemcolor(1,  0, 1, 1);
	self.menu.line3 elemcolor(1,  0, 1, 1);
	self.menu.background1 elemcolor(1,  0, 1, 1);
	wait(5);
	self.menu.scroller elemcolor(1, (0.04, 0.46, 0.49));
	self.menu.line elemcolor(1, (0.04, 0.46, 0.49));
	self.menu.line2 elemcolor(1, (0.04, 0.46, 0.49));
	self.menu.line3 elemcolor(1, (0.04, 0.46, 0.49));
	self.menu.background1 elemcolor(1, (0.04, 0.46, 0.49));
	wait(5);
	self thread flashingtheme();
}

/*
	Name: elemcolor
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3E08C615
	Offset: 0x22A2A
	Size: 0x1B
	Parameters: 2
	Flags: None
*/
function elemcolor(time, color)
{
	self fadeovertime(time);
	self.color = color;
}

/*
	Name: initflareman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF36696B2
	Offset: 0x22A46
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initflareman1()
{
	if(self.flaremanon1 == 0)
	{
		self.flaremanon1 = 1;
		self setclientthirdperson(1);
		self thread flareman();
		self iprintln("^2Flare Man: ^7[^2On^7]");
	}
	else
	{
		self.flaremanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_FlareManOn1");
		self iprintln("^2Flare Man: ^7[^1Off^7]");
	}
}

/*
	Name: flareman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE0AAE11B
	Offset: 0x22AAA
	Size: 0x29E
	Parameters: 0
	Flags: None
*/
function flareman()
{
	self endon("disconnect");
	self endon("stop_FlareManOn1");
	while(1)
	{
		flares = loadfx("env/smoke/fx_smoke_supply_drop_blue_mp");
		playfx(flares, self gettagorigin("j_head"));
		playfx(flares, self gettagorigin("j_spineupper"));
		playfx(flares, self gettagorigin("j_spinelower"));
		playfx(flares, self gettagorigin("j_spine4"));
		playfx(flares, self gettagorigin("j_spine1"));
		playfx(flares, self gettagorigin("J_Elbow_RI"));
		playfx(flares, self gettagorigin("J_Elbow_LE"));
		playfx(flares, self gettagorigin("j_knee_le"));
		playfx(flares, self gettagorigin("j_knee_ri"));
		playfx(flares, self gettagorigin("J_Ankle_LE"));
		playfx(flares, self gettagorigin("J_Ankle_RI"));
		playfx(flares, self gettagorigin(" J_Wrist_RI"));
		playfx(flares, self gettagorigin(" J_Wrist_LE"));
		playfx(flares, self gettagorigin("j_head"));
		playfx(flares, self gettagorigin("j_spineupper"));
		playfx(flares, self gettagorigin("j_spinelower"));
		playfx(flares, self gettagorigin("j_spine4"));
		playfx(flares, self gettagorigin("j_spine1"));
		playfx(flares, self gettagorigin("J_Elbow_RI"));
		playfx(flares, self gettagorigin("J_Elbow_LE"));
		playfx(flares, self gettagorigin("j_knee_le"));
		playfx(flares, self gettagorigin("j_knee_ri"));
		playfx(flares, self gettagorigin("J_Ankle_LE"));
		playfx(flares, self gettagorigin("J_Ankle_RI"));
		playfx(flares, self gettagorigin(" J_Wrist_RI"));
		playfx(flares, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: riotman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8628C3B4
	Offset: 0x22D4A
	Size: 0x123
	Parameters: 0
	Flags: None
*/
function riotman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "Riot Man ^1OFF", "Riot Man ^2ON"));
	if(self.riot == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self giveweapon("riotshield_mp", 0);
		self switchtoweapon("riotshield_mp");
		self attachshieldmodel("t6_wpn_shield_carry_world_detect", "back_low");
		self giveweapon("riotshield_mp", 0);
		self switchtoweapon("riotshield_mp");
		self attachshieldmodel("t6_wpn_shield_carry_world_detect", "j_head");
		self giveweapon("riotshield_mp", 0);
		self switchtoweapon("riotshield_mp");
		self attachshieldmodel("t6_wpn_shield_carry_world_detect", "tag_weapon_left");
		self.riot = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self takeweapon("riotshield_mp");
		self detachall();
		self.riot = 1;
	}
}

/*
	Name: toggleflaremanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD3298335
	Offset: 0x22E6E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleflaremanall()
{
	if(self.flaremanon == 0)
	{
		self.flaremanon = 1;
		self thread toggleflareman1all();
		self iprintln("^2Gave All Flare Man");
	}
	else
	{
		self.flaremanon = 0;
		self iprintln("^1All Flare Man OFF");
		self thread toggleflareman1all();
	}
}

/*
	Name: toggleflareman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x71C85CF9
	Offset: 0x22EC2
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleflareman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initflareman1();
		}
	}
}

/*
	Name: toggleriotall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA9BCE2A3
	Offset: 0x22F0E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleriotall()
{
	if(self.riotdafuckon == 0)
	{
		self.riotdafuckon = 1;
		self thread toggleriot1all();
		self iprintln("^2Gave All Riot Man");
	}
	else
	{
		self.riotdafuckon = 0;
		self iprintln("^1All Riot Man OFF");
		self thread toggleriot1all();
	}
}

/*
	Name: toggleriot1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3EDDEADE
	Offset: 0x22F62
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleriot1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread riotman();
		}
	}
}

/*
	Name: toggledogall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x50F99380
	Offset: 0x22FAE
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggledogall()
{
	if(self.dogdafuckon == 0)
	{
		self.dogdafuckon = 1;
		self thread toggledog1all();
		self iprintln("^2Gave All Dog Model");
	}
	else
	{
		self.dogdafuckon = 0;
		self iprintln("^1All Dog Model OFF");
		self thread toggledog1all();
	}
}

/*
	Name: toggledog1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x313645ED
	Offset: 0x23002
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggledog1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread setmodeldog();
		}
	}
}

/*
	Name: toggledebugall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8144AE93
	Offset: 0x2304E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggledebugall()
{
	if(self.debug4allon == 0)
	{
		self.debug4allon = 1;
		self thread toggledebug1all();
		self iprintln("^2Gave All Debug Model");
	}
	else
	{
		self.debug4allon = 0;
		self iprintln("^1All Debug Model OFF");
		self thread toggledebug1all();
	}
}

/*
	Name: toggledebug1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x31CCECB4
	Offset: 0x230A2
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggledebug1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread setmodeldefoact();
		}
	}
}

/*
	Name: toggleraygm24all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x379D029D
	Offset: 0x230EE
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleraygm24all()
{
	if(self.raygm2on == 0)
	{
		self.raygm2on = 1;
		self thread toggleraygm21all();
		self iprintln("^2Gave All Ray Gun M2");
	}
	else
	{
		self.raygm2on = 0;
		self iprintln("^1All Ray Gun M2 OFF");
		self thread toggleraygm21all();
	}
}

/*
	Name: toggleraygm21all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBD23AA11
	Offset: 0x23142
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleraygm21all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initraygunm2();
		}
	}
}

/*
	Name: togglerteleall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x947C58CC
	Offset: 0x2318E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglerteleall()
{
	if(self.rteleon == 0)
	{
		self.rteleon = 1;
		self thread togglertele1all();
		self iprintln("^2Gave All Rocket Teleporter");
	}
	else
	{
		self.rteleon = 0;
		self iprintln("^1All Rocket Teleporter OFF");
		self thread togglertele1all();
	}
}

/*
	Name: togglertele1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFB4DC14F
	Offset: 0x231E2
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglertele1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initrocketteleport();
		}
	}
}

/*
	Name: centipede
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3A0E1C40
	Offset: 0x2322E
	Size: 0x42
	Parameters: 0
	Flags: None
*/
function centipede()
{
	self endon("disconnect");
	self endon("death");
	self endon("stop_centipede");
	while(1)
	{
		ent = self cloneplayer(999999);
		wait(0.1);
		ent thread destroymodelontime(2);
	}
}

/*
	Name: destroymodelontime
	Namespace: _imcsx_gsc_studio
	Checksum: 0x27077016
	Offset: 0x23272
	Size: 0x13
	Parameters: 1
	Flags: None
*/
function destroymodelontime(time)
{
	wait(time);
	self delete();
}

/*
	Name: togglecentipede
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE4B1A059
	Offset: 0x23286
	Size: 0x7B
	Parameters: 0
	Flags: None
*/
function togglecentipede()
{
	self.centi = booleanopposite(self.centi);
	self iprintln(booleanreturnval(self.centi, "Human Centipede ^1OFF", "Human Centipede ^2ON"));
	if(self.centipede == 0 || self.centi)
	{
		self thread centipede();
		self.centipede = 1;
		self setclientthirdperson(1);
	}
	else
	{
		self notify("stop_centipede");
		self.centipede = 0;
		self setclientthirdperson(0);
	}
}

/*
	Name: togglecenall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAC0345AA
	Offset: 0x23302
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglecenall()
{
	if(self.centdafuckon == 0)
	{
		self.centdafuckon = 1;
		self thread togglecent1all();
		self iprintln("^2Gave All Flash Man");
	}
	else
	{
		self.centdafuckon = 0;
		self iprintln("^1All Flash Man OFF");
		self thread togglecent1all();
	}
}

/*
	Name: togglecent1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFB7BD019
	Offset: 0x23356
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglecent1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initflashman1();
		}
	}
}

/*
	Name: autonac
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBB865A2C
	Offset: 0x233A2
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function autonac()
{
	if(self.nacon == 0)
	{
		self.nacon = 1;
		self thread nac();
		self iprintln("Auto Nac Swap: ^2On");
	}
	else
	{
		self.nacon = 0;
		self notify("Stop_Nac");
		self iprintln("Auto Nac Swap: ^1Off");
	}
}

/*
	Name: nac
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD3A64919
	Offset: 0x233F2
	Size: 0xC6
	Parameters: 0
	Flags: None
*/
function nac()
{
	self endon("Stop_Nac");
	self endon("death");
	level endon("game_ended");
	for(;;)
	{
		self takeallweapons();
		self giveweapon("proximity_grenade_aoe_mp");
		self giveweapon("flash_grenade_mp");
		self giveweapon("knife_mp", 0, 43);
		self giveweapon("dsr50_mp+steadyaim", 0, 43);
		wait(2.5);
		self takeallweapons();
		self giveweapon("proximity_grenade_aoe_mp");
		self giveweapon("flash_grenade_mp");
		self giveweapon("kard_mp", 0, 44);
		self switchtoweapon("kard_mp");
		wait(1.5);
	}
}

/*
	Name: initdustman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCB562D4
	Offset: 0x234BA
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initdustman1()
{
	if(self.dustmanon1 == 0)
	{
		self.dustmanon1 = 1;
		self setclientthirdperson(1);
		self thread dustman();
		self iprintln("^2Dust Man: ^7[^2On^7]");
	}
	else
	{
		self.dustmanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_DustManOn1");
		self iprintln("^2Dust Man: ^7[^1Off^7]");
	}
}

/*
	Name: dustman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD3676D09
	Offset: 0x2351E
	Size: 0x29E
	Parameters: 0
	Flags: None
*/
function dustman()
{
	self endon("disconnect");
	self endon("stop_DustManOn1");
	while(1)
	{
		dustfxeffect = loadfx("weapon/bouncing_betty/fx_betty_launch_dust");
		playfx(dustfxeffect, self gettagorigin("j_head"));
		playfx(dustfxeffect, self gettagorigin("j_spineupper"));
		playfx(dustfxeffect, self gettagorigin("j_spinelower"));
		playfx(dustfxeffect, self gettagorigin("j_spine4"));
		playfx(dustfxeffect, self gettagorigin("j_spine1"));
		playfx(dustfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(dustfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(dustfxeffect, self gettagorigin("j_knee_le"));
		playfx(dustfxeffect, self gettagorigin("j_knee_ri"));
		playfx(dustfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(dustfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(dustfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(dustfxeffect, self gettagorigin(" J_Wrist_LE"));
		playfx(dustfxeffect, self gettagorigin("j_head"));
		playfx(dustfxeffect, self gettagorigin("j_spineupper"));
		playfx(dustfxeffect, self gettagorigin("j_spinelower"));
		playfx(dustfxeffect, self gettagorigin("j_spine4"));
		playfx(dustfxeffect, self gettagorigin("j_spine1"));
		playfx(dustfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(dustfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(dustfxeffect, self gettagorigin("j_knee_le"));
		playfx(dustfxeffect, self gettagorigin("j_knee_ri"));
		playfx(dustfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(dustfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(dustfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(dustfxeffect, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: initflashman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7A5E36E3
	Offset: 0x237BE
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initflashman1()
{
	if(self.flashmanon1 == 0)
	{
		self.flashmanon1 = 1;
		self setclientthirdperson(1);
		self thread flashman();
		self iprintln("^2Flash Man: ^7[^2On^7]");
	}
	else
	{
		self.flashmanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_FlashManOn1");
		self iprintln("^2Flash Man: ^7[^1Off^7]");
	}
}

/*
	Name: flashman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x554A6C31
	Offset: 0x23822
	Size: 0x29E
	Parameters: 0
	Flags: None
*/
function flashman()
{
	self endon("disconnect");
	self endon("stop_FlashManOn1");
	while(1)
	{
		flashfxeffect = loadfx("weapon/trophy_system/fx_trophy_flash_lng");
		playfx(flashfxeffect, self gettagorigin("j_head"));
		playfx(flashfxeffect, self gettagorigin("j_spineupper"));
		playfx(flashfxeffect, self gettagorigin("j_spinelower"));
		playfx(flashfxeffect, self gettagorigin("j_spine4"));
		playfx(flashfxeffect, self gettagorigin("j_spine1"));
		playfx(flashfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(flashfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(flashfxeffect, self gettagorigin("j_knee_le"));
		playfx(flashfxeffect, self gettagorigin("j_knee_ri"));
		playfx(flashfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(flashfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(flashfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(flashfxeffect, self gettagorigin(" J_Wrist_LE"));
		playfx(flashfxeffect, self gettagorigin("j_head"));
		playfx(flashfxeffect, self gettagorigin("j_spineupper"));
		playfx(flashfxeffect, self gettagorigin("j_spinelower"));
		playfx(flashfxeffect, self gettagorigin("j_spine4"));
		playfx(flashfxeffect, self gettagorigin("j_spine1"));
		playfx(flashfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(flashfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(flashfxeffect, self gettagorigin("j_knee_le"));
		playfx(flashfxeffect, self gettagorigin("j_knee_ri"));
		playfx(flashfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(flashfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(flashfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(flashfxeffect, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: initexplman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6523F184
	Offset: 0x23AC2
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initexplman1()
{
	if(self.explmanon1 == 0)
	{
		self.explmanon1 = 1;
		self setclientthirdperson(1);
		self thread explman();
		self iprintln("^2Explosion Man: ^7[^2On^7]");
	}
	else
	{
		self.explmanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_ExplManOn1");
		self iprintln("^2Explosion Man: ^7[^1Off^7]");
	}
}

/*
	Name: explman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4280F6AF
	Offset: 0x23B26
	Size: 0x29E
	Parameters: 0
	Flags: None
*/
function explman()
{
	self endon("disconnect");
	self endon("stop_ExplManOn1");
	while(1)
	{
		explfxeffect = loadfx("weapon/trophy_system/fx_trophy_radius_detonation");
		playfx(explfxeffect, self gettagorigin("j_head"));
		playfx(explfxeffect, self gettagorigin("j_spineupper"));
		playfx(explfxeffect, self gettagorigin("j_spinelower"));
		playfx(explfxeffect, self gettagorigin("j_spine4"));
		playfx(explfxeffect, self gettagorigin("j_spine1"));
		playfx(explfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(explfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(explfxeffect, self gettagorigin("j_knee_le"));
		playfx(explfxeffect, self gettagorigin("j_knee_ri"));
		playfx(explfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(explfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(explfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(explfxeffect, self gettagorigin(" J_Wrist_LE"));
		playfx(explfxeffect, self gettagorigin("j_head"));
		playfx(explfxeffect, self gettagorigin("j_spineupper"));
		playfx(explfxeffect, self gettagorigin("j_spinelower"));
		playfx(explfxeffect, self gettagorigin("j_spine4"));
		playfx(explfxeffect, self gettagorigin("j_spine1"));
		playfx(explfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(explfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(explfxeffect, self gettagorigin("j_knee_le"));
		playfx(explfxeffect, self gettagorigin("j_knee_ri"));
		playfx(explfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(explfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(explfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(explfxeffect, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: initsmokeman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC1DB72F1
	Offset: 0x23DC6
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initsmokeman1()
{
	if(self.smokemanon1 == 0)
	{
		self.smokemanon1 = 1;
		self setclientthirdperson(1);
		self thread smokeman();
		self iprintln("^2Smoke Man: ^7[^2On^7]");
	}
	else
	{
		self.smokemanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_SmokeManOn1");
		self iprintln("^2Smoke Man: ^7[^1Off^7]");
	}
}

/*
	Name: smokeman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4DD77CC
	Offset: 0x23E2A
	Size: 0x29E
	Parameters: 0
	Flags: None
*/
function smokeman()
{
	self endon("disconnect");
	self endon("stop_SmokeManOn1");
	while(1)
	{
		smokefxeffect = loadfx("weapon/trophy_system/fx_trophy_deploy_impact");
		playfx(smokefxeffect, self gettagorigin("j_head"));
		playfx(smokefxeffect, self gettagorigin("j_spineupper"));
		playfx(smokefxeffect, self gettagorigin("j_spinelower"));
		playfx(smokefxeffect, self gettagorigin("j_spine4"));
		playfx(smokefxeffect, self gettagorigin("j_spine1"));
		playfx(smokefxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(smokefxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(smokefxeffect, self gettagorigin("j_knee_le"));
		playfx(smokefxeffect, self gettagorigin("j_knee_ri"));
		playfx(smokefxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(smokefxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(smokefxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(smokefxeffect, self gettagorigin(" J_Wrist_LE"));
		playfx(smokefxeffect, self gettagorigin("j_head"));
		playfx(smokefxeffect, self gettagorigin("j_spineupper"));
		playfx(smokefxeffect, self gettagorigin("j_spinelower"));
		playfx(smokefxeffect, self gettagorigin("j_spine4"));
		playfx(smokefxeffect, self gettagorigin("j_spine1"));
		playfx(smokefxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(smokefxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(smokefxeffect, self gettagorigin("j_knee_le"));
		playfx(smokefxeffect, self gettagorigin("j_knee_ri"));
		playfx(smokefxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(smokefxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(smokefxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(smokefxeffect, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: initballthing
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB3D4F957
	Offset: 0x240CA
	Size: 0x77
	Parameters: 0
	Flags: None
*/
function initballthing()
{
	self.blueballs = booleanopposite(self.blueballs);
	self iprintln(booleanreturnval(self.blueballs, "Rotor Head ^1OFF", "Rotor Head ^2ON"));
	if(self.ff == 0 || self.blueballs)
	{
		self thread ballthing();
		self.ff = 1;
	}
	else if(self.ff == 1)
	{
		self.ff = 0;
		self notify("forceend");
		self detachall();
	}
}

/*
	Name: ballthing
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA4AA4EE6
	Offset: 0x24142
	Size: 0x86
	Parameters: 0
	Flags: None
*/
function ballthing()
{
	self endon("disconnect");
	self endon("death");
	self endon("forceend");
	ball = spawn("script_model", self.origin + (0, 0, 20));
	ball setmodel("vehicle_mi24p_hind_desert_d_piece02");
	ball.angles = (0, 115, 0);
	self thread monball(ball);
	self thread monplyr();
	self thread dod(ball);
	for(;;)
	{
		ball rotateyaw(-360, 2);
		wait(1);
	}
}

/*
	Name: monball
	Namespace: _imcsx_gsc_studio
	Checksum: 0x46E6BA61
	Offset: 0x241CA
	Size: 0x32
	Parameters: 1
	Flags: None
*/
function monball(obj)
{
	self endon("death");
	self endon("forceend");
	while(1)
	{
		obj.origin = self.origin + (0, 0, 120);
		wait(0.05);
	}
}

/*
	Name: monplyr
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAB22D761
	Offset: 0x241FE
	Size: 0xC2
	Parameters: 0
	Flags: None
*/
function monplyr()
{
	self endon("death");
	self endon("forceend");
	while(1)
	{
		foreach(p in level.players)
		{
			if(distance(self.origin, p.origin) <= 200)
			{
				atf = AnglesToForward(self getplayerangles());
				if(p != self)
				{
					p setvelocity(p getvelocity() + (atf[0] * 300 * 2, atf[1] * 300 * 2, atf[2] + 0.25 * 300 * 2));
				}
			}
		}
		wait(0.05);
	}
}

/*
	Name: dod
	Namespace: _imcsx_gsc_studio
	Checksum: 0x43AB9BBD
	Offset: 0x242C2
	Size: 0x17
	Parameters: 1
	Flags: None
*/
function dod(ent)
{
	self waittill("forceend");
	ent delete();
}

/*
	Name: toggleearthquakegirl
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAF7F0109
	Offset: 0x242DA
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function toggleearthquakegirl()
{
	if(self.earthquakegirl == 0)
	{
		self.earthquakegirl = 1;
		self thread earthquakegirl();
		self iprintln("Rotate Actor: [^2ON^7]");
	}
	else
	{
		self.earthquakegirl = 0;
		level.ipro delete();
		self notify("EarthquakeGirl");
		self iprintln("Rotate Actor: [^1OFF^7]");
	}
}

/*
	Name: earthquakegirl
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD782F93
	Offset: 0x24336
	Size: 0xFA
	Parameters: 0
	Flags: None
*/
function earthquakegirl()
{
	self endon("disconnect");
	self endon("EarthquakeGirl");
	level.ipro = spawn("script_model", self.origin + (0, 0, 40));
	level.ipro setmodel("defaultactor");
	level.effect["1"] = loadfx("impacts/fx_flesh_hit_head_coward");
	while(1)
	{
		playfx(level.effect["1"], level.ipro.origin);
		wait(0.1);
		level.ipro moveto(level.ipro.origin + (0, 0, 40), 1);
		level.ipro rotateyaw(2480, 2);
		if(distance(self.origin, self.origin) < 155)
		{
			self playsound("chr_spl_generic_gib_american");
		}
		wait(2);
		level.ipro moveto(level.ipro.origin - (0, 0, 40), 0.1);
		wait(0.2);
	}
}

/*
	Name: flagman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD2A767EE
	Offset: 0x24432
	Size: 0x1A3
	Parameters: 0
	Flags: None
*/
function flagman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "Red Flags Man ^1OFF", "Red Flags Man ^2ON"));
	if(self.flagred == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("mp_flag_red", "back_low");
		self attachshieldmodel("mp_flag_red", "j_head");
		self attachshieldmodel("mp_flag_red", "tag_weapon_left");
		self attachshieldmodel("mp_flag_red", "J_Elbow_RI");
		self attachshieldmodel("mp_flag_red", "J_Elbow_LE");
		self attachshieldmodel("mp_flag_red", "j_knee_le");
		self attachshieldmodel("mp_flag_red", "j_knee_ri");
		self attachshieldmodel("mp_flag_red", "J_Ankle_LE");
		self attachshieldmodel("mp_flag_red", "J_Ankle_RI");
		self attachshieldmodel("mp_flag_red", "J_Wrist_RI");
		self attachshieldmodel("mp_flag_red", "J_Wrist_LE");
		self attachshieldmodel("mp_flag_red", "j_spine4");
		self attachshieldmodel("mp_flag_red", "j_spine1");
		self attachshieldmodel("mp_flag_red", "j_spineupper");
		self attachshieldmodel("mp_flag_red", "j_spinelower");
		self.flagred = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.flagred = 1;
	}
}

/*
	Name: flagman2
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDEC2FFE7
	Offset: 0x245D6
	Size: 0x1A3
	Parameters: 0
	Flags: None
*/
function flagman2()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "Green Flags Man ^1OFF", "Green Flags Man ^2ON"));
	if(self.flaggreen == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("mp_flag_green", "back_low");
		self attachshieldmodel("mp_flag_green", "j_head");
		self attachshieldmodel("mp_flag_green", "tag_weapon_left");
		self attachshieldmodel("mp_flag_green", "J_Elbow_RI");
		self attachshieldmodel("mp_flag_green", "J_Elbow_LE");
		self attachshieldmodel("mp_flag_green", "j_knee_le");
		self attachshieldmodel("mp_flag_green", "j_knee_ri");
		self attachshieldmodel("mp_flag_green", "J_Ankle_LE");
		self attachshieldmodel("mp_flag_green", "J_Ankle_RI");
		self attachshieldmodel("mp_flag_green", "J_Wrist_RI");
		self attachshieldmodel("mp_flag_green", "J_Wrist_LE");
		self attachshieldmodel("mp_flag_green", "j_spine4");
		self attachshieldmodel("mp_flag_green", "j_spine1");
		self attachshieldmodel("mp_flag_green", "j_spineupper");
		self attachshieldmodel("mp_flag_green", "j_spinelower");
		self.flaggreen = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.flaggreen = 1;
	}
}

/*
	Name: silverman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x90EC6F39
	Offset: 0x2477A
	Size: 0x1A3
	Parameters: 0
	Flags: None
*/
function silverman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "Silver Man ^1OFF", "Silver Man ^2ON"));
	if(self.silver == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("projectile_hellfire_missile", "back_low");
		self attachshieldmodel("projectile_hellfire_missile", "j_head");
		self attachshieldmodel("projectile_hellfire_missile", "tag_weapon_left");
		self attachshieldmodel("projectile_hellfire_missile", "J_Elbow_RI");
		self attachshieldmodel("projectile_hellfire_missile", "J_Elbow_LE");
		self attachshieldmodel("projectile_hellfire_missile", "j_knee_le");
		self attachshieldmodel("projectile_hellfire_missile", "j_knee_ri");
		self attachshieldmodel("projectile_hellfire_missile", "J_Ankle_LE");
		self attachshieldmodel("projectile_hellfire_missile", "J_Ankle_RI");
		self attachshieldmodel("projectile_hellfire_missile", "J_Wrist_RI");
		self attachshieldmodel("projectile_hellfire_missile", "J_Wrist_LE");
		self attachshieldmodel("projectile_hellfire_missile", "j_spine4");
		self attachshieldmodel("projectile_hellfire_missile", "j_spine1");
		self attachshieldmodel("projectile_hellfire_missile", "j_spineupper");
		self attachshieldmodel("projectile_hellfire_missile", "j_spinelower");
		self.silver = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.silver = 1;
	}
}

/*
	Name: typewritter
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF04BBBB6
	Offset: 0x2491E
	Size: 0x3E
	Parameters: 1
	Flags: None
*/
function typewritter(messagelel)
{
	foreach(player in level.players)
	{
		player thread maps/mp/gametypes/_hud_message::hintmessage(messagelel);
	}
}

/*
	Name: flippingdebug
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4DB34217
	Offset: 0x2495E
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function flippingdebug()
{
	self endon("disconnect");
	self endon("cratesoff");
	spindebug = spawn("script_model", self.origin + (60, 0, 87));
	level.entities[level.amountofentities] = spindebug;
	level.amountofentities++;
	spindebug setmodel("defaultactor");
	spindebug setcontents(1);
	self iprintln("Flipping Actor ^2Spawned");
	for(;;)
	{
		spindebug rotateroll(-180, 1);
		wait(1);
	}
}

/*
	Name: rollingdebug
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC51C6F41
	Offset: 0x249DE
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function rollingdebug()
{
	self endon("disconnect");
	self endon("cratesoff");
	spindebug2 = spawn("script_model", self.origin + (60, 0, 87));
	level.entities[level.amountofentities] = spindebug2;
	level.amountofentities++;
	spindebug2 setmodel("defaultactor");
	spindebug2 setcontents(1);
	self iprintln("Rolling Actor ^2Spawned");
	for(;;)
	{
		spindebug2 rotatepitch(-180, 1);
		wait(1);
	}
}

/*
	Name: deadclone
	Namespace: _imcsx_gsc_studio
	Checksum: 0x351F92E8
	Offset: 0x24A5E
	Size: 0x33
	Parameters: 0
	Flags: None
*/
function deadclone()
{
	self iprintln("^5Dead Clone ^2Spawned");
	ffdc = self cloneplayer(9999);
	ffdc startragdoll(1);
}

/*
	Name: rocketzman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD57D396F
	Offset: 0x24A92
	Size: 0x1A3
	Parameters: 0
	Flags: None
*/
function rocketzman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Rockets Man ^1OFF", "^5Rockets Man ^2ON"));
	if(self.sidwinder == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("projectile_sidewinder_missile", "back_low");
		self attachshieldmodel("projectile_sidewinder_missile", "j_head");
		self attachshieldmodel("projectile_sidewinder_missile", "tag_weapon_left");
		self attachshieldmodel("projectile_sidewinder_missile", "J_Elbow_RI");
		self attachshieldmodel("projectile_sidewinder_missile", "J_Elbow_LE");
		self attachshieldmodel("projectile_sidewinder_missile", "j_knee_le");
		self attachshieldmodel("projectile_sidewinder_missile", "j_knee_ri");
		self attachshieldmodel("projectile_sidewinder_missile", "J_Ankle_LE");
		self attachshieldmodel("projectile_sidewinder_missile", "J_Ankle_RI");
		self attachshieldmodel("projectile_sidewinder_missile", "J_Wrist_RI");
		self attachshieldmodel("projectile_sidewinder_missile", "J_Wrist_LE");
		self attachshieldmodel("projectile_sidewinder_missile", "j_spine4");
		self attachshieldmodel("projectile_sidewinder_missile", "j_spine1");
		self attachshieldmodel("projectile_sidewinder_missile", "j_spineupper");
		self attachshieldmodel("projectile_sidewinder_missile", "j_spinelower");
		self.sidwinder = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.sidwinder = 1;
	}
}

/*
	Name: initbloodman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8BE81A64
	Offset: 0x24C36
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initbloodman1()
{
	if(self.bloodmanon1 == 0)
	{
		self.bloodmanon1 = 1;
		self setclientthirdperson(1);
		self thread bloodman();
		self iprintln("^5Blood Man: ^7[^2On^7]");
	}
	else
	{
		self.bloodmanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_BloodManOn1");
		self iprintln("^5Blood Man: ^7[^1Off^7]");
	}
}

/*
	Name: bloodman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x51C070BC
	Offset: 0x24C9A
	Size: 0x29E
	Parameters: 0
	Flags: None
*/
function bloodman()
{
	self endon("disconnect");
	self endon("stop_BloodManOn1");
	while(1)
	{
		bloodfxeffect = loadfx("impacts/fx_flesh_hit_head_coward");
		playfx(bloodfxeffect, self gettagorigin("j_head"));
		playfx(bloodfxeffect, self gettagorigin("j_spineupper"));
		playfx(bloodfxeffect, self gettagorigin("j_spinelower"));
		playfx(bloodfxeffect, self gettagorigin("j_spine4"));
		playfx(bloodfxeffect, self gettagorigin("j_spine1"));
		playfx(bloodfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(bloodfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(bloodfxeffect, self gettagorigin("j_knee_le"));
		playfx(bloodfxeffect, self gettagorigin("j_knee_ri"));
		playfx(bloodfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(bloodfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(bloodfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(bloodfxeffect, self gettagorigin(" J_Wrist_LE"));
		playfx(bloodfxeffect, self gettagorigin("j_head"));
		playfx(bloodfxeffect, self gettagorigin("j_spineupper"));
		playfx(bloodfxeffect, self gettagorigin("j_spinelower"));
		playfx(bloodfxeffect, self gettagorigin("j_spine4"));
		playfx(bloodfxeffect, self gettagorigin("j_spine1"));
		playfx(bloodfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(bloodfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(bloodfxeffect, self gettagorigin("j_knee_le"));
		playfx(bloodfxeffect, self gettagorigin("j_knee_ri"));
		playfx(bloodfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(bloodfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(bloodfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(bloodfxeffect, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: donoclip
	Namespace: _imcsx_gsc_studio
	Checksum: 0x933964AD
	Offset: 0x24F3A
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function donoclip()
{
	if(self.noclipon == 0)
	{
		self.noclipon = 1;
		self.ufomode = 0;
		self unlink();
		self iprintlnbold("^3Advanced Fly Mode: ^2On");
		self iprintln("[{+smoke}] ^5Hold To Fly");
		self iprintln("[{+gostand}] ^3Hold To Move Faster");
		self iprintln("[{+stance}] ^6To Cancel Fly Mode");
		self thread noclip();
		self thread returnnoc();
	}
	else
	{
		self.noclipon = 0;
		self notify("stop_Noclip");
		self unlink();
		self.originobj delete();
		self iprintlnbold("^3Advanced Fly Mode: ^1Off");
	}
}

/*
	Name: noclip
	Namespace: _imcsx_gsc_studio
	Checksum: 0x645F9788
	Offset: 0x24FEE
	Size: 0x13A
	Parameters: 0
	Flags: None
*/
function noclip()
{
	self endon("disconnect");
	self endon("stop_Noclip");
	self.flynoclip = 0;
	while(self.flynoclip == 0 && self secondaryoffhandbuttonpressed())
	{
		self.originobj = spawn("script_origin", self.origin, 1);
		self.originobj.angles = self.angles;
		self playerlinkto(self.originobj, undefined);
		self.flynoclip = 1;
		if(self secondaryoffhandbuttonpressed() && self.flynoclip == 1)
		{
			normalized = AnglesToForward(self getplayerangles());
			scaled = VectorScale(normalized, 46);
			originpos = self.origin + scaled;
			self.originobj.origin = originpos;
		}
		if(self jumpbuttonpressed() && self.flynoclip == 1)
		{
			normalized = AnglesToForward(self getplayerangles());
			scaled = VectorScale(normalized, 330);
			originpos = self.origin + scaled;
			self.originobj.origin = originpos;
		}
		if(self stancebuttonpressed() && self.flynoclip == 1)
		{
			self unlink();
			self.originobj delete();
			self.flynoclip = 0;
		}
		wait(0.001);
	}
}

/*
	Name: returnnoc
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE217709B
	Offset: 0x2512A
	Size: 0x1C
	Parameters: 0
	Flags: None
*/
function returnnoc()
{
	self endon("disconnect");
	self endon("stop_Noclip");
	for(;;)
	{
		self waittill("death");
		self.flynoclip = 0;
	}
}

/*
	Name: initbloodbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFA54D64C
	Offset: 0x25148
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function initbloodbullet()
{
	if(self.bloodbulleton == 0)
	{
		self.bloodbulleton = 1;
		self thread dobloodbullet();
		self iprintln("^3Blood Bullets: ^2On");
	}
	else
	{
		self.bloodbulleton = 0;
		self notify("stop_BloodBullet");
		self iprintln("^3Blood Bullets: ^1Off");
	}
}

/*
	Name: dobloodbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x81874CCE
	Offset: 0x25196
	Size: 0xE3
	Parameters: 0
	Flags: None
*/
function dobloodbullet()
{
	self endon("death");
	self endon("stop_BloodBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["impacts/fx_deathfx_dogbite"] = loadfx("impacts/fx_deathfx_dogbite");
		level._effect["animscript_laststand_suicide"] = loadfx("impacts/fx_flesh_hit_head_coward");
		playfx(level._effect["impacts/fx_deathfx_dogbite"], splosionlocation);
		playfx(level._effect["animscript_laststand_suicide"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: arrowsman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1EEB14D4
	Offset: 0x2527A
	Size: 0x18F
	Parameters: 0
	Flags: None
*/
function arrowsman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Arrows Man ^1OFF", "^5Arrows Man ^2ON"));
	if(self.axisarrowman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("fx_axis_createfx", "back_low");
		self attachshieldmodel("fx_axis_createfx", "j_head");
		self attachshieldmodel("fx_axis_createfx", "J_Elbow_RI");
		self attachshieldmodel("fx_axis_createfx", "J_Elbow_LE");
		self attachshieldmodel("fx_axis_createfx", "j_knee_le");
		self attachshieldmodel("fx_axis_createfx", "j_knee_ri");
		self attachshieldmodel("fx_axis_createfx", "J_Ankle_LE");
		self attachshieldmodel("fx_axis_createfx", "J_Ankle_RI");
		self attachshieldmodel("fx_axis_createfx", "J_Wrist_RI");
		self attachshieldmodel("fx_axis_createfx", "J_Wrist_LE");
		self attachshieldmodel("fx_axis_createfx", "j_spine4");
		self attachshieldmodel("fx_axis_createfx", "j_spine1");
		self attachshieldmodel("fx_axis_createfx", "j_spineupper");
		self attachshieldmodel("fx_axis_createfx", "j_spinelower");
		self.axisarrowman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.axisarrowman = 1;
	}
}

/*
	Name: clusterman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF147AEB6
	Offset: 0x2540A
	Size: 0x18F
	Parameters: 0
	Flags: None
*/
function clusterman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Cluster Bomb Man ^1OFF", "^5Cluster Bomb Man ^2ON"));
	if(self.clusterman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("projectile_cbu97_clusterbomb", "back_low");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "j_head");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "J_Elbow_RI");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "J_Elbow_LE");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "j_knee_le");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "j_knee_ri");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "J_Ankle_LE");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "J_Ankle_RI");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "J_Wrist_RI");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "J_Wrist_LE");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "j_spine4");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "j_spine1");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "j_spineupper");
		self attachshieldmodel("projectile_cbu97_clusterbomb", "j_spinelower");
		self.clusterman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.clusterman = 1;
	}
}

/*
	Name: goldman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x787E0C81
	Offset: 0x2559A
	Size: 0x18F
	Parameters: 0
	Flags: None
*/
function goldman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Gold Man ^1OFF", "^5Gold Man ^2ON"));
	if(self.goldm == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("p6_dogtags", "back_low");
		self attachshieldmodel("p6_dogtags", "j_head");
		self attachshieldmodel("p6_dogtags", "J_Elbow_RI");
		self attachshieldmodel("p6_dogtags", "J_Elbow_LE");
		self attachshieldmodel("p6_dogtags", "j_knee_le");
		self attachshieldmodel("p6_dogtags", "j_knee_ri");
		self attachshieldmodel("p6_dogtags", "J_Ankle_LE");
		self attachshieldmodel("p6_dogtags", "J_Ankle_RI");
		self attachshieldmodel("p6_dogtags", "J_Wrist_RI");
		self attachshieldmodel("p6_dogtags", "J_Wrist_LE");
		self attachshieldmodel("p6_dogtags", "j_spine4");
		self attachshieldmodel("p6_dogtags", "j_spine1");
		self attachshieldmodel("p6_dogtags", "j_spineupper");
		self attachshieldmodel("p6_dogtags", "j_spinelower");
		self.goldm = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.goldm = 1;
	}
}

/*
	Name: cmksskyz
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9F7E82BA
	Offset: 0x2572A
	Size: 0x4C
	Parameters: 0
	Flags: None
*/
function cmksskyz()
{
	if(self.cmksskyz == 0)
	{
		self iprintln("^5Light Up The Sky ^7[^2ON^7]");
		self.cmksskyz = 1;
		self thread cmkssky();
	}
	else
	{
		self iprintln("^5Light Up The Sky ^7[^1OFF^7]");
		self.cmksskyz = 0;
		self notify("stoprain");
	}
}

/*
	Name: cmkssky
	Namespace: _imcsx_gsc_studio
	Checksum: 0x21040BFE
	Offset: 0x25778
	Size: 0x34
	Parameters: 0
	Flags: None
*/
function cmkssky()
{
	self endon("death");
	self endon("stoprain");
	self endon("disconnect");
	iprintlnbold("^5Look At The Sky");
	for(;;)
	{
		self thread docmksskyscript();
		wait(0.0001);
	}
}

/*
	Name: docmksskyscript
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD1F7612F
	Offset: 0x257AE
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function docmksskyscript()
{
	lr = maps/mp/gametypes/_spawnlogic::findboxcenter(level.spawnmins, level.spawnmaxs);
	z = randomintrange(1000, 2000);
	x = randomintrange(-1500, 1500);
	y = randomintrange(-1500, 1500);
	l = lr + (x, y, z);
	bombs = spawn("script_model", l);
	bombs setmodel("");
	bombs.angles = bombs.angles + (90, 90, 90);
	wait(0.0001);
	bombs thread cmksskyscript();
	bombs delete();
}

/*
	Name: cmksskyscript
	Namespace: _imcsx_gsc_studio
	Checksum: 0x640F94DC
	Offset: 0x2586A
	Size: 0x2A
	Parameters: 0
	Flags: None
*/
function cmksskyscript()
{
	self endon("donemissile");
	for(;;)
	{
		playfx(level._effect["ChafFx"], self.origin);
		wait(0.0001);
	}
}

/*
	Name: firework
	Namespace: _imcsx_gsc_studio
	Checksum: 0x78A701D6
	Offset: 0x25896
	Size: 0x19B
	Parameters: 0
	Flags: None
*/
function firework()
{
	firework = spawn("script_model", self.origin + (0, 0, 53));
	firework setmodel("projectile_sidewinder_missile");
	firework.angles = (-90, 90, 90);
	self iprintlnbold("^5Shoot To Launch Firework");
	self waittill("weapon_fired");
	self playsound("wpn_rpg_whizby");
	firework moveto(firework.origin + (0, 0, 20000), 15);
	playfxontag(level.chopper_fx["damage"]["light_smoke"], firework, "tag_origin");
	iprintlnbold("^3Firework Inbound");
	wait(10);
	self playsound("wpn_emp_bomb");
	level._effect["emp_flash"] = loadfx("weapon/emp/fx_emp_explosion");
	playfx(level._effect["emp_flash"], firework.origin);
	playfx(level.remote_mortar_fx["missileExplode"], firework.origin);
	self playsound("wpn_emp_bomb");
	playfx(level.remote_mortar_fx["missileExplode"], firework.origin);
	self playsound("wpn_emp_bomb");
	wait(0.8);
	self playsound("wpn_emp_bomb");
	wait(0.8);
	self playsound("wpn_emp_bomb");
	wait(0.8);
	self playsound("wpn_emp_bomb");
	wait(0.8);
	self playsound("wpn_emp_bomb");
	firework delete();
}

/*
	Name: initfireman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAE2BA12F
	Offset: 0x25A32
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initfireman()
{
	if(self.firemanon == 0)
	{
		self.firemanon = 1;
		self setclientthirdperson(1);
		self thread dodafireman();
		self iprintln("^5Fire Man: ^2On");
	}
	else
	{
		self.firemanon = 0;
		self setclientthirdperson(0);
		self notify("stop_daFireMan");
		self iprintln("^5Fire Man: ^1Off");
	}
}

/*
	Name: dodafireman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9C488AE
	Offset: 0x25A96
	Size: 0x1D2
	Parameters: 0
	Flags: None
*/
function dodafireman()
{
	self endon("disconnect");
	self endon("stop_daFireMan");
	level._effect["DaFireFx"] = loadfx("weapon/talon/fx_muz_talon_rocket_flash_1p");
	while(1)
	{
		playfx(level._effect["DaFireFx"], self gettagorigin("j_head"));
		playfx(level._effect["DaFireFx"], self gettagorigin("j_spineupper"));
		playfx(level._effect["DaFireFx"], self gettagorigin("j_spinelower"));
		playfx(level._effect["DaFireFx"], self gettagorigin("j_spine4"));
		playfx(level._effect["DaFireFx"], self gettagorigin("j_spine1"));
		playfx(level._effect["DaFireFx"], self gettagorigin("J_Elbow_RI"));
		playfx(level._effect["DaFireFx"], self gettagorigin("J_Elbow_LE"));
		playfx(level._effect["DaFireFx"], self gettagorigin("j_knee_le"));
		playfx(level._effect["DaFireFx"], self gettagorigin("j_knee_ri"));
		playfx(level._effect["DaFireFx"], self gettagorigin("J_Ankle_LE"));
		playfx(level._effect["DaFireFx"], self gettagorigin("J_Ankle_RI"));
		playfx(level._effect["DaFireFx"], self gettagorigin(" J_Wrist_RI"));
		playfx(level._effect["DaFireFx"], self gettagorigin(" J_Wrist_LE"));
		wait(0.9);
	}
}

/*
	Name: initwaterman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x95F95660
	Offset: 0x25C6A
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initwaterman()
{
	if(self.watermanon == 0)
	{
		self.watermanon = 1;
		self setclientthirdperson(1);
		self thread dodawaterman();
		self iprintln("^5Water Man: ^2On");
	}
	else
	{
		self.watermanon = 0;
		self setclientthirdperson(0);
		self notify("stop_daWaterMan");
		self iprintln("^5Water Man: ^1Off");
	}
}

/*
	Name: dodawaterman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x21AEFFC9
	Offset: 0x25CCE
	Size: 0x1D2
	Parameters: 0
	Flags: None
*/
function dodawaterman()
{
	self endon("disconnect");
	self endon("stop_daWaterMan");
	level._effect["CmKsLelWater"] = loadfx("system_elements/fx_snow_sm_em");
	while(1)
	{
		playfx(level._effect["CmKsLelWater"], self gettagorigin("j_head"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("j_spineupper"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("j_spinelower"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("j_spine4"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("j_spine1"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("J_Elbow_RI"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("J_Elbow_LE"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("j_knee_le"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("j_knee_ri"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("J_Ankle_LE"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin("J_Ankle_RI"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin(" J_Wrist_RI"));
		playfx(level._effect["CmKsLelWater"], self gettagorigin(" J_Wrist_LE"));
		wait(0.9);
	}
}

/*
	Name: initchafman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7DE1A2CE
	Offset: 0x25EA2
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initchafman()
{
	if(self.chafmanon == 0)
	{
		self.chafmanon = 1;
		self setclientthirdperson(1);
		self thread dodachafman();
		self iprintln("^5Light Man: ^2On");
	}
	else
	{
		self.chafmanon = 0;
		self setclientthirdperson(0);
		self notify("stop_daChafMan");
		self iprintln("^5Light Man: ^1Off");
	}
}

/*
	Name: dodachafman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x421C75F0
	Offset: 0x25F06
	Size: 0x1D2
	Parameters: 0
	Flags: None
*/
function dodachafman()
{
	self endon("disconnect");
	self endon("stop_daChafMan");
	level._effect["ChafFx"] = loadfx("weapon/straferun/fx_straferun_chaf");
	while(1)
	{
		playfx(level._effect["ChafFx"], self gettagorigin("j_head"));
		playfx(level._effect["ChafFx"], self gettagorigin("j_spineupper"));
		playfx(level._effect["ChafFx"], self gettagorigin("j_spinelower"));
		playfx(level._effect["ChafFx"], self gettagorigin("j_spine4"));
		playfx(level._effect["ChafFx"], self gettagorigin("j_spine1"));
		playfx(level._effect["ChafFx"], self gettagorigin("J_Elbow_RI"));
		playfx(level._effect["ChafFx"], self gettagorigin("J_Elbow_LE"));
		playfx(level._effect["ChafFx"], self gettagorigin("j_knee_le"));
		playfx(level._effect["ChafFx"], self gettagorigin("j_knee_ri"));
		playfx(level._effect["ChafFx"], self gettagorigin("J_Ankle_LE"));
		playfx(level._effect["ChafFx"], self gettagorigin("J_Ankle_RI"));
		playfx(level._effect["ChafFx"], self gettagorigin(" J_Wrist_RI"));
		playfx(level._effect["ChafFx"], self gettagorigin(" J_Wrist_LE"));
		wait(0.9);
	}
}

/*
	Name: initreddotbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCEB189F
	Offset: 0x260DA
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initreddotbullet()
{
	if(self.reddotbulleton == 0)
	{
		self.reddotbulleton = 1;
		self thread doreddotbullet();
		self iprintln("^3Red Dot Bullets: ^2On");
	}
	else
	{
		self.reddotbulleton = 0;
		self notify("stop_RedDotBullet");
		self iprintln("^3Red Dot Bullets: ^1Off");
	}
}

/*
	Name: doreddotbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x97BCD83F
	Offset: 0x2612A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doreddotbullet()
{
	self endon("death");
	self endon("stop_RedDotBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level.remote_mortar_fx["laserTarget"] = loadfx("weapon/remote_mortar/fx_rmt_mortar_laser_loop");
		playfx(level.remote_mortar_fx["laserTarget"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initwarrowsbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x42304050
	Offset: 0x261E6
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initwarrowsbullet()
{
	if(self.whitearrowson == 0)
	{
		self.whitearrowson = 1;
		self thread dowhitearrows();
		self iprintln("^3White Arrows Bullets: ^2On");
	}
	else
	{
		self.whitearrowson = 0;
		self notify("stop_WhiteArrows");
		self iprintln("^3White Arrows Bullets: ^1Off");
	}
}

/*
	Name: dowhitearrows
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9DA953C5
	Offset: 0x26236
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dowhitearrows()
{
	self endon("death");
	self endon("stop_WhiteArrows");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["koth"] = loadfx("maps/mp_maps/fx_mp_koth_marker_neutral_1");
		playfx(level._effect["koth"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: robotman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2AA181A6
	Offset: 0x262F2
	Size: 0x18F
	Parameters: 0
	Flags: None
*/
function robotman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Robot Man ^1OFF", "^5Robot Man ^2ON"));
	if(self.robotman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "back_low");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_head");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "J_Elbow_RI");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "J_Elbow_LE");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_knee_le");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_knee_ri");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "J_Ankle_LE");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "J_Ankle_RI");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "J_Wrist_RI");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "J_Wrist_LE");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_spine4");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_spine1");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_spineupper");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_spinelower");
		self.robotman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.robotman = 1;
	}
}

/*
	Name: inityellowbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEE6E6A9B
	Offset: 0x26482
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function inityellowbullet()
{
	if(self.yellowbulleton == 0)
	{
		self.yellowbulleton = 1;
		self thread doyellowbullet();
		self iprintln("^3Yellow Light Bullets: ^2On");
	}
	else
	{
		self.yellowbulleton = 0;
		self notify("stop_YellowBullet");
		self iprintln("^3Yellow Light Bullets: ^1Off");
	}
}

/*
	Name: doyellowbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x29C963B2
	Offset: 0x264D2
	Size: 0xE3
	Parameters: 0
	Flags: None
*/
function doyellowbullet()
{
	self endon("death");
	self endon("stop_YellowBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["tacticalInsertionYellow"] = loadfx("misc/fx_equip_tac_insert_light_grn");
		level._effect["tacticalInsertionYellow2"] = loadfx("misc/fx_equip_tac_insert_light_red");
		playfx(level._effect["tacticalInsertionYellow"], splosionlocation);
		playfx(level._effect["tacticalInsertionYellow2"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: togglerocketmanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB769ED66
	Offset: 0x265B6
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglerocketmanall()
{
	if(self.rocketmanallon == 0)
	{
		self.rocketmanallon = 1;
		self thread togglerocketman1all();
		self iprintln("^2Gave All Rockets Man");
	}
	else
	{
		self.rocketmanallon = 0;
		self iprintln("^1All Rockets Man OFF");
		self thread togglerocketman1all();
	}
}

/*
	Name: togglerocketman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDC8645B6
	Offset: 0x2660A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglerocketman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread rocketzman();
		}
	}
}

/*
	Name: togglechromeall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6A4F4A05
	Offset: 0x26656
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglechromeall()
{
	if(self.chromeallon == 0)
	{
		self.chromeallon = 1;
		self thread togglechrome1all();
		self iprintln("^2Gave All Chrome Man");
	}
	else
	{
		self.chromeallon = 0;
		self iprintln("^1All Chrome Man OFF");
		self thread togglechrome1all();
	}
}

/*
	Name: togglechrome1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xABBFD942
	Offset: 0x266AA
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglechrome1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread silverman();
		}
	}
}

/*
	Name: togglegoldall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6EB9B269
	Offset: 0x266F6
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglegoldall()
{
	if(self.goldallon == 0)
	{
		self.goldallon = 1;
		self thread togglegoldman1all();
		self iprintln("^2Gave All Gold Tags Man");
	}
	else
	{
		self.goldallon = 0;
		self iprintln("^1All Gold Tags Man OFF");
		self thread togglegoldman1all();
	}
}

/*
	Name: togglegoldman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF5A10F73
	Offset: 0x2674A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglegoldman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread goldman();
		}
	}
}

/*
	Name: togglewaterall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD513F741
	Offset: 0x26796
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglewaterall()
{
	if(self.waterallon == 0)
	{
		self.waterallon = 1;
		self thread togglewaterman1all();
		self iprintln("^2Gave All Rave Man");
	}
	else
	{
		self.waterallon = 0;
		self iprintln("^1All Rave Man OFF");
		self thread togglewaterman1all();
	}
}

/*
	Name: togglewaterman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEF741BBB
	Offset: 0x267EA
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglewaterman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initraveman();
		}
	}
}

/*
	Name: togglebloodall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x29261B20
	Offset: 0x26836
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglebloodall()
{
	if(self.bloodallon == 0)
	{
		self.bloodallon = 1;
		self thread togglebloodman1all();
		self iprintln("^2Gave All Blood Man");
	}
	else
	{
		self.bloodallon = 0;
		self iprintln("^1All Blood Man OFF");
		self thread togglebloodman1all();
	}
}

/*
	Name: togglebloodman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8C7152F9
	Offset: 0x2688A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglebloodman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initbloodman1();
		}
	}
}

/*
	Name: togglearrowsall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD61AB322
	Offset: 0x268D6
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglearrowsall()
{
	if(self.arrowsallon == 0)
	{
		self.arrowsallon = 1;
		self thread togglearrowsman1all();
		self iprintln("^2Gave All Arrows Man");
	}
	else
	{
		self.arrowsallon = 0;
		self iprintln("^1All Arrows Man OFF");
		self thread togglearrowsman1all();
	}
}

/*
	Name: togglearrowsman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB56E89BF
	Offset: 0x2692A
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglearrowsman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread arrowsman();
		}
	}
}

/*
	Name: initwaterstormman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF508DBAD
	Offset: 0x26976
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initwaterstormman1()
{
	if(self.waterstormmanon1 == 0)
	{
		self.waterstormmanon1 = 1;
		self thread waterstormman();
		self iprintln("^5Water Waves Man: ^7[^2On^7]");
	}
	else
	{
		self.waterstormmanon1 = 0;
		self notify("stop_WaterStormManOn1");
		self iprintln("^5Water Waves Man: ^7[^1Off^7]");
	}
}

/*
	Name: waterstormman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x552BE96B
	Offset: 0x269C6
	Size: 0x166
	Parameters: 0
	Flags: None
*/
function waterstormman()
{
	self endon("disconnect");
	self endon("stop_WaterStormManOn1");
	while(1)
	{
		waterwavesfx = loadfx("vehicle/treadfx/fx_heli_water_spray");
		playfx(waterwavesfx, self gettagorigin("j_head"));
		playfx(waterwavesfx, self gettagorigin("j_spineupper"));
		playfx(waterwavesfx, self gettagorigin("j_spinelower"));
		playfx(waterwavesfx, self gettagorigin("j_spine4"));
		playfx(waterwavesfx, self gettagorigin("j_spine1"));
		playfx(waterwavesfx, self gettagorigin("J_Elbow_RI"));
		playfx(waterwavesfx, self gettagorigin("J_Elbow_LE"));
		playfx(waterwavesfx, self gettagorigin("j_knee_le"));
		playfx(waterwavesfx, self gettagorigin("j_knee_ri"));
		playfx(waterwavesfx, self gettagorigin("J_Ankle_LE"));
		playfx(waterwavesfx, self gettagorigin("J_Ankle_RI"));
		playfx(waterwavesfx, self gettagorigin(" J_Wrist_RI"));
		playfx(waterwavesfx, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: initsnowman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8E029ECF
	Offset: 0x26B2E
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initsnowman1()
{
	if(self.snowmanon1 == 0)
	{
		self.snowmanon1 = 1;
		self thread snowman();
		self iprintln("^5Snow Storm Man: ^7[^2On^7]");
	}
	else
	{
		self.snowmanon1 = 0;
		self notify("stop_SnowManOn1");
		self iprintln("^5Snow Storm Man: ^7[^1Off^7]");
	}
}

/*
	Name: snowman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAF7F72E2
	Offset: 0x26B7E
	Size: 0x166
	Parameters: 0
	Flags: None
*/
function snowman()
{
	self endon("disconnect");
	self endon("stop_SnowManOn1");
	while(1)
	{
		snowfxeffect = loadfx("vehicle/treadfx/fx_heli_snow_spray");
		playfx(snowfxeffect, self gettagorigin("j_head"));
		playfx(snowfxeffect, self gettagorigin("j_spineupper"));
		playfx(snowfxeffect, self gettagorigin("j_spinelower"));
		playfx(snowfxeffect, self gettagorigin("j_spine4"));
		playfx(snowfxeffect, self gettagorigin("j_spine1"));
		playfx(snowfxeffect, self gettagorigin("J_Elbow_RI"));
		playfx(snowfxeffect, self gettagorigin("J_Elbow_LE"));
		playfx(snowfxeffect, self gettagorigin("j_knee_le"));
		playfx(snowfxeffect, self gettagorigin("j_knee_ri"));
		playfx(snowfxeffect, self gettagorigin("J_Ankle_LE"));
		playfx(snowfxeffect, self gettagorigin("J_Ankle_RI"));
		playfx(snowfxeffect, self gettagorigin(" J_Wrist_RI"));
		playfx(snowfxeffect, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: initsparkman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5E6F5E20
	Offset: 0x26CE6
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initsparkman1()
{
	if(self.sparkmanon1 == 0)
	{
		self.sparkmanon1 = 1;
		self setclientthirdperson(1);
		self thread dosparkman();
		self iprintln("^5Spark Man: ^7[^2On^7]");
	}
	else
	{
		self.sparkmanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_SparkManOn1");
		self iprintln("^5Spark Man: ^7[^1Off^7]");
	}
}

/*
	Name: dosparkman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x956A9F3E
	Offset: 0x26D4A
	Size: 0x166
	Parameters: 0
	Flags: None
*/
function dosparkman()
{
	self endon("disconnect");
	self endon("stop_SparkManOn1");
	while(1)
	{
		sparkfx = loadfx("weapon/qr_drone/fx_qr_drone_impact_sparks");
		playfx(sparkfx, self gettagorigin("j_head"));
		playfx(sparkfx, self gettagorigin("j_spineupper"));
		playfx(sparkfx, self gettagorigin("j_spinelower"));
		playfx(sparkfx, self gettagorigin("j_spine4"));
		playfx(sparkfx, self gettagorigin("j_spine1"));
		playfx(sparkfx, self gettagorigin("J_Elbow_RI"));
		playfx(sparkfx, self gettagorigin("J_Elbow_LE"));
		playfx(sparkfx, self gettagorigin("j_knee_le"));
		playfx(sparkfx, self gettagorigin("j_knee_ri"));
		playfx(sparkfx, self gettagorigin("J_Ankle_LE"));
		playfx(sparkfx, self gettagorigin("J_Ankle_RI"));
		playfx(sparkfx, self gettagorigin(" J_Wrist_RI"));
		playfx(sparkfx, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: initelectricv2bullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x66BAEA7
	Offset: 0x26EB2
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initelectricv2bullet()
{
	if(self.electricv2bulleton == 0)
	{
		self.electricv2bulleton = 1;
		self thread doelectricv2bullet();
		self iprintln("^5Electric Bullets: ^2On");
	}
	else
	{
		self.electricv2bulleton = 0;
		self notify("stop_ElectricV2Bullet");
		self iprintln("^5Electric Bullets: ^1Off");
	}
}

/*
	Name: doelectricv2bullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDC19707
	Offset: 0x26F02
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doelectricv2bullet()
{
	self endon("death");
	self endon("stop_ElectricV2Bullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["ai_tank_stun_fx"] = loadfx("weapon/talon/fx_talon_emp_stun");
		playfx(level._effect["ai_tank_stun_fx"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: toggleclustermanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x216CFCD
	Offset: 0x26FBE
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleclustermanall()
{
	if(self.clustermanallon == 0)
	{
		self.clustermanallon = 1;
		self thread toggleclusterman1all();
		self iprintln("^2Gave All Cluster Man");
	}
	else
	{
		self.clustermanallon = 0;
		self iprintln("^1All Cluster Man OFF");
		self thread toggleclusterman1all();
	}
}

/*
	Name: toggleclusterman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x47B9238
	Offset: 0x27012
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleclusterman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread clusterman();
		}
	}
}

/*
	Name: toggleredflagsall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x122C7F1A
	Offset: 0x2705E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleredflagsall()
{
	if(self.redflagsallon == 0)
	{
		self.redflagsallon = 1;
		self thread toggleredflags1all();
		self iprintln("^2Gave All Red Flags Man");
	}
	else
	{
		self.redflagsallon = 0;
		self iprintln("^1All Red Flags Man OFF");
		self thread toggleredflags1all();
	}
}

/*
	Name: toggleredflags1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB171A0C4
	Offset: 0x270B2
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleredflags1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread flagman();
		}
	}
}

/*
	Name: togglegreenflagsall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDC98CC02
	Offset: 0x270FE
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglegreenflagsall()
{
	if(self.greenflagallon == 0)
	{
		self.greenflagallon = 1;
		self thread togglegreenflag1all();
		self iprintln("^2Gave All Green Flags Man");
	}
	else
	{
		self.greenflagallon = 0;
		self iprintln("^1All Green Flags Man OFF");
		self thread togglegreenflag1all();
	}
}

/*
	Name: togglegreenflag1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6E9344DD
	Offset: 0x27152
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglegreenflag1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread flagman2();
		}
	}
}

/*
	Name: togglerobotmanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEF9535F7
	Offset: 0x2719E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglerobotmanall()
{
	if(self.robotmanallon == 0)
	{
		self.robotmanallon = 1;
		self thread togglerobotman1all();
		self iprintln("^2Gave All Robot Man");
	}
	else
	{
		self.robotmanallon = 0;
		self iprintln("^1All Robot Man OFF");
		self thread togglerobotman1all();
	}
}

/*
	Name: togglerobotman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7B550A1
	Offset: 0x271F2
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglerobotman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread robotman();
		}
	}
}

/*
	Name: togglesmokemanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFB35DA65
	Offset: 0x2723E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglesmokemanall()
{
	if(self.smokemanallon == 0)
	{
		self.smokemanallon = 1;
		self thread togglesmokeman1all();
		self iprintln("^2Gave All Smoke Man");
	}
	else
	{
		self.smokemanallon = 0;
		self iprintln("^1All Smoke Man OFF");
		self thread togglesmokeman1all();
	}
}

/*
	Name: togglesmokeman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE158E51E
	Offset: 0x27292
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglesmokeman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initsmokeman1();
		}
	}
}

/*
	Name: togglesuitcasemanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1CD512CD
	Offset: 0x272DE
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglesuitcasemanall()
{
	if(self.suitcasemanallon == 0)
	{
		self.suitcasemanallon = 1;
		self thread togglesuitcaseman1all();
		self iprintln("^2Gave All Lasers Man");
	}
	else
	{
		self.suitcasemanallon = 0;
		self iprintln("^1All Lasers Man OFF");
		self thread togglesuitcaseman1all();
	}
}

/*
	Name: togglesuitcaseman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAB5F9377
	Offset: 0x27332
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglesuitcaseman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread akimbolasersman();
		}
	}
}

/*
	Name: togglewaterwavesall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEAB2AB23
	Offset: 0x2737E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglewaterwavesall()
{
	if(self.waterwavesallon == 0)
	{
		self.waterwavesallon = 1;
		self thread togglewaterwaves1all();
		self iprintln("^2Gave All Water Waves Man");
	}
	else
	{
		self.waterwavesallon = 0;
		self iprintln("^1All Water Waves Man OFF");
		self thread togglewaterwaves1all();
	}
}

/*
	Name: togglewaterwaves1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x37F1B173
	Offset: 0x273D2
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglewaterwaves1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initwaterstormman1();
		}
	}
}

/*
	Name: togglesnowstormall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x725ECC39
	Offset: 0x2741E
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglesnowstormall()
{
	if(self.snowstormallon == 0)
	{
		self.snowstormallon = 1;
		self thread togglesnowstorm1all();
		self iprintln("^2Gave All Snow Storm Man");
	}
	else
	{
		self.snowstormallon = 0;
		self iprintln("^1All Snow Storm Man OFF");
		self thread togglesnowstorm1all();
	}
}

/*
	Name: togglesnowstorm1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE3205175
	Offset: 0x27472
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglesnowstorm1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initsnowman1();
		}
	}
}

/*
	Name: initchaffv2bullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE0D13922
	Offset: 0x274BE
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initchaffv2bullet()
{
	if(self.chaffv2bulleton == 0)
	{
		self.chaffv2bulleton = 1;
		self thread dochaffv2bullet();
		self iprintln("^5Flash #2 Bullets: ^2On");
	}
	else
	{
		self.chaffv2bulleton = 0;
		self notify("stop_ChaffV2Bullet");
		self iprintln("^5Flash #2 Bullets: ^1Off");
	}
}

/*
	Name: dochaffv2bullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBF4368AA
	Offset: 0x2750E
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dochaffv2bullet()
{
	self endon("death");
	self endon("stop_ChaffV2Bullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["chaff2smoke"] = loadfx("vehicle/vexplosion/fx_heli_chaff");
		playfx(level._effect["chaff2smoke"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: akimbolasersman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9A1AB3C0
	Offset: 0x275CA
	Size: 0x10B
	Parameters: 0
	Flags: None
*/
function akimbolasersman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Lasers Man ^1OFF", "^5Lasers Man ^2ON"));
	if(self.lasersman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self takeallweapons();
		self giveweapon("knife_ballistic_mp", 0, 44);
		self givemaxammo("knife_ballistic_mp");
		self attach("fx_axis_createfx", "j_head");
		playfxontag(level.waypointgreen, self, "tag_weapon_left");
		playfxontag(level.waypointred, self, "j_head");
		playfxontag(level.waypointgreen, self, "j_head");
		playfxontag(level.waypointred, self, "tag_weapon_right");
		self.lasersman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.lasersman = 1;
	}
}

/*
	Name: togglewallhack
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA9A92998
	Offset: 0x276D6
	Size: 0x5D
	Parameters: 0
	Flags: None
*/
function togglewallhack()
{
	if(!self.togglewallhack)
	{
		self thread enableesp();
		self maps/mp/killstreaks/_spyplane::callsatellite("radardirection_mp");
		self iprintlnbold("^5ESP Wallhack : ^7[^2Enabled^7]");
		self.togglewallhack = 1;
	}
	else
	{
		self thread disableesp();
		self iprintlnbold("^5ESP Wallhack : ^7[^1Disabled^7]");
		self.togglewallhack = 0;
	}
}

/*
	Name: enableesp
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9712FBE9
	Offset: 0x27734
	Size: 0xD
	Parameters: 0
	Flags: None
*/
function enableesp()
{
	self thread gettargets();
}

/*
	Name: disableesp
	Namespace: _imcsx_gsc_studio
	Checksum: 0x64A26165
	Offset: 0x27742
	Size: 0x3E
	Parameters: 0
	Flags: None
*/
function disableesp()
{
	self notify("esp_end");
	for(i = 0; i < self.esp.targets.size; i++)
	{
		self.esp.targets[i].hudbox destroy();
	}
}

/*
	Name: gettargets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x294950D1
	Offset: 0x27782
	Size: 0xD8
	Parameters: 0
	Flags: None
*/
function gettargets()
{
	self endon("esp_end");
	for(;;)
	{
		self.esp = spawnstruct();
		self.esp.targets = [];
		a = 0;
		for(i = 0; i < level.players.size; i++)
		{
			if(self != level.players[i])
			{
				self.esp.targets[a] = spawnstruct();
				self.esp.targets[a].player = level.players[i];
				self.esp.targets[a].hudbox = self createbox(self.esp.targets[a].player.origin, 1);
				self thread monitortarget(self.esp.targets[a]);
				a++;
			}
		}
		level waittill("connected", player);
		self notify("esp_target_update");
	}
}

/*
	Name: monitortarget
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE6338962
	Offset: 0x2785C
	Size: 0x24C
	Parameters: 1
	Flags: None
*/
function monitortarget(target)
{
	self endon("esp_target_update");
	self endon("esp_end");
	for(;;)
	{
		target.hudbox destroy();
		h_pos = target.player.origin;
		t_pos = target.player.origin;
		if(bullettracepassed(self gettagorigin("j_spine4"), target.player gettagorigin("j_spine4"), 0, self))
		{
			if(distance(self.origin, target.player.origin) <= 1800)
			{
				if(level.teambased && target.player.pers["team"] != self.pers["team"])
				{
					target.hudbox = self createbox(h_pos, 900);
					target.hudbox.color =  0, 1, 0;
				}
				if(!level.teambased)
				{
					target.hudbox = self createbox(h_pos, 900);
					target.hudbox.color =  0, 1, 0;
				}
			}
			else
			{
				target.hudbox = self createbox(t_pos, 900);
			}
		}
		else
		{
			target.hudbox = self createbox(t_pos, 100);
		}
		if(!isalive(target.player))
		{
			target.hudbox destroy();
			if(level.teambased && target.player.pers["team"] != self.pers["team"])
			{
				target.hudbox = self createbox(t_pos, 900);
				target.hudbox setshader(level.deads, 6, 6);
			}
			else if(!level.teambased)
			{
				target.hudbox = self createbox(t_pos, 900);
				target.hudbox setshader(level.deads, 6, 6);
			}
		}
		if(self.pers["team"] == target.player.pers["team"] && level.teambased)
		{
			target.hudbox destroy();
			if(distance(target.player.origin, self.origin) < 3)
			{
				target.hudbox = self createbox(t_pos, 900);
			}
		}
		wait(0.01);
	}
}

/*
	Name: createbox
	Namespace: _imcsx_gsc_studio
	Checksum: 0x763B40D
	Offset: 0x27AAA
	Size: 0x8A
	Parameters: 2
	Flags: None
*/
function createbox(pos, type)
{
	shader = newclienthudelem(self);
	shader.sort = 0;
	shader.archived = 0;
	shader.x = pos[0];
	shader.y = pos[1];
	shader.z = pos[2] + 30;
	shader setshader(level.esps, 6, 6);
	shader setwaypoint(1, 1);
	shader.alpha = 0.8;
	shader.color =  1, 0, 0;
	return shader;
}

/*
	Name: doaxisarrowsbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD6735432
	Offset: 0x27B36
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function doaxisarrowsbullets()
{
	if(self.axisarrowsbulletz2 == 0)
	{
		self thread axisarrowsbullets();
		self.axisarrowsbulletz2 = 1;
		self iprintln("^5Axis Arrows Bullets ^7[^2ON^7]");
	}
	else
	{
		self notify("stop_axisbulletz2");
		self.axisarrowsbulletz2 = 0;
		self iprintln("^5Axis Arrows Bullets ^7[^1OFF^7]");
	}
}

/*
	Name: axisarrowsbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x38E7A054
	Offset: 0x27B86
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function axisarrowsbullets()
{
	self endon("stop_axisbulletz2");
	while(1)
	{
		self waittill("weapon_fired");
		forward = self gettagorigin("j_head");
		end = self thread vector_scal(AnglesToForward(self getplayerangles()), 1000000);
		splosionlocation = bullettrace(forward, end, 0, self)["position"];
		m = spawn("script_model", splosionlocation);
		m setmodel("fx_axis_createfx");
	}
}

/*
	Name: doredcpsbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x74A7440D
	Offset: 0x27C06
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function doredcpsbullets()
{
	if(self.redcpbulletz2 == 0)
	{
		self thread redcpbullets();
		self.redcpbulletz2 = 1;
		self iprintln("^5Red CarePackage Bullets ^7[^2ON^7]");
	}
	else
	{
		self notify("stop_RedCPBullets");
		self.redcpbulletz2 = 0;
		self iprintln("^5Red CarePackage Bullets ^7[^1OFF^7]");
	}
}

/*
	Name: redcpbullets
	Namespace: _imcsx_gsc_studio
	Checksum: 0x79CD553B
	Offset: 0x27C56
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function redcpbullets()
{
	self endon("stop_RedCPBullets");
	while(1)
	{
		self waittill("weapon_fired");
		forward = self gettagorigin("j_head");
		end = self thread vector_scal(AnglesToForward(self getplayerangles()), 1000000);
		splosionlocation = bullettrace(forward, end, 0, self)["position"];
		m = spawn("script_model", splosionlocation);
		m setmodel("t6_wpn_supply_drop_detect");
	}
}

/*
	Name: initflashv3bullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x96A8887F
	Offset: 0x27CD6
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initflashv3bullet()
{
	if(self.flashv3bulleton == 0)
	{
		self.flashv3bulleton = 1;
		self thread doflashv3bullet();
		self iprintln("^5Flash #3 Bullets: ^2On");
	}
	else
	{
		self.flashv3bulleton = 0;
		self notify("stop_FlashV3Bullet");
		self iprintln("^5Flash #3 Bullets: ^1Off");
	}
}

/*
	Name: doflashv3bullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9A14A51A
	Offset: 0x27D26
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doflashv3bullet()
{
	self endon("death");
	self endon("stop_FlashV3Bullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["fx_trophy_flash_lng"] = loadfx("weapon/trophy_system/fx_trophy_flash_lng");
		playfx(level._effect["fx_trophy_flash_lng"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: inittorchbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5F6A8BF2
	Offset: 0x27DE2
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function inittorchbullet()
{
	if(self.torchbulleton == 0)
	{
		self.torchbulleton = 1;
		self thread dotorchbullet();
		self iprintln("^5Torch Bullets: ^2On");
	}
	else
	{
		self.torchbulleton = 0;
		self notify("stop_TorchBullet");
		self iprintln("^5Torch Bullets: ^1Off");
	}
}

/*
	Name: dotorchbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6EFCFA07
	Offset: 0x27E32
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dotorchbullet()
{
	self endon("death");
	self endon("stop_TorchBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["torch"] = loadfx("maps/mp_maps/fx_mp_exp_rc_bomb");
		playfx(level._effect["torch"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: longkillcam
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC15A1D7A
	Offset: 0x27EEE
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function longkillcam()
{
	if(self.killcam == 1)
	{
		self iprintln("15 Sec. KillCam ^2ON");
		setdvar("scr_killcam_time", 15);
		self.killcam = 0;
	}
	else
	{
		self iprintln("15 Sec. KillCam ^1OFF");
		setdvar("scr_killcam_time", 5);
		self.killcam = 1;
	}
}

/*
	Name: dobignames
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF58555C3
	Offset: 0x27F4A
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function dobignames()
{
	if(self.bg == 1)
	{
		self iprintln("Big Names ^2ON");
		setdvar("cg_overheadnamessize", "2.0");
		self.bg = 0;
	}
	else
	{
		self iprintln("Big Names ^1OFF");
		setdvar("cg_overheadnamessize", "0.65");
		self.bg = 1;
	}
}

/*
	Name: togglefiremanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x410F22EE
	Offset: 0x27FA6
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglefiremanall()
{
	if(self.firemanallon == 0)
	{
		self.firemanallon = 1;
		self thread togglefireman1all();
		self iprintln("^2Gave All Fire Man");
	}
	else
	{
		self.firemanallon = 0;
		self iprintln("^1All Fire Man OFF");
		self thread togglefireman1all();
	}
}

/*
	Name: togglefireman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x43AE5604
	Offset: 0x27FFA
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglefireman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initfireman();
		}
	}
}

/*
	Name: initglassman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD00B27E2
	Offset: 0x28046
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initglassman1()
{
	if(self.glassmanon1 == 0)
	{
		self.glassmanon1 = 1;
		self setclientthirdperson(1);
		self thread doglassman();
		self iprintln("^5Glass Man: ^7[^2On^7]");
	}
	else
	{
		self.glassmanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_GlassManOn1");
		self iprintln("^5Glass Man: ^7[^1Off^7]");
	}
}

/*
	Name: doglassman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFC41D77
	Offset: 0x280AA
	Size: 0x166
	Parameters: 0
	Flags: None
*/
function doglassman()
{
	self endon("disconnect");
	self endon("stop_GlassManOn1");
	while(1)
	{
		breakglassmanfx = loadfx("impacts/fx_large_glass");
		playfx(breakglassmanfx, self gettagorigin("j_head"));
		playfx(breakglassmanfx, self gettagorigin("j_spineupper"));
		playfx(breakglassmanfx, self gettagorigin("j_spinelower"));
		playfx(breakglassmanfx, self gettagorigin("j_spine4"));
		playfx(breakglassmanfx, self gettagorigin("j_spine1"));
		playfx(breakglassmanfx, self gettagorigin("J_Elbow_RI"));
		playfx(breakglassmanfx, self gettagorigin("J_Elbow_LE"));
		playfx(breakglassmanfx, self gettagorigin("j_knee_le"));
		playfx(breakglassmanfx, self gettagorigin("j_knee_ri"));
		playfx(breakglassmanfx, self gettagorigin("J_Ankle_LE"));
		playfx(breakglassmanfx, self gettagorigin("J_Ankle_RI"));
		playfx(breakglassmanfx, self gettagorigin(" J_Wrist_RI"));
		playfx(breakglassmanfx, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: initleafman1
	Namespace: _imcsx_gsc_studio
	Checksum: 0x154C9BB9
	Offset: 0x28212
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initleafman1()
{
	if(self.leafmanon1 == 0)
	{
		self.leafmanon1 = 1;
		self setclientthirdperson(1);
		self thread doleafman();
		self iprintln("^5Leaf Man: ^7[^2On^7]");
	}
	else
	{
		self.leafmanon1 = 0;
		self setclientthirdperson(0);
		self notify("stop_LeafManOn1");
		self iprintln("^5Leaf Man: ^7[^1Off^7]");
	}
}

/*
	Name: doleafman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4F283C71
	Offset: 0x28276
	Size: 0x166
	Parameters: 0
	Flags: None
*/
function doleafman()
{
	self endon("disconnect");
	self endon("stop_LeafManOn1");
	while(1)
	{
		leafmanfx = loadfx("impacts/fx_small_foliage");
		playfx(leafmanfx, self gettagorigin("j_head"));
		playfx(leafmanfx, self gettagorigin("j_spineupper"));
		playfx(leafmanfx, self gettagorigin("j_spinelower"));
		playfx(leafmanfx, self gettagorigin("j_spine4"));
		playfx(leafmanfx, self gettagorigin("j_spine1"));
		playfx(leafmanfx, self gettagorigin("J_Elbow_RI"));
		playfx(leafmanfx, self gettagorigin("J_Elbow_LE"));
		playfx(leafmanfx, self gettagorigin("j_knee_le"));
		playfx(leafmanfx, self gettagorigin("j_knee_ri"));
		playfx(leafmanfx, self gettagorigin("J_Ankle_LE"));
		playfx(leafmanfx, self gettagorigin("J_Ankle_RI"));
		playfx(leafmanfx, self gettagorigin(" J_Wrist_RI"));
		playfx(leafmanfx, self gettagorigin(" J_Wrist_LE"));
		wait(0.5);
	}
}

/*
	Name: redtagsman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE79F0CFA
	Offset: 0x283DE
	Size: 0x18F
	Parameters: 0
	Flags: None
*/
function redtagsman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Red Tags Man ^1OFF", "^5Red Tags Man ^2ON"));
	if(self.reddogtagsman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("p6_dogtags_friend", "back_low");
		self attachshieldmodel("p6_dogtags_friend", "j_head");
		self attachshieldmodel("p6_dogtags_friend", "J_Elbow_RI");
		self attachshieldmodel("p6_dogtags_friend", "J_Elbow_LE");
		self attachshieldmodel("p6_dogtags_friend", "j_knee_le");
		self attachshieldmodel("p6_dogtags_friend", "j_knee_ri");
		self attachshieldmodel("p6_dogtags_friend", "J_Ankle_LE");
		self attachshieldmodel("p6_dogtags_friend", "J_Ankle_RI");
		self attachshieldmodel("p6_dogtags_friend", "J_Wrist_RI");
		self attachshieldmodel("p6_dogtags_friend", "J_Wrist_LE");
		self attachshieldmodel("p6_dogtags_friend", "j_spine4");
		self attachshieldmodel("p6_dogtags_friend", "j_spine1");
		self attachshieldmodel("p6_dogtags_friend", "j_spineupper");
		self attachshieldmodel("p6_dogtags_friend", "j_spinelower");
		self.reddogtagsman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.reddogtagsman = 1;
	}
}

/*
	Name: starinthesky
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBC72AE15
	Offset: 0x2856E
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function starinthesky()
{
	if(level.starinthesky == 1)
	{
		level.starinthesky = 0;
		level thread dotext4s();
		wp("275,480,300,480,675,480,700,480,300,510,325,510,650,510,675,510,700,510,300,540,325,540,350,540,375,540,625,540,650,540,675,540,300,570,325,570,350,570,375,570,400,570,575,570,600,570,625,570,650,570,675,570,325,600,350,600,375,600,400,600,425,600,550,600,575,600,600,600,625,600,650,600,675,600,325,630,350,630,375,630,400,630,425,630,450,630,475,630,525,630,550,630,575,630,600,630,625,630,650,630,325,660,350,660,375,660,400,660,425,660,450,660,475,660,500,660,525,660,550,660,575,660,600,660,625,660,650,660,325,690,350,690,375,690,400,690,425,690,450,690,475,690,500,690,525,690,550,690,575,690,600,690,625,690,650,690,350,720,375,720,400,720,425,720,450,720,475,720,500,720,525,720,550,720,575,720,600,720,625,720,350,750,375,750,400,750,425,750,450,750,475,750,500,750,525,750,550,750,575,750,600,750,625,750,350,780,375,780,400,780,425,780,450,780,475,780,500,780,525,780,550,780,575,780,600,780,625,780,300,810,325,810,350,810,375,810,400,810,425,810,450,810,475,810,500,810,525,810,550,810,575,810,600,810,625,810,650,810,675,810,275,840,300,840,325,840,350,840,375,840,400,840,425,840,450,840,475,840,500,840,525,840,550,840,575,840,600,840,625,840,650,840,675,840,700,840,250,870,275,870,300,870,325,870,350,870,375,870,400,870,425,870,450,870,475,870,500,870,525,870,550,870,575,870,600,870,625,870,650,870,675,870,700,870,725,870,750,870,200,900,225,900,250,900,275,900,300,900,325,900,350,900,375,900,400,900,425,900,450,900,475,900,500,900,525,900,550,900,575,900,600,900,625,900,650,900,675,900,700,900,725,900,750,900,775,900,150,930,175,930,200,930,225,930,250,930,275,930,300,930,325,930,350,930,375,930,400,930,425,930,450,930,475,930,500,930,525,930,550,930,575,930,600,930,625,930,650,930,675,930,700,930,725,930,750,930,775,930,800,930,825,930,400,960,425,960,450,960,475,960,500,960,525,960,550,960,575,960,425,990,450,990,475,990,500,990,525,990,550,990,575,990,425,1020,450,1020,475,1020,500,1020,525,1020,550,1020,425,1050,450,1050,475,1050,500,1050,525,1050,550,1050,450,1080,475,1080,500,1080,525,1080,550,1080,450,1110,475,1110,500,1110,525,1110,450,1140,475,1140,500,1140,525,1140,475,1170,500,1170,525,1170,475,1200,500,1200,475,1230,500,1230", 2000, 0);
	}
	else
	{
		self iprintln("^1Star is Already in The Sky");
	}
}

/*
	Name: dotext4s
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA3454761
	Offset: 0x285AE
	Size: 0x23
	Parameters: 0
	Flags: None
*/
function dotext4s()
{
	iprintlnbold("^5Look At The Sky");
	wait(2.5);
	iprintlnbold("^3Star in The Sky");
}

/*
	Name: telealltocrosshair
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8059AAD8
	Offset: 0x285D2
	Size: 0x96
	Parameters: 0
	Flags: None
*/
function telealltocrosshair()
{
	self iprintln("Teleported All To Crosshair");
	foreach(player in level.players)
	{
		if(!player ishost())
		{
			player setorigin(bullettrace(self gettagorigin("j_head"), self gettagorigin("j_head") + AnglesToForward(self getplayerangles()) * 1000000, 0, self)["position"]);
		}
	}
}

/*
	Name: toggleglassmanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8BA87556
	Offset: 0x2866A
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function toggleglassmanall()
{
	if(self.glassmanallon == 0)
	{
		self.glassmanallon = 1;
		self thread toggleglassman1all();
		self iprintln("^2Gave All Glass Man");
	}
	else
	{
		self.glassmanallon = 0;
		self iprintln("^1All Glass Man OFF");
		self thread toggleglassman1all();
	}
}

/*
	Name: toggleglassman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6C278DE8
	Offset: 0x286BE
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleglassman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initglassman1();
		}
	}
}

/*
	Name: sayisold
	Namespace: _imcsx_gsc_studio
	Checksum: 0x96CE85C9
	Offset: 0x2870A
	Size: 0x4A
	Parameters: 1
	Flags: None
*/
function sayisold(player)
{
	foreach(player_inlevel in level.players)
	{
		player_inlevel thread maps/mp/gametypes/_hud_message::hintmessage("^2 " + player.name + " Smokes Weed");
	}
}

/*
	Name: redcpwave
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC8DA3FAF
	Offset: 0x28756
	Size: 0x8A
	Parameters: 0
	Flags: None
*/
function redcpwave()
{
	if(isdefined(level.redcpwave))
	{
		array_delete(level.redcpwave);
		level.redcpwave = undefined;
		return;
	}
	self iprintln("Red CP Wave: [^2ON^7]");
	level.redcpwave = spawnmultiplemodels(self.origin + (0, 180, 0), 1, 10, 1, 0, -25, 0, "t6_wpn_supply_drop_detect", (0, 180, 0));
	for(m = 0; m < level.redcpwave.size; m++)
	{
		level.redcpwave[m] thread redcpwavemove();
		wait(0.1);
	}
}

/*
	Name: redcpwavemove
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC0986DBA
	Offset: 0x287E2
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function redcpwavemove()
{
	while(isdefined(self))
	{
		self movez(80, 1, 0.2, 0.4);
		wait(1);
		self movez(-80, 1, 0.2, 0.4);
		wait(1);
	}
}

/*
	Name: spawnmultiplemodels
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1B3D9FF8
	Offset: 0x2882E
	Size: 0x95
	Parameters: 9
	Flags: None
*/
function spawnmultiplemodels(orig, p1, p2, p3, xx, yy, zz, model, angles)
{
	array = [];
	for(a = 0; a < p1; a++)
	{
		for(b = 0; b < p2; b++)
		{
			for(c = 0; c < p3; c++)
			{
				array[array.size] = spawnsm((orig[0] + a * xx, orig[1] + b * yy, orig[2] + c * zz), model, angles);
				wait(0.05);
			}
		}
	}
	return array;
}

/*
	Name: spawnsm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xED985F20
	Offset: 0x288C4
	Size: 0x3C
	Parameters: 3
	Flags: None
*/
function spawnsm(origin, model, angles)
{
	ent = spawn("script_model", origin);
	ent setmodel(model);
	if(isdefined(angles))
	{
		ent.angles = angles;
	}
	return ent;
}

/*
	Name: array_delete
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9DC5058F
	Offset: 0x28902
	Size: 0x36
	Parameters: 1
	Flags: None
*/
function array_delete(array)
{
	self iprintln("Red CP Wave: [^1OFF^7]");
	for(i = 0; i < array.size; i++)
	{
		array[i] delete();
	}
}

/*
	Name: playerwallhack
	Namespace: _imcsx_gsc_studio
	Checksum: 0xBFB30780
	Offset: 0x2893A
	Size: 0x75
	Parameters: 1
	Flags: None
*/
function playerwallhack(player)
{
	if(player.togglewallhack == 1)
	{
		player thread enableesp();
		player maps/mp/killstreaks/_spyplane::callsatellite("radardirection_mp");
		self iprintln(player.name + " ^5ESP Wallhack : ^7[^2Enabled^7]");
		player.togglewallhack = 0;
	}
	else
	{
		player thread disableesp();
		self iprintln(player.name + " ^5ESP Wallhack : ^7[^1Disabled^7]");
		player.togglewallhack = 1;
	}
}

/*
	Name: initwhitelightbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x504E3560
	Offset: 0x289B0
	Size: 0x4D
	Parameters: 0
	Flags: None
*/
function initwhitelightbullet()
{
	if(self.whitelightbulleton == 0)
	{
		self.whitelightbulleton = 1;
		self thread dowhitelightbullet();
		self iprintln("^5White Light Bullets: ^2On");
	}
	else
	{
		self.whitelightbulleton = 0;
		self notify("stop_WhiteLightBulletOn");
		self iprintln("^5White Light Bullets: ^1Off");
	}
}

/*
	Name: dowhitelightbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA438D7E6
	Offset: 0x289FE
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dowhitelightbullet()
{
	self endon("death");
	self endon("stop_WhiteLightBulletOn");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["fx_riotshield_depoly_lights"] = loadfx("weapon/riotshield/fx_riotshield_depoly_lights");
		playfx(level._effect["fx_riotshield_depoly_lights"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initclaymorebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE11A88A7
	Offset: 0x28ABA
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initclaymorebullet()
{
	if(self.claymorebulleton == 0)
	{
		self.claymorebulleton = 1;
		self thread doclaymorebullet();
		self iprintln("^5Lasers Bullets: ^2On");
	}
	else
	{
		self.claymorebulleton = 0;
		self notify("stop_ClaymoreBulletOn");
		self iprintln("^5Lasers Bullets: ^1Off");
	}
}

/*
	Name: doclaymorebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5D2C8798
	Offset: 0x28B0A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doclaymorebullet()
{
	self endon("death");
	self endon("stop_ClaymoreBulletOn");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["fx_claymore_laser"] = loadfx("weapon/claymore/fx_claymore_laser");
		playfx(level._effect["fx_claymore_laser"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: inityellowv2bullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4995A99A
	Offset: 0x28BC6
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function inityellowv2bullet()
{
	if(self.yellowv2bulleton == 0)
	{
		self.yellowv2bulleton = 1;
		self thread doyellowv2bullet();
		self iprintln("^5Yellow #2 Bullets: ^2On");
	}
	else
	{
		self.yellowv2bulleton = 0;
		self notify("stop_YellowV2Bullet");
		self iprintln("^5Yellow #2 Bullets: ^1Off");
	}
}

/*
	Name: doyellowv2bullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4F0B6FFC
	Offset: 0x28C16
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doyellowv2bullet()
{
	self endon("death");
	self endon("stop_YellowV2Bullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["fx_theater_mode_camera_head_glow_yllw"] = loadfx("misc/fx_theater_mode_camera_head_glow_yllw");
		playfx(level._effect["fx_theater_mode_camera_head_glow_yllw"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: goldshoes
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC7BE0193
	Offset: 0x28CD2
	Size: 0x9F
	Parameters: 0
	Flags: None
*/
function goldshoes()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Gold Tags Shoes ^1OFF", "^5Gold Tags Shoes ^2ON"));
	if(self.goldshoesman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("p6_dogtags", "j_ball_le");
		self attachshieldmodel("p6_dogtags", "j_ball_ri");
		self.goldshoesman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.goldshoesman = 1;
	}
}

/*
	Name: chromeshoes
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC62934D0
	Offset: 0x28D72
	Size: 0x9F
	Parameters: 0
	Flags: None
*/
function chromeshoes()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Chrome Shoes ^1OFF", "^5Chrome Shoes ^2ON"));
	if(self.chromeshoesman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("projectile_hellfire_missile", "j_ball_le");
		self attachshieldmodel("projectile_hellfire_missile", "j_ball_ri");
		self.chromeshoesman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.chromeshoesman = 1;
	}
}

/*
	Name: redshoes
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4FFF9E50
	Offset: 0x28E12
	Size: 0x9F
	Parameters: 0
	Flags: None
*/
function redshoes()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Red Tags Shoes ^1OFF", "^5Red Tags Shoes ^2ON"));
	if(self.laptopshoesman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("p6_dogtags_friend", "j_ball_le");
		self attachshieldmodel("p6_dogtags_friend", "j_ball_ri");
		self.laptopshoesman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.laptopshoesman = 1;
	}
}

/*
	Name: rotorsman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB44ECCDB
	Offset: 0x28EB2
	Size: 0xDB
	Parameters: 0
	Flags: None
*/
function rotorsman()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Rotor Man ^1OFF", "^5Rotor Man ^2ON"));
	if(self.rotorzman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("vehicle_mi24p_hind_desert_d_piece02", "j_head");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "tag_weapon_left");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "tag_weapon_right");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_ball_le");
		self attachshieldmodel("t5_veh_rcbomb_gib_large", "j_ball_ri");
		self.rotorzman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.rotorzman = 1;
	}
}

/*
	Name: dropcan
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD16B36D5
	Offset: 0x28F8E
	Size: 0x2B
	Parameters: 0
	Flags: None
*/
function dropcan()
{
	weap = "svu_mp";
	self giveweapon(weap);
	wait(0.1);
	self dropitem(weap);
}

/*
	Name: givedefaultgun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x10B51879
	Offset: 0x28FBA
	Size: 0xBF
	Parameters: 0
	Flags: None
*/
function givedefaultgun()
{
	self takeallweapons();
	wait(0.1);
	self iprintln("^5Hands Gun ^2ON");
	self iprintln("^2Press [{+switchseat}] To Turn ^1OFF");
	self giveweapon("defaultweapon_mp");
	self givemaxammo("defaultweapon_mp");
	self giveweapon("dsr50_mp");
	self giveweapon("judge_mp");
	self giveweapon("870mcs_mp");
	self giveweapon("tar21_mp");
	self giveweapon("proximity_grenade_mp");
	self switchtoweapon("defaultweapon_mp");
	self thread monitordefault();
}

/*
	Name: monitordefault
	Namespace: _imcsx_gsc_studio
	Checksum: 0x29A5F5B4
	Offset: 0x2907A
	Size: 0x82
	Parameters: 0
	Flags: None
*/
function monitordefault()
{
	self endon("death");
	self endon("disconnect");
	while(self changeseatbuttonpressed() && self getcurrentweapon() == "dsr50_mp" || (self getcurrentweapon() == "judge_mp" || self getcurrentweapon() == "870mcs_mp") || self getcurrentweapon() == "tar21_mp")
	{
		wait(0.1);
		self switchtoweapon("defaultweapon_mp");
		wait(1);
		wait(0.05);
	}
}

/*
	Name: spinningwarthog
	Namespace: _imcsx_gsc_studio
	Checksum: 0x38FDC5C8
	Offset: 0x290FE
	Size: 0x82
	Parameters: 0
	Flags: None
*/
function spinningwarthog()
{
	self endon("disconnect");
	self endon("warthog1ssoff");
	spinwarthog = spawn("script_model", self.origin + (60, 0, 900));
	level.entities[level.amountofentities] = spinwarthog;
	level.amountofentities++;
	spinwarthog setmodel("veh_t6_air_a10f_alt");
	spinwarthog setcontents(1);
	self iprintlnbold("^2Spinning Warthog ^5Spawned In The Sky");
	for(;;)
	{
		spinwarthog rotateyaw(-180, 1);
		wait(1);
	}
}

/*
	Name: flippingwarthog
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8DE86CB0
	Offset: 0x29182
	Size: 0x82
	Parameters: 0
	Flags: None
*/
function flippingwarthog()
{
	self endon("disconnect");
	self endon("warthog2fsoff");
	flipwarthog = spawn("script_model", self.origin + (60, 0, 900));
	level.entities[level.amountofentities] = flipwarthog;
	level.amountofentities++;
	flipwarthog setmodel("veh_t6_air_a10f_alt");
	flipwarthog setcontents(1);
	self iprintlnbold("^2Flipping Warthog ^5Spawned In The Sky");
	for(;;)
	{
		flipwarthog rotateroll(-180, 1);
		wait(1);
	}
}

/*
	Name: rollingwarthog
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5527AA5
	Offset: 0x29206
	Size: 0x82
	Parameters: 0
	Flags: None
*/
function rollingwarthog()
{
	self endon("disconnect");
	self endon("warthog3rsoff");
	rollwarthog = spawn("script_model", self.origin + (60, 0, 900));
	level.entities[level.amountofentities] = rollwarthog;
	level.amountofentities++;
	rollwarthog setmodel("veh_t6_air_a10f_alt");
	rollwarthog setcontents(1);
	self iprintlnbold("^2Rolling Warthog ^5Spawned In The Sky");
	for(;;)
	{
		rollwarthog rotatepitch(-180, 1);
		wait(1);
	}
}

/*
	Name: rapidfire
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2599D8FE
	Offset: 0x2928A
	Size: 0x12C
	Parameters: 0
	Flags: None
*/
function rapidfire()
{
	self endon("disconnect");
	self.underfire = booleanopposite(self.underfire);
	self iprintln(booleanreturnval(self.underfire, "^5Rapid Fire ^1OFF", "^5Rapid Fire ^2ON"));
	if(self.rapidsfire == 0 || self.underfire)
	{
		self.rapidsfire = 1;
		setdvar("perk_weapRateMultiplier", "0.001");
		setdvar("perk_weapReloadMultiplier", "0.001");
		setdvar("perk_fireproof", "0.001");
		setdvar("cg_weaponSimulateFireAnims", "0.001");
		self setperk("specialty_rof");
		self setperk("specialty_fastreload");
	}
	else
	{
		self.rapidsfire = 0;
		setdvar("perk_weapRateMultiplier", "1");
		setdvar("perk_weapReloadMultiplier", "1");
		setdvar("perk_fireproof", "1");
		setdvar("cg_weaponSimulateFireAnims", "1");
		self unsetperk("specialty_rof");
		self unsetperk("specialty_fastreload");
		if(self.ammunition == 1)
		{
			self notify("stop_unlimammo");
		}
	}
}

/*
	Name: firetheskyz
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6B653058
	Offset: 0x293B8
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function firetheskyz()
{
	if(self.firetheskyz == 0)
	{
		self iprintln("^5Fire The Sky ^7[^2ON^7]");
		self.firetheskyz = 1;
		self thread firethebbsky();
	}
	else
	{
		self iprintln("^5Fire The Sky ^7[^1OFF^7]");
		self.firetheskyz = 0;
		self notify("stopFireTheSkyz");
	}
}

/*
	Name: firethebbsky
	Namespace: _imcsx_gsc_studio
	Checksum: 0x18D1213E
	Offset: 0x29404
	Size: 0x34
	Parameters: 0
	Flags: None
*/
function firethebbsky()
{
	self endon("death");
	self endon("stopFireTheSkyz");
	self endon("disconnect");
	iprintlnbold("^2Look At The Sky");
	for(;;)
	{
		self thread dofiretheskyscript();
		wait(0.0001);
	}
}

/*
	Name: dofiretheskyscript
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2DC04034
	Offset: 0x2943A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dofiretheskyscript()
{
	lr = maps/mp/gametypes/_spawnlogic::findboxcenter(level.spawnmins, level.spawnmaxs);
	z = randomintrange(1000, 2000);
	x = randomintrange(-1500, 1500);
	y = randomintrange(-1500, 1500);
	l = lr + (x, y, z);
	bombs = spawn("script_model", l);
	bombs setmodel("");
	bombs.angles = bombs.angles + (90, 90, 90);
	wait(0.0001);
	bombs thread firetheskyscript();
	bombs delete();
}

/*
	Name: firetheskyscript
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC319A2B5
	Offset: 0x294F6
	Size: 0x22
	Parameters: 0
	Flags: None
*/
function firetheskyscript()
{
	self endon("donefiretheskyzx");
	for(;;)
	{
		playfx(level.fx_u2_explode, self.origin);
		wait(0.0001);
	}
}

/*
	Name: jetplanegun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x259ACA19
	Offset: 0x2951A
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function jetplanegun()
{
	self.jetgunbb = booleanopposite(self.jetgunbb);
	self iprintln(booleanreturnval(self.jetgunbb, "^5Warthog Gun ^1OFF", "^5Warthog Gun ^2ON"));
	if(self.xbbjetshoot == 1 || self.jetgunbb)
	{
		self thread shootjetplane();
		self.xbbjetshoot = 0;
	}
	else
	{
		self notify("sexjetgun");
		self takeweapon("870mcs_mp+silencer");
		self.xbbjetshoot = 1;
	}
}

/*
	Name: shootjetplane
	Namespace: _imcsx_gsc_studio
	Checksum: 0x720A350C
	Offset: 0x2958A
	Size: 0x12A
	Parameters: 0
	Flags: None
*/
function shootjetplane()
{
	self endon("death");
	self endon("sexjetgun");
	self endon("disconnect");
	self giveweapon("870mcs_mp+silencer", 0, 32);
	self switchtoweapon("870mcs_mp+silencer");
	self givemaxammo("870mcs_mp+silencer");
	self iprintln("^3Jet Gun: ^2Ready");
	for(;;)
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "870mcs_mp+silencer")
		{
			l = self gettagorigin("tag_eye");
			lb = spawnhelicopter(self, l, self.angles + (0, 2, 0), "heli_guard_mp", "veh_t6_air_a10f_alt");
			if(!isdefined(lb))
			{
				return;
			}
			lb.owner = self;
			lb.team = self.team;
			self thread x_bb_jetgunx(lb);
			n = bullettrace(self gettagorigin("tag_eye"), AnglesToForward(self getplayerangles()) * 100000, 0, self)["position"];
			lb setspeed(5000, 689);
			lb setvehgoalpos(n);
			wait(0.169);
		}
	}
}

/*
	Name: x_bb_jetgunx
	Namespace: _imcsx_gsc_studio
	Checksum: 0x358CACEB
	Offset: 0x296B6
	Size: 0x67
	Parameters: 1
	Flags: None
*/
function x_bb_jetgunx(lb)
{
	self endon("disconnect");
	self endon("death");
	self endon("sexjetgun");
	wait(1.22);
	playfx(level._effect["vehicle/vexplosion/fx_vexplode_heli_killstreak_exp_sm"], lb.origin);
	radiusdamage(lb.origin, 300, 300, 1500, self);
	wait(0.1);
	lb delete();
}

/*
	Name: emptytriangleinsky
	Namespace: _imcsx_gsc_studio
	Checksum: 0x700778B8
	Offset: 0x2971E
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function emptytriangleinsky()
{
	if(level.triangleinskyempty == 1)
	{
		level.triangleinskyempty = 0;
		level thread text4emptytriangleinsky();
		wp("225,480,250,480,275,480,300,480,325,480,350,480,375,480,400,480,425,480,450,480,475,480,500,480,525,480,550,480,575,480,600,480,625,480,650,480,675,480,700,480,725,480,750,480,775,480,800,480,825,480,225,510,250,510,275,510,300,510,325,510,350,510,375,510,400,510,425,510,450,510,475,510,500,510,525,510,550,510,575,510,600,510,625,510,650,510,675,510,700,510,725,510,750,510,775,510,800,510,825,510,250,540,275,540,300,540,325,540,725,540,750,540,775,540,800,540,250,570,275,570,300,570,325,570,350,570,700,570,725,570,750,570,775,570,800,570,275,600,300,600,325,600,350,600,700,600,725,600,750,600,775,600,300,630,325,630,350,630,375,630,675,630,700,630,725,630,750,630,300,660,325,660,350,660,375,660,400,660,675,660,700,660,725,660,750,660,325,690,350,690,375,690,400,690,650,690,675,690,700,690,725,690,325,720,350,720,375,720,400,720,425,720,625,720,650,720,675,720,700,720,725,720,350,750,375,750,400,750,425,750,625,750,650,750,675,750,700,750,375,780,400,780,425,780,450,780,600,780,625,780,650,780,675,780,375,810,400,810,425,810,450,810,600,810,625,810,650,810,675,810,400,840,425,840,450,840,475,840,575,840,600,840,625,840,650,840,400,870,425,870,450,870,475,870,500,870,550,870,575,870,600,870,625,870,650,870,425,900,450,900,475,900,500,900,550,900,575,900,600,900,625,900,450,930,475,930,500,930,525,930,550,930,575,930,600,930,450,960,475,960,500,960,525,960,550,960,575,960,600,960,475,990,500,990,525,990,550,990,575,990,475,1020,500,1020,525,1020,550,1020,575,1020,500,1050,525,1050,550,1050,525,1080", 2000, 0);
	}
	else
	{
		self iprintln("^1Triangle is Already in The Sky");
	}
}

/*
	Name: text4emptytriangleinsky
	Namespace: _imcsx_gsc_studio
	Checksum: 0x43A90CDF
	Offset: 0x2975E
	Size: 0x37
	Parameters: 0
	Flags: None
*/
function text4emptytriangleinsky()
{
	iprintlnbold("^2Look At The Sky");
	wait(2.5);
	iprintlnbold("^5Triangle in The Sky");
	wait(2.5);
	iprintlnbold("^2illuminati Confirmed");
}

/*
	Name: shootvadertog
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF00D952
	Offset: 0x29796
	Size: 0x6F
	Parameters: 0
	Flags: None
*/
function shootvadertog()
{
	self.deathrock = booleanopposite(self.deathrock);
	self iprintln(booleanreturnval(self.deathrock, "^3Rocket Gun ^1OFF", "^3Rocket Gun ^2ON"));
	if(self.dball == 1 || self.deathrock)
	{
		self thread shootvader();
		self.dball = 0;
	}
	else
	{
		self notify("sex");
		self takeweapon("870mcs_mp+extbarrel");
		self.dball = 1;
	}
}

/*
	Name: shootvader
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC5CD261E
	Offset: 0x29806
	Size: 0x12A
	Parameters: 0
	Flags: None
*/
function shootvader()
{
	self endon("death");
	self endon("sex");
	self endon("disconnect");
	self giveweapon("870mcs_mp+extbarrel", 0, 29);
	self switchtoweapon("870mcs_mp+extbarrel");
	self givemaxammo("870mcs_mp+extbarrel");
	self iprintln("^5Rocket Gun ^2Ready");
	for(;;)
	{
		self waittill("weapon_fired");
		if(self getcurrentweapon() == "870mcs_mp+extbarrel")
		{
			l = self gettagorigin("tag_eye");
			lb = spawnhelicopter(self, l, self.angles + (0, 180, 0), "heli_guard_mp", "projectile_sa6_missile_desert_mp");
			if(!isdefined(lb))
			{
				return;
			}
			lb.owner = self;
			lb.team = self.team;
			self thread x_daftvader_xxx(lb);
			n = bullettrace(self gettagorigin("tag_eye"), AnglesToForward(self getplayerangles()) * 100000, 0, self)["position"];
			lb setspeed(5000, 196);
			lb setvehgoalpos(n);
			wait(0.9);
		}
	}
}

/*
	Name: x_daftvader_xxx
	Namespace: _imcsx_gsc_studio
	Checksum: 0x819225F6
	Offset: 0x29932
	Size: 0x67
	Parameters: 1
	Flags: None
*/
function x_daftvader_xxx(lb)
{
	self endon("disconnect");
	self endon("death");
	self endon("sex");
	wait(1.22);
	playfx(level._effect["ChafFx"], lb.origin);
	radiusdamage(lb.origin, 300, 300, 1500, self);
	wait(0.1);
	lb delete();
}

/*
	Name: redshieldshoes
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB67CFA20
	Offset: 0x2999A
	Size: 0x9F
	Parameters: 0
	Flags: None
*/
function redshieldshoes()
{
	self.armin = booleanopposite(self.armin);
	self iprintln(booleanreturnval(self.armin, "^5Red Shield Shoes ^1OFF", "^5Red Shield Shoes ^2ON"));
	if(self.redshieldshoesman == 1 || self.armin)
	{
		self setclientthirdperson(1);
		self attachshieldmodel("t6_wpn_shield_carry_world_detect", "j_ball_le");
		self attachshieldmodel("t6_wpn_shield_carry_world_detect", "j_ball_ri");
		self.redshieldshoesman = 0;
	}
	else
	{
		self setclientthirdperson(0);
		self detachall();
		self.redshieldshoesman = 1;
	}
}

/*
	Name: rotormanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2B03FB9C
	Offset: 0x29A3A
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function rotormanall()
{
	if(self.rotormanallon == 0)
	{
		self.rotormanallon = 1;
		self thread togglerotorman1all();
		self iprintln("^2Gave All Rotor Man");
	}
	else
	{
		self.rotormanallon = 0;
		self iprintln("^1All Rotor Man OFF");
		self thread togglerotorman1all();
	}
}

/*
	Name: togglerotorman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1E1BB2DB
	Offset: 0x29A8E
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglerotorman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread rotorsman();
		}
	}
}

/*
	Name: lightmanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF09D02DA
	Offset: 0x29ADA
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function lightmanall()
{
	if(self.lightmanallon == 0)
	{
		self.lightmanallon = 1;
		self thread togglelightman1all();
		self iprintln("^2Gave All Light Man");
	}
	else
	{
		self.lightmanallon = 0;
		self iprintln("^1All Light Man OFF");
		self thread togglelightman1all();
	}
}

/*
	Name: togglelightman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB59C1925
	Offset: 0x29B2E
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglelightman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initchafman();
		}
	}
}

/*
	Name: shieldshoesall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4050951E
	Offset: 0x29B7A
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function shieldshoesall()
{
	if(self.shieldshoesallon == 0)
	{
		self.shieldshoesallon = 1;
		self thread toggleshieldshoes1all();
		self iprintln("^2Gave All Red Shield Shoes");
	}
	else
	{
		self.shieldshoesallon = 0;
		self iprintln("^1All Red Shield Shoes OFF");
		self thread toggleshieldshoes1all();
	}
}

/*
	Name: toggleshieldshoes1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0x637DA685
	Offset: 0x29BCE
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function toggleshieldshoes1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread redshieldshoes();
		}
	}
}

/*
	Name: mw2waterman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB8C64025
	Offset: 0x29C1A
	Size: 0x66
	Parameters: 0
	Flags: None
*/
function mw2waterman()
{
	if(self.fountainman == 0)
	{
		self.fountainman = 1;
		self iprintln("^5Fountain Man ^7[^2On^7]");
		self setclientthirdperson(1);
		self thread waterfountainman();
	}
	else
	{
		self.fountainman = 0;
		self iprintln("^5Fountain Man ^7[^1Off^7]");
		self setclientthirdperson(0);
		self notify("stop_thirstybitch");
	}
}

/*
	Name: waterfountainman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8272D09A
	Offset: 0x29C82
	Size: 0x3E
	Parameters: 0
	Flags: None
*/
function waterfountainman()
{
	self endon("disconnect");
	self endon("stop_thirstybitch");
	while(1)
	{
		playfx(level._effect["impacts/fx_xtreme_water_hit_mp"], self gettagorigin("j_spine4"));
		wait(0.2);
	}
}

/*
	Name: initgreensensorbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4F4AA593
	Offset: 0x29CC2
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initgreensensorbullet()
{
	if(self.grensensorbulleton == 0)
	{
		self.grensensorbulleton = 1;
		self thread dogrensensorbullet();
		self iprintln("^5Green Sensor Bullets: ^2On");
	}
	else
	{
		self.grensensorbulleton = 0;
		self notify("stop_GrenSensorBullet");
		self iprintln("^5Green Sensor Bullets: ^1Off");
	}
}

/*
	Name: dogrensensorbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7B567A0D
	Offset: 0x29D12
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dogrensensorbullet()
{
	self endon("death");
	self endon("stop_GrenSensorBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["greensensorexpl"] = loadfx("weapon/sensor_grenade/fx_sensor_exp_scan_friendly");
		playfx(level._effect["greensensorexpl"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: megaairdrops
	Namespace: _imcsx_gsc_studio
	Checksum: 0x32B2A618
	Offset: 0x29DCE
	Size: 0x69
	Parameters: 0
	Flags: None
*/
function megaairdrops()
{
	if(self.megaairdropon == 0)
	{
		self thread megaairdrop();
		self iprintlnbold("^5Mega AirDrop ^2Incoming ^3Look At The Sky");
		self iprintln("^5Mega AirDrop ^7[^2On^7]");
		self.megaairdropon = 1;
	}
	else
	{
		self iprintln("^5Mega AirDrop ^7[^1Off^7]");
		level.cpheli delete();
		self notify("stopthecp");
		self.megaairdropon = 0;
	}
}

/*
	Name: megaairdrop
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB8121E33
	Offset: 0x29E38
	Size: 0x51
	Parameters: 0
	Flags: None
*/
function megaairdrop()
{
	level.megaairdropmodel = "heli_guard_mp";
	level.megaairdropmodel1 = "veh_t6_air_v78_vtol_killstreak";
	level.cpheli = spawnhelicopter(self, self.origin + (12000, 0, 1500), self.angles, level.megaairdropmodel, level.megaairdropmodel1);
	self thread followdudeairdrop();
	wait(5);
	self thread dropcarepackages();
}

/*
	Name: followdudeairdrop
	Namespace: _imcsx_gsc_studio
	Checksum: 0x381B4A55
	Offset: 0x29E8A
	Size: 0x46
	Parameters: 0
	Flags: None
*/
function followdudeairdrop()
{
	self endon("disconnect");
	self endon("stopthecp");
	for(;;)
	{
		level.cpheli setspeed(1000, 25);
		level.cpheli setvehgoalpos(self.origin + (100, 100, 1500), 1);
		wait(0.1);
	}
}

/*
	Name: dropcarepackages
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9FAC1380
	Offset: 0x29ED2
	Size: 0x66
	Parameters: 0
	Flags: None
*/
function dropcarepackages()
{
	self endon("disconnect");
	self endon("stopthecp");
	for(i = 0; i < 200; i++)
	{
		self thread maps/mp/killstreaks/_supplydrop::dropcrate(level.cpheli.origin + (10, 10, -120), self.angles, "supplydrop_mp", self, self.team, self.killcament, undefined, undefined, undefined);
		level.result = level.result + 1;
		wait(0.5);
	}
}

/*
	Name: spawnactordog
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9F8FBF9D
	Offset: 0x29F3A
	Size: 0x1B3
	Parameters: 1
	Flags: None
*/
function spawnactordog(team)
{
	self iprintln("^5Press [{+attack}] Shoot To Spawn Actor Dog");
	self endon("disconnect");
	self endon("death");
	self waittill("weapon_fired");
	dog_spawner = getent("dog_spawner", "targetname");
	level.dog_abort = 0;
	if(!isdefined(dog_spawner))
	{
		self iprintln("^5No dog spawners found in map");
		return;
	}
	direction = self getplayerangles();
	direction_vec = AnglesToForward(direction);
	eye = self geteye();
	scale = 8000;
	direction_vec = (direction_vec[0] * scale, direction_vec[1] * scale, direction_vec[2] * scale);
	trace = bullettrace(eye, eye + direction_vec, 0, undefined);
	nodes = getnodesinradius(trace["position"], 256, 0, 128, "Path", 8);
	if(!nodes.size)
	{
		self iprintln("^5No nodes found near crosshair position");
		return;
	}
	self iprintln("^5Actor Dog ^2Spawned");
	node = getclosest(trace["position"], nodes);
	dog = dog_manager_spawn_dog(self, self.team, node, 5);
	dog setcandamage(0);
	dog.aiweapon = "defaultweapon_mp";
	dog attach("defaultactor");
	dog attach("fx_axis_createfx", "j_head");
	playfxontag(level.waypointred, dog, "j_head");
	playfxontag(level.waypointgreen, dog, "j_head");
	playfxontag(level.waypointgreen, dog, "j_spineupper");
	playfxontag(level.waypointgreen, dog, "j_spinelower");
}

/*
	Name: mandog
	Namespace: _imcsx_gsc_studio
	Checksum: 0xABAB3872
	Offset: 0x2A0EE
	Size: 0x1B3
	Parameters: 1
	Flags: None
*/
function mandog(team)
{
	self iprintln("^5Press [{+attack}] Shoot To Spawn Man Dog");
	self endon("disconnect");
	self endon("death");
	self waittill("weapon_fired");
	dog_spawner = getent("dog_spawner", "targetname");
	level.dog_abort = 0;
	if(!isdefined(dog_spawner))
	{
		self iprintln("^5No dog spawners found in map");
		return;
	}
	direction = self getplayerangles();
	direction_vec = AnglesToForward(direction);
	eye = self geteye();
	scale = 8000;
	direction_vec = (direction_vec[0] * scale, direction_vec[1] * scale, direction_vec[2] * scale);
	trace = bullettrace(eye, eye + direction_vec, 0, undefined);
	nodes = getnodesinradius(trace["position"], 256, 0, 128, "Path", 8);
	if(!nodes.size)
	{
		self iprintln("^5No nodes found near crosshair position");
		return;
	}
	self iprintln("^5Man Dog ^2Spawned");
	node = getclosest(trace["position"], nodes);
	mandog = dog_manager_spawn_dog(self, self.team, node, 5);
	mandog setcandamage(0);
	mandog.aiweapon = "defaultweapon_mp";
	mandog attach("c_usa_mp_seal6_assault_fb");
	mandog attach("fx_axis_createfx", "j_head");
	playfxontag(level.waypointred, mandog, "j_head");
	playfxontag(level.waypointgreen, mandog, "j_head");
	playfxontag(level.waypointred, mandog, "j_spineupper");
	playfxontag(level.waypointred, mandog, "j_spinelower");
}

/*
	Name: paralizeddog
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB032DC0B
	Offset: 0x2A2A2
	Size: 0x167
	Parameters: 1
	Flags: None
*/
function paralizeddog(team)
{
	self iprintln("^5Press [{+attack}] Shoot To Spawn Paralized Dog");
	self endon("disconnect");
	self endon("death");
	self waittill("weapon_fired");
	dog_spawner = getent("dog_spawner", "targetname");
	level.dog_abort = 0;
	if(!isdefined(dog_spawner))
	{
		self iprintln("^5No dog spawners found in map");
		return;
	}
	direction = self getplayerangles();
	direction_vec = AnglesToForward(direction);
	eye = self geteye();
	scale = 8000;
	direction_vec = (direction_vec[0] * scale, direction_vec[1] * scale, direction_vec[2] * scale);
	trace = bullettrace(eye, eye + direction_vec, 0, undefined);
	nodes = getnodesinradius(trace["position"], 256, 0, 128, "Path", 8);
	if(!nodes.size)
	{
		self iprintln("^5No nodes found near crosshair position");
		return;
	}
	self iprintln("^5Paralized Dog ^2Spawned");
	node = getclosest(trace["position"], nodes);
	sweg = dog_manager_spawn_dog(self, self.team, node, 5);
	sweg setcandamage(0);
	sweg attach("defaultactor");
	sweg startragdoll(1);
	wait(0.1);
	sweg detachall();
}

/*
	Name: spawnlel
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5D6F7004
	Offset: 0x2A40A
	Size: 0x187
	Parameters: 1
	Flags: None
*/
function spawnlel(team)
{
	self iprintln("^5Press [{+attack}] Shoot To Spawn Man");
	self endon("disconnect");
	self endon("death");
	self waittill("weapon_fired");
	dog_spawner = getent("dog_spawner", "targetname");
	level.dog_abort = 0;
	if(!isdefined(dog_spawner))
	{
		self iprintln("^5No dog spawners found in map");
		return;
	}
	direction = self getplayerangles();
	direction_vec = AnglesToForward(direction);
	eye = self geteye();
	scale = 8000;
	direction_vec = (direction_vec[0] * scale, direction_vec[1] * scale, direction_vec[2] * scale);
	trace = bullettrace(eye, eye + direction_vec, 0, undefined);
	nodes = getnodesinradius(trace["position"], 256, 0, 128, "Path", 8);
	if(!nodes.size)
	{
		self iprintln("^5No nodes found near crosshair position");
		return;
	}
	self iprintln("^5Man ^2Spawned");
	node = getclosest(trace["position"], nodes);
	dog = dog_manager_spawn_dog(self, self.team, node, 5);
	dog setcandamage(0);
	dog.aiweapon = "defaultweapon_mp";
	dog hide();
	man = spawn("script_model", dog.origin);
	man [[game["set_player_model"][self.team]["default"]]]();
	man linkto(dog);
}

/*
	Name: tracebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF40DF9A5
	Offset: 0x2A592
	Size: 0x38
	Parameters: 0
	Flags: None
*/
function tracebullet()
{
	return bullettrace(self geteye(), self geteye() + VectorScale(AnglesToForward(self getplayerangles()), 1000000), 0, self)["position"];
}

/*
	Name: mbarrage
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEC645314
	Offset: 0x2A5CC
	Size: 0x10C
	Parameters: 0
	Flags: None
*/
function mbarrage()
{
	self endon("disconnect");
	self endon("death");
	closemenu();
	self iprintlnbold("^5Press [{+usereload}] To Select Missiles Barrage Location");
	self.barraging = 0;
	for(;;)
	{
		wait(0.05);
		if(self usebuttonpressed() && self.barraging == 0)
		{
			self beginlocationselection("hud_medals_default");
			self.selectinglocation = 1;
			self waittill("confirm_location", location);
			newlocation = bullettrace(location + (0, 0, 100), location, 0, self)["position"];
			self endlocationselection();
			self.selectinglocation = undefined;
			i = newlocation;
			self.barraging = 1;
			for(;;)
			{
				x = randomintrange(-7000, 7000);
				y = randomintrange(-7000, 7000);
				z = randomintrange(0, 7000);
				magicbullet("usrpg_mp", (x, y, z), i, self);
				wait(0.05);
			}
		}
	}
}

/*
	Name: changeminimap1
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9F02A1CE
	Offset: 0x2A6DA
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap1()
{
	if(self.changeminimap1on == 0)
	{
		self.changeminimap1on = 1;
		maps/mp/_compass::setupminimap("em_bg_ani_comics");
		self iprintlnbold("^5Comics ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap1on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Comics ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap2
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF7143A6E
	Offset: 0x2A73E
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap2()
{
	if(self.changeminimap2on == 0)
	{
		self.changeminimap2on = 1;
		maps/mp/_compass::setupminimap("em_bg_ani_octane");
		self iprintlnbold("^5Octane ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap2on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Octane ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap3
	Namespace: _imcsx_gsc_studio
	Checksum: 0x73972EB2
	Offset: 0x2A7A2
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap3()
{
	if(self.changeminimap3on == 0)
	{
		self.changeminimap3on = 1;
		maps/mp/_compass::setupminimap("compass_static");
		self iprintlnbold("^5Static ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap3on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Static ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: flyoncpufo
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7A75A818
	Offset: 0x2A806
	Size: 0x6E
	Parameters: 0
	Flags: None
*/
function flyoncpufo()
{
	self endon("disconnect");
	self endon("death");
	self iprintln("^5Flying On Red CarePackage");
	newufo = spawn("script_model", self.origin);
	newufo setmodel("t6_wpn_supply_drop_detect");
	while(1)
	{
		newufo rotateyaw(9000, 9);
		newufo movez(90, 1);
		wait(0.02);
	}
}

/*
	Name: rollawaydog
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3E62D542
	Offset: 0x2A876
	Size: 0xD6
	Parameters: 0
	Flags: None
*/
function rollawaydog()
{
	self endon("death");
	self endon("disconnect");
	rollawaydogs = spawn("script_model", self.origin + (60, 0, 35), 1);
	rollawaydogs setmodel("german_shepherd");
	rollawaydogs attach("c_usa_mp_seal6_assault_fb");
	rollawaydogs attach("fx_axis_createfx", "j_head");
	rollawaydogs rotatepitch(9720, 30);
	wait(0.3);
	self iprintlnbold("^2Shoot ^5To Roll Away The Dog");
	self waittill(self attackbuttonpressed());
	self waittill("weapon_fired");
	for(;;)
	{
		rollawaydogs moveto(rollawaydogs.origin + (300, 0, 0), 1);
		rollawaydogs rotatepitch(360, 1);
		wait(0.1);
	}
}

/*
	Name: doiceskater
	Namespace: _imcsx_gsc_studio
	Checksum: 0x43471A93
	Offset: 0x2A94E
	Size: 0x12A
	Parameters: 0
	Flags: None
*/
function doiceskater()
{
	self endon("death");
	skater = spawn("script_model", self.origin);
	skater setmodel("defaultactor");
	self iprintln("^5Ice Skater ^2Spawned");
	while(1)
	{
		skater rotateyaw(9000, 9);
		skater movey(-180, 1);
		wait(1);
		skater movey(180, 1);
		wait(1);
		skater movex(-180, 1);
		wait(1);
		skater movex(180, 1);
		wait(1);
		skater movez(90, 0.5);
		wait(0.5);
		skater movez(-90, 0.5);
		wait(0.5);
		skater movey(180, 1);
		wait(1);
		skater movey(-180, 1);
		wait(1);
		skater movex(180, 1);
		wait(1);
		skater movex(-180, 1);
		wait(1);
	}
}

/*
	Name: discosun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9C1AB3E8
	Offset: 0x2AA7A
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function discosun()
{
	if(self.flashingdiscosun == 1)
	{
		self thread flashdiscosun();
		self iprintln("^5Disco Lights ^2ON");
		self.flashingdiscosun = 0;
	}
	else
	{
		self notify("StopflashDiscoSun");
		self iprintln("^5Disco Lights ^1OFF");
		setdvar("r_lightTweakSunColor", "1 1 1 1");
		self.flashingdiscosun = 1;
	}
}

/*
	Name: flashdiscosun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x93F21B33
	Offset: 0x2AAD6
	Size: 0xBE
	Parameters: 0
	Flags: None
*/
function flashdiscosun()
{
	self endon("disconnect");
	self endon("StopflashDiscoSun");
	while(1)
	{
		setdvar("r_lightTweakSunColor", "1 0 0 0");
		wait(0.1);
		setdvar("r_lightTweakSunColor", "0 0 0 0");
		wait(0.1);
		setdvar("r_lightTweakSunColor", "0 0 1 0");
		wait(0.1);
		setdvar("r_lightTweakSunColor", "1 0 0 0");
		wait(0.1);
		setdvar("r_lightTweakSunColor", "0 1 0 0");
		wait(0.1);
		setdvar("r_lightTweakSunColor", "0 0 1 0");
		wait(0.1);
		setdvar("r_lightTweakSunColor", "1 0 0 0");
		wait(0.1);
	}
}

/*
	Name: marachidancer
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD244BF4C
	Offset: 0x2AB96
	Size: 0x1BE
	Parameters: 0
	Flags: None
*/
function marachidancer()
{
	self endon("disconnect");
	self endon("death");
	marachiman = spawn("script_model", self.origin);
	marachiman setmodel(self.model);
	self iprintln("^3Disco Dancer ^2Spawned");
	marachiman attach("fx_axis_createfx", "J_Head");
	marachiman attach("projectile_hellfire_missile", "J_Ankle_LE");
	marachiman attach("projectile_hellfire_missile", "J_Ankle_RI");
	marachiman attach("projectile_hellfire_missile", "J_Wrist_RI");
	marachiman attach("projectile_hellfire_missile", "J_Wrist_LE");
	playfxontag(level._effect["LightsGreenDisco"], marachiman, "J_Head");
	playfxontag(level._effect["LightsRedDisco"], marachiman, "tag_eye");
	for(;;)
	{
		marachiman rotateyaw(9000, 9);
		marachiman movey(-180, 1);
		wait(1);
		marachiman movey(180, 1);
		wait(1);
		marachiman movex(-180, 1);
		wait(1);
		marachiman movex(180, 1);
		wait(1);
		marachiman movez(90, 0.5);
		wait(0.5);
		marachiman movez(-90, 0.5);
		wait(0.5);
		marachiman movey(180, 1);
		wait(1);
		marachiman movey(-180, 1);
		wait(1);
		marachiman movex(180, 1);
		wait(1);
		marachiman movex(-180, 1);
	}
}

/*
	Name: pause
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCEF04B3D
	Offset: 0x2AD56
	Size: 0xB
	Parameters: 0
	Flags: None
*/
function pause()
{
	self thread maps/mp/gametypes/_hostmigration::callback_hostmigration();
}

/*
	Name: initdogstairs
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB072DA2A
	Offset: 0x2AD62
	Size: 0x3B
	Parameters: 0
	Flags: None
*/
function initdogstairs()
{
	self thread dogstairsheaven();
	self iprintln("^3Spawning Stairs...");
	wait(1);
	self iprintln("^2Spawning Stairs..");
	wait(1);
	self iprintln("^1STOP ^5Dog Spiral Stairs");
}

/*
	Name: inthelldogstairs
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDE9EA372
	Offset: 0x2AD9E
	Size: 0xB
	Parameters: 0
	Flags: None
*/
function inthelldogstairs()
{
	self thread initdogstairs();
}

/*
	Name: stopthadogstairs
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA6C65A81
	Offset: 0x2ADAA
	Size: 0x8
	Parameters: 0
	Flags: None
*/
function stopthadogstairs()
{
	self notify("Stop_Dogstairz");
}

/*
	Name: dogstairsheaven
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFC95A9BD
	Offset: 0x2ADB4
	Size: 0x178
	Parameters: 0
	Flags: None
*/
function dogstairsheaven()
{
	self endon("gotohelldogstairs");
	self endon("death");
	self endon("Stop_Dogstairz");
	self.stairsize = 99;
	for(;;)
	{
		vec = AnglesToForward(self getplayerangles());
		center = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000), 0, self)["position"];
		level.center = spawn("script_origin", center);
		level.stairs = [];
		origin = level.center.origin + (70, 0, 0);
		h = 0;
		for(i = 0; i <= 437; i++)
		{
			level.center rotateyaw(22.5, 0.05);
			wait(0.07);
			level.center moveto(level.center.origin + (0, 0, 18), 0.05);
			wait(0.02);
			level.stairs[i] = spawn("script_model", origin);
			level.stairs[i] setmodel("german_shepherd");
			level.stairs[i] linkto(level.center);
		}
		level.center moveto(level.center.origin - (0, 0, 10), 0.05);
	}
}

/*
	Name: initdirtbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1438C277
	Offset: 0x2AF2E
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initdirtbullet()
{
	if(self.dirtbulleton == 0)
	{
		self.dirtbulleton = 1;
		self thread dodirtbullet();
		self iprintln("^5Dirt Bullets: ^2On");
	}
	else
	{
		self.dirtbulleton = 0;
		self notify("stop_DirtBullet");
		self iprintln("^5Dirt Bullets: ^1Off");
	}
}

/*
	Name: dodirtbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFCFADF3F
	Offset: 0x2AF7E
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dodirtbullet()
{
	self endon("death");
	self endon("stop_DirtBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["impacts/fx_xtreme_dirthit_mp"] = loadfx("impacts/fx_xtreme_dirthit_mp");
		playfx(level._effect["impacts/fx_xtreme_dirthit_mp"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initsmokebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4A031C15
	Offset: 0x2B03A
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initsmokebullet()
{
	if(self.smokebulleton == 0)
	{
		self.smokebulleton = 1;
		self thread dosmokebullet();
		self iprintln("^5Smoke Bullets: ^2On");
	}
	else
	{
		self.smokebulleton = 0;
		self notify("stop_SmokeBullet");
		self iprintln("^5Smoke Bullets: ^1Off");
	}
}

/*
	Name: dosmokebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x611BDA9F
	Offset: 0x2B08A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dosmokebullet()
{
	self endon("death");
	self endon("stop_SmokeBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["fx_mp_exp_bomb_smk_streamer"] = loadfx("maps/mp_maps/fx_mp_exp_bomb_smk_streamer");
		playfx(level._effect["fx_mp_exp_bomb_smk_streamer"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: spinuav
	Namespace: _imcsx_gsc_studio
	Checksum: 0x902E5090
	Offset: 0x2B146
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function spinuav()
{
	self endon("disconnect");
	self endon("SpinUavOff");
	spinuav = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spinuav;
	level.amountofentities++;
	spinuav setmodel("veh_t6_drone_uav");
	spinuav setcontents(1);
	self iprintln("^3Spinning Uav ^2Spawned");
	for(;;)
	{
		spinuav rotateyaw(-360, 1);
		wait(1);
	}
}

/*
	Name: uavdog
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDD64C4D4
	Offset: 0x2B1C6
	Size: 0x163
	Parameters: 1
	Flags: None
*/
function uavdog(team)
{
	self iprintln("^5Press [{+attack}] Shoot To Spawn Uav Dog");
	self endon("disconnect");
	self endon("death");
	self waittill("weapon_fired");
	dog_spawner = getent("dog_spawner", "targetname");
	level.dog_abort = 0;
	if(!isdefined(dog_spawner))
	{
		self iprintln("^5No dog spawners found in map");
		return;
	}
	direction = self getplayerangles();
	direction_vec = AnglesToForward(direction);
	eye = self geteye();
	scale = 8000;
	direction_vec = (direction_vec[0] * scale, direction_vec[1] * scale, direction_vec[2] * scale);
	trace = bullettrace(eye, eye + direction_vec, 0, undefined);
	nodes = getnodesinradius(trace["position"], 256, 0, 128, "Path", 8);
	if(!nodes.size)
	{
		self iprintln("^5No nodes found near crosshair position");
		return;
	}
	self iprintln("^5Uav Dog ^2Spawned");
	node = getclosest(trace["position"], nodes);
	uavdog = dog_manager_spawn_dog(self, self.team, node, 5);
	uavdog setcandamage(0);
	uavdog.aiweapon = "defaultweapon_mp";
	uavdog attach("veh_t6_drone_uav");
	uavdog attach("veh_t6_drone_uav", "j_head");
}

/*
	Name: initravebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDCBD58DC
	Offset: 0x2B32A
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initravebullet()
{
	if(self.ravebulleton == 0)
	{
		self.ravebulleton = 1;
		self thread doravebullet();
		self iprintln("^5Rave Bullets: ^2On");
	}
	else
	{
		self.ravebulleton = 0;
		self notify("stop_RaveBullet");
		self iprintln("^5Rave Bullets: ^1Off");
	}
}

/*
	Name: doravebullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3BD507F4
	Offset: 0x2B37A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doravebullet()
{
	self endon("death");
	self endon("stop_RaveBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["misc/fx_theater_mode_camera_head_glow_white"] = loadfx("misc/fx_theater_mode_camera_head_glow_white");
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initraveman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1F5E2B1F
	Offset: 0x2B436
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initraveman()
{
	if(self.ravemanon == 0)
	{
		self.ravemanon = 1;
		self setclientthirdperson(1);
		self thread dodaraveman();
		self iprintln("^5Rave Man: ^2On");
	}
	else
	{
		self.ravemanon = 0;
		self setclientthirdperson(0);
		self notify("stop_daRaveMan");
		self iprintln("^5Rave Man: ^1Off");
	}
}

/*
	Name: dodaraveman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2FEEDC7
	Offset: 0x2B49A
	Size: 0x1D2
	Parameters: 0
	Flags: None
*/
function dodaraveman()
{
	self endon("disconnect");
	self endon("stop_daRaveMan");
	level._effect["misc/fx_theater_mode_camera_head_glow_white"] = loadfx("misc/fx_theater_mode_camera_head_glow_white");
	while(1)
	{
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("j_head"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("j_spineupper"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("j_spinelower"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("j_spine4"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("j_spine1"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("J_Elbow_RI"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("J_Elbow_LE"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("j_knee_le"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("j_knee_ri"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("J_Ankle_LE"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin("J_Ankle_RI"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin(" J_Wrist_RI"));
		playfx(level._effect["misc/fx_theater_mode_camera_head_glow_white"], self gettagorigin(" J_Wrist_LE"));
		wait(0.9);
	}
}

/*
	Name: retardman
	Namespace: _imcsx_gsc_studio
	Checksum: 0xCA9C6C9C
	Offset: 0x2B66E
	Size: 0x157
	Parameters: 1
	Flags: None
*/
function retardman(team)
{
	self iprintln("^5Press [{+attack}] Shoot To Spawn Retard Man");
	self endon("disconnect");
	self endon("death");
	self waittill("weapon_fired");
	dog_spawner = getent("dog_spawner", "targetname");
	level.dog_abort = 0;
	if(!isdefined(dog_spawner))
	{
		self iprintln("^5No Retard Man spawners found in map");
		return;
	}
	direction = self getplayerangles();
	direction_vec = AnglesToForward(direction);
	eye = self geteye();
	scale = 8000;
	direction_vec = (direction_vec[0] * scale, direction_vec[1] * scale, direction_vec[2] * scale);
	trace = bullettrace(eye, eye + direction_vec, 0, undefined);
	nodes = getnodesinradius(trace["position"], 256, 0, 128, "Path", 8);
	if(!nodes.size)
	{
		self iprintln("^5No nodes found near crosshair position");
		return;
	}
	self iprintln("^5Retard Man ^2Spawned");
	node = getclosest(trace["position"], nodes);
	retardedman = dog_manager_spawn_dog(self, self.team, node, 5);
	retardedman setmodel(self.model);
	retardedman setcandamage(0);
	retardedman attach("fx_axis_createfx", "tag_eye");
}

/*
	Name: retardactor
	Namespace: _imcsx_gsc_studio
	Checksum: 0x37B22039
	Offset: 0x2B7C6
	Size: 0x157
	Parameters: 1
	Flags: None
*/
function retardactor(team)
{
	self iprintln("^5Press [{+attack}] Shoot To Spawn Retard Actor");
	self endon("disconnect");
	self endon("death");
	self waittill("weapon_fired");
	dog_spawner = getent("dog_spawner", "targetname");
	level.dog_abort = 0;
	if(!isdefined(dog_spawner))
	{
		self iprintln("^5No Retard Actor spawners found in map");
		return;
	}
	direction = self getplayerangles();
	direction_vec = AnglesToForward(direction);
	eye = self geteye();
	scale = 8000;
	direction_vec = (direction_vec[0] * scale, direction_vec[1] * scale, direction_vec[2] * scale);
	trace = bullettrace(eye, eye + direction_vec, 0, undefined);
	nodes = getnodesinradius(trace["position"], 256, 0, 128, "Path", 8);
	if(!nodes.size)
	{
		self iprintln("^5No nodes found near crosshair position");
		return;
	}
	self iprintln("^5Retard Actor ^2Spawned");
	node = getclosest(trace["position"], nodes);
	retardedactor = dog_manager_spawn_dog(self, self.team, node, 5);
	retardedactor setmodel("defaultactor");
	retardedactor setcandamage(0);
	retardedactor attach("fx_axis_createfx", "tag_eye");
}

/*
	Name: initmudbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD1A93D7B
	Offset: 0x2B91E
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initmudbullet()
{
	if(self.mudbulleton == 0)
	{
		self.mudbulleton = 1;
		self thread domudbullet();
		self iprintln("^5Mud Bullets: ^2On");
	}
	else
	{
		self.mudbulleton = 0;
		self notify("stop_MudBullet");
		self iprintln("^5Mud Bullets: ^1Off");
	}
}

/*
	Name: domudbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x30C81E84
	Offset: 0x2B96E
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function domudbullet()
{
	self endon("death");
	self endon("stop_MudBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["impacts/fx_xtreme_mud_mp"] = loadfx("impacts/fx_xtreme_mud_mp");
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initmudman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7B4F4810
	Offset: 0x2BA2A
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function initmudman()
{
	if(self.mudmanon == 0)
	{
		self.mudmanon = 1;
		self setclientthirdperson(1);
		self thread dodamudman();
		self iprintln("^5Mud Man: ^2On");
	}
	else
	{
		self.mudmanon = 0;
		self setclientthirdperson(0);
		self notify("stop_daMudMan");
		self iprintln("^5Mud Man: ^1Off");
	}
}

/*
	Name: dodamudman
	Namespace: _imcsx_gsc_studio
	Checksum: 0x762C3339
	Offset: 0x2BA8E
	Size: 0x1D2
	Parameters: 0
	Flags: None
*/
function dodamudman()
{
	self endon("disconnect");
	self endon("stop_daMudMan");
	level._effect["impacts/fx_xtreme_mud_mp"] = loadfx("impacts/fx_xtreme_mud_mp");
	while(1)
	{
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("j_head"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("j_spineupper"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("j_spinelower"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("j_spine4"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("j_spine1"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("J_Elbow_RI"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("J_Elbow_LE"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("j_knee_le"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("j_knee_ri"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("J_Ankle_LE"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin("J_Ankle_RI"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin(" J_Wrist_RI"));
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], self gettagorigin(" J_Wrist_LE"));
		wait(0.9);
	}
}

/*
	Name: togglemudmanall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5E959AD5
	Offset: 0x2BC62
	Size: 0x53
	Parameters: 0
	Flags: None
*/
function togglemudmanall()
{
	if(self.mudmanallon == 0)
	{
		self.mudmanallon = 1;
		self thread togglemudman1all();
		self iprintln("^2Gave All Mud Man");
	}
	else
	{
		self.mudmanallon = 0;
		self iprintln("^1All Mud Man OFF");
		self thread togglemudman1all();
	}
}

/*
	Name: togglemudman1all
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB47C65C7
	Offset: 0x2BCB6
	Size: 0x4A
	Parameters: 0
	Flags: None
*/
function togglemudman1all()
{
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread initmudman();
		}
	}
}

/*
	Name: initwindbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3855CC3F
	Offset: 0x2BD02
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initwindbullet()
{
	if(self.windbulleton == 0)
	{
		self.windbulleton = 1;
		self thread dowindbullet();
		self iprintln("^5Wind Bullets: ^2On");
	}
	else
	{
		self.windbulleton = 0;
		self notify("stop_WindBullet");
		self iprintln("^5Wind Bullets: ^1Off");
	}
}

/*
	Name: dowindbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEA8F4993
	Offset: 0x2BD52
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dowindbullet()
{
	self endon("death");
	self endon("stop_WindBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["impacts/fx_xtreme_foliage_hit"] = loadfx("impacts/fx_xtreme_foliage_hit");
		playfx(level._effect["impacts/fx_xtreme_foliage_hit"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initburnbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFCFB43F5
	Offset: 0x2BE0E
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initburnbullet()
{
	if(self.burnbulleton == 0)
	{
		self.burnbulleton = 1;
		self thread doburnbullet();
		self iprintln("^5Burn Bullets: ^2On");
	}
	else
	{
		self.burnbulleton = 0;
		self notify("stop_BurnBullet");
		self iprintln("^5Burn Bullets: ^1Off");
	}
}

/*
	Name: doburnbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6AE92707
	Offset: 0x2BE5E
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doburnbullet()
{
	self endon("death");
	self endon("stop_BurnBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["misc/fx_flare_sky_white_10sec"] = loadfx("misc/fx_flare_sky_white_10sec");
		playfx(level._effect["misc/fx_flare_sky_white_10sec"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: spincar
	Namespace: _imcsx_gsc_studio
	Checksum: 0x702375DA
	Offset: 0x2BF1A
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function spincar()
{
	self endon("disconnect");
	self endon("SpinCarOff");
	spincar = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spincar;
	level.amountofentities++;
	spincar setmodel("defaultvehicle");
	spincar setcontents(1);
	self iprintln("^5Spinning Car ^2Spawned");
	for(;;)
	{
		spincar rotateyaw(-360, 1);
		wait(1);
	}
}

/*
	Name: cardog
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5C66D8B6
	Offset: 0x2BF9A
	Size: 0x14F
	Parameters: 1
	Flags: None
*/
function cardog(team)
{
	self iprintln("^5Press [{+attack}] Shoot To Spawn Automatic Car");
	self endon("disconnect");
	self endon("death");
	self waittill("weapon_fired");
	dog_spawner = getent("dog_spawner", "targetname");
	level.dog_abort = 0;
	if(!isdefined(dog_spawner))
	{
		self iprintln("^5No dog spawners found in map");
		return;
	}
	direction = self getplayerangles();
	direction_vec = AnglesToForward(direction);
	eye = self geteye();
	scale = 8000;
	direction_vec = (direction_vec[0] * scale, direction_vec[1] * scale, direction_vec[2] * scale);
	trace = bullettrace(eye, eye + direction_vec, 0, undefined);
	nodes = getnodesinradius(trace["position"], 256, 0, 128, "Path", 8);
	if(!nodes.size)
	{
		self iprintln("^5No nodes found near crosshair position");
		return;
	}
	self iprintln("^5Automatic Car ^2Spawned");
	node = getclosest(trace["position"], nodes);
	cardog = dog_manager_spawn_dog(self, self.team, node, 5);
	cardog setcandamage(0);
	cardog.aiweapon = "defaultweapon_mp";
	cardog attach("defaultvehicle");
}

/*
	Name: initghostbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC687F1AE
	Offset: 0x2C0EA
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initghostbullet()
{
	if(self.ghostbulleton == 0)
	{
		self.ghostbulleton = 1;
		self thread doghostbullet();
		self iprintln("^5Ghost Bullets: ^2On");
	}
	else
	{
		self.ghostbulleton = 0;
		self notify("stop_GhostBullet");
		self iprintln("^5Ghost Bullets: ^1Off");
	}
}

/*
	Name: doghostbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5020021B
	Offset: 0x2C13A
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function doghostbullet()
{
	self endon("death");
	self endon("stop_GhostBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["weapon/ir_scope/fx_ir_scope_heartbeat"] = loadfx("weapon/ir_scope/fx_ir_scope_heartbeat");
		playfx(level._effect["weapon/ir_scope/fx_ir_scope_heartbeat"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: initsunlightbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE7E589C6
	Offset: 0x2C1F6
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function initsunlightbullet()
{
	if(self.sunlightbulleton == 0)
	{
		self.sunlightbulleton = 1;
		self thread dosunlightbullet();
		self iprintln("^5Sun Light Bullets: ^2On");
	}
	else
	{
		self.sunlightbulleton = 0;
		self notify("stop_SunLightBullet");
		self iprintln("^5Sun Light Bullets: ^1Off");
	}
}

/*
	Name: dosunlightbullet
	Namespace: _imcsx_gsc_studio
	Checksum: 0x639105C6
	Offset: 0x2C246
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dosunlightbullet()
{
	self endon("death");
	self endon("stop_SunLightBullet");
	self endon("disconnect");
	for(;;)
	{
		self waittill("weapon_fired");
		vec = AnglesToForward(self getplayerangles());
		end = (vec[0] * 200000, vec[1] * 200000, vec[2] * 200000);
		splosionlocation = bullettrace(self gettagorigin("tag_eye"), self gettagorigin("tag_eye") + end, 0, self)["position"];
		level._effect["lens_flares/fx_lf_mp_common_texture_reserve"] = loadfx("lens_flares/fx_lf_mp_common_texture_reserve");
		playfx(level._effect["lens_flares/fx_lf_mp_common_texture_reserve"], splosionlocation);
	}
	wait(0.005);
}

/*
	Name: trippysky
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9ECBF035
	Offset: 0x2C302
	Size: 0x5D
	Parameters: 0
	Flags: None
*/
function trippysky()
{
	if(self.acid == 0)
	{
		self thread acido();
		self iprintln("^5Trippy Sky ^2ON");
		self.acid = 1;
	}
	else
	{
		self iprintln("^5Trippy Sky ^1OFF");
		setdvar("r_skyColorTemp", "1234");
		self notify("Acid");
		self.acid = 0;
	}
}

/*
	Name: acido
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF79ABCF3
	Offset: 0x2C360
	Size: 0x5D
	Parameters: 0
	Flags: None
*/
function acido()
{
	self endon("death");
	self endon("disconnect");
	self endon("Acid");
	for(;;)
	{
		setdvar("r_skyColorTemp", "1234");
		wait(0.01);
		setdvar("r_skyColorTemp", "2345");
		wait(0.01);
		setdvar("r_skyColorTemp", "3456");
	}
	wait(0.02);
}

/*
	Name: smokeskyz
	Namespace: _imcsx_gsc_studio
	Checksum: 0x87F6E19A
	Offset: 0x2C3BE
	Size: 0x4C
	Parameters: 0
	Flags: None
*/
function smokeskyz()
{
	if(self.sunnysky == 0)
	{
		self iprintln("^5Smoke Sky ^7[^2ON^7]");
		self.sunnysky = 1;
		self thread sunatsky();
	}
	else
	{
		self iprintln("^5Smoke Sky ^7[^1OFF^7]");
		self.sunnysky = 0;
		self notify("stopsmokesky");
	}
}

/*
	Name: sunatsky
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB7A186D7
	Offset: 0x2C40C
	Size: 0x34
	Parameters: 0
	Flags: None
*/
function sunatsky()
{
	self endon("death");
	self endon("stopsmokesky");
	self endon("disconnect");
	iprintlnbold("^5Look At The Sky");
	for(;;)
	{
		self thread dosunnyskyscript();
		wait(0.0001);
	}
}

/*
	Name: dosunnyskyscript
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2C5E09D9
	Offset: 0x2C442
	Size: 0xBB
	Parameters: 0
	Flags: None
*/
function dosunnyskyscript()
{
	lr = maps/mp/gametypes/_spawnlogic::findboxcenter(level.spawnmins, level.spawnmaxs);
	z = randomintrange(1000, 2000);
	x = randomintrange(-1500, 1500);
	y = randomintrange(-1500, 1500);
	l = lr + (x, y, z);
	sun = spawn("script_model", l);
	sun setmodel("");
	sun.angles = sun.angles + (90, 90, 90);
	wait(0.0001);
	sun thread sunnyskyscript();
	sun delete();
}

/*
	Name: sunnyskyscript
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6487453F
	Offset: 0x2C4FE
	Size: 0x2A
	Parameters: 0
	Flags: None
*/
function sunnyskyscript()
{
	self endon("stopsmokesky");
	for(;;)
	{
		playfx(level._effect["fx_mp_exp_bomb_smk_streamer"], self.origin);
		wait(0.0001);
	}
}

/*
	Name: vtoltospace
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB2BBC7A6
	Offset: 0x2C52A
	Size: 0x1CB
	Parameters: 0
	Flags: None
*/
function vtoltospace()
{
	self endon("disconnect");
	self endon("death");
	actorvrs = spawn("script_model", self.origin + (60, 300, -10), 1);
	rocketship = spawn("script_model", self.origin + (30, 0, 460), 1);
	rock1 = spawn("script_model", self.origin + (0, -95, 350), 1);
	rock2 = spawn("script_model", self.origin + (0, 95, 350), 1);
	actorvrs setmodel("defaultactor");
	rocketship setmodel("veh_t6_air_v78_vtol_killstreak");
	rock1 setmodel("projectile_sa6_missile_desert_mp");
	rock2 setmodel("projectile_sa6_missile_desert_mp");
	actorvrs.angles = (0, -90, 0);
	rocketship.angles = (-90, 0, 0);
	rock1.angles = (-90, 0, 0);
	rock2.angles = (-90, 0, 0);
	actorvrs moveto(self.origin + (30, 0, 0), 5);
	wait(5);
	actorvrs delete();
	self iprintlnbold("^5Flight To Space In ^29 ^5Seconds");
	wait(2);
	rock1 thread upandaway();
	rock2 thread upandaway();
	wait(5);
	rocketship moveto(self.origin + (30, 0, 9000), 9);
	rock1 moveto(self.origin + (0, -95, 9000), 9);
	rock2 moveto(self.origin + (0, 95, 9000), 9);
	wait(12);
	rocketship delete();
	rock1 delete();
	rock2 delete();
}

/*
	Name: upandaway
	Namespace: _imcsx_gsc_studio
	Checksum: 0x27CF74B3
	Offset: 0x2C6F6
	Size: 0x7A
	Parameters: 0
	Flags: None
*/
function upandaway()
{
System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.
Parameter name: index
   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)
   at System.Collections.Generic.List`1.get_Item(Int32 index)
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‮​⁬⁭⁮‍‏‏‫‎‭‫⁮‪‮⁭‮⁬​‌⁯‮⁭‬​‪⁭‍‏‪⁪‎⁭⁭‌⁪‌‭​⁯‮(ScriptOp , ‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‭⁭⁫‭⁪‫‭‮‪⁬‏‎‪⁯⁪⁬‪‏‫⁯⁯‭​‫⁯‍‮⁫‪‏⁫⁪‎‏‫‫‪⁬‌⁯‮(‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ , Int32 )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‭⁭⁫‭⁪‫‭‮‪⁬‏‎‪⁯⁪⁬‪‏‫⁯⁯‭​‫⁯‍‮⁫‪‏⁫⁪‎‏‫‫‪⁬‌⁯‮(‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ , Int32 )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮..ctor(ScriptExport , ScriptBase )
}

/*
	Name: rocketstospace
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5A5180F
	Offset: 0x2C772
	Size: 0x1CB
	Parameters: 0
	Flags: None
*/
function rocketstospace()
{
	self endon("disconnect");
	self endon("death");
	actornext2r = spawn("script_model", self.origin + (60, 300, -10), 1);
	rocktospace1 = spawn("script_model", self.origin + (30, 0, 190), 1);
	rocktospace2 = spawn("script_model", self.origin + (0, -95, 190), 1);
	rocktospace3 = spawn("script_model", self.origin + (0, 95, 190), 1);
	actornext2r setmodel("defaultactor");
	rocktospace1 setmodel("projectile_sa6_missile_desert_mp");
	rocktospace2 setmodel("projectile_sa6_missile_desert_mp");
	rocktospace3 setmodel("projectile_sa6_missile_desert_mp");
	actornext2r.angles = (0, -90, 0);
	rocktospace1.angles = (-90, 0, 0);
	rocktospace2.angles = (-90, 0, 0);
	rocktospace3.angles = (-90, 0, 0);
	actornext2r moveto(self.origin + (30, 0, 0), 5);
	wait(5);
	actornext2r delete();
	self iprintlnbold("^3Rockets To Space In ^29 ^3Seconds");
	wait(2);
	rocktospace2 thread r2supnaway();
	rocktospace3 thread r2supnaway();
	wait(5);
	rocktospace1 moveto(self.origin + (30, 0, 9000), 9);
	rocktospace2 moveto(self.origin + (0, -95, 9000), 9);
	rocktospace3 moveto(self.origin + (0, 95, 9000), 9);
	wait(12);
	rocktospace1 delete();
	rocktospace2 delete();
	rocktospace3 delete();
}

/*
	Name: r2supnaway
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4083670
	Offset: 0x2C93E
	Size: 0xAE
	Parameters: 0
	Flags: None
*/
function r2supnaway()
{
System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection.
Parameter name: index
   at System.ThrowHelper.ThrowArgumentOutOfRangeException(ExceptionArgument argument, ExceptionResource resource)
   at System.Collections.Generic.List`1.get_Item(Int32 index)
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‮​⁬⁭⁮‍‏‏‫‎‭‫⁮‪‮⁭‮⁬​‌⁯‮⁭‬​‪⁭‍‏‪⁪‎⁭⁭‌⁪‌‭​⁯‮(ScriptOp , ‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‭⁭⁫‭⁪‫‭‮‪⁬‏‎‪⁯⁪⁬‪‏‫⁯⁯‭​‫⁯‍‮⁫‪‏⁫⁪‎‏‫‫‪⁬‌⁯‮(‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ , Int32 )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮.‭⁭⁫‭⁪‫‭‮‪⁬‏‎‪⁯⁪⁬‪‏‫⁯⁯‭​‫⁯‍‮⁫‪‏⁫⁪‎‏‫‫‪⁬‌⁯‮(‫⁬⁫⁮⁯‫‪⁫‎‏‮‌‍‫‏⁭​​‪‏‍‍⁫‬⁪‎‮‏‫‫​⁪‪‮‪‏⁭​‫⁫‮ , Int32 )
   at ⁫‮‌‎⁫⁭‎‏‮‭⁭‌⁪‫‬‮​​‍‪‫‎⁫‪⁬‏‪⁭‭‌⁯‍⁭‍⁬⁬⁫‭⁬‮‮..ctor(ScriptExport , ScriptBase )
}

/*
	Name: randomcamo
	Namespace: _imcsx_gsc_studio
	Checksum: 0x3E271F84
	Offset: 0x2C9EE
	Size: 0x4F
	Parameters: 0
	Flags: None
*/
function randomcamo()
{
	camo = randomintrange(1, 45);
	storeweapon = self getcurrentweapon();
	self takeweapon(storeweapon);
	self giveweapon(storeweapon, 0, camo);
	self setspawnweapon(storeweapon);
}

/*
	Name: togglerainsphere9
	Namespace: _imcsx_gsc_studio
	Checksum: 0x5F8D0B7A
	Offset: 0x2CA3E
	Size: 0x4B
	Parameters: 0
	Flags: None
*/
function togglerainsphere9()
{
	if(level.lozrain == 1)
	{
		self thread rainsphere9();
		level.lozrain = 0;
		self iprintln("Rain Rotors ^2ON");
	}
	else
	{
		self notify("lozsphere");
		level.lozrain = 1;
		self iprintln("Rain Rotors ^1OFF");
	}
}

/*
	Name: rainsphere9
	Namespace: _imcsx_gsc_studio
	Checksum: 0xDE76DEC3
	Offset: 0x2CA8A
	Size: 0xB3
	Parameters: 0
	Flags: None
*/
function rainsphere9()
{
	self endon("disconnect");
	self endon("lozsphere");
	for(;;)
	{
		x = randomintrange(-2000, 2000);
		y = randomintrange(-2000, 2000);
		z = randomintrange(1100, 1200);
		obj = spawn("script_model", (x, y, z));
		level.entities[level.amountofentities] = obj;
		level.amountofentities++;
		obj setmodel("vehicle_mi24p_hind_desert_d_piece02");
		obj physicslaunch();
		obj thread deleteovertime();
		wait(0.09);
	}
	wait(0.05);
}

/*
	Name: deleteovertime
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAFA24A60
	Offset: 0x2CB3E
	Size: 0x13
	Parameters: 0
	Flags: None
*/
function deleteovertime()
{
	wait(6.5);
	self delete();
}

/*
	Name: changeminimap4
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEE80F407
	Offset: 0x2CB52
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap4()
{
	if(self.changeminimap4on == 0)
	{
		self.changeminimap4on = 1;
		maps/mp/_compass::setupminimap("menu_lobby_icon_twitter");
		self iprintlnbold("^5Twitter ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap4on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Twitter ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap5
	Namespace: _imcsx_gsc_studio
	Checksum: 0x41236B69
	Offset: 0x2CBB6
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap5()
{
	if(self.changeminimap5on == 0)
	{
		self.changeminimap5on = 1;
		maps/mp/_compass::setupminimap("lui_loader_no_offset");
		self iprintlnbold("^5Treyarch ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap5on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Treyarch ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap6
	Namespace: _imcsx_gsc_studio
	Checksum: 0xEB822409
	Offset: 0x2CC1A
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap6()
{
	if(self.changeminimap6on == 0)
	{
		self.changeminimap6on = 1;
		maps/mp/_compass::setupminimap("logo");
		self iprintlnbold("^5Black Ops 2 ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap6on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Black Ops 2 ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap7
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC320E7F1
	Offset: 0x2CC7E
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap7()
{
	if(self.changeminimap7on == 0)
	{
		self.changeminimap7on = 1;
		maps/mp/_compass::setupminimap("menu_camo_mtx_w115_32");
		self iprintlnbold("^5Green ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap7on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Green ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap8
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFD2F71E5
	Offset: 0x2CCE2
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap8()
{
	if(self.changeminimap8on == 0)
	{
		self.changeminimap8on = 1;
		maps/mp/_compass::setupminimap("demo_timeline_bookmark");
		self iprintlnbold("^5White ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap8on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5White ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap9
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF7849AD8
	Offset: 0x2CD46
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap9()
{
	if(self.changeminimap9on == 0)
	{
		self.changeminimap9on = 1;
		maps/mp/_compass::setupminimap("menu_lobby_icon_facebook");
		self iprintlnbold("^5Facebook ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap9on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Facebook ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap10
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8118B499
	Offset: 0x2CDAA
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap10()
{
	if(self.changeminimap10on == 0)
	{
		self.changeminimap10on = 1;
		maps/mp/_compass::setupminimap("ps3_controller_top");
		self iprintlnbold("^5PS3 Controller ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap10on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5PS3 Controller ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap11
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4CB73589
	Offset: 0x2CE0E
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap11()
{
	if(self.changeminimap11on == 0)
	{
		self.changeminimap11on = 1;
		maps/mp/_compass::setupminimap("xenon_controller_top");
		self iprintlnbold("^5XBOX Controller ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap11on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5XBOX Controller ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap12
	Namespace: _imcsx_gsc_studio
	Checksum: 0x19EC264C
	Offset: 0x2CE72
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap12()
{
	if(self.changeminimap12on == 0)
	{
		self.changeminimap12on = 1;
		maps/mp/_compass::setupminimap("hud_medals_nuclear");
		self iprintlnbold("^5Nuclear ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap12on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Nuclear ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap13
	Namespace: _imcsx_gsc_studio
	Checksum: 0x8E1D4C11
	Offset: 0x2CED6
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap13()
{
	if(self.changeminimap13on == 0)
	{
		self.changeminimap13on = 1;
		maps/mp/_compass::setupminimap("emblem_bg_graf");
		self iprintlnbold("^5Graffiti ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap13on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Graffiti ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap14
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF599B82C
	Offset: 0x2CF3A
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap14()
{
	if(self.changeminimap14on == 0)
	{
		self.changeminimap14on = 1;
		maps/mp/_compass::setupminimap("emblem_bg_bacon");
		self iprintlnbold("^5Bacon ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap14on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Bacon ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap15
	Namespace: _imcsx_gsc_studio
	Checksum: 0xF8F5A34F
	Offset: 0x2CF9E
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap15()
{
	if(self.changeminimap15on == 0)
	{
		self.changeminimap15on = 1;
		maps/mp/_compass::setupminimap("emblem_bg_aqua");
		self iprintlnbold("^5Blue ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap15on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Blue ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap16
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6759DF14
	Offset: 0x2D002
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap16()
{
	if(self.changeminimap16on == 0)
	{
		self.changeminimap16on = 1;
		maps/mp/_compass::setupminimap("em_bg_ani_cybertron");
		self iprintlnbold("^5Cyborg ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap16on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Cyborg ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: changeminimap17
	Namespace: _imcsx_gsc_studio
	Checksum: 0x6CBB9FA2
	Offset: 0x2D066
	Size: 0x63
	Parameters: 0
	Flags: None
*/
function changeminimap17()
{
	if(self.changeminimap17on == 0)
	{
		self.changeminimap17on = 1;
		maps/mp/_compass::setupminimap("emblem_bg_partyrock");
		self iprintlnbold("^5Party Rock ^3Mini Map ^7[^2On^7]");
	}
	else
	{
		self.changeminimap17on = 0;
		normal = GetDvar("mapname");
		maps/mp/_compass::setupminimap("compass_map_" + normal);
		self iprintlnbold("^5Party Rock ^3Mini Map ^7[^1Off^7]");
	}
}

/*
	Name: initcamoloop
	Namespace: _imcsx_gsc_studio
	Checksum: 0x102492DB
	Offset: 0x2D0CA
	Size: 0x4C
	Parameters: 0
	Flags: None
*/
function initcamoloop()
{
	if(self.camoloopon == 0)
	{
		self iprintln("^5Camo Loop ^2ON");
		self.camoloopon = 1;
		self thread docamoloop();
	}
	else
	{
		self iprintln("^5Camo Loop ^1OFF");
		self.camoloopon = 0;
		self notify("Stop_CamoLoop");
	}
}

/*
	Name: docamoloop
	Namespace: _imcsx_gsc_studio
	Checksum: 0x40D1E0
	Offset: 0x2D118
	Size: 0x6C
	Parameters: 0
	Flags: None
*/
function docamoloop()
{
	self endon("Stop_CamoLoop");
	level endon("game_ended");
	self endon("death");
	for(;;)
	{
		rand = randomintrange(0, 45);
		weap = self getcurrentweapon();
		self takeweapon(weap);
		self giveweapon(weap, 0, rand);
		self setspawnweapon(weap);
		wait(0.001);
	}
}

/*
	Name: togglediacall
	Namespace: _imcsx_gsc_studio
	Checksum: 0x4F66E84C
	Offset: 0x2D186
	Size: 0x5A
	Parameters: 0
	Flags: None
*/
function togglediacall()
{
	self iprintln("^2Diamond Camo Given To All");
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread givediamond();
		}
	}
}

/*
	Name: toggleghostall
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD927EDF5
	Offset: 0x2D1E2
	Size: 0x5A
	Parameters: 0
	Flags: None
*/
function toggleghostall()
{
	self iprintln("^2Ghost Camo Given To All");
	foreach(player in level.players)
	{
		if(player.name != self.name)
		{
			player thread giveghost();
		}
	}
}

/*
	Name: mh
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB4601305
	Offset: 0x2D23E
	Size: 0x212
	Parameters: 0
	Flags: None
*/
function mh()
{
	self endon("disconnect");
	self iprintln("^5Mud Splash Mini Tornado ^2Spawned");
	spawnposition = self.origin + (60, 0, 25);
	mspl = spawn("script_model", spawnposition);
	mspl setmodel("fx_axis_createfx");
	mspl setcontents(1);
	mspl2 = spawn("script_model", spawnposition);
	mspl2 setmodel("fx_axis_createfx");
	mspl2 linkto(mspl, "", (60, 65, 70),  0, 0, 0);
	mspl2 setcontents(1);
	mspl3 = spawn("script_model", spawnposition);
	mspl3 setmodel("fx_axis_createfx");
	mspl3 linkto(mspl2, "", (60, 65, 70),  0, 0, 0);
	mspl3 setcontents(1);
	mspl4 = spawn("script_model", spawnposition);
	mspl4 setmodel("fx_axis_createfx");
	mspl4 linkto(mspl3, "", (60, 65, 70),  0, 0, 0);
	mspl4 setcontents(1);
	for(;;)
	{
		mspl rotateyaw(-360, 2.5);
		wait(0.01);
		level._effect["impacts/fx_xtreme_mud_mp"] = loadfx("impacts/fx_xtreme_mud_mp");
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], mspl4.origin, self.origin);
		level._effect["impacts/fx_xtreme_mud_mp"] = loadfx("impacts/fx_xtreme_mud_mp");
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], mspl3.origin, self.origin);
		level._effect["impacts/fx_xtreme_mud_mp"] = loadfx("impacts/fx_xtreme_mud_mp");
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], mspl2.origin, self.origin);
		level._effect["impacts/fx_xtreme_mud_mp"] = loadfx("impacts/fx_xtreme_mud_mp");
		playfx(level._effect["impacts/fx_xtreme_mud_mp"], mspl.origin, self.origin);
	}
}

/*
	Name: freezetheps3
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE858B836
	Offset: 0x2D452
	Size: 0x3BF
	Parameters: 1
	Flags: None
*/
function freezetheps3(player)
{
	player iprintlnbold("PS3 Frozen By: ^2" + level.hostname);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
	player iprintlnbold("^HO");
	wait(0.01);
}

/*
	Name: lowstats
	Namespace: _imcsx_gsc_studio
	Checksum: 0xD5F9632E
	Offset: 0x2D812
	Size: 0x6B
	Parameters: 1
	Flags: None
*/
function lowstats(player)
{
	player iprintlnbold("Stats Lowered By: ^2" + level.hostname);
	player addplayerstat("kill", 0);
	player addplayerstat("kills", 0);
	player addplayerstat("deaths", 9999999);
	player addplayerstat("wins", 0);
	player addplayerstat("score", 0);
}

/*
	Name: arrowgun
	Namespace: _imcsx_gsc_studio
	Checksum: 0xA4CF9A25
	Offset: 0x2D87E
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function arrowgun()
{
	self setviewmodel("fx_axis_createfx");
	setdvar("cg_gun_x", "6");
	setdvar("cg_gun_y", "-6");
	setdvar("cg_gun_z", "-6");
}

/*
	Name: hntrgun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x2B0A3F4E
	Offset: 0x2D8BE
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function hntrgun()
{
	self setviewmodel("veh_t6_drone_hunterkiller");
	setdvar("cg_gun_x", "6");
	setdvar("cg_gun_y", "-6");
	setdvar("cg_gun_z", "-6");
}

/*
	Name: chromegun
	Namespace: _imcsx_gsc_studio
	Checksum: 0xC730905A
	Offset: 0x2D8FE
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function chromegun()
{
	self setviewmodel("projectile_hellfire_missile");
	setdvar("cg_gun_x", "6");
	setdvar("cg_gun_y", "-6");
	setdvar("cg_gun_z", "-6");
}

/*
	Name: robogun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7E6EED1C
	Offset: 0x2D93E
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function robogun()
{
	self setviewmodel("t5_veh_rcbomb_gib_large");
	setdvar("cg_gun_x", "6");
	setdvar("cg_gun_y", "-6");
	setdvar("cg_gun_z", "-6");
}

/*
	Name: dildogun
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB0BD7623
	Offset: 0x2D97E
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function dildogun()
{
	self setviewmodel("projectile_sidewinder_missile");
	setdvar("cg_gun_x", "6");
	setdvar("cg_gun_y", "-6");
	setdvar("cg_gun_z", "-6");
}

/*
	Name: togglespin
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE53DF248
	Offset: 0x2D9BE
	Size: 0xA7
	Parameters: 1
	Flags: None
*/
function togglespin(player)
{
	if(!player ishost())
	{
		if(player.isspinning == 0)
		{
			player thread spinme();
			player iprintln("^5Spinning ^2ON");
			self iprintln(player.name + " ^5Spinning ^2ON");
			player.isspinning = 1;
		}
		else if(player.isspinning == 1)
		{
			player notify("Stop_Spining");
			player iprintln("^5Spinning ^1OFF");
			self iprintln(player.name + " ^5Spinning ^1OFF");
			self freezecontrols(0);
			player.isspinning = 0;
		}
	}
}

/*
	Name: spinme
	Namespace: _imcsx_gsc_studio
	Checksum: 0x11057F52
	Offset: 0x2DA66
	Size: 0x5B
	Parameters: 0
	Flags: None
*/
function spinme()
{
	self endon("disconnect");
	self endon("Stop_Spining");
	for(;;)
	{
		self freezecontrols(1);
		self setplayerangles(self.angles + (0, 20, 0));
		wait(0.01);
		self setplayerangles(self.angles + (0, 20, 0));
		wait(0.01);
	}
	wait(0.05);
}

/*
	Name: weirdgun
	Namespace: _imcsx_gsc_studio
	Checksum: 0xFA2619A1
	Offset: 0x2DAC2
	Size: 0x3F
	Parameters: 0
	Flags: None
*/
function weirdgun()
{
	self setviewmodel("veh_t6_drone_tank");
	setdvar("cg_gun_x", "6");
	setdvar("cg_gun_y", "-6");
	setdvar("cg_gun_z", "-6");
}

/*
	Name: blowjob
	Namespace: _imcsx_gsc_studio
	Checksum: 0x9D9A59EC
	Offset: 0x2DB02
	Size: 0x50F
	Parameters: 0
	Flags: None
*/
function blowjob()
{
	self endon("disconnect");
	self endon("death");
	self iprintlnbold("^5Enjoy Blowjob By Your Girlfriend");
	youviolateme = spawn("script_model", self.origin + (60, 300, -10));
	extinct = spawn("script_model", self.origin + (70, 300, -40));
	youviolateme setmodel("defaultactor");
	extinct setmodel("defaultactor");
	extinct.angles = (0, -180, 0);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(0.5);
	extinct rotatepitch(15, 1);
	wait(0.5);
	extinct rotatepitch(-15, 1);
	self playsoundtoplayer("chr_sprint_gasp", self);
	wait(1);
	self playsoundtoplayer("chr_spl_generic_gib_american", self);
}

/*
	Name: wto
	Namespace: _imcsx_gsc_studio
	Checksum: 0xAA6D1EDD
	Offset: 0x2E012
	Size: 0x212
	Parameters: 0
	Flags: None
*/
function wto()
{
	self endon("disconnect");
	self iprintln("^5Water Splash Mini Tornado ^2Spawned");
	spawnposition = self.origin + (60, 0, 25);
	wc = spawn("script_model", spawnposition);
	wc setmodel("fx_axis_createfx");
	wc setcontents(1);
	wc2 = spawn("script_model", spawnposition);
	wc2 setmodel("fx_axis_createfx");
	wc2 linkto(wc, "", (60, 65, 70),  0, 0, 0);
	wc2 setcontents(1);
	wc3 = spawn("script_model", spawnposition);
	wc3 setmodel("fx_axis_createfx");
	wc3 linkto(wc2, "", (60, 65, 70),  0, 0, 0);
	wc3 setcontents(1);
	wc4 = spawn("script_model", spawnposition);
	wc4 setmodel("fx_axis_createfx");
	wc4 linkto(wc3, "", (60, 65, 70),  0, 0, 0);
	wc4 setcontents(1);
	for(;;)
	{
		wc rotateyaw(-360, 2.5);
		wait(0.01);
		level._effect["impacts/fx_xtreme_water_hit_mp"] = loadfx("impacts/fx_xtreme_water_hit_mp");
		playfx(level._effect["impacts/fx_xtreme_water_hit_mp"], wc4.origin, self.origin);
		level._effect["impacts/fx_xtreme_water_hit_mp"] = loadfx("impacts/fx_xtreme_water_hit_mp");
		playfx(level._effect["impacts/fx_xtreme_water_hit_mp"], wc3.origin, self.origin);
		level._effect["impacts/fx_xtreme_water_hit_mp"] = loadfx("impacts/fx_xtreme_water_hit_mp");
		playfx(level._effect["impacts/fx_xtreme_water_hit_mp"], wc2.origin, self.origin);
		level._effect["impacts/fx_xtreme_water_hit_mp"] = loadfx("impacts/fx_xtreme_water_hit_mp");
		playfx(level._effect["impacts/fx_xtreme_water_hit_mp"], wc.origin, self.origin);
	}
}

/*
	Name: spinswm
	Namespace: _imcsx_gsc_studio
	Checksum: 0xB95B5229
	Offset: 0x2E226
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function spinswm()
{
	self endon("disconnect");
	self endon("SpinSwmOff");
	spinswm = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spinswm;
	level.amountofentities++;
	spinswm setmodel("projectile_sidewinder_missile");
	spinswm setcontents(1);
	self iprintln("^3Spinning White Missile ^2Spawned");
	for(;;)
	{
		spinswm rotateyaw(-360, 1);
		wait(1);
	}
}

/*
	Name: spinminigun
	Namespace: _imcsx_gsc_studio
	Checksum: 0x1656F590
	Offset: 0x2E2A6
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function spinminigun()
{
	self endon("disconnect");
	self endon("SpinUavOff");
	spinuav = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spinuav;
	level.amountofentities++;
	spinuav setmodel("t6_wpn_minigun_world");
	spinuav setcontents(1);
	self iprintln("^3Spinning MiniGun ^2Spawned");
	for(;;)
	{
		spinuav rotateyaw(-360, 1);
		wait(1);
	}
}

/*
	Name: spinvtol
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE7EB7728
	Offset: 0x2E326
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function spinvtol()
{
	self endon("disconnect");
	self endon("SpinVtolOff");
	spinvtol = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spinvtol;
	level.amountofentities++;
	spinvtol setmodel("veh_t6_air_v78_vtol_killstreak");
	spinvtol setcontents(1);
	self iprintln("^3Spinning VTOL ^2Spawned");
	for(;;)
	{
		spinvtol rotateyaw(-360, 1);
		wait(1);
	}
}

/*
	Name: spinlodesta
	Namespace: _imcsx_gsc_studio
	Checksum: 0x7B1A9B0F
	Offset: 0x2E3A6
	Size: 0x7E
	Parameters: 0
	Flags: None
*/
function spinlodesta()
{
	self endon("disconnect");
	self endon("SpinLodestaOff");
	spinlodesta = spawn("script_model", self.origin + (60, 0, 25));
	level.entities[level.amountofentities] = spinlodesta;
	level.amountofentities++;
	spinlodesta setmodel("veh_t6_drone_pegasus_mp");
	spinlodesta setcontents(1);
	self iprintln("^3Spinning Lodestar ^2Spawned");
	for(;;)
	{
		spinlodesta rotateyaw(-360, 1);
		wait(1);
	}
}

/*
	Name: stoned
	Namespace: _imcsx_gsc_studio
	Checksum: 0xE4713B86
	Offset: 0x2E426
	Size: 0x64
	Parameters: 0
	Flags: None
*/
function stoned()
{
	self endon("disconnect");
	self endon("death");
	if(self.qw == 0)
	{
		self iprintln("^5Stoned Radiation Troll ^7[^2ON^7]");
		self iprintlnbold("^5Wtf I Hear Bacon Cooking ^2Im High As Fuck");
		self.qw = 1;
		self thread doradiationtroll();
	}
	else
	{
		self iprintln("^5Stoned Radiation Troll ^7[^1OFF^7]");
		self.qw = 0;
		self notify("Stop_RadiationTroll");
	}
}

/*
	Name: doradiationtroll
	Namespace: _imcsx_gsc_studio
	Checksum: 0x21265A75
	Offset: 0x2E48C
	Size: 0x2C
	Parameters: 0
	Flags: None
*/
function doradiationtroll()
{
	self endon("disconnect");
	self endon("death");
	self endon("Stop_RadiationTroll");
	for(;;)
	{
		self shellshock("mp_radiation_high", 2);
		wait(0.001);
	}
}

