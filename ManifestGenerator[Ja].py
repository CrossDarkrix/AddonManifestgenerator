# -*- coding: utf-8 -*-

"""
テキトーに作った割には上手くいったスクリプト。
manifest.jsonを手動で書き変えるのは面倒だと感じませんか？
そんな人の為に作ったスクリプトです。
"""

import json
import uuid
import sys

#ユーザー入力
print("◆◆◆ Minecraft Addon Manifest Generator(Ja) v1.5.5 ◆◆◆")
pack_name = input("Pack名: ")
descript = input("Packの説明文: ")
pack_type = input("Packのタイプ(resources(リソースパック) or data(ビヘイビアー) or skins(スキンパック))?: ").replace('Skins','skins').replace('Data','data').replace('DATA','data').replace('Resources','resources').replace('Respack','resources').replace('Sinks','skins').replace('SkinPack','skins').replace('スキン', 'skins').replace('スキンパック', 'skins').replace('リソースパック','resources').replace('ビヘイビアー', 'data').replace('skin','skins')
if pack_type == '':
	sys.exit("エラー: 入力された文字列が空欄でした")
else:
	pass
	
def behava_pack():
	pack_ver = input('Packのバージョン: ').replace('.',',').replace(' ',',')
	min_engines = input('min_engineのバージョン(デフォルトは1.11.0): ').replace('.',',').replace(' ',',')
	if min_engines == '':
		min_engines = ('1.11.0').replace('.',',').replace(' ',',')
	else:
		pass

	raw_data_manifest = ("""{
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

	#JSON形式の読み込み
	load_manifest = json.loads(raw_data_manifest)

	#ここからUUID
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#ここからJSON内の値変更
	#"header"部分の値変更
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#"modules"部分の値変更
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'data'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#manifest.jsonとして書き出し
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()


def Data_Resources_pack():
	pack_ver = input('Packのバージョン: ').replace('.',',').replace(' ',',')
	min_engines = input('min_engineのバージョン(デフォルトは1.11.0): ').replace('.',',').replace(' ',',')
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

	#JSON形式の読み込み
	load_manifest = json.loads(raw_manifest)

	#ここからUUID
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#ここからJSON内の値変更
	#"header"部分の値変更
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#"modules"部分の値変更
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = pack_type
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#manifest.jsonとして書き出し
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()

def Resources_pack():
	pack_ver = input('Packのバージョン: ').replace('.',',').replace(' ',',')
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

	#JSON形式の読み込み
	load_manifest = json.loads(raw_manifest)

	#ここからUUID
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#ここからJSON内の値変更
	#"header"部分の値変更
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#"modules"部分の値変更
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = pack_type
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#manifest.jsonとして書き出し
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()

def skins_pack():
	pack_ver = input('Packのバージョン: ').replace('.',',').replace(' ',',')
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

	#JSON形式の読み込み
	load_manifest = json.loads(raw_manifest)

	#ここからUUID
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#ここからJSON内の値変更
	#"header"部分の値変更
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#"modules"部分の値変更
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'skinpack'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#manifest.jsonとして書き出し
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()

if pack_type == 'data':
	print("\n>>Behaviorパックを選択しました!\n")
	behava_pack()
else:
	pass

if pack_type == 'resources':
	DataR_branch_point = input("データパック(1) or ノーマル(0)？: ")
	if DataR_branch_point == '1':
		Data_Resources_pack()
	if DataR_branch_point == '0':
		Resources_pack()
	if DataR_branch_point == 'データパック':
		Data_Resources_pack()
	if DataR_branch_point == 'ノーマル':
		Resources_pack()
	if DataR_branch_point == '':
		sys.exit("エラー: 入力された文字列が空欄でした")
else:
	pass

if pack_type == 'skins':
	print("\n>>Skinパックを選択しました!\n")
	skins_pack()
else:
	pass
