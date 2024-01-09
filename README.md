## Blender <> Moi3D connector

### Bridge between [Blender](https://www.blender.org/download/) and [Moi3D](http://moi3d.com/):
![BMOI BANNER](https://i.imgur.com/sjLP3k8.jpg)

### System requirements:
- Windows
    1. Windows 10/11
    2. Windows temp folder location must be by default
- Mac

- Blender 2.8 or higher

### Download:
[BMOI_Connector-master.zip](https://github.com/TitusLVR/BMOI_Connector/archive/master.zip)

### Installation through download:
1. Download "BMOI_Connector-master.zip"
2. Extract somewhere and rename extracted folder to "BMOI_Connector"
3. Copy  "BMOI_Connector" folder to `C:\Users\<username>\AppData\Roaming\Blender Foundation\Blender\2.8x(2.9x)\scripts\addons` ( ***(Mac User)*** `/Users/<username>/Library/Application Support/Blender/2.8x(2.9x)/scripts/addons`)
4. Run Blender > Edit > Preferences > Addons > And activate "BMOI Connector"
5. ***(Mac User)*** In addon settings, set `BMOI3D custom exchange folder` to `/Users/<username>/Library/Application Support/Moi/BMOI` (create `BMOI` folder inside `Moi` folder)

### Install Moi3D scripts:
1. Open "BMOI_Connector\MOI3D" folder
2. Copy Commands and Startup folders to `C:\Users\<username>\AppData\Roaming\Moi\` ( ***(Mac User)*** `/Users/<username>/Library/Application Support/Moi/`)
3. Run Moi3d

### How-to:
#### Blender:
1. Navigate or open side bar (default button "N")
2. Open BMOI3D tab
* If you want to send objects to Moi3d  - press "Send to Moi3d" button
* If you want to get result from Moi3d  - press "Get from Moi3d" button

### Moi3D:
* If you want to send objects to Blender - "BMOI Export" button
* If you want to get objects from Blender - "BMOI Import" button

Thank you!
 
