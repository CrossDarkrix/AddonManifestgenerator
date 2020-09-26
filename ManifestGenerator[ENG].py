# -*- coding: utf-8 -*-

import json
import uuid
import sys

#User Input
print("◆◆◆ Minecraft Addon Manifest Generator(EN) v1.5.5 ◆◆◆")
pack_name = input("Pack Name: ")
descript = input("Pack Description: ")
pack_type = input("Pack Type(resources(ResourcePack) or data(behava pack) or skins(Skin Pack))?: ").replace('Skins','skins').replace('Data','data').replace('DATA','data').replace('Resources','resources').replace('Respack','resources').replace('Sinks','skins').replace('SkinPack','skins').replace('behava pack','data').replace('ResourcePack','resources').replace('Skin Pack','skins').replace('skin','skins').replace('behavapack','data')
if pack_type == '':
	sys.exit('Error: "Pack Type" is Empty!')
else:
	pass

def behava_pack():
	pack_ver = input('Pack Version: ').replace('.',',').replace(' ',',')
	min_engines = input('min_engine Version(Default: 1.11.0): ').replace('.',',').replace(' ',',')
	if min_engines == '':
		min_engines = ('1.11.0').replace('.',',').replace(' ',',')
	else:
		pass

	#Json Template
	raw_manifest = ("""{
	   "format_version" : 2,
	   "header" : {
		  "description" : "",
		  "name" : "",
		  "uuid" : "",
		  "min_engine_version": [MIN_VERSION],
		  "version" : [PackVersion]
	   },
	   "modules" : [
		  {
			 "description" : "",
			 "type" : "",
			 "uuid" : "",
			 "version" : [PackVersion]
		  }
	   ]
	}
	""").replace('PackVersion', pack_ver).replace('MIN_VERSION', min_engines)

	#Reading JsonData
	load_manifest = json.loads(raw_manifest)

	#Generate UUID4
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#Replace "header"/
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#replace "modules"/
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'data'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#writing manifest.json
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()


def skin_pack():
	pack_ver = input('Pack Version: ').replace('.',',').replace(' ',',')
	#Json Template
	raw_manifest = ("""{
	   "format_version" : 1,
	   "header" : {
		  "description" : "",
		  "name" : "",
		  "uuid" : "",
		  "version" : [PackVersion]
	   },
	   "modules" : [
		  {
			 "description" : "",
			 "type" : "",
			 "uuid" : "",
			 "version" : [PackVersion]
		  }
	   ]
	}
	""").replace('PackVersion', pack_ver)

	#Reading JsonData
	load_manifest = json.loads(raw_manifest)

	#Generate UUID4
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#Replace "header"/
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#replace "modules"/
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'skinpack'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#writing manifest.json
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()


def Resources_pack():
	pack_ver = input('Pack Version: ').replace('.',',').replace(' ',',')
	#Json Template
	raw_manifest = ("""{
	   "format_version" : 1,
	   "header" : {
		  "description" : "",
		  "name" : "",
		  "uuid" : "",
		  "version" : [PackVersion]
	   },
	   "modules" : [
		  {
			 "description" : "",
			 "type" : "",
			 "uuid" : "",
			 "version" : [PackVersion]
		  }
	   ]
	}
	""").replace('PackVersion', pack_ver)

	#Reading JsonData
	load_manifest = json.loads(raw_manifest)

	#Generate UUID4
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#Replace "header"/
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#replace "modules"/
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'resources'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#writing manifest.json
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()

def Data_Resources_pack():
	pack_ver = input('Pack Version: ').replace('.',',').replace(' ',',')
	min_engines = input('min_engine Version(Default: 1.11.0): ').replace('.',',').replace(' ',',')
	if min_engines == '':
		min_engines = ('1.11.0').replace('.',',').replace(' ',',')
	else:
		pass
	#Json Template
	raw_manifest = ("""{
	   "format_version" : 2,
	   "header" : {
		  "description" : "",
		  "name" : "",
		  "uuid" : "",
		  "min_engine_version": [MIN_VERSION],
		  "version" : [PackVersion]
	   },
	   "modules" : [
		  {
			 "description" : "",
			 "type" : "",
			 "uuid" : "",
			 "version" : [PackVersion]
		  }
	   ]
	}
	""").replace('PackVersion', pack_ver).replace('MIN_VERSION', min_engines)

	#Reading JsonData
	load_manifest = json.loads(raw_manifest)

	#Generate UUID4
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#Replace "header"/
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#replace "modules"/
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'resources'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#writing manifest.json
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()

if pack_type == 'data':
	print("\n>>Selected Behavior Pack!\n")
	behava_pack()
else:
	pass

if pack_type == 'resources':
	DataR_branch_point = input("DataPack?(1) or Normal?(0): ")
	if DataR_branch_point == '1':
		Data_Resources_pack()
	if DataR_branch_point == '0':
		Resources_pack()
	if DataR_branch_point == 'DataPack':
		Data_Resources_pack()
	if DataR_branch_point == 'Normal':
		Resources_pack()
	if DataR_branch_point == '':
		sys.exit("Error: Input Empty!")
else:
	pass
if pack_type == 'skins':
	print("\n>>Selected Skin Pack!\n")
	skin_pack()
else:
	pass
