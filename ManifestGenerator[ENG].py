#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, uuid, sys

def behava_pack():
    pack_ver = input("Pack Version: ")
    if "." in pack_ver:
        pack_ver = pack_ver.replace(".", ",")
    elif " " in pack_ver:
        pack_ver = pack_ver.replace(" ", ",")
    else:
        print("Input Error")
        sys.exit(0)

    min_engines = input("min_engine Version(Default: 1.11.0): ")
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
    pack_ver = input("Pack Version: ")
    if "." in pack_ver:
        pack_ver = pack_ver.replace(".", ",")
    elif " " in pack_ver:
        pack_ver = pack_ver.replace(" ", ",")
    else:
        print("Input Error")
        sys.exit(0)

    min_engines = input("min_engine Version(Default: 1.11.0): ")
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
    pack_ver = input("Pack Version: ")
    if "." in pack_ver:
        pack_ver = pack_ver.replace(".", ",")
    elif " " in pack_ver:
        pack_ver = pack_ver.replace(" ", ",")
    else:
        print("Input Error")
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
    pack_ver = input("Pack Version: ")
    if "." in pack_ver:
        pack_ver = pack_ver.replace(".", ",")
    elif " " in pack_ver:
        pack_ver = pack_ver.replace(" ", ",")
    else:
        print("Input Error")
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
    print("◆◆◆ Minecraft Addon Manifest Generator(EN) v2.0 ◆◆◆")

    pack_name = input("Pack Name: ")
    descript = input("Pack Description: ")
    pack_type = pack_type = input("Pack Type(resources(ResourcePack) or data(behava pack) or skins(Skin Pack))?: ")
    if pack_type == "":
        print("Error: 'Pack Type' is Empty!")
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
    else:
        pass

    if pack_type == "data":
        print("\n>>Selected Behavior Pack!\n")
        behava_pack()
    else:
        pass

    if pack_type == "resources":
        DataR_branch_point = input("DataPack?(1) or Normal?(0): ")
        if DataR_branch_point == "1":
            Data_Resources_pack()
        elif DataR_branch_point == "0":
            Resources_pack()
        elif DataR_branch_point == "DataPack":
            Data_Resources_pack()
        elif DataR_branch_point == "Normal":
            Resources_pack()
        elif DataR_branch_point == "":
            print("Error: Input Empty!")
            sys.exit(0)
        else:
            pass
    else:
        pass

    if pack_type == "skins":
        print("\n>>Selected Skin Pack!\n")
        skins_pack()
    else:
        pass

if __name__== '__main__':
    main()
