#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, uuid, sys

def behava_pack():
    pack_ver = input("Packのバージョン: ")
    if "." in pack_ver:
        pack_ver = pack_ver.replace(".", ",")
    elif " " in pack_ver:
        pack_ver = pack_ver.replace(" ", ",")
    else:
        print("入力エラー")
        sys.exit(0)

    min_engines = input("min_engineのバージョン(デフォルトは1.11.0): ")
    if "." in min_engines:
        min_engines = min_engines.replace(".", ",")
    elif " " in min_engines:
        min_engines = min_engines.replace(" ", ",")
    else:
        pass
    if min_engines == "":
        min_engines = "1,11,0"
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

    load_manifest = json.loads(raw_data_manifest)

    uuid_1 = str(uuid.uuid4())
    uuid_2 = str(uuid.uuid4())

    load_manifest['header']['description'] = descript
    load_manifest['header']['name'] = pack_name
    load_manifest['header']['uuid'] = uuid_1

    load_manifest['modules'][0]['description'] = descript
    load_manifest['modules'][0]['type'] = pack_type
    load_manifest['modules'][0]['uuid'] = uuid_2

    JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

    Jf = open("manifest.json", "w", encoding="utf-8")
    Jf.write(JSON_Data)
    Jf.close()

def Data_Resources_pack():
    pack_ver = input("Packのバージョン: ")
    if "." in pack_ver:
        pack_ver = pack_ver.replace(".", ",")
    elif " " in pack_ver:
        pack_ver = pack_ver.replace(" ", ",")
    else:
        print("入力エラー")
        sys.exit(0)

    min_engines = input("min_engineのバージョン(デフォルトは1.11.0): ")
    if "." in min_engines:
        min_engines = min_engines.replace(".", ",")
    elif " " in min_engines:
        min_engines = min_engines.replace(" ", ",")
    else:
        pass
    if min_engines == "":
        min_engines = "1,11,0"
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


    load_manifest = json.loads(raw_data_manifest)

    uuid_1 = str(uuid.uuid4())
    uuid_2 = str(uuid.uuid4())

    load_manifest['header']['description'] = descript
    load_manifest['header']['name'] = pack_name
    load_manifest['header']['uuid'] = uuid_1

    load_manifest['modules'][0]['description'] = descript
    load_manifest['modules'][0]['type'] = pack_type
    load_manifest['modules'][0]['uuid'] = uuid_2

    JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

    Jf = open("manifest.json", "w", encoding="utf-8")
    Jf.write(JSON_Data)
    Jf.close()

def Resources_pack():
    pack_ver = input("Packのバージョン: ")
    if "." in pack_ver:
        pack_ver = pack_ver.replace(".", ",")
    elif " " in pack_ver:
        pack_ver = pack_ver.replace(" ", ",")
    else:
        print("入力エラー")
        sys.exit(0)
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

    load_manifest = json.loads(raw_manifest)

    uuid_1 = str(uuid.uuid4())
    uuid_2 = str(uuid.uuid4())

    load_manifest['header']['description'] = descript
    load_manifest['header']['name'] = pack_name
    load_manifest['header']['uuid'] = uuid_1

    load_manifest['modules'][0]['description'] = descript
    load_manifest['modules'][0]['type'] = pack_type
    load_manifest['modules'][0]['uuid'] = uuid_2

    JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

    Jf = open("manifest.json", "w", encoding="utf-8")
    Jf.write(JSON_Data)
    Jf.close()

def skins_pack():
    pack_ver = input("Packのバージョン: ")
    if "." in pack_ver:
        pack_ver = pack_ver.replace(".", ",")
    elif " " in pack_ver:
        pack_ver = pack_ver.replace(" ", ",")
    else:
        print("入力エラー")
        sys.exit(0)
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

    load_manifest = json.loads(raw_manifest)

    uuid_1 = str(uuid.uuid4())
    uuid_2 = str(uuid.uuid4())

    load_manifest['header']['description'] = descript
    load_manifest['header']['name'] = pack_name
    load_manifest['header']['uuid'] = uuid_1

    load_manifest['modules'][0]['description'] = descript
    load_manifest['modules'][0]['type'] = pack_type
    load_manifest['modules'][0]['uuid'] = uuid_2

    JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

    Jf = open("manifest.json", "w", encoding="utf-8")
    Jf.write(JSON_Data)
    Jf.close()

def main():
    global pack_name, pack_type, descript
    print("◆◆◆ Minecraft Addon Manifest Generator(Ja) v2.0 ◆◆◆")

    pack_name = input("パック名: ")
    descript = input("パックの説明: ")
    pack_type = pack_type = input("Packのタイプ(resources(リソースパック) or data(ビヘイビアー) or skins(スキンパック))?: ")
    if pack_type == "":
        print("Error: 入力された文字列が空欄でした")
        sys.exit(0)
    elif pack_type == "Skins":
        pack_type = "skins"
    elif pack_type == "Data":
        pack_type = "data"
    elif pack_type == "DATA":
        pack_type = "data"
    elif pack_type == "Resources":
        pack_type = "resources"
    elif pack_type == "Respack":
        pack_type = "resources"
    elif pack_type == "SkinPack":
        pack_type = "skins"
    elif pack_type == "スキン":
        pack_type = "skins"
    elif pack_type == "スキンパック":
        pack_type = "skins"
    elif pack_type == "リソースパック":
        pack_type = "resources"
    elif pack_type == "ビヘイビアー":
        pack_type = "data"
    else:
        pass

    if pack_type == "data":
        print("\n>>Behaviorパックを選択しました!\n")
        behava_pack()
    else:
        pass

    if pack_type == "resources":
        DataR_branch_point = input("データパック(1) or ノーマル(0)？: ")
        if DataR_branch_point == "1":
            Data_Resources_pack()
        elif DataR_branch_point == "0":
            Resources_pack()
        elif DataR_branch_point == "データパック":
            Data_Resources_pack()
        elif DataR_branch_point == "ノーマル":
            Resources_pack()
        elif DataR_branch_point == "":
            print("Error:  入力された文字列が空欄でした")
            sys.exit(0)
        else:
            pass
    else:
        pass

    if pack_type == "skins":
        print("\n>>Skinパックを選択しました!\n")
        skins_pack()
    else:
        pass

if __name__== '__main__':
    main()
